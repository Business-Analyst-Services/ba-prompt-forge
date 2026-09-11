---
name: ba-hosting-model-and-data-residency-analysis
description: Use when the user is working on platform design & infrastructure and needs hosting & deployment model definitions, data residency compliance inputs. Analyse hosting options (full cloud / hybrid / on-prem) and establish the data residency position. Produces a reviewable first draft for architects (decision), privacy and security (residency confirmation).
license: CC-BY-4.0
---

# Hosting Model & Data Residency Analysis

Derived from `TB-04-D1` in the BA Prompt Forge library
(Technical BA / Platform Design & Infrastructure, scored 20/20
against the CARE + G.E.T. rubric).

## When to use this

The user is doing platform design & infrastructure work and needs one of:
- Hosting & deployment model definitions
- data residency compliance inputs

The audience for whatever you produce is: **Architects (decision), privacy and security (residency confirmation)**.

## Before you start

The user's work must respect the user's organisation's privacy, information-security and data-residency obligations. Everything the user pastes is de-identified or synthetic — if any input appears to contain real personal or sensitive data, stop and alert them before proceeding.

Collect these inputs from the user. Do not guess them:

1. `[PROJECT NAME AND ONE-LINE DESCRIPTION]`
2. `[DESCRIBE]`
3. `[CLASSIFICATIONS INCL. PERSONAL/HEALTH]`
4. `[ON-PREM SYSTEMS, SaaS, PARTNERS]`
5. `[LIST OR 'NONE KNOWN']`
6. `[VERIFY WITH VENDOR DOCUMENTATION]`

Then ask up to 5 clarifying questions about anything still
missing, and **wait for the answers** before drafting.

## What to produce

- Analyse hosting options (full cloud / hybrid / on-prem) and establish the data residency position. Draft the analysis. Every residency claim about a vendor/cloud service is marked '[VERIFY WITH VENDOR DOCUMENTATION]'.

Format the output exactly as follows:

> Inputs summary: data sensitivity map; dependency map; latency needs; continuity expectations; regulatory/residency constraints. Options analysis: hosting model vs criteria (residency compliance, dependency fit, latency, resilience, cost profile, exit risk) with commentary. Residency assessment: where data is stored, processed and backed up per option; cross-border touchpoints (including vendor support access from offshore) flagged for privacy review.

Keep the language professional, plain-English and appropriate for a business audience.

## Rules

- Do not invent facts or figures: mark anything you could not verify from the user's inputs as [TBC] and any value you propose yourself as [PROPOSED — VALIDATE].
- Treat the output as a first draft for the user's review, not a finished artefact.
- Do not ask the user to paste real personal or sensitive data.

## Worked example to imitate

Example residency line: "Option A (SaaS): primary data in Sydney region, backups replicated to Melbourne — compliant; vendor L2 support follows-the-sun from Manila with screen-share access to production data — cross-border access touchpoint, flag for privacy review [VERIFY WITH VENDOR DOCUMENTATION]."

## Before you hand it back

1. **Explain** - break down, step by step, the logic you used: how you interpreted
   each input and why you structured the output the way you did.
2. **Test** - list the sources you drew on (the user's inputs, earlier turns, or
   your own general knowledge; label which is which), cross-reference the key facts
   against them, flag anything that does not trace back to a source, and list every
   assumption you made so the user can verify or correct it.
