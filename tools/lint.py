"""Deterministic half of the CARE + G.E.T. scorecard.

This is a FLOOR, not a score. Six of the ten criteria are mechanically decidable
(is there an example? does the anti-fabrication flag convention exist? is there a
marked placeholder?) and this module decides them. The other four - Context,
Action, Result/Format and Right-sized - need judgement, so they are reported as
`review` with a provisional mark and left to a human or to skills/ba-prompt-scorer.

    python tools/lint.py                 # lint the whole library
    python tools/lint.py library/.../X.md
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib_ir import CRITERIA, ROOT, all_prompts, read_prompt, verdict_for  # noqa: E402
from formats import care  # noqa: E402

STRUCTURE_WORDS = re.compile(
    r"\b(?:table|column|row|section|heading|bullet|list|field|paragraph|template|"
    r"subheading|checklist|matrix|register)s?\b"
    r"|\b(?:per (?:kpi|risk|story|requirement|item)|max(?:imum)? \d+|no more than \d+"
    r"|one row per|given/when/then|numbered)\b",
    re.I,
)
# Three or more semicolon-separated clauses is an enumerated slot list ("the
# question; why it blocks delivery; method; timebox; done means") - structure,
# even with none of the words above.
SLOT_LIST = re.compile(r"(?:[^;]+;){3,}")
CONCRETE_EXAMPLE = re.compile(r"[\"|]|\d")
# The rubric's 0-anchor is the *vague* opener ("help me with..."), not any use of
# "help me". "Help me define the real problem: ..." names a strong verb and an
# object, so it is a real task and must not be scored 0.
WEAK_VERBS = re.compile(
    r"^\s*(?:(?:help|assist) me (?:with|out|about)\b"
    r"|(?:help|assist) me\s*[.,:;]"
    r"|(?:look at|think about|explore|consider)\b)",
    re.I,
)
HARDCODED = re.compile(
    r"\b(acme|contoso|department of|ministry of|pty ltd|our client [A-Z])\b", re.I
)


def mark(value: int, why: str, confidence: str = "auto") -> dict:
    return {"mark": value, "why": why, "confidence": confidence}


def c1_context(p: dict) -> dict:
    has_persona, has_audience = bool(p.get("persona")), bool(p.get("audience"))
    has_constraints = bool(p.get("data_safety"))
    if has_persona and has_audience and has_constraints:
        return mark(2, "role, audience and constraints all stated", "review")
    if has_persona or has_audience:
        return mark(1, "role or audience stated, not both with constraints", "review")
    return mark(0, "neither role nor audience stated")


def c2_action(p: dict) -> dict:
    task = p.get("task") or ""
    if not task:
        return mark(0, "no task")
    if WEAK_VERBS.search(task):
        return mark(0, "opens with a weak verb - no clear task")
    modes = p.get("modes") or []
    if len(modes) > 1:
        return mark(
            1,
            f"a menu of {len(modes)} modes, not one task - deliberate for a Master prompt, "
            "but it costs single-task clarity",
        )
    if not p.get("inputs"):
        return mark(1, "clear task but no named inputs", "review")
    return mark(2, f"one task with {len(p['inputs'])} named input(s)", "review")


def c3_result(p: dict) -> dict:
    fmt = p.get("output_format") or ""
    if not fmt:
        return mark(0, "no output format")
    if STRUCTURE_WORDS.search(fmt) or SLOT_LIST.search(fmt):
        return mark(2, "names a checkable structure", "review")
    return mark(1, "format is stated but loose - a reviewer could not tick it off", "review")


def c4_example(p: dict) -> dict:
    example = p.get("example") or ""
    if not example:
        return mark(0, "no example")
    if CONCRETE_EXAMPLE.search(example):
        return mark(2, "concrete sample the model can imitate")
    return mark(1, "example is described rather than shown")


def c5_explain(p: dict) -> dict:
    if p.get("validation") == "get":
        return mark(2, "G.E.T. Explain step: step-by-step synthesis logic tied to the inputs")
    return mark(0, "no Explain step")


def c6_test(p: dict) -> dict:
    if p.get("validation") == "get":
        return mark(2, "G.E.T. Test step: sources + cross-reference + assumptions")
    return mark(0, "no Test step")


def c7_anti_fabrication(p: dict) -> dict:
    text = " ".join(p.get("guardrails") or [])
    forbids = re.search(r"do not invent|must not (?:invent|fabricate)|no invented", text, re.I)
    flags = re.search(r"\[TBC\]|\[PROPOSED", text, re.I)
    if forbids and flags:
        return mark(2, "explicit prohibition plus a flagging convention")
    if forbids or flags:
        return mark(1, "prohibition or flagging convention, not both")
    return mark(0, "silent on fabrication")


def c8_data_safety(p: dict) -> dict:
    text = p.get("data_safety") or ""
    if re.search(r"de-identif|synthetic|anonymis|redact", text, re.I):
        return mark(2, "explicit de-identification guidance")
    if text:
        return mark(1, "mentions constraints but gives no de-identification instruction")
    return mark(0, "silent on data safety")


def c9_reusability(p: dict) -> dict:
    if HARDCODED.search(care(p)):
        return mark(0, "contains an organisation-specific name - not portable")
    count = len(p.get("inputs") or [])
    if count >= 2:
        return mark(2, f"fully parameterised with {count} marked placeholders")
    if count == 1:
        return mark(1, "only one marked placeholder - partly generic")
    return mark(0, "no marked placeholders")


def c10_right_sized(p: dict) -> dict:
    words = len(care(p).split())
    if words > 900:
        return mark(1, f"{words} words - check every element is load-bearing", "review")
    if words < 80:
        return mark(1, f"only {words} words - likely under-specified", "review")
    return mark(2, f"{words} words, within band", "review")


CHECKS = {
    "c1_context": c1_context,
    "c2_action": c2_action,
    "c3_result": c3_result,
    "c4_example": c4_example,
    "c5_explain": c5_explain,
    "c6_test": c6_test,
    "c7_anti_fabrication": c7_anti_fabrication,
    "c8_data_safety": c8_data_safety,
    "c9_reusability": c9_reusability,
    "c10_right_sized": c10_right_sized,
}

REQUIRED = ["id", "name", "type", "role", "service", "persona", "audience", "task",
            "output_format", "provenance"]


def _schema_problems(p: dict) -> list[str]:
    """Validate front-matter against schema/prompt.schema.json, if available."""
    try:
        import json

        import jsonschema
    except ImportError:  # schema validation is optional locally, required in CI
        return []
    schema_path = ROOT / "schema" / "prompt.schema.json"
    if not schema_path.exists():
        return []
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    payload = {k: v for k, v in p.items() if not k.startswith("_")}
    validator = jsonschema.Draft7Validator(schema)
    return [
        f"schema: {'/'.join(str(x) for x in e.path) or '(root)'} - {e.message}"
        for e in sorted(validator.iter_errors(payload), key=lambda e: list(e.path))
    ]


def lint(p: dict) -> dict:
    problems = [f"missing required field: {f}" for f in REQUIRED if not p.get(f)]
    if p.get("id") and not re.match(r"^[A-Z]{2}-\d{2}-(M|D\d+|U\d+)$", p["id"]):
        problems.append(f"id {p['id']!r} does not match <RR>-<NN>-<M|Dn|Un>")
    problems += _schema_problems(p)

    results = {key: fn(p) for key, fn in CHECKS.items()}
    total = sum(r["mark"] for r in results.values())
    auto_only = sum(r["mark"] for r in results.values() if r["confidence"] == "auto")
    auto_max = sum(2 for r in results.values() if r["confidence"] == "auto")

    claimed = (p.get("score") or {}).get("total")
    if claimed is not None:
        for key, _ in CRITERIA:
            declared = (p.get("score") or {}).get(key)
            found = results[key]["mark"]
            if declared is not None and results[key]["confidence"] == "auto" and declared != found:
                problems.append(
                    f"{key}: front-matter claims {declared}, machine check finds {found} "
                    f"({results[key]['why']})"
                )

    return {
        "id": p.get("id", "?"),
        "criteria": results,
        "total": total,
        "verdict": verdict_for(total),
        "auto_confidence": f"{auto_only}/{auto_max} machine-verified",
        "problems": problems,
    }


def main(argv: list[str]) -> int:
    prompts = [read_prompt(Path(a)) for a in argv] if argv else all_prompts()
    failed = 0
    for p in prompts:
        report = lint(p)
        if report["problems"] or report["verdict"] == "Rework":
            failed += 1
            print(f"FAIL {report['id']}  {report['total']}/20  {report['verdict']}")
            for problem in report["problems"]:
                print(f"       - {problem}")
        elif argv:
            print(f"PASS {report['id']}  {report['total']}/20  {report['verdict']} "
                  f"({report['auto_confidence']})")
            for key, label in CRITERIA:
                r = report["criteria"][key]
                flag = " " if r["confidence"] == "auto" else "?"
                print(f"  {flag} {r['mark']}  {label:<16} {r['why']}")

    print(f"\n{len(prompts) - failed}/{len(prompts)} prompts pass "
          f"(mean {sum(lint(p)['total'] for p in prompts) / len(prompts):.2f}/20)")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
