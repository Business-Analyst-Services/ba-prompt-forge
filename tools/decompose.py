"""Split a multi-mode Master prompt into single-task units.

Every Master in the library scores 1/2 on criterion 2 (Action) for the same
reason: it offers a menu of modes rather than one task. That is deliberate - a
Master is a working session - but it makes the prompt hard to *test*, because a
test needs one input and one expected shape of output.

This tool turns each mode into a candidate unit prompt (`<ID>-U1`, `-U2`, ...),
which is a single task and therefore scores 2/2 on Action and can carry a
regression test.

Generated units land in `proposals/` - NOT in `library/`. They are drafts: the
task text is machine-derived, and the worked example is inherited from the parent
and will usually be wrong for the narrower task. A human promotes a unit into the
library after fixing its example and running it for real.

    python tools/decompose.py BB-01-M          # preview
    python tools/decompose.py --all --write    # write every candidate
"""
from __future__ import annotations

import argparse
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib_ir import ROOT, all_prompts, slugify, write_prompt  # noqa: E402
from lint import lint  # noqa: E402

PROPOSALS = ROOT / "proposals"


def units(master: dict) -> list[dict]:
    modes = master.get("modes") or []
    if len(modes) < 2:
        return []

    out = []
    for index, mode in enumerate(modes, 1):
        task = mode[0].upper() + mode[1:]
        if not task.endswith("."):
            task += "."
        unit = {
            "id": f"{master['id'].removesuffix('-M')}-U{index}",
            "name": f"{mode[0].upper() + mode[1:]}".rstrip("."),
            "type": "unit",
            "status": "proposal",
            "derived_from": master["id"],
            "role": master["role"],
            "service": master["service"],
            "deliverables": master.get("deliverables", []),
            "delivery_contexts": master.get("delivery_contexts", []),
            "persona": master["persona"],
            "audience": master["audience"],
            "situation": master.get("situation"),
            "project_placeholder": master.get("project_placeholder"),
            "data_safety": master["data_safety"],
            "task": f"Produce exactly one artefact and nothing else: {task}",
            "clarifiers": master.get("clarifiers", 5),
            "output_format": master["output_format"],
            "tone": master.get("tone"),
            "guardrails": master.get("guardrails", []),
            "example": master.get("example"),
            "validation": "get",
            "inputs": master.get("inputs", []),
            "review_needed": [
                "Narrow output_format to this one artefact - it is still the parent's.",
                "Replace the worked example: it was written for the parent prompt.",
                "Trim situation/inputs this single task does not need.",
                "Run it once on real de-identified work before promoting to library/.",
            ],
            "provenance": {
                "author": (master.get("provenance") or {}).get("author"),
                "author_github": (master.get("provenance") or {}).get("author_github"),
                "source": f"machine-decomposed from {master['id']} by tools/decompose.py",
                "added": str(date.today()),
                "license": (master.get("provenance") or {}).get("license", "CC-BY-4.0"),
            },
        }
        unit = {k: v for k, v in unit.items() if v not in (None, [], "")}
        unit["score"] = {
            **{k: v["mark"] for k, v in lint(unit)["criteria"].items()},
            "total": lint(unit)["total"],
            "verdict": lint(unit)["verdict"],
            "notes": "Provisional: machine-derived from the parent Master, not yet human-reviewed.",
            "scored_by": "tools/lint.py (machine floor)",
        }
        out.append(unit)
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("id", nargs="?", help="a Master prompt id, e.g. BB-01-M")
    ap.add_argument("--all", action="store_true", help="every multi-mode prompt")
    ap.add_argument("--write", action="store_true", help="write to proposals/")
    args = ap.parse_args()

    prompts = all_prompts()
    if args.id:
        prompts = [p for p in prompts if p["id"].lower() == args.id.lower()]
        if not prompts:
            raise SystemExit(f"No prompt with id {args.id!r}")
    elif not args.all:
        ap.error("give a prompt id, or --all")

    total, parents = 0, 0
    for parent in prompts:
        candidates = units(parent)
        if not candidates:
            continue
        parents += 1
        for unit in candidates:
            total += 1
            if args.write:
                path = PROPOSALS / slugify(parent["role"]) / f"{unit['id']}.md"
                path.parent.mkdir(parents=True, exist_ok=True)
                write_prompt(path, unit, "<!-- proposal: run tools/build.py after promoting -->")
            else:
                gain = unit["score"]["total"] - (parent.get("score") or {}).get("total", 0)
                print(f"{unit['id']:<12} {unit['score']['total']}/20 "
                      f"({gain:+d} vs {parent['id']})  {unit['name'][:70]}")

    verb = "Wrote" if args.write else "Would write"
    print(f"\n{verb} {total} unit proposal(s) from {parents} multi-mode prompt(s)"
          + (f" into {PROPOSALS.relative_to(ROOT)}/" if args.write else ""))
    if not args.write and total:
        print("Re-run with --write to create them. They are drafts: each needs its "
              "example rewritten and its format narrowed before promotion.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
