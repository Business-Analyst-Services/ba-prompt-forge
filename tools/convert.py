"""Convert a library prompt into another framework, or into an agent skill.

    python tools/convert.py BB-01-D1                      # CARE (default)
    python tools/convert.py BB-01-D1 --format co-star     # another framework
    python tools/convert.py BB-01-D1 --format rtf --fidelity
    python tools/convert.py BB-01-D1 --to-skill           # print a SKILL.md
    python tools/convert.py --all --to-skill -o skills/generated
    python tools/convert.py --formats                     # list frameworks
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from formats import FORMATS, fidelity, render  # noqa: E402
from lib_ir import all_prompts, slugify  # noqa: E402


def find(prompt_id: str) -> dict:
    for p in all_prompts():
        if p["id"].lower() == prompt_id.lower():
            return p
    raise SystemExit(f"No prompt with id {prompt_id!r}. See INDEX.md.")


# Library prompts are written in the first person ("My work must respect...",
# "mark anything you could not verify from my inputs"). A SKILL.md addresses the
# agent *about* the user, so those pronouns have to shift before they are reused.
PERSON_SHIFT = [
    (r"\bMy work\b", "The user's work"),
    (r"\bmy organisation's\b", "the user's organisation's"),
    (r"\bmy organisation\b", "the user's organisation"),
    (r"\bEverything I paste\b", "Everything the user pastes"),
    (r"\bI paste\b", "the user pastes"),
    (r"\bmy inputs\b", "the user's inputs"),
    (r"\bmy review\b", "the user's review"),
    (r"\bmy pasted inputs\b", "the user's pasted inputs"),
    (r"\balert me\b", "alert them"),
    (r"\bask me\b", "ask the user"),
    (r"\btell me\b", "tell the user"),
    (r"\bI expect\b", "the user expects"),
    (r"\bI am\b", "the user is"),
    # Catch-all, applied last: every remaining "my X" in the library is possessive
    # and refers to the user ("my notes", "my constraints", "my analysis partner").
    (r"\bMy\b", "The user's"),
    (r"\bmy\b", "the user's"),
]


def shift_person(text: str) -> str:
    for pattern, replacement in PERSON_SHIFT:
        text = re.sub(pattern, replacement, text)
    return text


def skill_name(p: dict) -> str:
    base = slugify(f"ba {p['service']}" if p["type"] == "master" else f"ba {p['name']}")
    return base[:64].rstrip("-")


def to_skill(p: dict) -> str:
    """A prompt becomes an agent skill: SKILL.md front-matter plus instructions.

    The skill is not just the prompt text pasted in. A prompt is a single turn; a
    skill is a procedure, so the CARE fields become steps the agent works through -
    gather inputs, ask the clarifying questions, produce, then self-verify.
    """
    triggers = ", ".join(p.get("deliverables", [])[:4]) or p["service"]
    description = shift_person(
        f"Use when the user is working on {p['service'].lower()} and needs "
        f"{triggers.lower()}. {p['task'].split('.')[0].rstrip(':')}. "
        f"Produces a reviewable first draft for {p['audience'].split(';')[0].lower()}."
    )[:1020]
    # Descriptions routinely contain ": " and other YAML metacharacters, so the
    # front-matter must be emitted by the YAML writer, never by f-string.
    front = yaml.dump(
        {
            "name": skill_name(p),
            "description": description,
            "license": (p.get("provenance") or {}).get("license", "CC-BY-4.0"),
        },
        sort_keys=False,
        allow_unicode=True,
        width=10**6,
        default_flow_style=False,
    )
    inputs = "\n".join(f"{i}. `[{name}]`" for i, name in enumerate(p.get("inputs", []), 1))
    modes = p.get("modes") or []
    steps = "\n".join(f"- {shift_person(m)}" for m in (modes or [p["task"]]))
    guardrails = "\n".join(f"- {shift_person(g)}" for g in p.get("guardrails", []))

    return f"""---
{front}---

# {p['name']}

Derived from `{p['id']}` in the BA Prompt Forge library
({p['role']} / {p['service']}, scored {(p.get('score') or {}).get('total', '?')}/20
against the CARE + G.E.T. rubric).

## When to use this

The user is doing {p['service'].lower()} work and needs one of:
{chr(10).join(f"- {d}" for d in p.get("deliverables", [])) or "- " + p["service"]}

The audience for whatever you produce is: **{p['audience']}**.

## Before you start

{shift_person(p['data_safety'])}

Collect these inputs from the user. Do not guess them:

{inputs or "1. The work to be analysed."}

Then ask up to {p.get('clarifiers', 5)} clarifying questions about anything still
missing, and **wait for the answers** before drafting.

## What to produce

{steps}

Format the output exactly as follows:

> {shift_person(p['output_format'])}

{p.get('tone') or ''}

## Rules

{guardrails}
- Do not ask the user to paste real personal or sensitive data.

## Worked example to imitate

{shift_person(p.get('example') or '(none supplied)')}

## Before you hand it back

1. **Explain** - break down, step by step, the logic you used: how you interpreted
   each input and why you structured the output the way you did.
2. **Test** - list the sources you drew on (the user's inputs, earlier turns, or
   your own general knowledge; label which is which), cross-reference the key facts
   against them, flag anything that does not trace back to a source, and list every
   assumption you made so the user can verify or correct it.
"""


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("id", nargs="?", help="prompt id, e.g. BB-01-D1")
    ap.add_argument("-f", "--format", default="care", help="target framework")
    ap.add_argument("--to-skill", action="store_true", help="emit a SKILL.md instead")
    ap.add_argument("--all", action="store_true", help="every prompt in the library")
    ap.add_argument("-o", "--out", type=Path, help="write to this directory")
    ap.add_argument("--fidelity", action="store_true", help="report what the conversion costs")
    ap.add_argument("--formats", action="store_true", help="list supported frameworks")
    args = ap.parse_args()

    if args.formats:
        for key, meta in FORMATS.items():
            print(f"{key:<10} {meta['label']:<16} {meta['note']}")
        return 0

    if not (args.id or args.all):
        ap.error("give a prompt id, or --all")

    prompts = all_prompts() if args.all else [find(args.id)]

    for p in prompts:
        if args.to_skill:
            content, name = to_skill(p), f"{skill_name(p)}/SKILL.md"
        else:
            content, name = render(p, args.format), f"{p['id']}.{args.format}.md"

        if args.out:
            target = args.out / name
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(content, encoding="utf-8")
        elif not args.all:
            print(content)

    if args.out:
        print(f"Wrote {len(prompts)} file(s) to {args.out}")

    if args.fidelity and not args.all:
        report = fidelity(prompts[0], args.format)
        print(f"\n--- fidelity: {report['label']} ---", file=sys.stderr)
        print(f"{report['original_total']}/20 -> {report['converted_total']}/20", file=sys.stderr)
        if report["criteria_lost"]:
            for label, cost in report["criteria_lost"].items():
                print(f"  -{cost}  {label}", file=sys.stderr)
        else:
            print("  lossless", file=sys.stderr)
        print(f"  {report['note']}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
