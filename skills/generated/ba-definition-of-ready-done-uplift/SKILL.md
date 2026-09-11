---
name: ba-definition-of-ready-done-uplift
description: Use when the user is working on agile ways of working uplift and needs definition of ready, definition of done, working agreements. Draft an uplifted DoR and DoD that would have caught the recent failures, sized to the squad's maturity. Produces a reviewable first draft for the squad, who must own and apply it every sprint.
license: CC-BY-4.0
---

# Definition of Ready / Done Uplift

Derived from `AB-06-D1` in the BA Prompt Forge library
(Agile BA / Agile Ways of Working Uplift, scored 20/20
against the CARE + G.E.T. rubric).

## When to use this

The user is doing agile ways of working uplift work and needs one of:
- Definition of Ready
- Definition of Done
- Working Agreements

The audience for whatever you produce is: **The squad, who must own and apply it every sprint**.

## Before you start

The user's work must respect the user's organisation's privacy, information-security and data-residency obligations. Everything the user pastes is de-identified or synthetic — if any input appears to contain real personal or sensitive data, stop and alert them before proceeding.

Collect these inputs from the user. Do not guess them:

1. `[PROJECT NAME AND ONE-LINE DESCRIPTION]`
2. `[SQUAD NAME, PRODUCT/SYSTEM, CADENCE e.g. 2-week sprints, TOOL e.g. Jira]`
3. `[PASTE OR 'STANDARD']`
4. `[PASTE OR 'NONE']`
5. `[E.G. STORIES BOUNCED MID-SPRINT, DEFECTS FROM UNCLEAR CRITERIA]`

Then ask up to 5 clarifying questions about anything still
missing, and **wait for the answers** before drafting.

## What to produce

- Draft an uplifted DoR and DoD that would have caught the recent failures, sized to the squad's maturity. Draft both definitions. For each recent failure I gave, point to the criterion that now catches it — and admit any failure your draft still wouldn't catch.

Format the output exactly as follows:

> Per criterion: the check (one testable sentence); why it exists (tied where possible to a failure I described); who verifies and when. Keep each definition to 5-8 criteria — flag anything beyond that as process weight to justify. Include a 'trial for 3 sprints then review' adoption note and a lightweight exception rule.

Keep the language professional, plain-English and appropriate for a business audience.

## Rules

- Do not invent facts or figures: mark anything you could not verify from the user's inputs as [TBC] and any value you propose yourself as [PROPOSED — VALIDATE].
- Treat the output as a first draft for the user's review, not a finished artefact.
- Do not ask the user to paste real personal or sensitive data.

## Worked example to imitate

Example DoR criterion: "Criterion: acceptance criteria confirmed by PO. Why: 5 of 6 bounced stories had criteria agreed after start. Verified: PO thumbs-up recorded on the ticket at refinement. (Exception rule: PO may waive in writing for production-fix stories.)"

## Before you hand it back

1. **Explain** - break down, step by step, the logic you used: how you interpreted
   each input and why you structured the output the way you did.
2. **Test** - list the sources you drew on (the user's inputs, earlier turns, or
   your own general knowledge; label which is which), cross-reference the key facts
   against them, flag anything that does not trace back to a source, and list every
   assumption you made so the user can verify or correct it.
