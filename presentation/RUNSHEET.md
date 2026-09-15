# Facilitator Run Sheet — MOSAIC Tutorial (90 minutes)

The rendered deck has 30 slides: 25 in the main tutorial and 5 appendix slides.
The main sequence has three parts: understand MOSAIC, install it, then assemble
and use the search-and-rescue testbed.

## Before the room opens

- [ ] Render `mosaic-tutorial.qmd` and open `mosaic-tutorial.html` in a browser.
- [ ] Test the deck at the projector's 16:9 resolution.
- [ ] Keep one working MOSAIC environment and one running mission as a fallback.
- [ ] Open `mosaic-tutorial.ipynb` using the MOSAIC virtual environment.
- [ ] Send `SETUP.md` to attendees before the conference.
- [ ] Ask one lab member to help with installation during Part Two.
- [ ] Keep one working MOSAIC GUI session open as a fallback for Part Three.

## Timing

| Time | Slides | Block | Facilitator focus |
| --- | --- | --- | --- |
| 0:00–0:04 | 1–2 | Welcome and lab | Introduce the tutorial goal and the iHuman Lab. |
| 0:04–0:16 | 3–8 | Part One | Explain why the platform exists, what it connects, and what researchers can study. |
| 0:16–0:36 | 9–13 | Part Two | Walk through the supported installation path and hold at each checkpoint. |
| 0:36–1:20 | 14–24 | Part Three | Explain the building blocks, interface, gameplay, camera views, and the code that connects the environment to the GUI. |
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

- Slide 15 explains the runtime relationship among the participant, GUI, SAR
  environment, Gymnasium/MiniGrid foundation, and optional advisor.
- Slide 16 uses numbered callouts on the real interface. Point out that the
  dashed game-view boundary is where event vignettes appear.
- Slide 17 introduces both victim object types, then the lava and door/key
  mechanics. Clarify that the default placer uses real victims only.
- Slide 18 introduces the controls through the observe–navigate–identify–rescue
  gameplay loop.
- Slide 19 compares real renders of one seeded world under the three camera
  strategies. Only visibility changes; the task state does not.
- Slides 20–21 show the complete minimum code in two readable pieces: build the
  SAR environment, then pass it to `SAREnvGUI` and run it. The companion
  notebook contains the same sequence; no standalone Python file is created.
- On slide 22, change one constructor value and describe the resulting task.
- Slide 23 shows the AI-advisor capability and one injection point only. Refer
  provider configuration to the project documentation.
- Slide 24 closes on the four main extension points in MOSAIC.

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

1. Explain slides 16–17 in one minute each without pausing on every feature.
2. Demonstrate the parameter change on slide 22 instead of waiting for everyone.
3. Summarize the advisor path on slide 23 and close on the extension points on slide 24.

Do not cut the installation checkpoints, controls, camera comparison, or the
environment-to-GUI code path.

## Closing ask

Ask attendees to keep the small working mission and open an issue when installation
or an extension point fails on their machine. Concrete reports from new users are
the most useful outcome for the project after the tutorial.
