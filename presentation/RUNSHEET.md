# Facilitator Run Sheet — MOSAIC Tutorial (two hours)

The rendered deck has 53 slides: 35 in the main tutorial, a closing slide (36),
and 17 appendix slides (37–53). The main sequence runs in four parts: why MOSAIC
exists, install and verify it, run and understand the included experiment, then
build one human–AI reliability study.

The learning arc is: understand the research need → install the software →
experience the baseline and locate its extension points → use those extension
points to build one study.

## Before the room opens

- [ ] Render `mosaic-tutorial.qmd` and open `index.html` in a browser.
- [ ] Test the deck at the projector's 16:9 resolution (authored at 1280×720).
- [ ] Keep one working MOSAIC environment and one running mission as a fallback.
- [ ] Test a clean Windows PowerShell install with the `mosaic_env` commands.
- [ ] Test the Conda alternative in a separate clean environment.
- [ ] Send `SETUP.md` to attendees before the conference.
- [ ] Ask one lab member to help with installation during Part Two.
- [ ] Confirm `PYTHONPATH=src python -m experiment.main` opens a window.
- [ ] Upstream MOSAIC carries the three fixes: `main.py` imports restored with the
      `dummy` default, the `tutorial` block set to `skip` (else `Esc` ends in
      `pygame.error: video system not initialized`), and `pygame-ce` in
      `pyproject.toml`.
- [ ] **Part Four infrastructure (not built yet).** The lab-hosted notebook
      service, one isolated session per participant, and the LLM connection
      behind a lab-controlled service with rate and cost limits. Until they
      exist and have been tested, slides 26–31 describe the planned workflow
      and carry "Development placeholder" tags. Do not hand out an address that
      has not been tested.
- [ ] Test the proposed mission defaults on slide 27 (seed 7, 2×2 building, 2 of
      each per room, 180 s) and replace them if they are too easy or too hard.
      The notebook must call `random.seed(seed)` as well as `env.reset(seed=...)`
      so both conditions see the same layout (README issue 3).
- [ ] Replace the placeholders once real captures exist: the notebook
      screenshot (slide 26), the summary view (slide 31), and the synchronized
      timeline (slide 33).
- [ ] Eye-tracker demo (slide 32), presenter laptop only: install the lab's
      `ixp`, `tobii_research`, PsychoPy, and pylsl; connect the Tobii; run the
      main-game block of `src/experiment/experiment.py` with the sensor added
      once end to end; keep a screenshot of the LSL stream list as a fallback.
- [ ] At that rehearsal, record one short session (LabRecorder) and build the
      aligned timeline for slide 33.

## Timing

| Time | Slides | Block | Facilitator focus |
| --- | --- | --- | --- |
| 0:00–0:15 | 1–8 | Part One: why MOSAIC | The field's questions, why they need a configurable testbed, what MOSAIC is, how it works. |
| 0:15–0:40 | 9–13 | Part Two: install and verify | Prerequisites, clone, install, and the `MOSAIC ready` check. Nothing is launched yet. |
| 0:40–1:05 | 14–22 | Part Three: run and understand | First run of `experiment.main`, the mission, the interface, the controls, the runtime, how `main.py` composes it, and where changes are made. |
| 1:05–1:50 | 23–31 | Part Four: build the reliability study | One question, two conditions, configured and run in the hosted notebook, then the behavioral record. |
| 1:50–2:00 | 32–36 | Eye tracking and wrap-up | The instructor eye-tracking demo, the synchronized record, what participants built, the code map, then questions. |

Adjust the slide-level timing after rehearsal.

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
  Gymnasium/MiniGrid detail here; it appears on Runtime Architecture (slide 19).
- Slide 7 introduces the task participants perform: search and rescue.
- Slide 8 is the core claim of the tutorial. The teammate advises; the
  participant retains final action authority. Say it out loud.
- Keep Part One to fifteen minutes. Its purpose is to make the hands-on work
  meaningful, not to be complete.

## Part Two notes (slides 9–13): install and verify

Installation and verification only. Nobody launches the game in this part.

- Ask attendees to use Python 3.10 or 3.11 for a shared troubleshooting baseline.
  MOSAIC's `pyproject.toml` claims 3.8+, but the code needs 3.10.
- Slide 10 groups the packages `pip install -e .` brings in by role. Nothing is
  installed by hand, and there is no local Jupyter and no API key: Part Four
  will use a lab-hosted notebook in the browser.
- Slide 11 clones one repository. The numbered notes on the right match the
  code line numbers. Everyone stays in `mosaic` all session.
- Slide 12 is three commands: upgrade pip, `pip install -e .`, then a one-line
  import check. The `pygame-ce` banner above `MOSAIC ready` shows each
  attendee's own versions.
- Hold at slide 13 until most attendees see `MOSAIC ready`. Its table covers the
  install failures; the appendix recovery slide (38) has the rarer ones while
  helpers work with individual machines.

## Part Three notes (slides 14–22): run and understand MOSAIC

Participants run the baseline and learn where its components connect. No code
edits in this part.

- Slide 15 is the first launch: `PYTHONPATH=src python -m experiment.main` —
  MOSAIC's own study runner. The screenshot is the stock first frame
  (`gui-first-frame.png`): a crowded room and about 108 remaining. It opens
  fullscreen; F11 gives a window; if the keys do nothing, click the window. The
  terminal fills with font warnings and `connect_all failed` lines; both are
  harmless. Run failures are in the slide notes. Anyone who cloned before the
  import fix needs `git pull`.
- Slide 16 states the mission and its elements with the real sprites: real
  victims (+1), decoys (−1, off-center stem), lava, doors and keys, the
  five-minute clock and score, and advice on `Alt`. The clip is the real
  interface: one real victim (green flash), one decoy (red flash), then another
  real victim. Victim health is not active in this run; the appendix slide on
  victims and decoys (40) covers it if asked.
- Slide 17 reveals one region at a time — press forward six times: game
  viewport, mission-information panel, score and time, controls, AI chat panel,
  and the event feedback vignette. The screenshot is caught mid-flash, so the
  green glow around the game view is the vignette firing after a rescue.
- Slide 18: each clip shows one action. `Tab` does both pickup and rescue on
  purpose. Before moving on, everyone should move, open a door, press `Alt`, and
  attempt a rescue. Their own `Alt` gets "Currently, no commands are
  available." from the keyless `dummy` teammate; the clip uses the grounded
  teammate from the appendix.
- Slide 19 (runtime architecture) is the map. Read the hook as written: human
  actions, the GUI, the SAR environment, and the AI teammate form the
  interaction loop (orange); sensors record the session on a shared clock
  (dashed); Gymnasium and MiniGrid are the foundation (muted).
- Slide 20 shows how `src/experiment/main.py` composes the included study
  (press forward to move the highlight). The code is simplified; the exact lines
  are on appendix slide 39. Say that this is the tutorial's included study, not
  the only way to use MOSAIC. There is no `rewards=` argument: scoring uses
  `RescueRewards` defaults unless `action=` is passed.
- Slide 21 replaces the old tour of settings with one map: research decision →
  MOSAIC area → examples → where it lives in the code.
- Slide 22 closes Part Three with the bridge sentence into Part Four.

## Part Four notes (slides 23–31): build a human–AI reliability study

One coherent activity, not a catalogue of settings. The central question:
**when AI advice may be wrong, does the participant verify it before acting?**

- Slide 24 lists the five steps; each names the Part Three area it uses.
- Slide 25: AI reliability (1.0 vs 0.7) is the only manipulated variable; seed,
  layout, camera, and advice timing are the same. The measurements are study
  outputs, not findings.
- Slide 26: the hosted notebook runs in the browser with an isolated session per
  participant and a simplified inline mission view (the Pygame window does not
  stream to the browser). The lab service provides the LLM connection; no
  participant key. **Planned, not built** — the slide carries a development
  placeholder tag. Do not give an address until it exists and has been tested.
- Slide 27: the proposed mission defaults (not calibrated). Counts are per room,
  so a 2×2 building has 8 real victims, 8 decoys, and 8 lava tiles.
- Slide 28: one limited camera (`AgentConeCamera`) for both conditions. The
  images are real captures of one frame through two cameras. The point: the
  camera controls what evidence the participant can use to verify the advice.
- Slide 29: the experiment decides whether each recommendation is correct and
  picks its target; the LLM only phrases it; MOSAIC records target,
  correctness, message, and response. Do not claim an LLM on its own produces
  70% reliable advice. `labs/advisor.py` (`ReliableTeammate`) is the reference
  for the first two steps.
- Slide 30 shows the procedure only. Say that a formal experiment counterbalances
  condition order and that today demonstrates the workflow.
- Slide 31 lists the fields the notebook will summarize. No example values —
  there is no collected data.

## Eye tracking and wrap-up (slides 32–36)

- Slide 32 is the live eye-tracking demo, instructor-only, framed by one
  question: after advice, does the participant look straight at the
  recommended target or scan the room to verify it? The slide shows no
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
     `max_time: 2` under `game:` and press `Esc` to end a trial early. The
     hosted providers need the lab's keys on the presenter laptop only, in
     `.env`, never on a slide or in the tutorial repository.
  4. `python -m experiment.experiment` from the `mosaic` folder. Calibration is
     five dots; SPACE accepts, R redoes. Then the volunteer plays.
  5. Press forward to reveal item 3 once LabRecorder shows both streams
     (TobiiEyeTracker and the game trial).

  If the device fails, show the rehearsal screenshot and move on.
- Slide 33 is a placeholder until the rehearsal recording exists; it names the
  five lanes the timeline will show (task events, advice, gaze, actions,
  outcomes).
- Slide 34 maps the activity back to the four components.
- Slide 35 is the code map. Point at `src/experiment/` as the folder to copy.

## Appendix (slides 37–53)

Customization reference and troubleshooting, for Q&A and self-study:

| Slide | Topic |
| --- | --- |
| 38 | Detailed installation recovery |
| 39 | Mission composition, line by line (the exact `main.py` listing the task slides edit) |
| 40 | Victims and decoys: symbols, health, and scoring |
| 41–44 | SAR: counts per room, locked rooms, rescue rewards, time limit |
| 45–48 | GUI: camera views, change the camera, feedback flashes (vignette styling), the info panel |
| 49–52 | Teammate: swap in `ReliableTeammate`, advice timing, what the teammate knows and says (prompt construction), provider setup |
| 53 | Sensing: what each step records (observation fields and subclassing) |

The task slides keep their Change → Run → Observe → Interpret layout and their
before/after images. Notes for them:

- Top-level YAML keys: `main.py` passes the whole YAML to `SAREnvGUI`, which
  reads `max_time`, `llm_nudge_interval`, and `prompt_type` from the top level.
  The same keys under `game:` configure the lab's study runner, not this run.
- Slide 42: `locked_room_prob` at `1.0` hangs the generator — keep it below.
- Slide 45: the three clips are one walk rendered through three cameras. Do not
  offer `FullviewCamera` or `AgentCenteredCamera` — both raise `AttributeError`
  on env reset.
- Slides 48 and 49 use `labs/panel.py` and `labs/advisor.py` from the tutorial
  repository; attendees download each into `src/experiment/` first. Slide 50
  builds on slide 49's teammate.
- The result images come from `tools/capture_config_results.py` (and the
  camera and chat captures). Re-run it if MOSAIC's rendering changes, and
  re-check the locked-door counts quoted on slide 42.

## Expected problems

| Symptom | Response |
| --- | --- |
| `ModuleNotFoundError: No module named 'mosaic'` | Confirm `mosaic_env` is active and `pip install -e .` completed in the `mosaic` directory. |
| `NameError: name 'LavaRiskVictimPlacer' is not defined` | Their clone predates the import fix. `git pull` in `mosaic`. |
| `pygame.error: video system not initialized` after `Esc` | Their clone predates the `tutorial`-block fix. `git pull` in `mosaic`; the mission itself was fine. |
| `No module named 'experiment'` | Run from the repo root with `PYTHONPATH=src`. |
| PowerShell cannot load `mosaic_env` | Use `.\mosaic_env\Scripts\Activate.ps1`; the leading `.\` is required. |
| No window or `No available video device` | The GUI needs a local graphical session. Use the fallback laptop. |
| The keys do nothing | Click the game window to give it focus. |
| `Alt` replies "Currently, no commands are available." | Expected — the runner uses the keyless `dummy` teammate. |
| Someone asks to use their own API key | Not needed for the tutorial. Point them to appendix slide 52 for after the session. |
| Appendix task: generation hangs | `locked_room_prob` is at `1.0`. Use `0.9` or less. |
| Appendix task: `NameError: name 'RescueAction' is not defined` | The rewards import is missing; it is the first line of the slide 43 code card. |
| Appendix task: `AttributeError: 'FullviewCamera' object has no attribute 'reset'` | Known bug, same for `AgentCenteredCamera`. Use `AgentFOVCamera`, `AgentConeCamera`, or the default. |
| Appendix task: `max_time`, `llm_nudge_interval`, or `prompt_type` has no effect | The key is under `game:`. Add it as a top-level line instead. |

## Cut list

If the session runs long:

1. In Part Three, explain slides 17 and 21 in one minute each.
2. In Part Four, present slides 27–29 as one configuration pass.
3. Drop the eye-tracker demo (32) if the device is not ready; show the
   rehearsal screenshot instead.

Do not cut the installation checkpoint (13), the first run (15), the controls
(18), the `experiment.main` slide (20), the conditions (25), or the wrap-up
(34–35).

## Closing ask

Ask attendees to keep the small working mission and open an issue when
installation or an extension point fails on their machine. Concrete reports from
new users are the most useful outcome for the project after the tutorial.
