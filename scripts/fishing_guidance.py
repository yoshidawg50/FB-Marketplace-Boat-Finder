#!/usr/bin/env python3
"""fishing_guidance.py — structured per-species fishing guidance from the KB.

`get_fishing_guidance(species)` parses a `species/*.md` note (front matter +
the mandatory section template defined in CLAUDE.md — Where & when, Finding
them, Situations → techniques, Gear summary, Doctrine & conflicts) into a
plain dict an app can render, independent of the note's markdown formatting.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SPECIES_DIR = ROOT / "species"

LINK_RE = re.compile(r"\[([^\]]*)\]\(([^)]+)\)")
RANK_RE = re.compile(r"(\d+)\)\s*(.*?)(?=(?:\s*\d+\)|$))")


def _slugify(name: str) -> str:
    s = name.strip().lower().replace("_", "-").replace(" ", "-")
    return re.sub(r"[^a-z0-9-]", "", s)


def _strip_md(text: str) -> str:
    text = LINK_RE.sub(r"\1", text)
    text = text.replace("**", "").replace("`", "")
    return re.sub(r"\s+", " ", text).strip()


def _parse_front_matter(text: str) -> tuple[dict, str]:
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---", 4)
    if end == -1:
        return {}, text
    raw = text[4:end]
    body_start = text.find("\n", end + 1)
    body = text[body_start + 1 :] if body_start != -1 else ""
    meta: dict = {}
    for line in raw.splitlines():
        if ":" not in line:
            continue
        key, _, val = line.partition(":")
        key, val = key.strip(), val.strip()
        if val.startswith("[") and val.endswith("]"):
            meta[key] = [v.strip() for v in val[1:-1].split(",") if v.strip()]
        else:
            meta[key] = val
    return meta, body


def _split_sections(body: str) -> tuple[str, dict[str, str]]:
    """Intro paragraph (after the H1) plus a dict of '## ' section -> content."""
    lines = body.splitlines()
    idx = 0
    while idx < len(lines) and not lines[idx].startswith("# "):
        idx += 1
    if idx < len(lines):
        idx += 1
    rest = "\n".join(lines[idx:])
    parts = re.split(r"\n##\s+", rest)
    intro = parts[0].strip()
    sections: dict[str, str] = {}
    for part in parts[1:]:
        header, _, content = part.partition("\n")
        header = header.strip()
        if header == "Linked from":
            continue  # auto-generated backlinks block, not KB content
        content = re.sub(r"<!--.*?-->", "", content, flags=re.DOTALL).strip()
        sections[header] = content
    return intro, sections


def _section(sections: dict[str, str], *prefixes: str) -> str:
    for prefix in prefixes:
        for key, val in sections.items():
            if key.lower().startswith(prefix.lower()):
                return _strip_md(val)
    return ""


def _parse_situations_table(md: str) -> list[dict]:
    rows = [l for l in md.splitlines() if l.strip().startswith("|")]
    if len(rows) < 2:
        return []

    def cells(line: str) -> list[str]:
        return [c.strip() for c in line.strip().strip("|").split("|")]

    headers = [h.lower() for h in cells(rows[0])]
    out = []
    for line in rows[2:]:  # skip header row + '---' separator row
        vals = cells(line)
        if len(vals) < len(headers):
            continue
        row = dict(zip(headers, vals))
        situation_raw = next(
            (v for k, v in row.items() if k.startswith("situation")), ""
        )
        actions_raw = next((v for k, v in row.items() if k.startswith("do this")), "")
        gear_raw = next((v for k, v in row.items() if k.startswith("gear")), "")
        notes_raw = row.get("notes", "")

        ranked = RANK_RE.findall(actions_raw)
        actions = (
            [_strip_md(a) for _, a in ranked]
            if ranked
            else ([_strip_md(actions_raw)] if actions_raw.strip() else [])
        )
        out.append(
            {
                "situation": _strip_md(situation_raw),
                "recommended_actions": actions,
                "gear_class": _strip_md(gear_raw),
                "notes": _strip_md(notes_raw),
            }
        )
    return out


def _find_species_file(species: str) -> Path:
    slug = _slugify(species)
    direct = SPECIES_DIR / f"{slug}.md"
    if direct.exists():
        return direct

    candidates = []
    for p in sorted(SPECIES_DIR.glob("*.md")):
        if p.name == "README.md":
            continue
        meta, _ = _parse_front_matter(p.read_text(encoding="utf-8"))
        tags = [t.lower() for t in meta.get("tags", [])]
        if slug in tags or slug in p.stem:
            candidates.append(p)
    if len(candidates) == 1:
        return candidates[0]

    available = sorted(
        p.stem for p in SPECIES_DIR.glob("*.md") if p.name != "README.md"
    )
    raise ValueError(
        f"no species note found for {species!r}; available: {', '.join(available)}"
    )


def get_fishing_guidance(species: str) -> dict:
    """Structured guidance for `species`, sourced from `species/<slug>.md`."""
    path = _find_species_file(species)
    meta, body = _parse_front_matter(path.read_text(encoding="utf-8"))
    intro, sections = _split_sections(body)

    situations_md = next(
        (v for k, v in sections.items() if k.lower().startswith("situations")), ""
    )

    return {
        "species": path.stem,
        "title": path.stem.replace("-", " ").title(),
        "confidence": meta.get("confidence", ""),
        "tags": meta.get("tags", []),
        "sources": meta.get("sources", []),
        "summary": _strip_md(intro),
        "where_and_when": _section(sections, "Where & when"),
        "finding_them": _section(sections, "Finding them"),
        "situations_to_techniques": _parse_situations_table(situations_md),
        "gear_summary": _section(sections, "Gear summary"),
        "doctrine_and_conflicts": _section(sections, "Doctrine & conflicts"),
        "source_file": str(path.relative_to(ROOT)),
    }


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Print structured fishing guidance for a species (default: yellowtail)."
    )
    ap.add_argument("species", nargs="?", default="yellowtail")
    args = ap.parse_args()
    try:
        guidance = get_fishing_guidance(args.species)
    except ValueError as e:
        print(f"error: {e}")
        return 1
    print(json.dumps(guidance, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
