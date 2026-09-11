"""Render one canonical prompt (IR) into any supported prompt framework.

Every renderer declares which of the 10 rubric criteria its slots can actually
carry. That makes conversion honest: converting a 20/20 CARE prompt into RTF
does not produce a 20/20 RTF prompt, and `fidelity()` says so with numbers.
"""
from __future__ import annotations

from lib_ir import CRITERIA

ALL = {key for key, _ in CRITERIA}


def _numbered(items: list[str]) -> str:
    return "\n".join(f"{i}. {item.rstrip('.;')}." for i, item in enumerate(items, 1))


def _sentence_case(text: str) -> str:
    """Upper-case the first letter only - str.capitalize() would lower-case
    the rest and turn "(Business BA)" into "(business ba)"."""
    return text[:1].upper() + text[1:] if text else text


def _bullets(items) -> str:
    return "\n".join(f"- {item}" for item in items if item)


def _clarify(p: dict) -> str:
    n = p.get("clarifiers")
    if not n:
        return ""
    return (
        f"Before drafting, ask me up to {n} clarifying questions about anything missing, "
        "then wait for my answers."
    )


def _task_block(p: dict) -> str:
    task = p["task"]
    modes = p.get("modes") or []
    if modes:
        return f"{task.rstrip(':. ')}:\n{_numbered(modes)}"
    return task


def _validation(p: dict) -> str:
    return (
        "Generate: produce the output requested above.\n"
        "Explain: then break down, step by step, the logic you used to synthesise your answer "
        "- how you interpreted each of my inputs and why you structured the output the way you did.\n"
        "Test: list the source references you used (my pasted inputs, earlier turns, or your general "
        "knowledge - label which is which); cross-reference the key facts in your output against those "
        "sources and flag anything that does not trace back to a source; and list every additional "
        "assumption you made so I can verify or correct it."
    )


def _context_sentences(p: dict) -> str:
    parts = [f"I am {p['persona']}."]
    if p.get("project_placeholder"):
        parts.append(f"I am working on {p['project_placeholder']}.")
    parts.append(p["data_safety"])
    if p.get("situation"):
        parts.append(p["situation"])
    parts.append(f"The audience for this output: {p['audience']}.")
    return " ".join(parts)


def _join(parts) -> str:
    return "\n".join(x for x in parts if x is not None)


# --------------------------------------------------------------------------- #
# Renderers
# --------------------------------------------------------------------------- #

def care(p: dict) -> str:
    fmt = [p["output_format"]]
    if p.get("tone"):
        fmt.append(p["tone"])
    fmt += p.get("guardrails", [])
    out = ["# CONTEXT", _context_sentences(p), "", "# ACTION", _task_block(p)]
    if _clarify(p):
        out += ["", _clarify(p)]
    out += ["", "# RESULT / FORMAT", " ".join(fmt)]
    if p.get("example"):
        out += ["", "# EXAMPLE", p["example"]]
    out += ["", "# VALIDATION (GENERATE -> EXPLAIN -> TEST)", _validation(p)]
    return _join(out)


def co_star(p: dict) -> str:
    example = f"Worked example to imitate: {p['example']}" if p.get("example") else None
    return _join([
        "# CONTEXT", _context_sentences(p), "",
        "# OBJECTIVE", _task_block(p), "", _clarify(p), "",
        "# STYLE", p["output_format"], "",
        "# TONE", p.get("tone") or "Professional, plain English, no marketing language.", "",
        "# AUDIENCE", p["audience"] + ".", "",
        "# RESPONSE", " ".join(p.get("guardrails", [])), "", example, "",
        _validation(p),
    ])


def rtf(p: dict) -> str:
    return _join([
        f"**Role:** {_sentence_case(p['persona'])}, writing for {p['audience']}.", "",
        f"**Task:** {_task_block(p)}", "",
        f"**Format:** {p['output_format']}",
    ])


def race(p: dict) -> str:
    context = " ".join(
        x for x in [p.get("situation"), p["data_safety"], f"Audience: {p['audience']}."] if x
    )
    return _join([
        f"**Role:** I am {p['persona']}.", "",
        f"**Action:** {_task_block(p)}", "",
        f"**Context:** {context}", "",
        "**Expectation:** " + " ".join([p["output_format"], *p.get("guardrails", [])]),
    ])


def risen(p: dict) -> str:
    steps = p.get("modes") or [
        "Ask the clarifying questions below and wait for my answers",
        p["task"],
        "Self-check the draft against the constraints before returning it",
    ]
    return _join([
        f"**Role:** {_sentence_case(p['persona'])}.", "",
        f"**Instructions:** {p['task']}", "",
        "**Steps:**", _numbered(steps), "",
        f"**End goal:** A reviewable first draft that {p['audience']} can act on.", "",
        "**Narrowing (constraints):**",
        _bullets([p["output_format"], p.get("tone"), *p.get("guardrails", []),
                  p["data_safety"], _clarify(p)]),
    ])


def tidd_ec(p: dict) -> str:
    donts = list(p.get("guardrails", [])) + [
        "Do not ask me to paste real personal or sensitive data."
    ]
    return _join([
        "# TASK", _task_block(p), "",
        "# INSTRUCTIONS", _clarify(p),
        "Then generate the output, explain the synthesis logic you used, and test it: cite which parts "
        "came from my inputs versus your general knowledge, flag anything that does not trace back to a "
        "source, and list the assumptions you made.", "",
        "# DO", _bullets([p["output_format"], p.get("tone")]), "",
        "# DONT", _bullets(donts), "",
        "# EXAMPLES", p.get("example") or "(none supplied)", "",
        "# CONTEXT", _context_sentences(p),
    ])


def crispe(p: dict) -> str:
    insight = " ".join(
        x for x in [p.get("situation"), p["data_safety"], f"This is for {p['audience']}."] if x
    )
    personality = (p.get("tone") or "Professional, plain English, no marketing language.")
    return _join([
        f"**Capacity / Role:** Act as {p['persona']}.", "",
        f"**Insight:** {insight}", "",
        f"**Statement:** {_task_block(p)} {_clarify(p)}", "",
        f"**Personality:** {personality} " + " ".join(p.get("guardrails", [])), "",
        "**Experiment:** Give me the draft in the format below, then offer one alternative structure "
        "and say when you would use it instead.", "",
        f"**Format:** {p['output_format']}",
    ])


def ape(p: dict) -> str:
    return _join([
        f"**Action:** {_task_block(p)}", "",
        f"**Purpose:** So that {p['audience']} can review and act on it.", "",
        f"**Expectation:** {p['output_format']} " + " ".join(p.get("guardrails", [])),
    ])


def bab(p: dict) -> str:
    before = p.get("situation") or "I have the raw inputs but no structured artefact."
    return _join([
        f"**Before:** I am {p['persona']}. {before} Right now this work is unstructured and "
        "cannot be reviewed.", "",
        f"**After:** {p['audience']} has a reviewable draft: {p['output_format']}", "",
        f"**Bridge:** {_task_block(p)} {_clarify(p)} " + " ".join(p.get("guardrails", [])),
    ])


def chat(p: dict) -> str:
    """Compact single-paragraph build for short-context chat boxes."""
    return (
        f"Act as {p['persona']} writing for {p['audience']}. {p['task']} "
        f"{_clarify(p)} Format: {p['output_format']} "
        + " ".join(p.get("guardrails", []))
        + " Finish by listing your assumptions and which claims came from my inputs "
        "versus your own knowledge."
    )


# --------------------------------------------------------------------------- #
# Registry: renderer + the criteria each format's slots can carry
# --------------------------------------------------------------------------- #

FORMATS: dict[str, dict] = {
    "care": {
        "label": "CARE + G.E.T.",
        "fn": care,
        "carries": ALL,
        "note": "The library's native format. Context, Action, Result/Format, Example, "
                "plus Generate -> Explain -> Test.",
    },
    "co-star": {
        "label": "CO-STAR",
        "fn": co_star,
        "carries": ALL,
        "note": "Splits CARE's Result into Style/Tone/Response and promotes Audience to its "
                "own slot. Lossless.",
    },
    "tidd-ec": {
        "label": "TIDD-EC",
        "fn": tidd_ec,
        "carries": ALL,
        "note": "The only common format with an explicit DONT slot, so anti-fabrication and "
                "data-safety rules land naturally.",
    },
    "risen": {
        "label": "RISEN",
        "fn": risen,
        "carries": ALL - {"c4_example"},
        "note": "Strong for multi-step work. No Example slot, so the worked example is lost.",
    },
    "crispe": {
        "label": "CRISPE",
        "fn": crispe,
        "carries": ALL - {"c4_example", "c6_test"},
        "note": "Its Experiment slot asks for alternatives rather than verification, and there "
                "is no Example slot.",
    },
    "race": {
        "label": "RACE",
        "fn": race,
        "carries": ALL - {"c4_example", "c5_explain", "c6_test"},
        "note": "Compact four-slot format. Keeps guardrails and audience; drops the worked "
                "example and the whole G.E.T. validation step.",
    },
    "rtf": {
        "label": "RTF",
        "fn": rtf,
        "carries": {"c1_context", "c2_action", "c3_result", "c9_reusability", "c10_right_sized"},
        "note": "Minimal. Fine for a quick one-off; strips every verification and safety rule.",
    },
    "ape": {
        "label": "APE",
        "fn": ape,
        "carries": {"c2_action", "c3_result", "c7_anti_fabrication", "c9_reusability",
                    "c10_right_sized"},
        "note": "Purpose-led and very short. No role, audience or example.",
    },
    "bab": {
        "label": "BAB",
        "fn": bab,
        "carries": {"c1_context", "c2_action", "c3_result", "c7_anti_fabrication",
                    "c9_reusability"},
        "note": "Persuasive narrative shape. A poor fit for deliverable prompts - use it to "
                "pitch the work, not to produce it.",
    },
    "chat": {
        "label": "Compact chat",
        "fn": chat,
        "carries": {"c1_context", "c2_action", "c3_result", "c7_anti_fabrication",
                    "c9_reusability", "c10_right_sized"},
        "note": "One paragraph for short-context chat boxes. Deliberately lossy.",
    },
}


def render(prompt: dict, fmt: str) -> str:
    if fmt not in FORMATS:
        raise KeyError(f"unknown format {fmt!r}; known: {', '.join(sorted(FORMATS))}")
    return FORMATS[fmt]["fn"](prompt).strip()


def fidelity(prompt: dict, fmt: str) -> dict:
    """What the conversion costs, in rubric points."""
    carries = FORMATS[fmt]["carries"]
    score = prompt.get("score", {})
    original = score.get("total", 0)
    lost = {
        label: score.get(key, 0)
        for key, label in CRITERIA
        if key not in carries and score.get(key, 0)
    }
    return {
        "format": fmt,
        "label": FORMATS[fmt]["label"],
        "original_total": original,
        "converted_total": original - sum(lost.values()),
        "criteria_lost": lost,
        "note": FORMATS[fmt]["note"],
    }
