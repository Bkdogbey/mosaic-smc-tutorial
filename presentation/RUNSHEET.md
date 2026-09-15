# Facilitator Run Sheet — MOSAIC Tutorial (90 minutes)

The rendered deck has 32 slides: 25 in the main tutorial and 7 appendix slides.
The main sequence has three parts: understand MOSAIC, install it, then run and
modify the provided mission.

## Before the room opens

- [ ] Render `mosaic-tutorial.qmd` and open `mosaic-tutorial.html` in a browser.
- [ ] Test the deck at the projector's 16:9 resolution.
- [ ] Keep one working MOSAIC environment and one running mission as a fallback.
- [ ] Send `SETUP.md` to attendees before the conference.
- [ ] Ask one lab member to help with installation during Part Two.
- [ ] Keep `labs/first_mission.py` open as the reference answer for Part Three.

## Timing

| Time | Slides | Block | Facilitator focus |
| --- | --- | --- | --- |
| 0:00–0:04 | 1–2 | Welcome and lab | Introduce the tutorial goal and the iHuman Lab. |
| 0:04–0:16 | 3–8 | Part One | Explain why the platform exists, what it connects, and what researchers can study. |
| 0:16–0:36 | 9–13 | Part Two | Walk through the supported installation path and hold at each checkpoint. |
| 0:36–1:20 | 14–24 | Part Three | Explain the building blocks, run `first_mission.py`, and change one parameter. |
| 1:20–1:30 | 25 | Questions | Close on the working baseline and use appendix slides as needed. |

## Part One notes

- Slide 4 establishes the four requirements that MOSAIC coordinates.
- Slide 5 is the system overview. Explain the human, MOSAIC, and advisor first,
  then show how their interaction becomes one experiment record.
- Slide 7 distinguishes independent action from the optional advice path. The
  participant always chooses the final action.
- Keep Part One brief. Its purpose is to make the hands-on work meaningful.

## Part Two notes

- Ask attendees to use Python 3.10 or 3.11 for a shared troubleshooting baseline.
- The current package metadata can install both `pygame` and `pygame-ce`. Use the
  exact force-reinstall command on slide 12.
- `tabulate` is currently undeclared but required when the advisor builds a
  prompt. Do not skip that command.
- Do not advance from slide 13 until most attendees see `MOSAIC ready`.
- Keep the installation troubleshooting slide in the appendix available while
  helpers work with individual machines.

## Part Three notes

- Slide 15 explains how task content, camera strategy, and optional advice enter
  the environment and GUI.
- Slides 16–18 introduce the SAR task, controls, and three camera choices.
- Slide 19 runs the provided `presentation/labs/first_mission.py`. Attendees do
  not need to create or copy a file.
- Slide 20 explains the important sections of the file after participants have
  seen it run. `gui.run()` performs the first reset.
- On slide 21, ask each attendee to change only one parameter.
- Slide 22 shows the LLM integration point only. Refer implementation questions
  to the project documentation.
- Slides 23–24 distinguish the example iHuman Lab protocol from the reusable
  `mosaic/` package.

## Expected problems

| Symptom | Response |
| --- | --- |
| `ImportError: cannot import name 'DIRECTION_LTR'` | Repeat the pygame uninstall and force-reinstall commands from slide 12. |
| `ModuleNotFoundError: No module named 'tabulate'` | Run `python -m pip install tabulate`. |
| `ModuleNotFoundError: No module named 'mosaic'` | Confirm that the virtual environment is active and `python -m pip install -e .` completed. |
| No window or `No available video device` | The GUI needs a local graphical session. Use the fallback laptop or run the environment headless. |
| Generation appears to hang after customization | Check that `locked_room_prob` is below `1.0`. |
| More victims than expected | `num_real_victims` is per room, not a building-wide total. |
| `Alt` produces no reply | Confirm that `tabulate` is installed, then inspect the terminal for the background-thread error. |

## Cut list

If the session runs long:

1. Explain slide 16 in one minute without pausing on every feature.
2. Demonstrate the parameter change on slide 22 instead of waiting for everyone.
3. Summarize slide 23 verbally and close on the architecture shown on slide 24.

Do not cut the installation checkpoints, controls, camera comparison, provided
mission run, or the task-manipulation exercise.

## Closing ask

Ask attendees to keep the small working mission and open an issue when installation
or an extension point fails on their machine. Concrete reports from new users are
the most useful outcome for the project after the tutorial.
