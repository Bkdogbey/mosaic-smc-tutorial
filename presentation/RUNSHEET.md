# Facilitator Run Sheet — MOSAIC Tutorial (two hours)

The rendered deck has 42 slides: 37 in the main tutorial, a closing slide, and
four appendix slides (the divider, the code map, and two reference slides).
The main sequence runs in four parts: why MOSAIC exists, install it, experience
one mission, then configure it.

## Before the room opens

- [ ] Render `mosaic-tutorial.qmd` and open `index.html` in a browser.
- [ ] Test the deck at the projector's 16:9 resolution (authored at 1280×720).
- [ ] Keep one working MOSAIC environment and one running mission as a fallback.
- [ ] Test a clean Windows PowerShell install with the `mosaic_env` commands.
- [ ] Test the Conda alternative in a separate clean environment.
- [ ] Send `SETUP.md` to attendees before the conference.
- [ ] Ask one lab member to help with installation during Part Two.
- [ ] Confirm `PYTHONPATH=src python -m experiment.main` opens a window.
- [ ] Eye-tracker demo (slide 36), presenter laptop only: install the lab's
      `ixp`, `tobii_research`, PsychoPy, and pylsl; connect the Tobii; run the
      main-game block of `src/experiment/experiment.py` with the sensor added
      once end to end; keep a screenshot of the LSL stream list as a fallback.
- [ ] At that rehearsal, record one short session (LabRecorder) and build the
      aligned timeline for slide 37, which is a placeholder until then.

## Timing

| Time | Slides | Block | Facilitator focus |
| --- | --- | --- | --- |
| 0:00–0:15 | 1–8 | Part One: why MOSAIC | The field's questions, why they need a configurable testbed, what MOSAIC is, how it works. |
| 0:15–0:50 | 9–15 | Part Two: install | Prerequisites, clone, install, verify, run the included mission. |
| 0:50–1:08 | 16–21 | Part Three: experience | Play one mission as a participant: objective, interface and tiles, victims, controls. No code. |
| 1:08–1:14 | 22–24 | Part Four: the map | The runtime, then the starting code every task edits. |
| 1:14–1:25 | 25–27 | The mission | Victims, decoys, and lava; locked rooms; rewards and the time limit. |
| 1:25–1:37 | 28–31 | The interface | Cameras, then camera, feedback, and info-panel tasks. |
| 1:37–1:48 | 32–34 | The teammate | Reliability, advice timing, what it knows and says. |
| 1:48–1:57 | 35–37 | Sensing | What each step records, the live eye tracker, the synchronized record. |
| 1:57–2:00 | 38 | Questions | Close on the working baseline; use appendix slides as needed. |

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
  Gymnasium/MiniGrid detail here; it appears on Runtime Architecture (slide 23).
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
  `-e` (editable) is what lets Part Four's edits take effect without reinstalling.
- Do not advance from slide 13 until most attendees see `MOSAIC ready`.
- Slide 14 launches `PYTHONPATH=src python -m experiment.main` — MOSAIC's own
  study runner. The GIF on the slide is the real interface: one real victim
  (green flash, +1), one decoy (red flash, −1), then another real victim. Talk
  through it while people are still installing. It opens fullscreen; F11 gives
  a window. Anyone who cloned before the import fix landed needs `git pull`.
- Hold at slide 15 until most attendees can move the agent, then ask everyone to
  press `Esc`. The appendix recovery slide is available while helpers work with
  individual machines.

## Part Three notes (slides 16–21): experience the mission

No code in this part. Attendees play the baseline mission and learn to read it.

- Slide 17 states the objective: explore, tell real victims from decoys, decide
  who to rescue before time runs out. The clip is the real interface.
- Slide 18 relaunches the game. Most attendees closed it at the checkpoint;
  wait for most windows to be open, windowed with `F11`, before moving on.
- Slide 19 reveals one region at a time — press forward five times. The
  screenshot is caught mid-flash, so the green glow around the game view is the
  edge vignette firing after a rescue — point at it. The legend on the right
  names every tile with its rule: lava ends the mission, a door opens with
  `Space`, a locked door needs the key of its colour.
- Slide 20 labels the real-victim and decoy rows directly. The reusable
  `VictimPlacer` places real victims only; decoys come from the study layer's
  `LavaRiskVictimPlacer`. Health drains only in the lab's study env
  (`TunedPickupVictimEnv`), faster near lava, and the bar is drawn only while
  advice is on screen. In the tutorial's run health stays full — say so if asked.
- Slide 21: each clip shows one key. `Tab` does both pickup and rescue on
  purpose. The advice clip uses the grounded teammate from slide 32; in the
  attendees' run the keyless `dummy` teammate replies "Currently, no commands
  are available." Let everyone move, open a door, pick up a key, and rescue a
  victim before Part Four.

## Part Four notes (slides 22–37): configure MOSAIC

- Slide 23 (runtime architecture) is the map: which part of the window is which
  component. Slide 24 steps through the real `main.py` call (press forward to
  move the highlight); every task that follows edits this call or
  `configs/experiment.yaml`.
- Each section follows the order of that call: the mission (25–27), the
  interface (28–31), the teammate (32–34), and sensing (35–37). The strip at
  the top of every slide shows the section.
- Task slides share one layout. Left: Change (an editor-style card: the file and
  where in it on the header, the edit as a diff underneath, muted line out and
  orange line in) and Run (what to do after saving, plus a question for the
  room). Ask the question and wait for a guess, then press forward: Observe shows
  before/after images rendered from real MOSAIC, Interpret names the research
  variable, and the undo command resets the file. Every task starts from stock
  files. Let attendees try 25 and 29 live; for the rest, predict and reveal.
- Slides 27 and 34 each show two settings side by side, without a live edit.
- Top-level YAML keys: `main.py` passes the whole YAML to `SAREnvGUI`, which
  reads `max_time`, `llm_nudge_interval`, and `prompt_type` from the top level.
  The same keys under `game:` configure the lab's study runner, not this run —
  that is why the tasks add them as new top-level lines.
- Slide 25: the YAML counts are per room; the before/after is the same building.
  Slide 26: `locked_room_prob` at `1.0` hangs the generator — keep it below. The
  lock setting changes how the building generates, so its before/after are two
  buildings; the slide quotes their locked-door counts.
- Slide 28: the three clips are one walk rendered through three cameras. Do not
  offer `FullviewCamera` or `AgentCenteredCamera` — both raise `AttributeError`
  on env reset.
- Slide 31 uses `labs/panel.py` and slide 32 uses `labs/advisor.py`, both from
  the tutorial repository (github.com/Bkdogbey/mosaic-smc-tutorial): attendees
  save each into `src/experiment/` first. Hosted providers need a key and
  `llama-index`; mention, do not attempt live.
- Slide 33: with the keyless dummy teammate the unprompted message is "Currently,
  no commands are available." The point is that it arrives without `Alt`.
- Slide 34: the table is real output of MOSAIC's default prompt builder,
  trimmed to five columns; the quotes are the example replies in MOSAIC's
  `prompts.yaml`.
- Slide 35: the full study runner needs the lab's `ixp` package and LSL, which
  are not installed in the tutorial. Show, do not run.
- Slide 36 is instructor-only: connect and calibrate the Tobii, a volunteer
  plays a short mission, and show both LSL streams (TobiiEyeTracker and the game
  trial). If the device fails, show the rehearsal screenshot and move on.
- Slide 37 is a placeholder until the rehearsal recording exists; with one eye
  tracker in the room, everyone inspects that prepared recording.
- The result images come from `tools/capture_config_results.py` (and the
  camera and chat captures). Re-run it if MOSAIC's rendering changes, and
  re-check the locked-door counts quoted on slide 26.

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
| `max_time`, `llm_nudge_interval`, or `prompt_type` has no effect | The key is under `game:`. Add it as a top-level line instead. |

## Cut list

If the session runs long:

1. In Part Three, explain slides 19–20 in one minute each.
2. In Part Four, ask the question and reveal the result yourself instead of
   waiting for everyone; show slides 27 and 34 in one minute each.
3. Describe the teammate swap on slide 32 without running it.
4. Drop the eye-tracker demo (37) if the device is not ready; show the
   rehearsal screenshot instead.

Do not cut the installation checkpoints, the first run, the controls, or the
camera comparison. The code map is in the appendix (slide 40).

## Closing ask

Ask attendees to keep the small working mission and open an issue when
installation or an extension point fails on their machine. Concrete reports from
new users are the most useful outcome for the project after the tutorial.
