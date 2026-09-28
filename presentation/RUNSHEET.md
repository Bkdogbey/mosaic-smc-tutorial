# Facilitator Run Sheet — MOSAIC Tutorial (two hours)

The rendered deck has 46 slides: 35 in the main tutorial, a closing slide, and
10 appendix slides (the divider, seven more changes and details, installation
recovery, and the AI teammate interface). The main sequence runs in four parts: why MOSAIC exists,
install it, experience one mission, then configure it by walking through
`experiment/main.py` one part at a time.

## Before the room opens

- [ ] Render `mosaic-tutorial.qmd` and open `index.html` in a browser.
- [ ] Test the deck at the projector's 16:9 resolution (authored at 1280×720).
- [ ] Keep one working MOSAIC environment and one running mission as a fallback.
- [ ] Test a clean Windows PowerShell install with the `mosaic_env` commands.
- [ ] Test the Conda alternative in a separate clean environment.
- [ ] Send `SETUP.md` to attendees before the conference.
- [ ] Ask one lab member to help with installation during Part Two.
- [ ] Confirm `PYTHONPATH=src python -m experiment.main` opens a window.
- [ ] `presentation/labs/panel.py` and `advisor.py` are on `main` of the tutorial
      repo (appendix slides 41 and 44 send people there).
- [ ] **LLM demo (slide 28), presenter machine only.** Install
      `llama-index-llms-openai` in `mosaic_env`, put the lab's key in the
      presenter's `.env`, and add `provider: openai` / `model:` to the YAML only
      when you reach slide 28. Test `gpt-4o-mini` and `gpt-5-mini-2025-08-07` and
      pick the model by reply time; if it is not `gpt-4o-mini`, update the model
      line on slides 27, 28, and 43. **Never put the key in the repo or the deck: the
      deck is public on GitHub Pages.**
- [ ] With the key, capture a real LLM reply for slide 28 (it shows a placeholder
      until then).
- [ ] Upstream MOSAIC carries the three fixes: `main.py` imports restored with the
      `dummy` default, the `tutorial` block set to `skip` (else `Esc` ends in
      `pygame.error: video system not initialized`), and `pygame-ce` in
      `pyproject.toml`.
- [ ] Eye-tracker demo (slide 33), presenter laptop only: install the lab's
      `ixp`, `tobii_research`, PsychoPy, and pylsl; connect the Tobii; run the
      main-game block of `src/experiment/experiment.py` with the sensor added
      once end to end; keep a screenshot of the LSL stream list as a fallback.
- [ ] At that rehearsal, record one short session (LabRecorder) and build the
      aligned timeline for slide 34, which is a placeholder until then.

## Timing

| Time | Slides | Block | Facilitator focus |
| --- | --- | --- | --- |
| 0:00–0:15 | 1–8 | Part One: why MOSAIC | The field's questions, why they need a configurable testbed, what MOSAIC is, how it works. |
| 0:15–0:50 | 9–14 | Part Two: install | Prerequisites, clone, install and check, run the included mission. |
| 0:50–1:08 | 15–19 | Part Three: experience | Play one mission as a participant: objective, interface and tiles, victims, controls. No code. |
| 1:08–1:14 | 20–22 | Part Four: the map | The runtime, then `main.py` stepped through part by part (4.1–4.5). |
| 1:14–1:23 | 23–24 | 4.1 The world | Three things to change; everyone changes the counts. |
| 1:23–1:31 | 25–26 | 4.2 The camera | Three cameras; everyone swaps the camera. |
| 1:31–1:40 | 27–28 | 4.3 The teammate | Three things to change; the real LLM, live. |
| 1:40–1:46 | 29–30 | 4.4 The interface | Three things to change; the decoy flash, demoed. |
| 1:46–1:57 | 31–34 | 4.5 Sensing | Three things to change; what each step records (everyone), the live eye tracker, the synchronized record. |
| 1:57–2:00 | 35–36 | Wrap-up | Where to go next, then questions; appendix slides as needed. |

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
  purpose. The advice clip uses the keyless map-reading teammate from appendix slide 44; the slide
  tells attendees their own `Alt` gets "Currently, no commands are available."
  from the keyless `dummy` teammate. Let everyone move, open a door, pick up a key, and rescue a
  victim before Part Four.

## Part Four notes (slides 20–34): configure MOSAIC

- Part Four walks through `experiment/main.py`, the file attendees launched in
  Part Two, in five numbered parts: 4.1 the world, 4.2 the camera, 4.3 the
  teammate, 4.4 the interface, 4.5 sensing. The strip at the top of each slide
  shows the part.
- Slide 21 (runtime architecture) maps the window to its components. Slide 22
  steps through the real `main.py` call (press forward to move the highlight);
  each highlight is one numbered part, in order.
- Each part opens with one slide (23, 25, 27, 29, 31): the exact `main.py` lines
  on the left, **three things to change** on the right, each as the setting and
  what it changes for the participant. The highlighted one is the example that
  follows. Keep each to about a minute: name the three, then move on.
- Example slides share one layout: Change (an editor-style card with the file
  and where in it, the edit as a diff), Run, a question for the room, then
  "What happens" with before/after images from real MOSAIC and the undo
  command. Every example starts from the stock files.
- The badge under each example says who does it. **Try it** (24 counts, 26
  camera, 32 records): everyone, live. **Presenter demo** (28 the LLM, 30 the
  flash): you, on the projector.
- Top-level YAML keys: `main.py` passes the whole YAML to `SAREnvGUI`, which
  reads `max_time`, `llm_nudge_interval`, and `prompt_type` from the top level.
  The same keys under `game:` configure the lab's study runner, not this run.
- Slide 24: the YAML counts are per room; the before/after is the same building.
- Slide 25: the three clips are one walk rendered through three cameras. Do not
  offer `FullviewCamera` or `AgentCenteredCamera`; both raise `AttributeError`
  on env reset.
- Slide 28 (the real LLM): only the presenter connects. `build_llm_client`
  connects on the first `Alt`, so a bad key shows as a chat error, not a crash.
  If the API is down, use the keyless teammate (appendix 44) instead. If asked
  what the LLM actually sees, appendix 42 shows it: every real victim, even out
  of view, and **no decoys** (`process_prompts.py` skips them).
- Slide 32 prints the observation fields; the list lands among the launch
  warnings, above the window. The full study runner that streams them needs the
  lab's `ixp` package and LSL, which are not installed in the tutorial.
- Slide 33 is the live eye-tracking demo, instructor-only. The slide shows no
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
- Slide 34 is a placeholder until the rehearsal recording exists; with one eye
  tracker in the room, everyone inspects that prepared recording.
- The result images come from `tools/capture_config_results.py` (and the
  camera and chat captures). Re-run it if MOSAIC's rendering changes, and
  re-check the locked-door counts quoted on appendix slide 38.
- Slide 35 (where to go next) is the code map. Point at `src/experiment/` as
  the folder to copy for a new study.
- Appendix 38–44 hold the other changes from the part slides, in the same
  layout: locked rooms, rescue rewards, the time limit (at 0:00 the timer stops
  but the mission keeps going), the info panel, what the teammate is told, how
  it talks (needs the real LLM), and a keyless map-reading teammate.

## Expected problems

| Symptom | Response |
| --- | --- |
| `ModuleNotFoundError: No module named 'mosaic'` | Confirm `mosaic_env` is active and `pip install -e .` completed in the `mosaic` directory. |
| `NameError: name 'LavaRiskVictimPlacer' is not defined` | Their clone predates the import fix. `git pull` in `mosaic`. |
| `pygame.error: video system not initialized` after `Esc` | Their clone predates the `tutorial`-block fix. `git pull` in `mosaic`; the mission itself was fine. |
| `NameError: name 'RescueAction' is not defined` | The rewards import is missing; it is the first line of the appendix slide 39 code card. |
| `No module named 'experiment'` | Run from the repo root with `PYTHONPATH=src`. |
| PowerShell cannot load `mosaic_env` | Use `.\mosaic_env\Scripts\Activate.ps1`; the leading `.\` is required. |
| No window or `No available video device` | The GUI needs a local graphical session. Use the fallback laptop. |
| `Alt` replies "Currently, no commands are available." | Expected: the runner uses the keyless `dummy` teammate. In the LLM demo it means the `provider:` line is missing or not at the top level of the YAML. |
| Chat shows an authentication or 401 error | The key in `.env` is mistyped, has spaces, or the file is not in the `mosaic` folder. |
| Chat shows `No module named 'llama_index'` | `python -m pip install llama-index-llms-openai` with `mosaic_env` active. |
| LLM replies are slow or show a rate-limit error | Wait and retry; if it persists, switch to the keyless teammate (appendix 44). |

| Generation appears to hang after customization | `locked_room_prob` is at `1.0`. Use `0.9` or less. |
| More victims than expected | `num_real_victims` is per room; 12 per room across a 3×3 building is 108. |
| `AttributeError: 'FullviewCamera' object has no attribute 'reset'` | Known bug, same for `AgentCenteredCamera`. Use `AgentFOVCamera`, `AgentConeCamera`, or the default. |
| `max_time`, `llm_nudge_interval`, or `prompt_type` has no effect | The key is under `game:`. Add it as a top-level line instead. |

## Cut list

If the session runs long:

1. In Part Three, explain slides 17–18 in one minute each.
2. Keep the part slides (23, 25, 27, 29, 31) to thirty seconds each.
3. Make the camera swap (26) a presenter demo instead of a live try.
4. Drop the eye-tracker demo (33) if the device is not ready; show the
   rehearsal screenshot instead.

Do not cut the installation checkpoints, the first run, the controls, the
`main.py` walkthrough (22), or the LLM demo (28).

## Closing ask

Ask attendees to keep the small working mission and open an issue when
installation or an extension point fails on their machine. Concrete reports from
new users are the most useful outcome for the project after the tutorial.
