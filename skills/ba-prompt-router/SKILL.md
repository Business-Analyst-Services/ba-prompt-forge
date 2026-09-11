---
name: ba-prompt-router
description: Find and fill the right business-analysis prompt for what the user is actually doing. Use when a BA describes a piece of work - "I need to write acceptance criteria", "we're procuring a new case management system", "I have to justify this to the sponsor" - and needs a proven prompt rather than a hand-rolled one. Routes across 126 scored prompts covering 42 BA services, 6 roles and 11 delivery contexts, then interviews the user to fill the placeholders.
license: CC-BY-4.0
---

# BA prompt router

A library of 126 prompts is unusable as a list. Nobody knows whether they want
`BT-06-D2` or `BB-07-M`. Your job is to make the catalogue disappear: the user
describes their situation in their own words, and you hand back one filled-in
prompt they can paste straight into a model.

**Never show the user a list of 126 anything.** Narrow first, then offer at most
three, then recommend one.

## What you have to work with

- `catalogue.json` at the repo root - every prompt with its id, role, service,
  target deliverables, delivery contexts, audience, task, modes and input
  placeholders. Load this, not the 126 individual files.
- `contexts/delivery-contexts.yml` - the 11 delivery contexts, each with the
  kind of work it covers and the prompt ids to start from.
- `library/**/<ID>.md` - read one of these only once you have chosen a prompt.

## How to route

### 1. Work out what they are actually producing

The single most useful question is **what artefact has to exist at the end**, not
what topic they are working on. "I'm doing requirements" routes nowhere; "I need
acceptance criteria a tester can work from" routes to one prompt.

Match their words against `deliverables` and `task` in the catalogue. BAs use
different vocabulary than the catalogue does - map it:

| They say | Look for |
| --- | --- |
| "user stories", "ready for the sprint" | Just-in-Time Requirements Elaboration, User Story Mapping & Slicing |
| "business case", "why are we doing this" | Business Project Discovery & Problem Definition, Benefits Realisation |
| "RFT", "tender", "evaluating vendors" | Commercial, Licencing & Vendor Mgmt |
| "as-is / to-be", "process map", "levelling" | Process Analysis & Improvement |
| "data model", "reports", "medallion", "BI" | Data & Reporting Analysis |
| "go-live", "cutover", "training" | Operational Readiness & Transition |
| "traceability", "requirements sign-off" | Requirements Governance & Traceability |
| "my team", "allocating BAs", "reviewing their work" | Lead BA and Practice Lead services |

### 2. If the artefact is unclear, ask about the delivery context instead

Ask which of these their work looks like, in plain language - most BAs recognise
their project type instantly even when they cannot name the deliverable:

system update &middot; agile delivery &middot; new system or transition &middot;
procurement &middot; process design &middot; process improvement &middot;
data warehouse &middot; back-end tech services &middot; AI/agentic &middot;
consultancy &middot; leading a BA team

Then use that context's `start_with` ids.

### 3. Ask at most three questions before recommending

Good questions, in priority order:

1. What has to exist at the end, and who reads it?
2. Is this a one-off artefact, or are you going to work the whole topic through?
   (Artefact -> a **Deliverable** prompt. Whole topic -> the **Master**.)
3. Which role are you playing - business-facing BA, technical BA, agile BA, or
   leading other BAs?

Do not ask a question whose answer you can infer. If they said "acceptance
criteria for the sprint", you already know all three.

### 4. Recommend one, name two alternates

Say what you picked, why, and what it produces. Something like:

> **`AB-03-D1` - Story Elaboration to Definition of Ready (with BDD)** (20/20)
> Takes one story and returns business rules, Given/When/Then criteria with
> happy, negative and boundary cases, and the open questions blocking Ready.
>
> Alternatives: `AB-03-M` if you want to work the whole backlog rather than one
> story, or `BT-09-D1` if what you actually need is test coverage.

### 5. Fill it in with them

This is the part that makes the library worth having. Read the chosen prompt
file and look at its `inputs`. For each placeholder, ask for the value - **one
message, all the placeholders**, not one question at a time.

Then return the completed prompt in a code block with every `[PLACEHOLDER]`
replaced, ready to paste.

Two rules you must not drop when you fill it in:

- **Data safety.** The prompt tells the user to paste de-identified or synthetic
  inputs. If what they give you looks like real personal or sensitive data - real
  names, case numbers, addresses, health or financial detail - stop and say so
  before going further.
- **No invention.** Do not invent a value to fill a placeholder. If the user does
  not know it, leave it as `[TBC]` in the output and say which ones you left.

### 6. Offer the format they need

The prompt is rendered in CARE + G.E.T. by default. If they are pasting into
something with a short input box, or they have a house format, offer a
conversion - and tell them what it costs:

```bash
python tools/convert.py AB-03-D1 --format co-star --fidelity
python tools/convert.py AB-03-D1 --to-skill
```

CO-STAR and TIDD-EC are lossless. RTF, APE and the compact chat build strip the
verification and safety rules - a 20/20 prompt becomes a 10/20 one. Say so rather
than silently handing over a weaker prompt.

## When nothing fits

Two honest answers, and you should give one of them rather than forcing a match:

- **The gap is known.** `contexts/delivery-contexts.yml` records seven flagged
  decomposition gaps (procuring AI products, stakeholder engagement for system
  updates, story sizing, agile testing support, BI requirements governance, agent
  requirement traceability, agent evaluation). If their need is one of these, say
  it is a known gap and offer to draft a new prompt with `ba-prompt-forge`.
- **The library genuinely does not cover it.** Say so. Then offer to author one -
  and to open it as a contribution so the next person gets it. See
  `CONTRIBUTING.md`; accepted prompts are credited to their author.
