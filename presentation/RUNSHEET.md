# Facilitator Run Sheet — MOSAIC Tutorial (two hours)

The rendered deck has 32 slides: 25 in the main tutorial, a closing slide, and
six appendix slides. The main sequence runs in three parts: what MOSAIC is,
install and run it, then understand and customize it.

## Before the room opens

- [ ] Render `mosaic-tutorial.qmd` and open `index.html` in a browser.
- [ ] Test the deck at the projector's 16:9 resolution (authored at 1280×720).
- [ ] Keep one working MOSAIC environment and one running mission as a fallback.
- [ ] Test a clean Windows PowerShell install with the `mosaic_env` commands.
- [ ] Test the Conda alternative in a separate clean environment.
- [ ] Send `SETUP.md` to attendees before the conference.
- [ ] Ask one lab member to help with installation during Part Two.
- [ ] Confirm `PYTHONPATH=src python -m experiment.main` opens a window.

## Timing

| Time | Slides | Block | Facilitator focus |
| --- | --- | --- | --- |
| 0:00–0:15 | 1–7 | Part One | Why the testbed exists and what human–AI teaming questions it supports. |
| 0:15–0:45 | 8–12 | Part Two: install | Prerequisites, clone, install, verify. |
| 0:45–1:00 | 13–14 | First run | Launch the mission and troubleshoot stragglers. |
| 1:00–1:20 | 15–20 | Interface and task | What just ran, the interface, task objects, controls, cameras. |
| 1:20–1:35 | 21–22 | Software layers | The five layers and how the mission is composed. |
| 1:35–1:50 | 23 | Modify and rerun | One parameter change, rerun, compare. |
| 1:50–1:55 | 24–25 | AI teammate | The teammate interface and the extension points. |
| 1:55–2:00 | 26 | Questions | Close on the working baseline; use appendix slides as needed. |

## Part One notes (slides 1–7)

- There is no Part One divider — the deck opens straight into the lab and the
  motivation. The first divider is slide 8.
- Slide 3 establishes the four requirements MOSAIC coordinates. Keep it brief.
- Slide 4 is the system overview: human, MOSAIC task, AI teammate, session data.
  Do not add the Gymnasium/MiniGrid detail here; it appears on slides 16 and 21.
- Slide 6 is the core claim of the tutorial. The teammate advises; the
  participant retains final action authority. Say it out loud.
- Keep Part One to fifteen minutes. Its purpose is to make the hands-on work
  meaningful, not to be complete.

## Part Two notes (slides 8–14)

- Ask attendees to use Python 3.10 or 3.11 for a shared troubleshooting baseline.
  MOSAIC's `pyproject.toml` claims 3.8+, but the code needs 3.10.
- Slide 9 lists the eight packages `pip install -e .` brings in and shows the
  one swap — `pygame` out, `pygame-ce` in. That swap is the only manual step.
- Slide 10 clones one repository. Everyone stays in `mosaic` all session.
- Slide 11: use the exact uninstall and force-reinstall commands; `--force-reinstall`
  is required. `tabulate` is declared upstream, so no separate install.
- Do not advance from slide 12 until most attendees see `MOSAIC ready`.
- Slide 13 launches `PYTHONPATH=src python -m experiment.main` — MOSAIC's own
  study runner. The GIF on the slide is the real interface, so you can talk
  through it while people are still installing. It opens fullscreen; F11 gives
  a window. Anyone who cloned before the import fix landed needs `git pull`.
- Hold at slide 14 until most attendees can move the agent, then ask everyone to
  press `Esc`. The appendix recovery slide is available while helpers work with
  individual machines.

## Part Three notes (slides 15–25)

- Slide 16 explains the runtime relationship: participant, GUI, SAR environment,
  the Gymnasium/MiniGrid foundation under the environment, and the AI teammate
  wired to both the environment and the chat panel.
- Slide 17 reveals one region at a time — press forward five times. The tile rail
  down the right is the visual vocabulary and now includes the decoy. The
  screenshot is caught mid-flash, so the green glow around the game view is the
  edge vignette firing after a rescue — point at it.
- Slide 18 labels the real-victim and decoy rows directly. Clarify that the
  reusable `VictimPlacer` places real victims only; decoys come from the study
  layer's `LavaRiskVictimPlacer`.
- Slide 19 groups six keys by intent. `Tab` does both pickup and rescue on
  purpose. Note what people will actually see: the runner attaches the keyless
  `dummy` teammate, so `Alt` replies "Currently, no commands are available."
  Advice also fires automatically every 50 steps once a real teammate is set.
- Slide 20 compares three live captures of one frozen frame. The white ring is
  the agent and the dashed box is the room it stands in. Only visibility
  changes; the task state does not. Do not offer `FullviewCamera` or
  `AgentCenteredCamera` — both raise `AttributeError` on env reset.
- Slide 21 names each directory, the files inside it, and the interface it
  exposes. Spend the time here; this is what attendees need in order to place
  their own study. Have the repo open in an editor alongside the slide.
- Slide 22 is the real `src/experiment/main.py`, including the
  `configs/experiment.yaml` lookup. Point out that the victim counts come from
  the config file, not the source.
- Slide 23: change `num_rows`, `num_cols`, `room_size` or `locked_room_prob` in
  `src/experiment/main.py` — those four are hardcoded there. Rerun the slide-13
  command. `LOCKED_ROOM_PROB` at 1.0 hangs the generator.
- Slide 24 is the teammate interface. The runner already passes
  `build_llm_client("dummy")`; swapping in `"openai"` or `"google"` is a
  one-argument change that needs a key and the `llama-index` package. Mention
  it, do not attempt it live.
- Slide 25 closes on the real extension seams.

## Expected problems

| Symptom | Response |
| --- | --- |
| `ImportError: cannot import name 'DIRECTION_LTR'` | Repeat the pygame uninstall and force-reinstall from slide 11. |
| `AttributeError: module 'pygame' has no attribute 'surface'` | Step 11 was run without `--force-reinstall`. Rerun with the flag. |
| `ModuleNotFoundError: No module named 'mosaic'` | Confirm `mosaic_env` is active and `pip install -e .` completed in the `mosaic` directory. |
| `NameError: name 'LavaRiskVictimPlacer' is not defined` | Their clone predates the import fix. `git pull` in `mosaic`. |
| `No module named 'experiment'` | Run from the repo root with `PYTHONPATH=src`. |
| PowerShell cannot load `mosaic_env` | Use `.\mosaic_env\Scripts\Activate.ps1`; the leading `.\` is required. |
| `ModuleNotFoundError: No module named 'tabulate'` | `python -m pip install tabulate`. |
| No window or `No available video device` | The GUI needs a local graphical session. Use the fallback laptop. |
| `Alt` replies "Currently, no commands are available." | Expected — the runner uses the keyless `dummy` teammate. |
| Generation appears to hang after customization | `locked_room_prob` is at `1.0`. Use `0.9` or less. |
| More victims than expected | `num_real_victims` is per room; 12 per room across a 3×3 building is 108. |
| `AttributeError: 'FullviewCamera' object has no attribute 'reset'` | Known bug, same for `AgentCenteredCamera`. Use `AgentFOVCamera`, `AgentConeCamera`, or the default. |

## Cut list

If the session runs long:

1. Explain slides 16–17 in one minute each without pausing on every feature.
2. Demonstrate the slide-23 parameter change instead of waiting for everyone.
3. Describe the teammate swap on slide 24 without running it, and close on the
   extension points on slide 25.

Do not cut the installation checkpoints, the first run, the controls, the camera
comparison, or the software-layer table.

## Closing ask

Ask attendees to keep the small working mission and open an issue when
installation or an extension point fails on their machine. Concrete reports from
new users are the most useful outcome for the project after the tutorial.
