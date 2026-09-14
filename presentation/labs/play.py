"""Run from presentation/: python labs/play.py. Edit settings, save and rerun."""
import random

from mosaic.gui.main import SAREnvGUI
from mosaic.sar.env import build_sar_env
from mosaic.sar.placers import LavaPlacer, LockedRoomPlacer, VictimPlacer

SEED = 42
NUM_ROWS = 2
NUM_COLS = 2
ROOM_SIZE = 8
VICTIMS_PER_ROOM = 2
LAVA_PER_ROOM = 2
LAVA_ENABLED = True
LOCKED_ROOM_PROB = 0.35  # Below 1.0; even zero locks one room on this revision.
SCREEN_SIZE = 600       # Window width is 1.5 times this value.

GUI_CONFIG = {
    "fullscreen": False,
    "max_time": 5,  # Displayed minutes; the base GUI does not enforce expiry.
    "prompt_type": "sparse",
    "llm_nudge_interval": 50,  # Must be positive on the pinned revision.
}


def make_env(**components):
    """Build and seed a small mission, optionally replacing camera or actions."""
    random.seed(SEED)
    env = build_sar_env(
        screen_size=SCREEN_SIZE,
        num_rows=NUM_ROWS,
        num_cols=NUM_COLS,
        room_size=ROOM_SIZE,
        victim_placer=VictimPlacer(num_real_victims=VICTIMS_PER_ROOM),
        lava_placer=LavaPlacer(lava_per_room=LAVA_PER_ROOM, enabled=LAVA_ENABLED),
        locked_room_placer=LockedRoomPlacer(locked_room_prob=LOCKED_ROOM_PROB),
        **components,
    )
    env.reset(seed=SEED)
    return env


if __name__ == "__main__":
    env = make_env()
    try:
        SAREnvGUI(env, config=GUI_CONFIG).run()
    finally:
        env.close()
