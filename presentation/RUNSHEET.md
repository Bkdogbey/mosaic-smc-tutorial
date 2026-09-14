# Facilitator Run Sheet — MOSAIC Tutorial (90 minutes)

Slide numbers refer to the rendered deck (`mosaic-tutorial.html`): 43 slides: 31 in
the main flow, then an appendix (32–43) after the closing slide. Timings live
here only — the slides themselves carry none.

The deck is three parts: **understanding MOSAIC** (brief), **getting it running**
(the bulk of the value), **playing with it** (the bulk of the time). Part 1 runs
problem-first: why a human–AI study needs a platform like this, then what it is.

## Before the room opens

- [ ] Projector at 16:9. Render the deck fresh; open `mosaic-tutorial.html`, press `f`.
- [ ] Your own MOSAIC install working, in a venv, with a **large terminal font**.
- [ ] A 3×3 mission already running in a second window, paused, as the fallback demo.
- [ ] `SETUP.md` printed or on a slide QR code — the install step is the single
      biggest source of lost minutes. **Part 1 no longer holds the install slide**,
      so ask the room to start `git clone` while you talk over slide 3; they run
      the rest together at slide 9.
- [ ] Spare laptop with MOSAIC pre-installed for anyone whose machine fights back.
- [ ] Ask a labmate to float as an install helper during Part 2.

## Timing

| Time | Slides | Block | Notes |
| --- | --- | --- | --- |
| 0:00–0:03 | 1–2 | Welcome | Say the one sentence that matters: "open a terminal and run `git clone https://github.com/iHuman-Lab/mosaic.git` now — we install together in ten minutes." The clone finishes while you do Part 1. |
| 0:03–0:15 | 3–7 | Part 1 · understanding MOSAIC | Twelve minutes, no more. Slide 3 states the problem — stay on it long enough that the four disconnected pieces land, because slide 4 is the same four connected. Slide 5 is the annotated screenshot: click through all four reveals, it is the fastest way to teach the task. Slide 6 (the collaboration loop) is the one slide that earns the tutorial its title; do not rush it. |
| 0:15–0:42 | 8–17 | **Part 2 · install** | The hands-on block. Slide 9 is the whole install on one slide — leave it up while people catch up, then walk the same seven lines slowly. Announce a hard stop at 0:42. Walk the room. Slides 13–14 are the pygame-ce trap — say the fix out loud to the whole room the first time it comes up. Leave slides 16–17 (troubleshooting) up while you circulate. |
| 0:42–1:20 | 18–29 | **Part 3 · play, then tweak** | Two beats: play a mission (19–23), then turn the knobs (24–28). Slide 29 is the "try this now" card grid — that is where they should spend the last ten minutes of the block. |
| 1:20–1:30 | 30–31 | Next steps and Q&A | Appendix slides 33–43 are on hand for whatever they ask. |

## Things that will happen

**A third of the room will not have installed.** That is normal. Part 1 buys them
only the clone, not the install, so expect more stragglers than the old running
order produced — start Part 2 on time anyway and let helpers catch them up while
slide 10 stays on screen.

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
the per-room semantics, and it is on slide 15.

**Someone will try `FullviewCamera` after slide 26 and get an `AttributeError`.**
Known bug (no `reset()` on that camera). The slide warns about it, but say it
anyway. Working cameras: `AgentFOVCamera`, `AgentConeCamera`, `EdgeFollowCamera`.

**Someone will say their seeded world changed anyway.** They seeded only
`env.reset(seed=...)`. The placers draw from the global `random`, so
`random.seed(...)` is needed too — that is slide 28, and it is a real bug on our
side, not user error.

**Someone will ask where the advisor lab went.** It is in the appendix
(slides 37–39) and in `labs/advisor.py`. Offer to walk it with them afterwards;
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

1. Slide 21 — what's on screen (slide 5 already annotates the same screenshot,
   and the controls slide covers the rest)
2. Slide 27 — knob 4, what mistakes cost
3. Slide 7 — what researchers can study (only if Part 1 is overrunning badly;
   the four research questions are the easiest thing to say out loud instead)

Never cut: slide 3 (why it exists — it sets up slide 4's diagram), slide 6 (the
collaboration loop), the install slides, Part 2 in full, the controls slide,
playing a mission, or the "try this now" grid.

## Closing ask

End on slide 30 and make one concrete request: **open an issue when it breaks on
your machine.** That converts an audience into contributors better than any
roadmap slide does.
