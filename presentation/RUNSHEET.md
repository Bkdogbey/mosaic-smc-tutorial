# Facilitator Run Sheet — MOSAIC Tutorial (two hours)

The rendered deck has 36 slides: 31 in the main tutorial, a closing slide, and
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
| 0:00–0:15 | 1–8 | Part One | Why the testbed exists and what human–AI teaming questions it supports. |
| 0:15–0:45 | 9–13 | Part Two: install | Prerequisites, clone, install, verify. |
| 0:45–1:00 | 14–15 | First run | Launch the mission and troubleshoot stragglers. |
| 1:00–1:08 | 16–18 | Relaunch and architecture | Everyone reopens the game; what each part of the window is. |
| 1:08–1:22 | 19–22 | Interface and task | The interface, task objects, controls, cameras — try each live. |
| 1:22–1:30 | 23–24 | Code map | Where each part lives, and how `main.py` composes them. |
| 1:30–1:55 | 25–31 | Customize | One component per slide, about 3.5 minutes each, one "Try it" each. |
| 1:55–2:00 | 32 | Questions | Close on the working baseline; use appendix slides as needed. |

## Part One notes (slides 1–8)

- There is no Part One divider — the deck opens straight into the lab and the
  motivation. The first divider is slide 9.
- Part One runs why → what → how: the field's questions (3), why they need a
  configurable testbed (4), what MOSAIC is (5), how it works (6), then the task (7) and the
  teaming loop (8).
- Slide 3 names six questions human–AI teaming research asks, one theme per
  row: reliance (trust and reliance, decisions under pressure), what the person
  knows and can handle (situation awareness, cognitive state), and the AI side
  (AI teammate design — the lab's own none / GPT / Gemini comparison — and
  adaptive assistance). Its last line is the bridge: answering them means
  observing the interaction as it unfolds.
- Slide 4 argues for a configurable testbed without naming MOSAIC yet: four
  capabilities, 01–04, that one experiment needs and existing tools rarely
  combine. The slide leaves out what studies often do instead — say it: a single
  accept-or-reject judgment, an AI that stays fixed or shifts unpredictably, a
  new testbed for every question, separate systems on separate clocks.
- Slide 5 defines MOSAIC (Modular System for Adaptive Human–AI Collaboration)
  and answers slide 4 box for box, in the same positions: the task, a
  controllable teammate, conditions set per study, and one synchronized record.
- Slide 6 is the system overview: human, MOSAIC task, and AI teammate on top;
  study sensors, LSL, and session data underneath. Do not add the
  Gymnasium/MiniGrid detail here; it appears on Runtime Architecture (slide 18).
- Slide 7 introduces the task participants perform: search and rescue.
- Slide 8 is the core claim of the tutorial. The teammate advises; the
  participant retains final action authority. Say it out loud.
- Keep Part One to fifteen minutes. Its purpose is to make the hands-on work
  meaningful, not to be complete.

## Part Two notes (slides 9–15)

- Ask attendees to use Python 3.10 or 3.11 for a shared troubleshooting baseline.
  MOSAIC's `pyproject.toml` claims 3.8+, but the code needs 3.10.
- Slide 10 groups the packages `pip install -e .` brings in by role. Nothing is
  installed by hand.
- Slide 11 clones one repository. The numbered notes on the right match the
  code line numbers. Everyone stays in `mosaic` all session.
- Slide 12 is two commands: upgrade pip, then `pip install -e .`. Mention that
  `-e` (editable) is what lets Part Three's edits take effect without reinstalling.
- Do not advance from slide 13 until most attendees see `MOSAIC ready`.
- Slide 14 launches `PYTHONPATH=src python -m experiment.main` — MOSAIC's own
  study runner. The GIF on the slide is the real interface: one real victim
  (green flash, +1), one decoy (red flash, −1), then another real victim. Talk
  through it while people are still installing. It opens fullscreen; F11 gives
  a window. Anyone who cloned before the import fix landed needs `git pull`.
- Hold at slide 15 until most attendees can move the agent, then ask everyone to
  press `Esc`. The appendix recovery slide is available while helpers work with
  individual machines.

## Part Three notes (slides 16–31)

- Slide 17 relaunches the game. Most attendees closed it at the checkpoint;
  wait for most windows to be open, windowed with `F11`, before moving on.
- Slide 18 is the runtime: participant, GUI, and environment in a loop, with
  sensing, the AI teammate, and Gymnasium/MiniGrid beneath them. Point at the
  attendee's own window. The chat image is a real reply from the slide-29
  teammate. Sensors never connect to the game directly: they stream into Lab
  Streaming Layer, which puts sensor and game samples on one clock. Sensing
  exists only in the lab's study runner, not this run.
- Slide 19 reveals one region at a time — press forward five times. The
  screenshot is caught mid-flash, so the green glow around the game view is the
  edge vignette firing after a rescue — point at it.
- Slide 20 labels the real-victim and decoy rows directly. The reusable
  `VictimPlacer` places real victims only; decoys come from the study layer's
  `LavaRiskVictimPlacer`. The health strip shows the white health bar. Health
  drains only in the lab's study env (`TunedPickupVictimEnv`), faster near lava,
  and the bar is drawn only while advice is on screen. In the tutorial's run
  health stays full — say so if asked why nobody sees it.
- Slide 21: each clip shows one key. `Tab` does both pickup and rescue on
  purpose. The advice clip uses the grounded teammate from slide 29; in the
  attendees' run the keyless `dummy` teammate replies "Currently, no commands
  are available." Advice also fires every 50 steps once a real teammate is set.
- Slide 22: the three clips are one walk rendered through three cameras, and
  restart together when the slide opens. Do not offer `FullviewCamera` or
  `AgentCenteredCamera` — both raise `AttributeError` on env reset.
- Slide 23 is the code map. Have the repository open in an editor beside it.
  `mosaic/` is the reusable package; `experiment/` is one study built on it.
- Slide 24 steps through the real `main.py` call (press forward to move the
  highlight). Each highlight is one of the next seven slides; scoring is the one
  argument not in the call.
- Slides 24–31 show code exactly as it is in the files, with the real line
  numbers and a caption naming the file and lines — open the same lines in an
  editor. Slides 25–31 share one layout: the strip at the top shows where you
  are, the code is the real source, the row under it is what to change, and the
  bar at the bottom is one thing to try. Every "Try it" was run against MOSAIC before the tutorial.
  Let attendees try one or two live (25 and 28 are the quickest); describe the
  rest.
- Slide 25: the YAML counts are per room. `main.py` reads only those keys plus
  top-level `provider`, `model`, `fullscreen`; building size is set in code.
- Slide 26: `locked_room_prob` at `1.0` hangs the generator — keep it below.
- Slide 29 shows `labs/advisor.py` from the tutorial repository
  (github.com/Bkdogbey/mosaic-smc-tutorial). To try it, attendees save it as
  `src/experiment/advisor.py` and add `from .advisor import ReliableTeammate`
  and `import json` to `main.py`. Hosted providers need a key and
  `llama-index`; mention, do not attempt live.
- Slide 31: the full study runner needs the lab's `ixp` package and LSL, which
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

1. Explain slides 18–20 in one minute each without pausing on every feature.
2. In the customize series, demonstrate the "Try it" yourself instead of
   waiting for everyone; skip slides 30–31 and point to the code map.
3. Describe the teammate swap on slide 29 without running it.

Do not cut the installation checkpoints, the first run, the controls, the camera
comparison, or the code map.

## Closing ask

Ask attendees to keep the small working mission and open an issue when
installation or an extension point fails on their machine. Concrete reports from
new users are the most useful outcome for the project after the tutorial.
