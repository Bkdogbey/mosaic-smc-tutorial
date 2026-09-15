# MOSAIC Tutorial — IEEE SMC 2026

A 90-minute hands-on tutorial introducing MOSAIC to HCI and human-factors
researchers, built on the iHuman Lab Quarto reveal.js template.

The deck is three parts:

1. **Understanding MOSAIC** — why a human–AI study needs a platform like this, what
   MOSAIC connects, the search-and-rescue task, and the research questions it supports
2. **Install and verify** — one supported setup path with checkpoints and a compact
   troubleshooting appendix
3. **Using the search-and-rescue testbed** — see how a mission is assembled, run
   the provided example, compare camera views, and change one task parameter

Technical details about the observation schema, the advisor contract, the iHuman
Lab protocol, instrumentation, and the roadmap live in the appendix for Q&A.

## Contents

```
presentation/
├── mosaic-tutorial.qmd   # the deck — edit this (32 slides: 25 main + appendix)
├── theme.scss            # lab theme (template + team, fill-mode cards, horizontal flow,
│                         #   architecture diagram + .detached variant, annotated
│                         #   screenshots, .band notes, layer bands, you-are-here strip,
│                         #   .checkpoint callouts, dark-theme panel-tabset)
├── SETUP.md              # send this to attendees BEFORE the session
├── RUNSHEET.md           # facilitator timings, cut list, expected failures
├── assets/               # figures used in the deck
└── labs/                 # the scripts attendees run
    ├── first_mission.py  # provided minimal example run in Part Three
    ├── play.py           # play a mission; has an EDIT ME block of knobs
    ├── tweak.py          # all four injection points in one file
    └── advisor.py        # optional development example; not used in the main deck
```

## Render

```bash
quarto render mosaic-tutorial.qmd     # build once
quarto preview mosaic-tutorial.qmd    # live-reload while editing
```

Navigate with arrow keys, `f` for fullscreen, `s` for speaker notes.

## Assets

| File | Source |
| --- | --- |
| `gui-screenshot.png`, `game-view.png` | MOSAIC docs |
| `cam-full.png`, `cam-room.png` | Generated from camera strategies at `room_size=8`, 3×3 rooms |
| `cam-cone.png` | Forward-visibility illustration based on the tutorial game artwork |
| `victims.png` | Generated from `Victim` / `FakeVictim` render coordinates — top row real, bottom row decoys |
| `logo.png`, `background.jpg` | iHuman Lab template |
| `team/*.jpg` | iHuman Lab website people page (`ihuman-lab.github.io/lab-website/people/`) |

`cam-full.png` introduces the search-and-rescue testbed in Part One.
`gui-screenshot.png` introduces the complete interface in Part Three.
`game-view.png`, `cam-room.png`, and `cam-cone.png` introduce the three supported
camera choices in Part Three. `victims.png` remains available for reference.

## Before presenting

1. Send `SETUP.md` to registrants at least a week out.
2. Re-verify every command in Part 2 against the current `main`. The whole
   pygame-ce section should be **deleted** once the PyPI release fixes the
   dependency.
3. Read `RUNSHEET.md`.

## Repo issues this tutorial exposed

Verified against a clean clone of `iHuman-Lab/mosaic` (`c571f94`) on Python
3.10.20. The deck currently teaches around all of these.

1. **`pygame` vs `pygame-ce`.** `pyproject.toml` declares `pygame`; `pygame_gui`
   requires `pygame-ce`. `pip install -e .` installs **both**, and `pygame` lands
   last, so the GUI dies with
   `ImportError: cannot import name 'DIRECTION_LTR' from 'pygame'`.
   Fix: depend on `pygame-ce>=2.5.2`.
2. **The obvious workaround for issue 1 does not work.**
   `pip uninstall -y pygame && pip install "pygame-ce>=2.5.2"` leaves pygame-ce
   *broken* — uninstalling `pygame` removes shared files from the namespace, and
   pip then reports "Requirement already satisfied" and repairs nothing. The
   symptom is `AttributeError: module 'pygame' has no attribute 'surface'`.
   `--force-reinstall` is required. Worth putting in the README until it is fixed.
3. **`env.reset(seed=N)` does not reproduce a world.** The placers use the global
   `random` module (`src/mosaic/sar/placers.py:1,42,102,103,130,131,153`) rather
   than the environment's seeded `np_random`. Only the room-and-door skeleton is
   seeded; victims, lava and keys are not. Calling `random.seed(N)` before
   `env.reset(seed=N)` is a working workaround, but reproducibility is a headline
   claim and should not need one. Fix: thread `self.np_random` through `Placer`.
4. **`FullviewCamera` and `AgentCenteredCamera` have no `reset()`.**
   `PickupVictimEnv.reset()` calls `self.camera.reset()` unconditionally, so
   passing either as `camera_strategy` raises `AttributeError`. Fix: add a no-op
   `reset()` to `CameraStrategy`.
5. **`locked_room_prob=1.0` hangs forever.** `LockedRoomPlacer` computes
   `n_locked = max(1, int(num_cols * num_rows * prob))`, so at `1.0` every room is
   locked, no solvable layout exists, and the level generator retries without a
   cap — the process never returns and no window opens. Reproduced on 2×2 at
   seeds 1, 2 and 3; `0.9` is fine. Fix: cap `n_locked` below the room count, or
   bound the retry loop and raise.
6. **`tabulate` is required but undeclared.** `build_prompt()` →
   `_build_table()` calls `DataFrame.to_markdown()`, which needs `tabulate`. It
   appears in neither `pyproject.toml` nor `requirements.txt`, so on a clean
   install **both** `sparse` and `detailed` prompts raise
   `ImportError: Missing optional dependency 'tabulate'` — which means the `Alt`
   key (ask the advisor) does nothing at all. Fix: add `tabulate` to dependencies.
7. **`experiment_main.py` does not exist.** `README.md`, `REFERENCE.md`,
   `docs/getting-started.md`, `docs/architecture.md` and `docs/experiment.md` all
   point at `python -m experiment.experiment_main`; the file is
   `src/experiment/experiment.py`.
8. **README quick-start does not run.** It calls
   `SAREnvGUI(env, fullscreen=False)`, but the constructor takes
   `config: dict` — the working form is `SAREnvGUI(env, config={"fullscreen": False})`.
   The clone URL is also still `github.com/yourusername/mosaic.git`.
9. **`docs/game-concept.md` documents keys that are not mapped.** It lists `W` for
   forward; `key_to_action` in `src/mosaic/gui/user.py` has no `W`. It also lists
   the decoy penalty as `-0.5`; `RescueRewards.fake_victim` defaults to `-1.0`.
10. **`requires-python = ">=3.8"`** is optimistic given the current dependency set;
   the docs say 3.9+ and we only test 3.10.
11. **The `cam_*` observation fields are camera-dependent.** `cam_top_x`,
   `cam_top_y`, `cam_view_w` and `cam_view_h` are only written when the camera has
   `_update_position` (i.e. `EdgeFollowCamera`). Analyses written against the
   default camera break silently under `AgentConeCamera`.
