---
name: ba-tool-ai-capability-evaluation
description: Use when the user is working on tooling & ai enablement and needs tool evaluations, recommendations. Evaluate the candidate against real BA use cases and recommend adopt / trial / decline with evidence. Produces a reviewable first draft for practice sponsor and it/security.
license: CC-BY-4.0
---

# Tool / AI Capability Evaluation

Derived from `PL-07-D1` in the BA Prompt Forge library
(Practice Lead / Tooling & AI Enablement, scored 20/20
against the CARE + G.E.T. rubric).

## When to use this

The user is doing tooling & ai enablement work and needs one of:
- Tool Evaluations
- Recommendations

The audience for whatever you produce is: **Practice sponsor and IT/security; the BAs who trialled it**.

## Before you start

The user's work must respect the user's organisation's privacy, information-security and data-residency obligations. Everything the user pastes is de-identified or synthetic — if any input appears to contain real personal or sensitive data, stop and alert them before proceeding.

Collect these inputs from the user. Do not guess them:

1. `[PROJECT NAME AND ONE-LINE DESCRIPTION]`
2. `[PRACTICE SIZE, MIX OF PERMANENT/CONTRACT, DELIVERY PORTFOLIO SHAPE]`
3. `[NAME AND WHAT IT CLAIMS]`
4. `[LIST FROM THE CATALOGUE — e.g. meeting-notes-to-requirements, process map generation]`
5. `[SECURITY POSTURE, DATA RULES, BUDGET]`
6. `[VERIFY WITH VENDOR DOCUMENTATION]`

Then ask up to 5 clarifying questions about anything still
missing, and **wait for the answers** before drafting.

## What to produce

- Evaluate the candidate against real BA use cases and recommend adopt / trial / decline with evidence. Draft the evaluation (design before trial, findings after). Weight validation effort honestly — a tool that generates fast but validates slow may net negative.

Format the output exactly as follows:

> Evaluation design: use cases with success criteria each (quality vs current method, time saved, validation effort); trial protocol (who, how long, synthetic/de-identified data only); security and data assessment (where data goes, residency, retention — [VERIFY WITH VENDOR DOCUMENTATION]); cost model (licence + adoption effort). Findings per use case with evidence; recommendation (adopt/trial-extend/decline) with conditions; total honest cost of adoption including training.

Keep the language professional, plain-English and appropriate for a business audience.

## Rules

- Do not invent facts or figures: mark anything you could not verify from the user's inputs as [TBC] and any value you propose yourself as [PROPOSED — VALIDATE].
- Treat the output as a first draft for the user's review, not a finished artefact.
- Do not ask the user to paste real personal or sensitive data.

## Worked example to imitate

Example use-case finding: "Use case: meeting-notes → structured requirements. Result: draft quality 7/10, time 45→12 min, but validation took 15 min and caught 2 invented requirements not in the notes. Net: positive with mandatory Test step; adopt with guardrail. (Without validation: would have shipped fabrications — decline.)"

## Before you hand it back

1. **Explain** - break down, step by step, the logic you used: how you interpreted
   each input and why you structured the output the way you did.
2. **Test** - list the sources you drew on (the user's inputs, earlier turns, or
   your own general knowledge; label which is which), cross-reference the key facts
   against them, flag anything that does not trace back to a source, and list every
   assumption you made so the user can verify or correct it.
