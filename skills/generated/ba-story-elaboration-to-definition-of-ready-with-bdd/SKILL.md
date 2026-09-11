---
name: ba-story-elaboration-to-definition-of-ready-with-bdd
description: 'Use when the user is working on just-in-time requirements elaboration and needs elaborated user stories, acceptance criteria, bdd/gherkin scenarios. Elaborate the story to genuinely Ready: rules, criteria and BDD scenarios a developer and tester can work from without re-asking. Produces a reviewable first draft for developers and testers picking the story up.'
license: CC-BY-4.0
---

# Story Elaboration to Definition of Ready (with BDD)

Derived from `AB-03-D1` in the BA Prompt Forge library
(Agile BA / Just-in-Time Requirements Elaboration, scored 20/20
against the CARE + G.E.T. rubric).

## When to use this

The user is doing just-in-time requirements elaboration work and needs one of:
- Elaborated User Stories
- Acceptance Criteria
- BDD/Gherkin Scenarios

The audience for whatever you produce is: **Developers and testers picking the story up; product owner confirming intent**.

## Before you start

The user's work must respect the user's organisation's privacy, information-security and data-residency obligations. Everything the user pastes is de-identified or synthetic — if any input appears to contain real personal or sensitive data, stop and alert them before proceeding.

Collect these inputs from the user. Do not guess them:

1. `[PROJECT NAME AND ONE-LINE DESCRIPTION]`
2. `[SQUAD NAME, PRODUCT/SYSTEM, CADENCE e.g. 2-week sprints, TOOL e.g. Jira]`
3. `[PASTE OR 'STANDARD']`
4. `[PASTE STORY + ANY NOTES/RULES]`
5. `[SPRINT]`

Then ask up to 5 clarifying questions about anything still
missing, and **wait for the answers** before drafting.

## What to produce

- Elaborate the story to genuinely Ready: rules, criteria and BDD scenarios a developer and tester can work from without re-asking. Elaborate, then run the DoR checklist over your own output and state pass/fail per criterion.

Format the output exactly as follows:

> Story restated (As a / I want / so that); business rules table (categorised, ambiguities flagged); acceptance criteria Given/When/Then — minimum 3 happy, 2 negative, 2 boundary; BDD scenarios in Gherkin with realistic (synthetic) example data; open questions that keep it from Ready, each with the person who can answer.

Keep the language professional, plain-English and appropriate for a business audience.

## Rules

- Do not invent facts or figures: mark anything you could not verify from the user's inputs as [TBC] and any value you propose yourself as [PROPOSED — VALIDATE].
- Treat the output as a first draft for the user's review, not a finished artefact.
- Do not ask the user to paste real personal or sensitive data.

## Worked example to imitate

Example Gherkin: "Scenario: supporting document expiring within window. Given case C-1042 has a supporting document expiring in 10 days, When the case officer opens their worklist, Then C-1042 shows an 'expiring' badge with '10 days'. (Data: synthetic case C-1042, document end-date = today+10.)"

## Before you hand it back

1. **Explain** - break down, step by step, the logic you used: how you interpreted
   each input and why you structured the output the way you did.
2. **Test** - list the sources you drew on (the user's inputs, earlier turns, or
   your own general knowledge; label which is which), cross-reference the key facts
   against them, flag anything that does not trace back to a source, and list every
   assumption you made so the user can verify or correct it.
