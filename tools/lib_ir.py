"""Shared helpers: the canonical intermediate representation (IR) for a prompt.

A prompt file is Markdown with YAML front-matter. The front-matter IS the prompt --
format-neutral semantic fields. The body is *generated* from those fields by
tools/build.py and is never hand-edited; CI checks it is in sync.
"""
from __future__ import annotations

import re
import unicodedata
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
LIBRARY = ROOT / "library"

ROLE_SLUGS = {
    "Business BA": "business-ba",
    "Business/Tech BA": "business-tech-ba",
    "Technical BA": "technical-ba",
    "Agile BA": "agile-ba",
    "Lead BA": "lead-ba",
    "Practice Lead": "practice-lead",
}

CRITERIA = [
    ("c1_context", "Context"),
    ("c2_action", "Action"),
    ("c3_result", "Result / Format"),
    ("c4_example", "Example"),
    ("c5_explain", "Explain step"),
    ("c6_test", "Test step"),
    ("c7_anti_fabrication", "Anti-fabrication"),
    ("c8_data_safety", "Data safety"),
    ("c9_reusability", "Reusability"),
    ("c10_right_sized", "Right-sized"),
]


def slugify(text: str) -> str:
    text = unicodedata.normalize("NFKD", str(text))
    text = text.replace("&", " and ").replace("/", " ")
    text = re.sub(r"[^A-Za-z0-9]+", "-", text).strip("-").lower()
    return re.sub(r"-{2,}", "-", text)


def verdict_for(total: int) -> str:
    if total >= 17:
        return "Library-ready"
    if total >= 12:
        return "Usable - refine first"
    return "Rework"


def placeholders(*texts: str) -> list[str]:
    """Every [BRACKETED PLACEHOLDER] found, in first-seen order."""
    seen: list[str] = []
    for text in texts:
        for match in re.findall(r"\[([A-Z0-9][^\[\]]*?)\]", text or ""):
            token = match.strip()
            # [TBC] / [PROPOSED - VALIDATE] are output conventions, not inputs.
            if token in {"TBC"} or token.startswith("PROPOSED"):
                continue
            if token not in seen:
                seen.append(token)
    return seen


def read_prompt(path: Path) -> dict:
    raw = path.read_text(encoding="utf-8")
    if not raw.startswith("---\n"):
        raise ValueError(f"{path.name}: missing YAML front-matter")
    _, front, body = raw.split("---\n", 2)
    data = yaml.safe_load(front)
    data["_body"] = body.lstrip("\n")
    data["_path"] = path
    return data


def write_prompt(path: Path, data: dict, body: str) -> None:
    payload = {k: v for k, v in data.items() if not k.startswith("_")}
    front = yaml.dump(
        payload, sort_keys=False, allow_unicode=True, width=100, default_flow_style=False
    )
    path.write_text(f"---\n{front}---\n\n{body.rstrip()}\n", encoding="utf-8")


def all_prompts() -> list[dict]:
    out = [read_prompt(p) for p in sorted(LIBRARY.rglob("*.md")) if p.name != "README.md"]
    return sorted(out, key=lambda d: d["id"])
