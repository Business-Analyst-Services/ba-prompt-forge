"""One-shot import: BA_Prompt_Library_CARE_GET_v1_0_Portable.xlsx -> library/*.md

Parses each CARE cell into format-neutral IR fields. The workbook is written to a
strict template, so every rule below is asserted against all 126 rows -- a parse
miss is a hard failure, not a silent fallback.

    python tools/extract_workbook.py source/BA_Prompt_Library_CARE_GET_v1_0_Portable.xlsx
"""
from __future__ import annotations

import re
import sys
from datetime import date
from pathlib import Path

import openpyxl

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib_ir import CRITERIA, LIBRARY, ROLE_SLUGS, ROOT, placeholders, slugify, verdict_for, write_prompt  # noqa: E402

SAFETY_RE = re.compile(
    r"(My work must respect.*?before proceeding\.)\s*", re.S
)
PERSONA_RE = re.compile(r"^I am (an? [^.]+|the [^.]+)\.\s*")
WORKING_RE = re.compile(r"^I am working on (\[[^\]]+\])\.\s*")
AUDIENCE_RE = re.compile(r"The audience for this output:?\s*(.+)$", re.S)
CLARIFY_RE = re.compile(
    r"\s*(?:Before drafting|Before you draft|Before starting|Before you start)[^.]*?ask me up to (\d+) clarifying questions[^.]*\.\s*(?:then wait[^.]*\.)?\s*$",
    re.S | re.I,
)
ANTIFAB_RE = re.compile(r"(Do not invent facts or figures:.*?\[PROPOSED[^\]]*\]\.)", re.S)
DRAFT_RE = re.compile(r"(Treat the output as a first draft[^.]*\.)")
TONE_RE = re.compile(r"(Keep the language[^.]*\.)")
MODE_RE = re.compile(r"\((\d+)\)\s*(.+?)(?=\s*[;.]\s*\(\d+\)|\.?\s*$)", re.S)


class ParseError(Exception):
    pass


def take(pattern: re.Pattern, text: str, *, required: bool = True, label: str = "") -> tuple[str | None, str]:
    """Pop the first match out of `text`; return (captured, remainder)."""
    match = pattern.search(text)
    if not match:
        if required:
            raise ParseError(f"no match for {label or pattern.pattern[:40]}")
        return None, text
    return match.group(1).strip(), (text[: match.start()] + " " + text[match.end() :]).strip()


def clean(text: str) -> str:
    return re.sub(r"\s{2,}", " ", (text or "").replace("\u00a0", " ")).strip()


def parse_context(cell: str) -> dict:
    text = clean(cell)
    persona, text = take(PERSONA_RE, text, label="persona")
    project, text = take(WORKING_RE, text, required=False, label="project")
    safety, text = take(SAFETY_RE, text, label="data-safety rule")
    audience, text = take(AUDIENCE_RE, text, label="audience")
    situation = clean(text)
    return {
        "persona": persona,
        "project_placeholder": project,
        "situation": situation or None,
        "audience": audience.rstrip("."),
        "data_safety": safety,
    }


def parse_action(cell: str) -> dict:
    text = clean(cell)
    clarifiers, text = take(CLARIFY_RE, text, label="clarifying-questions sentence")
    task = clean(text)
    modes = [clean(m.group(2)).rstrip(";.") for m in MODE_RE.finditer(task)]
    if modes:
        task = clean(MODE_RE.split(task)[0]).rstrip(":; ")
    return {"task": task, "modes": modes, "clarifiers": int(clarifiers)}


def parse_result(cell: str) -> dict:
    text = clean(cell)
    guardrails = []
    for pattern, label in ((ANTIFAB_RE, "anti-fabrication"), (DRAFT_RE, "draft-status")):
        value, text = take(pattern, text, label=label)
        guardrails.append(value)
    tone, text = take(TONE_RE, text, required=False)
    return {"output_format": clean(text), "tone": tone, "guardrails": guardrails}


def delivery_context_map(workbook) -> dict[str, list[str]]:
    """prompt id -> the delivery contexts that reference it."""
    mapping: dict[str, list[str]] = {}
    for row in workbook["Delivery Contexts"].iter_rows(min_row=2, values_only=True):
        if not row[0]:
            continue
        name = clean(row[0])
        for pid in re.split(r"[,\s]+", clean(row[4] or "")):
            if pid:
                mapping.setdefault(pid, []).append(name)
    return mapping


def main(xlsx: Path) -> int:
    workbook = openpyxl.load_workbook(xlsx, data_only=True)
    library = list(workbook["Prompt Library"].iter_rows(min_row=2, values_only=True))
    scores = {
        r[0]: r
        for r in workbook["Prompt Scores"].iter_rows(min_row=2, values_only=True)
        if r[0] and re.match(r"^[A-Z]{2}-\d{2}-", str(r[0]))
    }
    contexts = delivery_context_map(workbook)

    written, failures = 0, []
    for row in library:
        pid = clean(row[0])
        if not pid:
            continue
        try:
            ctx = parse_context(row[6])
            act = parse_action(row[7])
            res = parse_result(row[8])
        except ParseError as exc:
            failures.append(f"{pid}: {exc}")
            continue

        role = clean(row[1])
        service = clean(row[2])
        score_row = scores.get(pid)
        if not score_row:
            failures.append(f"{pid}: no score row")
            continue
        marks = {key: int(score_row[4 + i]) for i, (key, _) in enumerate(CRITERIA)}
        total = sum(marks.values())

        data = {
            "id": pid,
            "name": clean(row[3]),
            "type": clean(row[4]).lower(),
            "role": role,
            "service": service,
            "deliverables": [d.strip() for d in clean(row[5]).split(";") if d.strip()],
            "delivery_contexts": contexts.get(pid, []),
            "persona": ctx["persona"],
            "audience": ctx["audience"],
            "situation": ctx["situation"],
            "project_placeholder": ctx["project_placeholder"],
            "data_safety": ctx["data_safety"],
            "task": act["task"],
            "modes": act["modes"],
            "clarifiers": act["clarifiers"],
            "output_format": res["output_format"],
            "tone": res["tone"],
            "guardrails": res["guardrails"],
            "example": clean(row[9]),
            "validation": "get",
            "inputs": placeholders(row[6], row[7], row[8]),
            "score": {
                **marks,
                "total": total,
                "verdict": verdict_for(total),
                "notes": clean(score_row[16]),
                "scored_by": "workbook v1.0 (author self-assessment)",
            },
            "provenance": {
                "author": "Business Analyst Services",
                "author_github": "Business-Analyst-Services",
                "source": f"{xlsx.name} (v1.0 portable edition)",
                "added": str(date.today()),
                "license": "CC-BY-4.0",
            },
        }
        data = {k: v for k, v in data.items() if v not in (None, [], "")}

        out_dir = LIBRARY / ROLE_SLUGS[role] / slugify(service)
        out_dir.mkdir(parents=True, exist_ok=True)
        write_prompt(out_dir / f"{pid}.md", data, "<!-- generated by tools/build.py -->")
        written += 1

    if failures:
        print(f"FAILED to parse {len(failures)} row(s):", file=sys.stderr)
        for line in failures:
            print("  " + line, file=sys.stderr)
        return 1
    print(f"Extracted {written} prompts into {LIBRARY.relative_to(ROOT)}/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(Path(sys.argv[1] if len(sys.argv) > 1 else ROOT / "source" / "BA_Prompt_Library_CARE_GET_v1_0_Portable.xlsx")))
