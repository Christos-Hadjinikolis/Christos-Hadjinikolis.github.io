#!/usr/bin/env python3
"""Export the working seminar to the public site without private preparation data.

Run after editing/rebuilding tmp/ucl-seminar. Only the explicitly listed public
fields are exported; a slide marked private_source is omitted entirely.
"""
from pathlib import Path
import json, shutil, subprocess, sys, tempfile

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "tmp/ucl-seminar"
DEST = ROOT / "presentations/ucl-ai-trust"
PUBLIC_FIELDS = {"key", "id", "title", "body", "kind", "img", "credit", "alt",
                 "group", "appendix", "sec", "intro", "bullets", "refs", "context"}
BUILD_FILES = ["build-deck.py", "build-notes.py", "notes-viewer.html",
               "presenter-sync.js", "institution-diagrams.css", "context-revision.css",
               "rehearsal.css", "plain-language.css"]

def main():
    original = json.loads((SOURCE / "research/deck-content.json").read_text())
    public = []
    for slide in original:
        if slide.get("private_source"):
            continue
        item = {k: v for k, v in slide.items() if k in PUBLIC_FIELDS}
        item["id"] = len(public) + 1
        item["cue"] = ""
        item["note"] = item["intro"] + "\n" + "\n".join(item["bullets"])
        public.append(item)
    with tempfile.TemporaryDirectory(prefix="ucl-public-") as folder:
        work = Path(folder)
        (work / "research").mkdir()
        for filename in BUILD_FILES:
            shutil.copy2(SOURCE / "research" / filename, work / "research" / filename)
        (work / "research/deck-content.json").write_text(json.dumps(public, ensure_ascii=False))
        for filename in ["build-deck.py", "build-notes.py"]:
            subprocess.run([sys.executable, str(work / "research" / filename)], check=True, capture_output=True)
        DEST.mkdir(parents=True, exist_ok=True)
        for filename in ["slides.html", "notes.html", "notes.md", "sources.md"]:
            text = (work / filename).read_text()
            if filename == "sources.md":
                text = text.replace("Historical extended notes are in archive/before-presenter-cues-2026-10-06/.", "Public presentation references and image credits.")
            for forbidden in ["private_source", "N1275", "/Users/", "Registration deadline passed"]:
                if forbidden in text:
                    raise ValueError(f"Private preparation marker in {filename}: {forbidden}")
            (DEST / filename).write_text(text.rstrip() + "\n")
        shutil.copytree(SOURCE / "assets/logos", DEST / "assets/logos", dirs_exist_ok=True)
    print(f"Exported {len(public)} slides with public speaker notes to {DEST.relative_to(ROOT)}")

if __name__ == "__main__":
    main()
