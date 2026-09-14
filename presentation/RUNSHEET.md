# Facilitator Run Sheet — MOSAIC Tutorial (90 minutes)

The rendered deck has 38 slides: 25 in the main tutorial and 13 appendix
slides. The main sequence has three parts: understand MOSAIC, install it, then
build and run a first mission.

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
| 0:36–1:20 | 14–24 | Part Three | Show the game, build `first_mission.py`, run it, and change one parameter. |
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

- Slides 15–17 introduce the game before any code appears.
- Slides 18–20 assemble one file in three short steps. Attendees should type or
  paste each block into `first_mission.py` inside the MOSAIC checkout.
- `gui.run()` performs the first reset. The main example does not need a separate
  `env.reset()` call.
- Leave slide 21 visible during the first play period. The checkpoint is more
  useful than continuing to speak while attendees explore the interface.
- On slide 22, ask each attendee to change only one parameter. This makes the
  comparison easier to discuss.
- Slide 23 connects the exercise back to research design: the reusable task stays
  stable while study configuration and protocol code change around it.

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
3. Summarize slide 23 verbally while slide 24 remains visible.

Do not cut the installation checkpoints, the controls slide, the three mission
code slides, or the first-run checkpoint.

## Closing ask

Ask attendees to keep the small working mission and open an issue when installation
or an extension point fails on their machine. Concrete reports from new users are
the most useful outcome for the project after the tutorial.
