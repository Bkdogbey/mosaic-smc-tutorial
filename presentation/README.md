# MOSAIC SMC tutorial

A 39-slide tutorial in the existing iHuman Lab design, with three major parts:

1. Overview of the search-and-rescue task, capabilities and components.
2. OS-specific installation through a verified environment and first game window.
3. Game features, rescue practice, map and camera changes, offline advice and research setup.

There are 36 slides in the main sequence and 3 reference appendix slides. The original lab theme, logo, footer, cover and 1280×720 slide dimensions remain.

## View

From presentation:

~~~bash
python -m http.server 8000
~~~

Open http://localhost:8000/mosaic-tutorial.html in a browser. Keep the HTML, assets and mosaic-tutorial_files together. Quarto is not required to view the committed deck.

F toggles fullscreen, S opens speaker notes and Esc shows the overview. The deck includes linked sections, OS tabs, code-copy buttons and restrained reveals. The theme may request the original online font; a sans-serif fallback remains available.

## Files

| File | Purpose |
| --- | --- |
| mosaic-tutorial.html | Ready-to-open interactive deck |
| mosaic-tutorial.qmd | Editable Quarto source |
| theme.scss | Original lab theme |
| tutorial.css, tutorial.js | Tutorial layout and accessible OS tabs |
| interaction.html | Script include used by Quarto |
| SETUP.md, SETUP.html | Attendee installation, troubleshooting and exercises |
| RUNSHEET.md | 90-minute facilitation guide |
| REFERENCES.md, REFERENCES.html | Source mapping, image credits and behavior notes |
| labs/play.py | Small game with editable settings |
| labs/tweak.py | Camera and rescue-component example |
| labs/advisor.py | Offline custom advisor |
| labs/check_install.py | Environment, rendering and advisor check |
| labs/record.py | Three-action JSONL trace |

## Edit and render

Edit mosaic-tutorial.qmd. It uses native HTML for tables, code-copy controls and OS tabs within Quarto slides. This keeps the committed HTML content and source aligned.

~~~bash
quarto render mosaic-tutorial.qmd
~~~

The interactive deck was reconstructed directly from the existing HTML shell after the earlier workspace became unavailable. This revision received structural checks; a fresh browser and projector rehearsal is still required. Earlier exercise-behavior checks used Linux/Python 3.12.14. Windows and macOS instructions need platform rehearsal.

## Software baseline

MOSAIC commit a409222534dcd234dd2925a5adab8da9db17e6b2. Follow SETUP.html for the pygame/pygame-ce repair. The main exercises need neither ixp nor a model API key.

Run labs from presentation with the MOSAIC venv selected. Clone the software and tutorial into sibling folders as shown in the handout. Example recordings are ignored by Git.

Sources include the MOSAIC code, REFERENCE.md, docs/ and gh-pages. Existing repository screenshots are reused; no newly captured assets are claimed in this reconstruction.
