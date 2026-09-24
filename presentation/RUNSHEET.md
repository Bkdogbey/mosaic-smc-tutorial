# Facilitator Run Sheet — MOSAIC Tutorial (two hours)

The rendered deck has 35 slides: 30 in the main tutorial, a closing slide, and
four appendix slides. The main sequence runs in three parts: what MOSAIC is,
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
| 1:00–1:08 | 15–17 | Relaunch and architecture | Everyone reopens the game; what each part of the window is. |
| 1:08–1:22 | 18–21 | Interface and task | The interface, task objects, controls, cameras — try each live. |
| 1:22–1:30 | 22–23 | Code map | Where each part lives, and how `main.py` composes them. |
| 1:30–1:55 | 24–30 | Customize | One component per slide, about 3.5 minutes each, one "Try it" each. |
| 1:55–2:00 | 31 | Questions | Close on the working baseline; use appendix slides as needed. |

## Part One notes (slides 1–7)

- There is no Part One divider — the deck opens straight into the lab and the
  motivation. The first divider is slide 8.
- Slide 3 establishes the four requirements MOSAIC coordinates. Keep it brief.
- Slide 4 is the system overview: human, MOSAIC task, and AI teammate on top;
  study sensors, LSL, and session data underneath.
  Do not add the Gymnasium/MiniGrid detail here; it appears on slides 16 and 21.
- Slide 6 is the core claim of the tutorial. The teammate advises; the
  participant retains final action authority. Say it out loud.
- Slide 7 names four research areas and what MOSAIC provides for each: trust
  and reliance, evaluating AI teammates (the lab's own none / GPT / Gemini
  design), workload and cognitive state, and situation awareness.
- Keep Part One to fifteen minutes. Its purpose is to make the hands-on work
  meaningful, not to be complete.

## Part Two notes (slides 8–14)

- Ask attendees to use Python 3.10 or 3.11 for a shared troubleshooting baseline.
  MOSAIC's `pyproject.toml` claims 3.8+, but the code needs 3.10.
- Slide 9 groups the packages `pip install -e .` brings in by role. Nothing is
  installed by hand.
- Slide 10 clones one repository. The numbered notes on the right match the
  code line numbers. Everyone stays in `mosaic` all session.
- Slide 11 is two commands: upgrade pip, then `pip install -e .`. Mention that
  `-e` (editable) is what lets Part Three's edits take effect without reinstalling.
- Do not advance from slide 12 until most attendees see `MOSAIC ready`.
- Slide 13 launches `PYTHONPATH=src python -m experiment.main` — MOSAIC's own
  study runner. The GIF on the slide is the real interface: one real victim
  (green flash, +1), one decoy (red flash, −1), then another real victim. Talk
  through it while people are still installing. It opens fullscreen; F11 gives
  a window. Anyone who cloned before the import fix landed needs `git pull`.
- Hold at slide 14 until most attendees can move the agent, then ask everyone to
  press `Esc`. The appendix recovery slide is available while helpers work with
  individual machines.

## Part Three notes (slides 15–30)

- Slide 16 relaunches the game. Most attendees closed it at the checkpoint;
  wait for most windows to be open, windowed with `F11`, before moving on.
- Slide 17 is the runtime: participant, GUI, and environment in a loop, with
  sensing, the AI teammate, and Gymnasium/MiniGrid beneath them. Point at the
  attendee's own window. The chat image is a real reply from the slide-28
  teammate. Sensors never connect to the game directly: they stream into Lab
  Streaming Layer, which puts sensor and game samples on one clock. Sensing
  exists only in the lab's study runner, not this run.
- Slide 18 reveals one region at a time — press forward five times. The
  screenshot is caught mid-flash, so the green glow around the game view is the
  edge vignette firing after a rescue — point at it.
- Slide 19 labels the real-victim and decoy rows directly. The reusable
  `VictimPlacer` places real victims only; decoys come from the study layer's
  `LavaRiskVictimPlacer`. The health strip shows the white health bar. Health
  drains only in the lab's study env (`TunedPickupVictimEnv`), faster near lava,
  and the bar is drawn only while advice is on screen. In the tutorial's run
  health stays full — say so if asked why nobody sees it.
- Slide 20: each clip shows one key. `Tab` does both pickup and rescue on
  purpose. The advice clip uses the grounded teammate from slide 28; in the
  attendees' run the keyless `dummy` teammate replies "Currently, no commands
  are available." Advice also fires every 50 steps once a real teammate is set.
- Slide 21: the three clips are one walk rendered through three cameras, and
  restart together when the slide opens. Do not offer `FullviewCamera` or
  `AgentCenteredCamera` — both raise `AttributeError` on env reset.
- Slide 22 is the code map. Have the repository open in an editor beside it.
  `mosaic/` is the reusable package; `experiment/` is one study built on it.
- Slide 23 steps through the real `main.py` call (press forward to move the
  highlight). Each highlight is one of the next seven slides; scoring is the one
  argument not in the call.
- Slides 23–30 show code exactly as it is in the files, with the real line
  numbers and a caption naming the file and lines — open the same lines in an
  editor. Slides 24–30 share one layout: the strip at the top shows where you
  are, the code is the real source, the row under it is what to change, and the
  bar at the bottom is one thing to try. Every "Try it" was run against MOSAIC before the tutorial.
  Let attendees try one or two live (24 and 27 are the quickest); describe the
  rest.
- Slide 24: the YAML counts are per room. `main.py` reads only those keys plus
  top-level `provider`, `model`, `fullscreen`; building size is set in code.
- Slide 25: `locked_room_prob` at `1.0` hangs the generator — keep it below.
- Slide 28 shows `labs/advisor.py` from the tutorial repository
  (github.com/Bkdogbey/mosaic-smc-tutorial). To try it, attendees save it as
  `src/experiment/advisor.py` and add `from .advisor import ReliableTeammate`
  and `import json` to `main.py`. Hosted providers need a key and
  `llama-index`; mention, do not attempt live.
- Slide 30: the full study runner needs the lab's `ixp` package and LSL, which
  are not installed in the tutorial. Show, do not run.

## Expected problems

| Symptom | Response |
| --- | --- |
| `ModuleNotFoundError: No module named 'mosaic'` | Confirm `mosaic_env` is active and `pip install -e .` completed in the `mosaic` directory. |
| `NameError: name 'LavaRiskVictimPlacer' is not defined` | Their clone predates the import fix. `git pull` in `mosaic`. |
| `No module named 'experiment'` | Run from the repo root with `PYTHONPATH=src`. |
| PowerShell cannot load `mosaic_env` | Use `.\mosaic_env\Scripts\Activate.ps1`; the leading `.\` is required. |
| No window or `No available video device` | The GUI needs a local graphical session. Use the fallback laptop. |
| `Alt` replies "Currently, no commands are available." | Expected — the runner uses the keyless `dummy` teammate. |
| Generation appears to hang after customization | `locked_room_prob` is at `1.0`. Use `0.9` or less. |
| More victims than expected | `num_real_victims` is per room; 12 per room across a 3×3 building is 108. |
| `AttributeError: 'FullviewCamera' object has no attribute 'reset'` | Known bug, same for `AgentCenteredCamera`. Use `AgentFOVCamera`, `AgentConeCamera`, or the default. |

## Cut list

If the session runs long:

1. Explain slides 17–19 in one minute each without pausing on every feature.
2. In the customize series, demonstrate the "Try it" yourself instead of
   waiting for everyone; skip slides 29–30 and point to the code map.
3. Describe the teammate swap on slide 28 without running it.

Do not cut the installation checkpoints, the first run, the controls, the camera
comparison, or the code map.

## Closing ask

Ask attendees to keep the small working mission and open an issue when
installation or an extension point fails on their machine. Concrete reports from
new users are the most useful outcome for the project after the tutorial.
