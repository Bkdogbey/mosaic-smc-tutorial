# Facilitator Run Sheet — MOSAIC Tutorial (two hours)

The rendered deck has 41 slides: 36 in the main tutorial, a closing slide, and
four appendix slides (the divider, installation recovery, what the teammate knows
and says, and the AI teammate interface).
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
- [ ] Merge this branch so `presentation/labs/panel.py` and `advisor.py` are on
      `main` of the tutorial repo — slides 30–31 send attendees there.
- [ ] Upstream MOSAIC carries the three fixes: `main.py` imports restored with the
      `dummy` default, the `tutorial` block set to `skip` (else `Esc` ends in
      `pygame.error: video system not initialized`), and `pygame-ce` in
      `pyproject.toml`.
- [ ] Eye-tracker demo (slide 34), presenter laptop only: install the lab's
      `ixp`, `tobii_research`, PsychoPy, and pylsl; connect the Tobii; run the
      main-game block of `src/experiment/experiment.py` with the sensor added
      once end to end; keep a screenshot of the LSL stream list as a fallback.
- [ ] At that rehearsal, record one short session (LabRecorder) and build the
      aligned timeline for slide 35, which is a placeholder until then.

## Timing

| Time | Slides | Block | Facilitator focus |
| --- | --- | --- | --- |
| 0:00–0:15 | 1–8 | Part One: why MOSAIC | The field's questions, why they need a configurable testbed, what MOSAIC is, how it works. |
| 0:15–0:50 | 9–14 | Part Two: install | Prerequisites, clone, install and check, run the included mission. |
| 0:50–1:08 | 15–19 | Part Three: experience | Play one mission as a participant: objective, interface and tiles, victims, controls. No code. |
| 1:08–1:14 | 20–22 | Part Four: the map | The runtime, then the starting code every task edits. |
| 1:14–1:26 | 23–26 | The mission | Victims, decoys, and lava; locked rooms; rewards; the time limit. |
| 1:26–1:37 | 27–30 | The interface | Cameras, then camera, feedback, and info-panel tasks. |
| 1:37–1:45 | 31–32 | The teammate | Reliability, then advice timing with the same teammate. |
| 1:45–1:55 | 33–35 | Sensing | What each step records, the live eye tracker, the synchronized record. |
| 1:55–2:00 | 36–37 | Wrap-up | Where to go next (the code map), then questions; appendix slides as needed. |

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
  Gymnasium/MiniGrid detail here; it appears on Runtime Architecture (slide 21).
- Slide 7 introduces the task participants perform: search and rescue.
- Slide 8 is the core claim of the tutorial. The teammate advises; the
  participant retains final action authority. Say it out loud.
- Keep Part One to fifteen minutes. Its purpose is to make the hands-on work
  meaningful, not to be complete.

## Part Two notes (slides 9–14)

- Ask attendees to use Python 3.10 or 3.11 for a shared troubleshooting baseline.
  MOSAIC's `pyproject.toml` claims 3.8+, but the code needs 3.10.
- Slide 10 groups the packages `pip install -e .` brings in by role. Nothing is
  installed by hand.
- Slide 11 clones one repository. The numbered notes on the right match the
  code line numbers. Everyone stays in `mosaic` all session.
- Slide 12 is three commands: upgrade pip, `pip install -e .`, then a one-line
  import check. Mention that `-e` (editable) is what lets Part Four's edits take
  effect without reinstalling. Do not advance until most attendees see
  `MOSAIC ready`; the `pygame-ce` banner above it will show their own versions.
- Slide 13 launches `PYTHONPATH=src python -m experiment.main` — MOSAIC's own
  study runner. The screenshot is the stock first frame (`gui-first-frame.png`):
  a crowded room and about 108 remaining. It opens fullscreen; F11 gives a
  window. The terminal fills with font warnings and `connect_all failed` lines;
  both are harmless. Anyone who cloned before the import fix needs `git pull`.
- Hold at slide 14 until most attendees can move the agent. Ask everyone to
  leave the game open for Part Three. The appendix recovery slide is available
  while helpers work with individual machines.

## Part Three notes (slides 15–19): experience the mission

No code in this part. Attendees play the baseline mission and learn to read it.

- Slide 16 states the objective: explore, tell real victims from decoys, decide
  who to rescue before time runs out. The clip is the real interface: one real
  victim (green flash, +1), one decoy (red flash, −1), then another real victim.
  Anyone who closed the game relaunches it now with the slide 13 command.
- Slide 17 reveals one region at a time — press forward five times. The
  screenshot is caught mid-flash, so the green glow around the game view is the
  edge vignette firing after a rescue — point at it. The legend on the right
  names every tile with its rule: lava ends the mission, a door opens with
  `Space`, a locked door needs the key of its color.
- Slide 18 labels the real-victim and decoy rows directly. Both are red T
  shapes; the decoy's stem is off-center. Point at one of each on screen. The reusable
  `VictimPlacer` places real victims only; decoys come from the study layer's
  `LavaRiskVictimPlacer`. Health drains only in the lab's study env
  (`TunedPickupVictimEnv`), faster near lava, and the bar is drawn only while
  advice is on screen. In the tutorial's run health stays full — say so if asked.
- Slide 19: each clip shows one action. `Tab` does both pickup and rescue on
  purpose. The advice clip uses the grounded teammate from slide 31; the slide
  tells attendees their own `Alt` gets "Currently, no commands are available."
  from the keyless `dummy` teammate. Let everyone move, open a door, pick up a key, and rescue a
  victim before Part Four.

## Part Four notes (slides 20–35): configure MOSAIC

- Slide 21 (runtime architecture) is the map: which part of the window is which
  component. Slide 22 steps through the real `main.py` call (press forward to
  move the highlight); every task that follows edits this call or
  `configs/experiment.yaml`.
- Each section follows the order of that call: the mission (23–26), the
  interface (27–30), the teammate (31–32), and sensing (33–35). The strip at
  the top of every slide shows the section.
- Task slides share one layout. Left: Change (an editor-style card: the file and
  where in it on the header, the edit as a diff underneath, muted line out and
  orange line in) and Run (what to do after saving, plus a question for the
  room). Ask the question and wait for a guess, then press forward: Observe shows
  before/after images rendered from real MOSAIC, Interpret names the research
  variable, and the undo command resets the file. Every task starts from stock
  files, except the advice-timing task (32), which keeps the teammate from 31.
  Let attendees try 23 and 27 live; for the rest, predict and reveal.
- Every task slide ends its left column with a "Lives in" card: the package
  file and class behind the setting, and what you would change there for more
  than the one knob. Point at it; do not read it out. On slide 31 it also says
  how to switch to a hosted LLM (`provider:` / `model:` in the YAML, key in
  `.env`, built in `src/experiment/llm.py`).
- Slide 25 (rewards): the code includes its import; without it the run fails
  with `NameError`. Slide 26 (time limit) is a one-line YAML change.
- Top-level YAML keys: `main.py` passes the whole YAML to `SAREnvGUI`, which
  reads `max_time`, `llm_nudge_interval`, and `prompt_type` from the top level.
  The same keys under `game:` configure the lab's study runner, not this run —
  that is why the tasks add them as new top-level lines.
- Slide 23: the YAML counts are per room; the before/after is the same building.
  Slide 24: `locked_room_prob` at `1.0` hangs the generator — keep it below. The
  lock setting changes how the building generates, so its before/after are two
  buildings; the slide quotes their locked-door counts.
- Slide 27: the three clips are one walk rendered through three cameras. Do not
  offer `FullviewCamera` or `AgentCenteredCamera` — both raise `AttributeError`
  on env reset.
- Slide 30 uses `labs/panel.py` and slide 31 uses `labs/advisor.py`, both from
  the tutorial repository (github.com/Bkdogbey/mosaic-smc-tutorial, shown on
  the slides): attendees download each into `src/experiment/` first. Hosted providers need a key and
  `llama-index`; mention, do not attempt live.
- Slide 31 says to keep the teammate change; slide 32 builds on it, so the
  unprompted message is real advice. Anyone who undid slide 31 gets the dummy's
  "Currently, no commands are available." — same timing, empty content. Slide
  32's undo resets both files.
- Slide 33 prints the observation fields; the list lands among the launch
  warnings, above the window. The full study runner that streams them needs the
  lab's `ixp` package and LSL, which are not installed in the tutorial.
- Slide 34 is the live eye-tracking demo, instructor-only. The slide shows no
  installation on purpose: attendees cannot follow along (the lab's `ixp` is
  not on PyPI, and it needs the hardware). Demo setup on the presenter laptop:
  1. Install `ixp` from the lab's sibling repo (`pip install -e ../ixp`),
     `tobii-research`, PsychoPy, pylsl, and ray; open LabRecorder.
  2. In `src/experiment/experiment.py`, add the two calls shown on the slide
     (`register_sensor`, `calibrate_sensor`) to the `sar_experiment_test`
     block, set that block to `"run"` and every other block to `"skip"`.
     (`tobii_test` is the sensor-only version, if the game part fails.)
  3. `SARGame` runs three trials in random order (OpenAI, dummy, Gemini), each
     up to `game: max_time` (15 minutes in the stock YAML). For the demo, put
     both API keys in `.env`, set `max_time: 2` under `game:`, and press `Esc`
     to end a trial early; `Esc` ends the current trial.
  4. `python -m experiment.experiment` from the `mosaic` folder. Calibration is
     five dots; SPACE accepts, R redoes. Then the volunteer plays.
  5. Press forward to reveal item 3 once LabRecorder shows both streams
     (TobiiEyeTracker and the game trial).

  If the device fails, show the rehearsal screenshot and move on.
- Slide 35 is a placeholder until the rehearsal recording exists; with one eye
  tracker in the room, everyone inspects that prepared recording.
- The result images come from `tools/capture_config_results.py` (and the
  camera and chat captures). Re-run it if MOSAIC's rendering changes, and
  re-check the locked-door counts quoted on slide 24.
- Slide 36 is the wrap-up: the code map, with each card's "Customize" line
  naming the tasks done today. Point at `src/experiment/` as the folder to copy.
- Appendix slide 40 (what the teammate knows and says) is for Q&A: the prompt
  table shows the teammate sees objects the participant cannot; `prompt_type`
  only matters for hosted LLM teammates.

## Expected problems

| Symptom | Response |
| --- | --- |
| `ModuleNotFoundError: No module named 'mosaic'` | Confirm `mosaic_env` is active and `pip install -e .` completed in the `mosaic` directory. |
| `NameError: name 'LavaRiskVictimPlacer' is not defined` | Their clone predates the import fix. `git pull` in `mosaic`. |
| `pygame.error: video system not initialized` after `Esc` | Their clone predates the `tutorial`-block fix. `git pull` in `mosaic`; the mission itself was fine. |
| `NameError: name 'RescueAction' is not defined` | The rewards import is missing; it is the first line of the slide 25 code card. |
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

1. In Part Three, explain slides 17–18 in one minute each.
2. In Part Four, ask the question and reveal the result yourself instead of
   waiting for everyone; show slides 25–26 in one minute each.
3. Describe the teammate swap on slide 31 without running it (then slide 32's
   result comes from the slide, not the room).
4. Drop the eye-tracker demo (34) if the device is not ready; show the
   rehearsal screenshot instead.

Do not cut the installation checkpoints, the first run, the controls, the
camera comparison, or the wrap-up (36).

## Closing ask

Ask attendees to keep the small working mission and open an issue when
installation or an extension point fails on their machine. Concrete reports from
new users are the most useful outcome for the project after the tutorial.
