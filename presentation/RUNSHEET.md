# Facilitator Run Sheet — MOSAIC Tutorial (two hours, plus a 15-minute break)

The rendered deck has 40 slides: 34 in the main tutorial (one of them the break
slide after Part Three), a closing slide, and
5 appendix slides (the divider and four more changes). One more slide, *The Synchronized Record*, is hidden until the
rehearsal recording exists (see below); it is not counted.

The main sequence runs in four parts: why MOSAIC exists, install it, experience
one mission, then configure it by walking through `experiment/main.py` in four
parts: **SAR**, **GUI**, **LLM**, and **Sensing**.

## Before the room opens

- [ ] Render `mosaic-tutorial.qmd` and open `index.html` in a browser.
- [ ] Test the deck at the projector's 16:9 resolution (authored at 1280×720).
- [ ] Keep one working MOSAIC environment and one running mission as a fallback.
- [ ] Test a clean Windows PowerShell install with the `mosaic_env` commands.
- [ ] Test the Conda alternative in a separate clean environment.
- [ ] Send `SETUP.md` to attendees before the conference.
- [ ] Ask one lab member to help with installation during Part Two.
- [ ] Confirm `PYTHONPATH=src python -m experiment.main` opens a window, and that
      `F11` (macOS: `fn`+`F11`) leaves fullscreen on the machines you can test.
- [ ] `presentation/labs/advisor.py` is on `main` of the tutorial repo. **Slide 30
      (everyone) sends people there**, so test the download and the
      `ReliableTeammate(0.7)` edit on a clean clone. `panel.py` (appendix slide
      39) is the same.
- [ ] **No API keys in this session.** Nothing in the tutorial connects to a
      hosted model, on the presenter machine or anyone else's. Slide 31 (the
      real LLM) is walked through as "on your own", not run. The teammate
      everyone sees give real advice is the keyless `ReliableTeammate` (slide
      30). Leave `provider:` out of the presenter's YAML, or set it to `dummy`.
- [ ] Upstream MOSAIC fixes, checked against `iHuman-Lab/mosaic` main
      (`1018587`, Sep 30) on a clean clone with Python 3.11:
      - Landed: `main.py` imports restored; the `tutorial` block set to `skip`
        (so `Esc` exits cleanly).
      - **Not landed: the `dummy` default.** `main.py` line 48 still defaults
        the provider to `openai`, so `Alt` replies "Import tabulate failed"
        instead of "Currently, no commands are available." (slides 19, 29, 30).
        If it is still missing on the day, have everyone add `provider: dummy`
        as a top-level line in `configs/experiment.yaml` at slide 13.
      - **Not landed: `pygame-ce` in `pyproject.toml`.** Slide 12 now carries
        the two-line fix, so the install works either way. Take lines 3–4 off
        the slide once upstream depends on `pygame-ce`.
      - **Not landed: `tabulate` in `pyproject.toml`.** Only a real LLM needs
        it; slide 31 lists it.
- [ ] Eye-tracker demo (slide 33), presenter laptop only: install the lab's
      `ixp`, `tobii_research`, PsychoPy, and pylsl; connect the Tobii; run the
      main-game block of `src/experiment/experiment.py` with the sensor added
      once end to end; keep a screenshot of the LSL stream list as a fallback.
- [ ] At that rehearsal, record one short session (LabRecorder) and build the
      aligned timeline. Then **unhide** the *Synchronized Record* slide in
      `mosaic-tutorial.qmd` (delete `{visibility="hidden"}` from its heading) and
      replace its placeholder with the timeline. It would become slide 34.
- [ ] **Notebook.** The slides point at a notebook for the building settings
      (counts, size, locked rooms) and for printing the observation fields
      (slides 24 and 32). It is `notebooks/02_mosaic_human_ai.ipynb` in the
      MOSAIC repository attendees clone: Step 6 is the building settings, Step
      4 the observation fields, Steps 8–9 record and analyse game state with
      gaze. It draws off-screen, so it runs on the tutorial hub (kernel
      "Python (smc)") or locally after
      `python -m pip install matplotlib scipy pylsl pyxdf notebook`
      (as upstream ships it, Step 1 does not check for `scipy`, and Step 9's
      heatmap fails without it).
      Confirm the hub address with Hemanth and write it here: ____________.
      Know two differences from the deck before pointing people at it: its
      building has no decoys (plain `VictimPlacer`), and it reads its own
      `notebooks/config.yaml`, not `configs/experiment.yaml`.

## Timing

| Time | Slides | Block | Facilitator focus |
| --- | --- | --- | --- |
| 0:00–0:14 | 1–8 | Part One: why MOSAIC | The field's questions, why they need a configurable testbed, what MOSAIC is, how it works, the task, the teaming loop. |
| 0:14–0:48 | 9–14 | Part Two: install | Prerequisites, clone, install and check, run the included mission. |
| 0:48–1:05 | 15–19 | Part Three: experience | Play one mission as a participant: objective, interface and tiles, victims, controls. No code. |
| 1:05–1:20 | 20 | Break | Fifteen minutes, slide 20 left up. Helpers finish stuck installs; everyone keeps the mission window open. |
| 1:20–1:26 | 21–23 | Part Four: the map | The runtime, then `main.py` stepped through in four parts. |
| 1:26–1:36 | 24–26 | 4.1 SAR | The task, the three cameras, then everyone changes a reward. |
| 1:36–1:43 | 27–28 | 4.2 GUI | The window; the decoy flash, demoed. |
| 1:43–1:58 | 29–31 | 4.3 LLM | The teammate; everyone swaps in the keyless `ReliableTeammate`; how to connect a real LLM afterwards (shown, not run). |
| 1:58–2:08 | 32–33 | 4.4 Sensing | What every step records; the live eye tracker. |
| 2:08–2:15 | 34–35 | Wrap-up | Where to go next, then questions; appendix slides as needed. |

The session runs 2:15 on the clock: two hours of content and the break. The
2:08–2:15 wrap-up is the only slack, and the notebook does not fit in it:
its nine steps include a 40-second recording. Treat it as take-home: name it at
slides 24 and 32 and again in the wrap-up. To run part of it live, cut first
(cut-list items 3 and 4). Slide 31 is no longer a live demo, so 4.3 should
finish a little early; keep that for install overruns.

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
  customizable teammate, conditions set per study, and one synchronized record.
- Slide 6 is the system overview: human, MOSAIC task, and AI teammate on top;
  study sensors, LSL, and session data underneath. Do not add the
  Gymnasium/MiniGrid detail here; it appears on Runtime Architecture (slide 22).
- Slide 7 introduces the task participants perform: search and rescue. The
  hook is that real victims and decoys look alike, so advice can help or mislead.
  Part Three teaches the rules.
- Slide 8 is the core claim of the tutorial. The teammate advises; the
  participant retains final action authority. Say it out loud.
- Keep Part One to fourteen minutes. Its purpose is to make the hands-on work
  meaningful, not to be complete.

## Part Two notes (slides 9–14)

- Ask attendees to use Python 3.10 or 3.11 for a shared troubleshooting baseline.
  MOSAIC's `pyproject.toml` claims 3.8+, but the code needs 3.10. Laptops that
  ship 3.12 or newer are common; slide 14 tells them to recreate `mosaic_env`
  with 3.10 or 3.11 (`conda create -n mosaic_env python=3.11` is the quickest).
- Slide 10 groups the packages `pip install -e .` brings in by role. Nothing is
  installed by hand. If you are behind, skip it: the next slide does not need it.
- Slide 11 clones one repository. The numbered notes on the right match the
  code line numbers. Everyone stays in `mosaic` all session.
- Slide 12 is five commands: upgrade pip, `pip install -e .`, two lines that
  swap `pygame` for `pygame-ce`, then a one-line import check. Mention that
  `-e` (editable) is what lets Part Four's edits take effect without
  reinstalling. Lines 3–4 are needed until upstream depends on `pygame-ce`:
  without them the check fails with `cannot import name 'DIRECTION_LTR'`.
  Attendees who followed `SETUP.md` already ran them; running them again is
  harmless. Do not advance until most attendees see `MOSAIC ready`; the
  `pygame-ce` banner above it will show their own versions.
- Slide 13 launches `PYTHONPATH=src python -m experiment.main` — MOSAIC's own
  study runner. The screenshot is the stock first frame (`gui-first-frame.png`):
  a crowded room and about 108 remaining. It opens fullscreen; `F11` gives a
  window, and on macOS it is `fn`+`F11` (or set `fullscreen: false` in the YAML).
  The terminal fills with font warnings and `connect_all failed` lines;
  both are harmless. Anyone who cloned before the import fix needs `git pull`.
- Hold at slide 14 until most attendees can move the agent. Ask everyone to
  leave the game open for Part Three. The *Expected problems* table below
  is the fuller recovery list while helpers work with individual machines.

## Part Three notes (slides 15–20): experience the mission

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
  shapes; the decoy's stem is off-center. Point at one of each on screen. Health
  and the −2.0 "victim died" outcome exist **only in the lab's study runner**
  (`TunedPickupVictimEnv`); the slide marks them so. In the tutorial's run
  health stays full and no victim dies — say so if asked. The reusable
  `VictimPlacer` places real victims only; decoys come from the study layer's
  `LavaRiskVictimPlacer`.
- Slide 19: each clip shows one action. `Tab` does both pickup and rescue on
  purpose. The advice clip uses the keyless map-reading teammate from slide 30; the slide
  tells attendees their own `Alt` gets "Currently, no commands are available."
  from the keyless `dummy` teammate, which is a flat moment: say that Part Four
  fixes it. Let everyone move, open a door, pick up a key, and rescue a
  victim before Part Four.
- Slide 20 is the break: fifteen minutes, after the controls and before any
  code. Leave the slide up. It is the best time to rescue stuck installs, so
  send helpers to anyone who could not move the agent at slide 14. Before
  moving on, check that every window is still open; anyone who closed the
  game relaunches it with the slide 13 command. Restart on time: Part Four
  has no slack to absorb a long break.

## Part Four notes (slides 21–34): configure MOSAIC

- Part Four walks through `experiment/main.py`, the file attendees launched in
  Part Two, in four parts: 4.1 SAR (the building, its contents, the camera,
  rewards), 4.2 GUI (the window), 4.3 LLM (who answers `Alt`), 4.4 Sensing
  (what every step records). The strip at the top of each slide shows the part.
- Slide 22 (runtime architecture) maps the window to its four changeable parts
  plus Gymnasium/MiniGrid underneath. Slide 23 steps through the real `main.py`
  call (press forward to move the highlight): SAR, GUI, LLM, then Sensing.
- Each part opens with one slide (24, 27, 29, 32): the exact `main.py` lines on
  the left, **three things to change** on the right, each as the setting and
  what it changes for the participant. The highlighted cards are the examples
  that follow. Keep each to about two minutes: name the three, then move on.
- Example slides share one layout: the task in one line, the edit as a diff in
  an editor-style card (file and where in it), Run, a question for the room,
  then on the next click the before/after from real MOSAIC. Every example
  starts from the stock files. The slides do not show how to undo an edit, so
  say it once at slide 26: `git checkout -- src/experiment/main.py` (or
  `configs/experiment.yaml`) puts the stock file back.
- The pill at the start of each example's task line says who does it. **Try it** (26 rewards, 30
  keyless teammate): everyone, live. **Presenter demo** (28 the flash, 33 the
  eye tracker): you, on the projector. **On your own** (31 the real LLM):
  nobody runs it; it needs an API key, and none is used in this session.
- Building settings (counts, size, locked rooms) and the observation-field
  print are **not** live slides any more; they are in the notebook (the cards
  on slides 24 and 32 are tagged "Notebook", and slide 24 names the file:
  `notebooks/02_mosaic_human_ai.ipynb`). The before/after images for counts are still
  in `assets/results/` (`config-*.png`, `world-*.png`) if you want to show them.
- Top-level YAML keys: `main.py` passes the whole YAML to `SAREnvGUI`, which
  reads `max_time`, `llm_nudge_interval`, and `prompt_type` from the top level.
  The same keys under `game:` configure the lab's study runner, not this run.
- Slide 25: the three clips are one walk rendered through three cameras. Do not
  offer `FullviewCamera` or `AgentCenteredCamera`; both raise `AttributeError`
  on env reset.
- Slide 26: `action=RescueAction(rewards=RescueRewards(fake_victim=-5.0))` goes
  inside `build_sar_env(...)`, after `camera_strategy=`. If someone sees
  `NameError: name 'RescueAction' is not defined`, the import line is missing.
- Slide 30 (keyless teammate): attendees save `advisor.py` into `src/experiment/`
  first (link on the slide and in `SETUP.md`). At reliability 0.7 about three
  replies in ten point at a decoy: ask the room whether they noticed. With no
  API key in the session, this is the only teammate that gives real advice.
- Slide 31 (the real LLM): not run. Walk through the three cards (two
  packages, a key in a local `.env`, two YAML lines) so attendees can do it
  later with their own key, then reveal how the reply is produced.
  `build_llm_client` connects on the first `Alt`, so a missing or bad key
  shows as a chat error, not a crash. If asked
  what the LLM actually sees, appendix slide 40 shows it: every real victim, even out
  of view, and **no decoys** (`process_prompts.py` skips them).
- Slide 32 prints nothing itself: the field list on it is what the study runner
  streams. The full study runner needs the lab's `ixp` package and LSL, which
  are not installed in the tutorial.
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
     up to `game: max_time` (15 minutes in the stock YAML). For the demo, set
     `max_time: 2` under `game:`, and press `Esc` to end a trial early; `Esc`
     ends the current trial. No API keys are used, so in the OpenAI and Gemini
     trials `Alt` (and the automatic request every 50 steps) shows an error in
     the chat instead of advice; the game and both streams carry on. That is
     read from the code, not run here: confirm it at the rehearsal. The demo
     is about gaze next to game steps, so say that advice is off.
  4. `python -m experiment.experiment` from the `mosaic` folder. Calibration is
     five dots; SPACE accepts, R redoes. Then the volunteer plays.
  5. Press forward to reveal item 3 once LabRecorder shows both streams
     (TobiiEyeTracker and the game trial).

  If the device fails, show the rehearsal screenshot and move on.
- The hidden *Synchronized Record* slide (would be 34) stays out of the deck
  until the rehearsal recording exists. With one eye tracker in the room,
  everyone inspects that prepared recording.
- The result images come from `tools/capture_config_results.py` (and the
  camera captures). The reward, time, mission-box, and chat crops are rendered
  at twice the window size so they stay sharp on the projector:
  `python tools/capture_config_results.py scoring chatpair time panel`. Re-run
  it if MOSAIC's rendering changes, and re-check the locked-door counts quoted
  on appendix slide 37.
- Slide 34 (where to go next) is the code map. Point at `src/experiment/` as
  the folder to copy for a new study.
- Appendix 37–40 hold the other changes from the part slides, in the same
  layout: locked rooms, the time limit (at 0:00 the timer stops but the mission
  keeps going, which is expected), the info panel, and what the teammate is
  told (the "Prompt" card on slide 29 points there). `prompt_type: sparse` and
  `llm_nudge_interval` no longer have a slide; they are in the slide 29 notes.
- The closing slide (35) carries only the MOSAIC repository link.

## Expected problems

| Symptom | Response |
| --- | --- |
| `ImportError: cannot import name 'DIRECTION_LTR' from 'pygame'` | Plain `pygame` is hiding `pygame-ce`. Run lines 3–4 of slide 12: `python -m pip uninstall -y pygame`, then `python -m pip install --force-reinstall "pygame-ce>=2.5.2"`. |
| `AttributeError: module 'pygame' has no attribute 'surface'` | They uninstalled `pygame` without `--force-reinstall`. Rerun line 4 of slide 12 with the flag. |
| `ModuleNotFoundError: No module named 'mosaic'` | Confirm `mosaic_env` is active and `pip install -e .` completed in the `mosaic` directory. |
| `python --version` shows 3.12 or newer | Recreate `mosaic_env` with Python 3.10 or 3.11. |
| `NameError: name 'LavaRiskVictimPlacer' is not defined` | Their clone predates the import fix. `git pull` in `mosaic`. |
| `pygame.error: video system not initialized` after `Esc` | Their clone predates the `tutorial`-block fix. `git pull` in `mosaic`; the mission itself was fine. |
| `NameError: name 'RescueAction' is not defined` | The rewards import is missing; it is the first line of the code card on slide 26. |
| `ModuleNotFoundError: No module named 'experiment.advisor'` (or `.advisor`) | `advisor.py` is not in `src/experiment/`. Download it from `presentation/labs/` (slide 30). |
| `No module named 'experiment'` | Run from the repo root with `PYTHONPATH=src`. |
| PowerShell cannot load `mosaic_env` | Use `.\mosaic_env\Scripts\Activate.ps1`; the leading `.\` is required. |
| No window or `No available video device` | The GUI needs a local graphical session. Use the fallback laptop. |
| `F11` does nothing on macOS | Use `fn`+`F11`, or set `fullscreen: false` in `configs/experiment.yaml`. |
| `Alt` replies "Currently, no commands are available." | Expected until slide 30: the runner uses the keyless `dummy` teammate. For anyone trying their own key, it means the `provider:` line is missing or not at the top level of the YAML. |
| `Alt` replies "Import tabulate failed" (before slide 30) | Upstream still defaults the provider to `openai`. Add `provider: dummy` as a top-level line in `configs/experiment.yaml` and relaunch. With a real provider: `python -m pip install tabulate`. |
| Chat shows an authentication or 401 error | The key in `.env` is mistyped, has spaces, or the file is not in the `mosaic` folder. |
| Chat shows `No module named 'llama_index'` | `python -m pip install llama-index-llms-openai` with `mosaic_env` active. |
| LLM replies are slow or show a rate-limit error | Wait and retry; if it persists, switch to the keyless teammate (slide 30). |
| Generation appears to hang after customization | `locked_room_prob` is at `1.0`. Use `0.9` or less. |
| More victims than expected | `num_real_victims` is per room; 12 per room across a 3×3 building is 108. |
| `AttributeError: 'FullviewCamera' object has no attribute 'reset'` | Known bug, same for `AgentCenteredCamera`. Use `AgentFOVCamera`, `AgentConeCamera`, or the default. |
| `max_time`, `llm_nudge_interval`, or `prompt_type` has no effect | The key is under `game:`. Add it as a top-level line instead. |

## Cut list

If the session runs long:

1. In Part Three, explain slides 17–18 in one minute each.
2. Keep the part slides (24, 27, 29, 32) to a minute each.
3. Skip slide 10 (dependency list) in Part Two.
4. Make the keyless-teammate swap (30) a presenter demo instead of a live try.
5. Drop the eye-tracker demo (33) if the device is not ready; show the
   rehearsal screenshot instead.

Do not cut the installation checkpoints, the first run, the controls, the
`main.py` walkthrough (23), or the keyless teammate (30): with no API key in
the session it is the only grounded advice attendees see. If item 4 is used,
still demo it.

## Closing ask

Ask attendees to keep the small working mission and open an issue when
installation or an extension point fails on their machine. Concrete reports from
new users are the most useful outcome for the project after the tutorial.
