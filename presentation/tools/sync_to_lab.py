"""Copy this deck into the iHuman Lab presentations site (mosaic-tutorial/).

    python tools/sync_to_lab.py <path to a checkout of the presentations repo>

The lab repo is one Quarto website with one folder per talk, so the deck goes
in as `<checkout>/mosaic-tutorial/` and needs four conversions:

- build output (`index.html`, `mosaic-tutorial_files/`) is left out; the site
  builds its own and the lab repo's .gitignore skips `*.html` and `*_files/`;
- `output-file: index.html` is removed, or it would collide with the site's
  home page;
- `gif-restart.html` is inlined into the front matter, because `*.html` is
  gitignored there and a missing include breaks the CI render;
- links to the tutorial repo point at the lab repo instead.

The copy mirrors this folder: files deleted here are deleted there. Running it
twice in a row changes nothing. Used by .github/workflows/sync-to-lab.yml.
"""
import pathlib
import re
import shutil
import sys

SRC = pathlib.Path(__file__).resolve().parent.parent
DECK = "mosaic-tutorial"
SKIP_NAMES = {"index.html", "gif-restart.html", "sync_to_lab.py", "__pycache__", ".DS_Store"}
SKIP_SUFFIXES = {".pyc"}
SKIP_DIRS = {"mosaic-tutorial_files", "__pycache__", ".quarto"}

# Longest match first: the specific paths must win over the bare repo link.
LINKS = [
    ("https://github.com/Bkdogbey/mosaic-smc-tutorial/tree/main/presentation/labs",
     "https://github.com/iHuman-Lab/presentations/tree/main/mosaic-tutorial/labs"),
    ("<https://github.com/Bkdogbey/mosaic-smc-tutorial>",
     "<https://github.com/iHuman-Lab/presentations/tree/main/mosaic-tutorial>"),
    ("github.com/Bkdogbey/mosaic-smc-tutorial", "github.com/iHuman-Lab/presentations"),
    ("`presentation/labs/`", "`mosaic-tutorial/labs/`"),
    ("presentation/labs/", "mosaic-tutorial/labs/"),
]


def wanted(path):
    rel = path.relative_to(SRC)
    if any(part in SKIP_DIRS for part in rel.parts):
        return False
    return path.name not in SKIP_NAMES and path.suffix not in SKIP_SUFFIXES


def inline_include(qmd, script):
    """Replace `include-after-body: gif-restart.html` with the script text."""
    old = "    include-after-body: gif-restart.html\n"
    assert old in qmd, "include-after-body line not found"
    body = "".join(f"          {line}\n" if line else "\n" for line in script.strip().splitlines())
    return qmd.replace(old, "    include-after-body:\n      - text: |\n" + body)


def convert_qmd(text, script):
    text = re.sub(r"^    output-file: index\.html\n", "", text, count=1, flags=re.M)
    text = inline_include(text, script)
    return text


def convert_links(text):
    for old, new in LINKS:
        text = text.replace(old, new)
    return text


def main(lab):
    lab = pathlib.Path(lab).resolve()
    if not (lab / "_quarto.yml").exists():
        sys.exit(f"{lab} does not look like the presentations repo (no _quarto.yml)")
    dest = lab / DECK
    script = (SRC / "gif-restart.html").read_text(encoding="utf-8")

    keep = set()
    for path in sorted(SRC.rglob("*")):
        if not path.is_file() or not wanted(path):
            continue
        rel = path.relative_to(SRC)
        target = dest / rel
        keep.add(target)
        target.parent.mkdir(parents=True, exist_ok=True)
        if path.suffix in {".qmd", ".md"}:
            text = path.read_text(encoding="utf-8")
            if path.name == "mosaic-tutorial.qmd":
                text = convert_qmd(text, script)
            text = convert_links(text)
            new = text.encode("utf-8")
        else:
            new = path.read_bytes()
        if not target.exists() or target.read_bytes() != new:
            target.write_bytes(new)
            print(f"wrote   {DECK}/{rel}")

    if dest.exists():                      # mirror deletions
        for path in sorted(dest.rglob("*"), reverse=True):
            if path.is_file() and path not in keep:
                path.unlink()
                print(f"removed {DECK}/{path.relative_to(dest)}")
            elif path.is_dir() and not any(path.iterdir()):
                path.rmdir()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
