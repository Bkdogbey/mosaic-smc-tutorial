# Facilitator Run Sheet — MOSAIC Tutorial (90 minutes)

Slide numbers refer to the rendered deck (`mosaic-tutorial.html`): 41 slides: 29 in
the main flow, then an appendix (30–41) after the closing slide. Timings live
here only — the slides themselves carry none.

The deck is three parts: **what it is** (brief), **getting it running**
(the bulk of the value), **playing with it** (the bulk of the time).

## Before the room opens

- [ ] Projector at 16:9. Render the deck fresh; open `mosaic-tutorial.html`, press `f`.
- [ ] Your own MOSAIC install working, in a venv, with a **large terminal font**.
- [ ] A 3×3 mission already running in a second window, paused, as the fallback demo.
- [ ] `SETUP.md` printed or on a slide QR code — the install step is the single
      biggest source of lost minutes.
- [ ] Spare laptop with MOSAIC pre-installed for anyone whose machine fights back.
- [ ] Ask a labmate to float as an install helper during Part 2.

## Timing

| Time | Slides | Block | Notes |
| --- | --- | --- | --- |
| 0:00–0:05 | 1–2 | Welcome, **start the install now** | Put slide 2 up and leave it up. People install while you talk. Do not wait for everyone. |
| 0:05–0:15 | 3–6 | Part 1 · what MOSAIC is | Ten minutes, no more. Slide 5 (the pieces) is the only architecture they need; slide 6 is the only argument slide. Resist the urge to add back the research framing — it is in the appendix if someone asks. |
| 0:15–0:40 | 7–15 | **Part 2 · install** | The hands-on block. Announce a hard stop at 0:40. Walk the room. Slides 11–12 are the pygame-ce trap — say the fix out loud to the whole room the first time it comes up. Leave slides 14–15 (troubleshooting) up while you circulate. |
| 0:40–1:20 | 16–27 | **Part 3 · play, then tweak** | Two beats: play a mission (17–21), then turn the knobs (22–26). Slide 27 is the "try this now" card grid — that is where they should spend the last ten minutes of the block. |
| 1:20–1:30 | 28–29 | Next steps and Q&A | Appendix slides 31–41 are on hand for whatever they ask. |

## Things that will happen

**A third of the room will not have installed.** That is normal and it is why the
install slide is slide 2. Start Part 2 on time anyway; helpers catch up with
stragglers.

**Someone will hit the pygame / pygame-ce clash.** Have the two-line fix on a
sticky note. Note that `--force-reinstall` is genuinely required — the older
one-line version of this fix leaves pygame-ce broken with
`module 'pygame' has no attribute 'surface'`. Do not debug it individually; say
it out loud to the room the first time.

**Someone will press `Alt` and nothing will happen.** They skipped
`pip install tabulate` in step 3. The prompt builder calls
`DataFrame.to_markdown()`, which needs it, and the failure happens on a
background thread — so the game keeps running and just never answers. Say this
out loud when you reach the controls slide.

**Someone will ask why they got 8 victims when they asked for 2.** Good — that is
the per-room semantics, and it is on slide 13.

**Someone will try `FullviewCamera` after slide 24 and get an `AttributeError`.**
Known bug (no `reset()` on that camera). The slide warns about it, but say it
anyway. Working cameras: `AgentFOVCamera`, `AgentConeCamera`, `EdgeFollowCamera`.

**Someone will say their seeded world changed anyway.** They seeded only
`env.reset(seed=...)`. The placers draw from the global `random`, so
`random.seed(...)` is needed too — that is slide 26, and it is a real bug on our
side, not user error.

**Someone will ask where the advisor lab went.** It is in the appendix
(slides 35–37) and in `labs/advisor.py`. Offer to walk it with them afterwards;
it is the single best hook for a collaborator, so do not rush it in the room.

**Someone will ask about RL / Gymnasium.** The environment is Gymnasium-compatible
(`Discrete(7)` action space, dict observation); formal registration as
`MOSAIC-SAR-v0` is on the roadmap (appendix). Take it offline if the room is
HCI-heavy.

**Someone will ask if it runs in Colab.** Not the GUI — it needs a real display.
The environment itself runs headless fine (`render_mode="rgb_array"`), which is
enough for scripted agents and for generating figures.

## Cut list, in order

If you are running long, drop in this order:

1. Slide 19 — what's on screen (the controls slide and live play cover it)
2. Slide 25 — knob 4, what mistakes cost
3. Slide 6 — why it exists (only if Part 1 is overrunning badly)

Never cut: the install slide, Part 2 in full, the controls slide, playing a
mission, or the "try this now" grid.

## Closing ask

End on slide 28 and make one concrete request: **open an issue when it breaks on
your machine.** That converts an audience into contributors better than any
roadmap slide does.
