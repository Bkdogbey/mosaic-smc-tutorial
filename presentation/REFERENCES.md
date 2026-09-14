# MOSAIC tutorial source guide

## Source snapshots

- [MOSAIC code](https://github.com/Bkdogbey/mosaic/tree/a409222534dcd234dd2925a5adab8da9db17e6b2): a409222534dcd234dd2925a5adab8da9db17e6b2.
- [Rendered gh-pages branch](https://github.com/Bkdogbey/mosaic/tree/67ea20400710de7edcd296ddce39821b00173f7c): 67ea20400710de7edcd296ddce39821b00173f7c.
- The review covered README.md, REFERENCE.md, docs/ and the rendered documentation search index. The repository uses the singular filename REFERENCE.md.
- Executable code takes precedence where website examples lag implementation.

## Topic mapping

| Topic | Source files in the snapshot |
| --- | --- |
| Overview and architecture | README.md, REFERENCE.md, docs/index.md, docs/architecture.md |
| Installation | pyproject.toml, docs/getting-started.md |
| Environment and reset | src/mosaic/sar/env.py, src/mosaic/core/level.py |
| Objects and placement | src/mosaic/sar/objects.py, src/mosaic/sar/placers.py |
| Rescue and completion | src/mosaic/sar/actions.py, src/mosaic/sar/instructions.py |
| Keys, advice timing and countdown | src/mosaic/gui/user.py, src/mosaic/gui/main.py |
| Panels and feedback | src/mosaic/gui/info.py, chat.py, feedback.py |
| Cameras | src/mosaic/core/camera.py |
| Advice contracts | src/mosaic/llm/client.py, process_prompts.py |
| Observation encoding | src/mosaic/sar/observations.py |
| Study infrastructure | src/experiment/experiment.py, game.py, placers.py |
| Providers and replay | src/experiment/llm.py, replay.py |

## Corrections carried into the tutorial

- The factory requires screen_size and the GUI accepts a config dictionary.
- pygame and pygame-ce share an import namespace; the pinned revision needs the documented repair.
- The default placer adds only real victims. Health decay and decoys need study logic.
- The default false-pickup reward is −1, rather than −0.5.
- Actual victim glyphs use balanced versus offset arms; both families appear T-like.
- Mission completion means all real victims were removed, including dead ones.
- The GUI's countdown does not enforce expiry; termination causes an immediate reset.
- Custom rescue handling does not increment the ordinary MiniGrid step count.
- A zero advice interval causes modulo-by-zero; input pauses during a request.
- A zero lock fraction still locks a room; 1.0 can hang generation.
- A zero lava count can trigger random placement; use enabled=False for none.
- Seed Python random as well as the environment. GUI launch and Backspace reset again.
- Use square room grids and the three cameras with reset support.
- A full observation grid contains information outside the camera view. image is an encoding, not GUI RGB.
- Runtime checks require LLMClient subclasses. The old random correctness label was unsupported and was removed.
- The actual runner is experiment/experiment.py. Replay takes a positional JSONL filename.

## Image and design credits

All images in this reconstructed version already belong to the tutorial repository:
- assets/logo.png and assets/background.jpg: the original iHuman Lab template.
- assets/game-view.png and assets/gui-screenshot.png: MOSAIC documentation screenshots.
- assets/victims.png: the original tutorial glyph render from MOSAIC object coordinates.
- assets/cam-room.png and assets/cam-cone.png: the original camera strategy renders.

The lab theme, slide dimensions, heading motif, footer and logo remain. This version reuses existing images; it does not claim they are newly captured screenshots.

## Installation sources

- [Python 3.12 platform installers](https://www.python.org/downloads/release/python-31210/).
- [Python venv documentation](https://docs.python.org/3/library/venv.html).
- [Git for Windows](https://git-scm.com/downloads/win).
- [Git for macOS](https://git-scm.com/downloads/mac).
