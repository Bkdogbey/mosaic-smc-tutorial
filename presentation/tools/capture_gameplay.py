"""Record a short gameplay loop as the animated GIF on the "run the mission" slide.

    python tools/capture_gameplay.py

Builds the same mission `python -m experiment.main` builds, drives the agent to
the nearest real victim with a breadth-first search over the observed grid, and
rescues it. Frames come from the real GUI compositor, so the info panel, the
chat panel and the rescue vignette are all the ones attendees will see.

Two things are faked, both because we are not inside `gui.run()`:

- the vignette clock is a frozen counter we advance by one frame interval per
  captured frame, so the green flash fades across the GIF instead of vanishing;
- the walk is scripted rather than typed.

Needs a MOSAIC checkout (MOSAIC_SRC below) and its runtime deps. Runs headless
through SDL's dummy video driver, so no window appears.

Not bit-reproducible: level generation retries internally on "connect_all
failed" and each retry consumes RNG, so the same seed can lay out a different
building from run to run. Re-run until you get a clip that reads well.
"""
import collections
import os
import pathlib
import random
import sys

MOSAIC_SRC = "/home/bennett/Research/mosaic/src"
os.environ.setdefault("SDL_VIDEODRIVER", "dummy")
os.environ.setdefault("SDL_AUDIODRIVER", "dummy")
sys.path.insert(0, MOSAIC_SRC)

import numpy as np  # noqa: E402
import pygame  # noqa: E402
import yaml  # noqa: E402
from experiment.placers import LavaRiskVictimPlacer, SectorSpreadLavaPlacer  # noqa: E402
from minigrid.core.actions import Actions  # noqa: E402
from mosaic.core.camera import AgentFOVCamera  # noqa: E402
from mosaic.gui.feedback import EdgeVignette  # noqa: E402
from mosaic.gui.main import SAREnvGUI  # noqa: E402
from mosaic.sar.env import build_sar_env  # noqa: E402
from mosaic.sar.placers import LockedRoomPlacer  # noqa: E402
from PIL import Image  # noqa: E402

OUT = pathlib.Path(__file__).resolve().parent.parent / "assets" / "gameplay.gif"
SEED = 7
GAME = 800
FPS = 12                 # GIF playback rate
FRAME_MS = 1000 // FPS
MAX_FRAMES = 52          # ~4.3 s at 12 fps; keeps the asset near 500 KB
HOLD_AFTER_RESCUE = 10   # frames to linger so the vignette fade is visible
SCALE = 0.44             # 1200x800 compositor output -> 528x352
PALETTE = 96             # GIF colours; the interface is mostly flat fills

# Grid codes from mosaic/sar/observations.py.
EMPTY, WALL, LAVA, VICTIM, FAKE = 0, 1, 4, 5, 6
DOOR_BASE, KEY_BASE = 10, 30
# MiniGrid direction vectors, indexed by agent_dir.
DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


class FrozenClock:
    """pygame.time.get_ticks stand-in whose value we advance by hand."""

    def __init__(self):
        self.ms = 0

    def __call__(self):
        return self.ms


def passable(code):
    """Walkable floor. Lava, walls, and any door that is not already open are
    out; so are victim tiles, which we approach from an adjacent cell."""
    if code in (EMPTY, KEY_BASE):
        return True
    if KEY_BASE <= code < KEY_BASE + 6:
        return True
    if DOOR_BASE <= code < DOOR_BASE + 18:
        return (code - DOOR_BASE) % 3 == 0  # 0 = open
    return False


def route_to_victim(grid, start):
    """Breadth-first search to a cell adjacent to the nearest real victim.
    Returns (path_of_cells, victim_cell) or (None, None)."""
    h, w = len(grid), len(grid[0])
    prev = {start: None}
    queue = collections.deque([start])
    while queue:
        cell = queue.popleft()
        x, y = cell
        for dx, dy in DIRS:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < w and 0 <= ny < h) or (nx, ny) in prev:
                continue
            if grid[ny][nx] == VICTIM:
                path = [cell]
                while prev[path[0]] is not None:
                    path.insert(0, prev[path[0]])
                return path, (nx, ny)
            if passable(grid[ny][nx]):
                prev[(nx, ny)] = cell
                queue.append((nx, ny))
    return None, None


def turns_to(cur_dir, want_dir):
    """Fewest left/right actions to face want_dir."""
    delta = (want_dir - cur_dir) % 4
    if delta == 0:
        return []
    if delta == 1:
        return [Actions.right]
    if delta == 3:
        return [Actions.left]
    return [Actions.right, Actions.right]


def plan(obs):
    """Action list that walks to the nearest real victim and rescues it."""
    grid = obs["grid"]
    start = (obs["agent_x"], obs["agent_y"])
    path, victim = route_to_victim(grid, start)
    if path is None:
        return []
    actions, cur, facing = [], start, obs["agent_dir"]
    for nxt in path[1:]:
        want = DIRS.index((nxt[0] - cur[0], nxt[1] - cur[1]))
        actions += turns_to(facing, want)
        actions.append(Actions.forward)
        cur, facing = nxt, want
    actions += turns_to(facing, DIRS.index((victim[0] - cur[0], victim[1] - cur[1])))
    actions.append(Actions.pickup)
    return actions


def main():
    clock = FrozenClock()
    vignette = EdgeVignette(GAME, clock_ms=clock)

    with open(pathlib.Path(MOSAIC_SRC).parent / "configs/experiment.yaml") as fh:
        game_config = yaml.safe_load(fh).get("game", {})

    env = build_sar_env(
        screen_size=GAME,
        num_rows=3,
        num_cols=3,
        room_size=10,
        victim_placer=LavaRiskVictimPlacer(
            num_real_victims=game_config.get("num_real_victims", 6),
            num_fake_victims=game_config.get("num_fake_victims", 12),
        ),
        lava_placer=SectorSpreadLavaPlacer(
            lava_per_room=game_config.get("lava_per_room", 8),
        ),
        locked_room_placer=LockedRoomPlacer(locked_room_prob=0.5),
        camera_strategy=AgentFOVCamera(),
    )
    gui = SAREnvGUI(env, config={"fullscreen": False, "max_time": 5}, vignette=vignette)

    random.seed(SEED)
    obs, _ = env.reset(seed=SEED)
    gui.user.obs = obs
    gui.user.total_reward = 0.0

    frames, actions, rescues = [], plan(obs), 0

    def capture():
        surface = gui._build_combined_surface(env.render())
        raw = pygame.surfarray.array3d(surface).transpose(1, 0, 2)
        img = Image.fromarray(raw.astype(np.uint8))
        img = img.resize(
            (int(img.width * SCALE), int(img.height * SCALE)), Image.LANCZOS)
        frames.append(img.quantize(colors=PALETTE, method=Image.MEDIANCUT))
        clock.ms += FRAME_MS

    capture()
    while actions and len(frames) < MAX_FRAMES:
        gui.user.step(actions.pop(0))
        events = (gui.user.last_info or {}).get("events", [])
        if events:
            vignette.trigger(events)
            rescues += sum(e["type"] == "victim_rescued" for e in events)
        capture()
        if not actions:
            for _ in range(HOLD_AFTER_RESCUE):
                capture()
            actions = plan(gui.user.obs)  # keep going if frames remain

    OUT.parent.mkdir(parents=True, exist_ok=True)
    frames[0].save(
        OUT, save_all=True, append_images=frames[1:],
        duration=FRAME_MS, loop=0, optimize=True,
    )
    kb = OUT.stat().st_size / 1024
    print(f"wrote {OUT.name}  {len(frames)} frames  {frames[0].size}  "
          f"{rescues} rescue(s)  {kb:.0f} KB")
    pygame.quit()


if __name__ == "__main__":
    main()
