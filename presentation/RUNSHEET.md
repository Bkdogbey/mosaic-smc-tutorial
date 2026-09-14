# Facilitator run sheet

Suggested length: 90 minutes. Use slide titles rather than fixed numbers.

## Before the session

- Send SETUP.html and ask attendees to reach MOSAIC CHECK PASSED.
- Pin the MOSAIC revision in the handout. Rehearse on the actual presentation laptop.
- Open the slides through a local HTTP server. Check OS tabs, clipboard and speaker notes.
- Select the MOSAIC venv in a terminal inside presentation. Increase terminal and editor font sizes.
- Open play.py, tweak.py and advisor.py. Restore 2×2, seed 42 and CAMERA="room".
- Keep a working game available and arrange paired workstations for installation difficulties.

## Timing

| Minutes | Block | Outcome |
| --- | --- | --- |
| 0–3 | Welcome and route | Attendees know what they will build |
| 3–15 | Overview | Task, usage paths and configurable components are clear |
| 15–40 | Installation | The checker passes and a window responds to input |
| 40–52 | Game tour and rescue | Everyone rescues a victim |
| 52–60 | Building exercise | Attendees edit a setting and observe its effect |
| 60–69 | Camera comparison | Attendees understand room versus cone visibility |
| 69–76 | Advisor exercise | A custom offline sentence appears in chat |
| 76–82 | Recording and study design | Attendees inspect a trace and define a condition |
| 82–90 | Extensions and discussion | Each attendee identifies a useful next change |

## Teaching cues

Demonstrate the participant's task before discussing architecture. At every exercise, state the current folder, file to edit, command and expected result. Give attendees time at checkpoints.

Use one relevant OS tab at a time. Check sys.executable rather than only the prompt prefix. The lab exercises do not read experiment.yaml.

For the camera exercise, repeat settings but discuss learning effects in real studies. For advice, describe the fixed reminder honestly; it is not tactical reasoning or measured reliability.

## Live demo sequence

1. Launch play.py and point out viewport, mission panel, compass and chat.
2. Turn and move once.
3. Face an early victim and use Tab. Show the saved count before the final rescue resets the map.
4. Find a key, pick it up and open a matching door with Space.
5. Request the fallback reply with Alt.
6. Change both map dimensions to 3, rerun, then restore 2.
7. Compare room and cone in tweak.py.
8. Run advisor.py, edit its reminder and repeat.
9. Run record.py and inspect the three JSONL records.

## Behaviors to explain when relevant

The basic GUI resets on termination, displays but does not enforce its countdown, and does not add automatic health depletion. Default victims contain no decoys. Keep locking below 1, the advice interval positive and maps square. To remove lava, disable it explicitly.

Backspace generates another map; a fresh script launch repeats the seeded initialization sequence. The experiment framework needs separate dependency and configuration work.

## If time is short

Preserve first launch, controls, one rescue and the camera comparison. Demonstrate the advisor instead of asking everyone to edit it. Leave recording and advanced framework details for follow-up.

F toggles fullscreen, S opens notes and Esc shows slide overview. OS tabs accept mouse clicks and arrow-key navigation. The task slide uses progressive reveals.
