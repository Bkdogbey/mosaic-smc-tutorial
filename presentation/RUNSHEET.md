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
- [ ] Confirm `python labs/play.py` opens a window on the presenting machine.

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
- Slide 10 clones **two** repositories: MOSAIC and the tutorial materials. People
  who followed `SETUP.md` already have both.
- Slide 11: the package metadata installs both `pygame` and `pygame-ce`. Use the
  exact uninstall and force-reinstall commands. `tabulate` is now declared
  upstream, so the separate install is only a fallback.
- Do not advance from slide 12 until most attendees see `MOSAIC ready`.
- Slide 13 launches `python labs/play.py` from `mosaic-smc-tutorial/presentation`.
  **Do not use `python -m experiment.main`** — it is broken on MOSAIC's `main`
  (two imports commented out in `src/experiment/main.py`) and exits with
  `NameError: name 'LavaRiskVictimPlacer' is not defined`.
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
  purpose. Note what people will actually see: with no teammate attached, `Alt`
  replies "Currently, no commands are available." Advice also fires
  automatically every 50 steps once a teammate is configured.
- Slide 20 compares three live captures of one frozen frame. The white ring is
  the agent and the dashed box is the room it stands in. Only visibility
  changes; the task state does not. Do not offer `FullviewCamera` or
  `AgentCenteredCamera` — both raise `AttributeError` on env reset.
- Slide 21 is the five-layer table. Spend the time here; this is what attendees
  need in order to place their own study.
- Slide 22 shows the shape of `labs/play.py`, then names
  `src/experiment/main.py` as this lab's study-specific composition — mention
  it, do not run it.
- Slide 23: change one value in the `EDIT ME` block and rerun the slide-13
  command. Remind people that `VICTIMS_PER_ROOM` is per room, not a total, and
  that `LOCKED_ROOM_PROB = 1.0` hangs the generator.
- Slide 24 is the teammate interface. `labs/advisor.py` runs a `ScriptedAdvisor`
  with tunable `p_correct` and needs no API key — demo it if time allows. The
  provider swap needs a key and the `llama-index` package; mention it, do not
  attempt it live.
- Slide 25 closes on the real extension seams.

## Expected problems

| Symptom | Response |
| --- | --- |
| `ImportError: cannot import name 'DIRECTION_LTR'` | Repeat the pygame uninstall and force-reinstall from slide 11. |
| `AttributeError: module 'pygame' has no attribute 'surface'` | Step 11 was run without `--force-reinstall`. Rerun with the flag. |
| `ModuleNotFoundError: No module named 'mosaic'` | Confirm `mosaic_env` is active and `pip install -e .` completed in the `mosaic` directory. |
| `NameError: name 'LavaRiskVictimPlacer' is not defined` | They ran `python -m experiment.main`. Send them to `python labs/play.py`. |
| PowerShell cannot load `mosaic_env` | Use `.\mosaic_env\Scripts\Activate.ps1`; the leading `.\` is required. |
| `ModuleNotFoundError: No module named 'tabulate'` | `python -m pip install tabulate`. |
| No window or `No available video device` | The GUI needs a local graphical session. Use the fallback laptop. |
| `Alt` replies "Currently, no commands are available." | Expected — no teammate is attached in `labs/play.py`. |
| Generation appears to hang after customization | `LOCKED_ROOM_PROB` is at `1.0`. Use `0.9` or less. |
| More victims than expected | `VICTIMS_PER_ROOM` is per room; a 2×2 building with 2 per room is 8. |
| `AttributeError: 'FullviewCamera' object has no attribute 'reset'` | Known bug, same for `AgentCenteredCamera`. Use `AgentFOVCamera`, `AgentConeCamera`, or the default. |

## Cut list

If the session runs long:

1. Explain slides 16–17 in one minute each without pausing on every feature.
2. Demonstrate the slide-23 parameter change instead of waiting for everyone.
3. Describe the `labs/advisor.py` demo on slide 24 without running it, and close
   on the extension points on slide 25.

Do not cut the installation checkpoints, the first run, the controls, the camera
comparison, or the software-layer table.

## Closing ask

Ask attendees to keep the small working mission and open an issue when
installation or an extension point fails on their machine. Concrete reports from
new users are the most useful outcome for the project after the tutorial.
