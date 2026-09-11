# Prompt frameworks

The library is written in CARE + G.E.T., but CARE is a storage format, not a
commitment. Each prompt is stored as **fields**, not as one blob of text, so it
can be re-rendered into any framework below - or into an agent skill.

## Conversion is lossy, and the repo says by how much

A framework with no Example slot cannot carry the worked example. A framework
with no place for verification rules drops them. Each renderer declares which of
the ten rubric criteria its slots can actually carry, so the cost is a number
rather than a shrug:

```bash
python tools/convert.py BB-01-D1 --format rtf --fidelity
```

Below, `BB-01-D1` (20/20 in CARE) converted into each framework:

| Flag | Framework | Score after conversion | Criteria lost |
| --- | --- | --- | --- |
| `care` | CARE + G.E.T. | 20 / 20 | - |
| `co-star` | CO-STAR | 20 / 20 | - |
| `tidd-ec` | TIDD-EC | 20 / 20 | - |
| `risen` | RISEN | 18 / 20 | Example |
| `crispe` | CRISPE | 16 / 20 | Example, Test step |
| `race` | RACE | 14 / 20 | Example, Explain step, Test step |
| `rtf` | RTF | 10 / 20 | Example, Explain step, Test step, Anti-fabrication, Data safety |
| `ape` | APE | 10 / 20 | Context, Example, Explain step, Test step, Data safety |
| `bab` | BAB | 10 / 20 | Example, Explain step, Test step, Data safety, Right-sized |
| `chat` | Compact chat | 12 / 20 | Example, Explain step, Test step, Data safety |

Pick a lossy framework deliberately - for a short input box, or a house standard -
not by accident.

## Adding a framework

Add a renderer to `tools/formats.py` and register it in `FORMATS` with the set of
criteria its slots can carry. That set is the honest part: claiming a framework
carries a criterion it has no slot for makes the fidelity report lie.

## The frameworks


### CARE + G.E.T. - `care`

The library's native format. Context, Action, Result/Format, Example, plus Generate -> Explain -> Test.

```bash
python tools/convert.py BB-01-D1 --format care
```

<details><summary>BB-01-D1 rendered as CARE + G.E.T.</summary>

```text
# CONTEXT
I am a business analyst (Business BA). I am working on [PROJECT NAME AND ONE-LINE DESCRIPTION]. My work must respect my organisation's privacy, information-security and data-residency obligations. Everything I paste is de-identified or synthetic — if any input appears to contain real personal or sensitive data, stop and alert me before proceeding. Benefits to be measured: [PASTE BENEFITS STATEMENTS OR BUSINESS CASE EXTRACT]. The audience for this output: Benefit owners and the reporting/data team who must build the measures.

# ACTION
Turn the listed benefits into a rigorous KPI definition table that reporting teams could implement without further interpretation. Draft the table, then list measurement risks (gaming, lag, data quality) per KPI.

Before drafting, ask me up to 5 clarifying questions about anything missing, then wait for my answers.

# RESULT / FORMAT
One table, one row per KPI: KPI name; plain-English definition; calculation formula; unit; baseline; target and target date; data source system; collection frequency; accountable owner (role, not name). Flag any KPI that cannot currently be measured. Keep the language professional, plain-English and appropriate for a business audience. Do not invent facts or figures: mark anything you could not verify from my inputs as [TBC] and any value you propose yourself as [PROPOSED — VALIDATE]. Treat the output as a first draft for my review, not a finished artefact.

# EXAMPLE
Example row: "KPI: Cases resolved within 26 weeks | Definition: % of accepted cases closed within 26 weeks of lodgement | Formula: (cases closed ≤26wks ÷ accepted cases) × 100 | Baseline: [TO BE QUANTIFIED] | Target: +3pp on baseline | Source: case management system | Frequency: quarterly | Owner: Service Delivery Lead".

# VALIDATION (GENERATE -> EXPLAIN -> TEST)
Generate: produce the output requested above.
Explain: then break down, step by step, the logic you used to synthesise your answer - how you interpreted each of my inputs and why you structured the output the way you did.
Test: list the source references you used (my pasted inputs, earlier turns, or your general knowledge - label which is which); cross-reference the key facts in your output against those sources and flag anything that does not trace back to a source; and list every additional assumption you made so I can verify or correct it.
```

</details>

### CO-STAR - `co-star`

Splits CARE's Result into Style/Tone/Response and promotes Audience to its own slot. Lossless.

```bash
python tools/convert.py BB-01-D1 --format co-star
```

<details><summary>BB-01-D1 rendered as CO-STAR</summary>

```text
# CONTEXT
I am a business analyst (Business BA). I am working on [PROJECT NAME AND ONE-LINE DESCRIPTION]. My work must respect my organisation's privacy, information-security and data-residency obligations. Everything I paste is de-identified or synthetic — if any input appears to contain real personal or sensitive data, stop and alert me before proceeding. Benefits to be measured: [PASTE BENEFITS STATEMENTS OR BUSINESS CASE EXTRACT]. The audience for this output: Benefit owners and the reporting/data team who must build the measures.

# OBJECTIVE
Turn the listed benefits into a rigorous KPI definition table that reporting teams could implement without further interpretation. Draft the table, then list measurement risks (gaming, lag, data quality) per KPI.

Before drafting, ask me up to 5 clarifying questions about anything missing, then wait for my answers.

# STYLE
One table, one row per KPI: KPI name; plain-English definition; calculation formula; unit; baseline; target and target date; data source system; collection frequency; accountable owner (role, not name). Flag any KPI that cannot currently be measured.

# TONE
Keep the language professional, plain-English and appropriate for a business audience.

# AUDIENCE
Benefit owners and the reporting/data team who must build the measures.

# RESPONSE
Do not invent facts or figures: mark anything you could not verify from my inputs as [TBC] and any value you propose yourself as [PROPOSED — VALIDATE]. Treat the output as a first draft for my review, not a finished artefact.

Worked example to imitate: Example row: "KPI: Cases resolved within 26 weeks | Definition: % of accepted cases closed within 26 weeks of lodgement | Formula: (cases closed ≤26wks ÷ accepted cases) × 100 | Baseline: [TO BE QUANTIFIED] | Target: +3pp on baseline | Source: case management system | Frequency: quarterly | Owner: Service Delivery Lead".

Generate: produce the output requested above.
Explain: then break down, step by step, the logic you used to synthesise your answer - how you interpreted each of my inputs and why you structured the output the way you did.
Test: list the source references you used (my pasted inputs, earlier turns, or your general knowledge - label which is which); cross-reference the key facts in your output against those sources and flag anything that does not trace back to a source; and list every additional assumption you made so I can verify or correct it.
```

</details>

### TIDD-EC - `tidd-ec`

The only common format with an explicit DONT slot, so anti-fabrication and data-safety rules land naturally.

```bash
python tools/convert.py BB-01-D1 --format tidd-ec
```

<details><summary>BB-01-D1 rendered as TIDD-EC</summary>

```text
# TASK
Turn the listed benefits into a rigorous KPI definition table that reporting teams could implement without further interpretation. Draft the table, then list measurement risks (gaming, lag, data quality) per KPI.

# INSTRUCTIONS
Before drafting, ask me up to 5 clarifying questions about anything missing, then wait for my answers.
Then generate the output, explain the synthesis logic you used, and test it: cite which parts came from my inputs versus your general knowledge, flag anything that does not trace back to a source, and list the assumptions you made.

# DO
- One table, one row per KPI: KPI name; plain-English definition; calculation formula; unit; baseline; target and target date; data source system; collection frequency; accountable owner (role, not name). Flag any KPI that cannot currently be measured.
- Keep the language professional, plain-English and appropriate for a business audience.

# DONT
- Do not invent facts or figures: mark anything you could not verify from my inputs as [TBC] and any value you propose yourself as [PROPOSED — VALIDATE].
- Treat the output as a first draft for my review, not a finished artefact.
- Do not ask me to paste real personal or sensitive data.

# EXAMPLES
Example row: "KPI: Cases resolved within 26 weeks | Definition: % of accepted cases closed within 26 weeks of lodgement | Formula: (cases closed ≤26wks ÷ accepted cases) × 100 | Baseline: [TO BE QUANTIFIED] | Target: +3pp on baseline | Source: case management system | Frequency: quarterly | Owner: Service Delivery Lead".

# CONTEXT
I am a business analyst (Business BA). I am working on [PROJECT NAME AND ONE-LINE DESCRIPTION]. My work must respect my organisation's privacy, information-security and data-residency obligations. Everything I paste is de-identified or synthetic — if any input appears to contain real personal or sensitive data, stop and alert me before proceeding. Benefits to be measured: [PASTE BENEFITS STATEMENTS OR BUSINESS CASE EXTRACT]. The audience for this output: Benefit owners and the reporting/data team who must build the measures.
```

</details>

### RISEN - `risen`

Strong for multi-step work. No Example slot, so the worked example is lost.

```bash
python tools/convert.py BB-01-D1 --format risen
```

<details><summary>BB-01-D1 rendered as RISEN</summary>

```text
**Role:** A business analyst (Business BA).

**Instructions:** Turn the listed benefits into a rigorous KPI definition table that reporting teams could implement without further interpretation. Draft the table, then list measurement risks (gaming, lag, data quality) per KPI.

**Steps:**
1. Ask the clarifying questions below and wait for my answers.
2. Turn the listed benefits into a rigorous KPI definition table that reporting teams could implement without further interpretation. Draft the table, then list measurement risks (gaming, lag, data quality) per KPI.
3. Self-check the draft against the constraints before returning it.

**End goal:** A reviewable first draft that Benefit owners and the reporting/data team who must build the measures can act on.

**Narrowing (constraints):**
- One table, one row per KPI: KPI name; plain-English definition; calculation formula; unit; baseline; target and target date; data source system; collection frequency; accountable owner (role, not name). Flag any KPI that cannot currently be measured.
- Keep the language professional, plain-English and appropriate for a business audience.
- Do not invent facts or figures: mark anything you could not verify from my inputs as [TBC] and any value you propose yourself as [PROPOSED — VALIDATE].
- Treat the output as a first draft for my review, not a finished artefact.
- My work must respect my organisation's privacy, information-security and data-residency obligations. Everything I paste is de-identified or synthetic — if any input appears to contain real personal or sensitive data, stop and alert me before proceeding.
- Before drafting, ask me up to 5 clarifying questions about anything missing, then wait for my answers.
```

</details>

### CRISPE - `crispe`

Its Experiment slot asks for alternatives rather than verification, and there is no Example slot.

```bash
python tools/convert.py BB-01-D1 --format crispe
```

<details><summary>BB-01-D1 rendered as CRISPE</summary>

```text
**Capacity / Role:** Act as a business analyst (Business BA).

**Insight:** Benefits to be measured: [PASTE BENEFITS STATEMENTS OR BUSINESS CASE EXTRACT]. My work must respect my organisation's privacy, information-security and data-residency obligations. Everything I paste is de-identified or synthetic — if any input appears to contain real personal or sensitive data, stop and alert me before proceeding. This is for Benefit owners and the reporting/data team who must build the measures.

**Statement:** Turn the listed benefits into a rigorous KPI definition table that reporting teams could implement without further interpretation. Draft the table, then list measurement risks (gaming, lag, data quality) per KPI. Before drafting, ask me up to 5 clarifying questions about anything missing, then wait for my answers.

**Personality:** Keep the language professional, plain-English and appropriate for a business audience. Do not invent facts or figures: mark anything you could not verify from my inputs as [TBC] and any value you propose yourself as [PROPOSED — VALIDATE]. Treat the output as a first draft for my review, not a finished artefact.

**Experiment:** Give me the draft in the format below, then offer one alternative structure and say when you would use it instead.

**Format:** One table, one row per KPI: KPI name; plain-English definition; calculation formula; unit; baseline; target and target date; data source system; collection frequency; accountable owner (role, not name). Flag any KPI that cannot currently be measured.
```

</details>

### RACE - `race`

Compact four-slot format. Keeps guardrails and audience; drops the worked example and the whole G.E.T. validation step.

```bash
python tools/convert.py BB-01-D1 --format race
```

<details><summary>BB-01-D1 rendered as RACE</summary>

```text
**Role:** I am a business analyst (Business BA).

**Action:** Turn the listed benefits into a rigorous KPI definition table that reporting teams could implement without further interpretation. Draft the table, then list measurement risks (gaming, lag, data quality) per KPI.

**Context:** Benefits to be measured: [PASTE BENEFITS STATEMENTS OR BUSINESS CASE EXTRACT]. My work must respect my organisation's privacy, information-security and data-residency obligations. Everything I paste is de-identified or synthetic — if any input appears to contain real personal or sensitive data, stop and alert me before proceeding. Audience: Benefit owners and the reporting/data team who must build the measures.

**Expectation:** One table, one row per KPI: KPI name; plain-English definition; calculation formula; unit; baseline; target and target date; data source system; collection frequency; accountable owner (role, not name). Flag any KPI that cannot currently be measured. Do not invent facts or figures: mark anything you could not verify from my inputs as [TBC] and any value you propose yourself as [PROPOSED — VALIDATE]. Treat the output as a first draft for my review, not a finished artefact.
```

</details>

### RTF - `rtf`

Minimal. Fine for a quick one-off; strips every verification and safety rule.

```bash
python tools/convert.py BB-01-D1 --format rtf
```

<details><summary>BB-01-D1 rendered as RTF</summary>

```text
**Role:** A business analyst (Business BA), writing for Benefit owners and the reporting/data team who must build the measures.

**Task:** Turn the listed benefits into a rigorous KPI definition table that reporting teams could implement without further interpretation. Draft the table, then list measurement risks (gaming, lag, data quality) per KPI.

**Format:** One table, one row per KPI: KPI name; plain-English definition; calculation formula; unit; baseline; target and target date; data source system; collection frequency; accountable owner (role, not name). Flag any KPI that cannot currently be measured.
```

</details>

### APE - `ape`

Purpose-led and very short. No role, audience or example.

```bash
python tools/convert.py BB-01-D1 --format ape
```

<details><summary>BB-01-D1 rendered as APE</summary>

```text
**Action:** Turn the listed benefits into a rigorous KPI definition table that reporting teams could implement without further interpretation. Draft the table, then list measurement risks (gaming, lag, data quality) per KPI.

**Purpose:** So that Benefit owners and the reporting/data team who must build the measures can review and act on it.

**Expectation:** One table, one row per KPI: KPI name; plain-English definition; calculation formula; unit; baseline; target and target date; data source system; collection frequency; accountable owner (role, not name). Flag any KPI that cannot currently be measured. Do not invent facts or figures: mark anything you could not verify from my inputs as [TBC] and any value you propose yourself as [PROPOSED — VALIDATE]. Treat the output as a first draft for my review, not a finished artefact.
```

</details>

### BAB - `bab`

Persuasive narrative shape. A poor fit for deliverable prompts - use it to pitch the work, not to produce it.

```bash
python tools/convert.py BB-01-D1 --format bab
```

<details><summary>BB-01-D1 rendered as BAB</summary>

```text
**Before:** I am a business analyst (Business BA). Benefits to be measured: [PASTE BENEFITS STATEMENTS OR BUSINESS CASE EXTRACT]. Right now this work is unstructured and cannot be reviewed.

**After:** Benefit owners and the reporting/data team who must build the measures has a reviewable draft: One table, one row per KPI: KPI name; plain-English definition; calculation formula; unit; baseline; target and target date; data source system; collection frequency; accountable owner (role, not name). Flag any KPI that cannot currently be measured.

**Bridge:** Turn the listed benefits into a rigorous KPI definition table that reporting teams could implement without further interpretation. Draft the table, then list measurement risks (gaming, lag, data quality) per KPI. Before drafting, ask me up to 5 clarifying questions about anything missing, then wait for my answers. Do not invent facts or figures: mark anything you could not verify from my inputs as [TBC] and any value you propose yourself as [PROPOSED — VALIDATE]. Treat the output as a first draft for my review, not a finished artefact.
```

</details>

### Compact chat - `chat`

One paragraph for short-context chat boxes. Deliberately lossy.

```bash
python tools/convert.py BB-01-D1 --format chat
```

<details><summary>BB-01-D1 rendered as Compact chat</summary>

```text
Act as a business analyst (Business BA) writing for Benefit owners and the reporting/data team who must build the measures. Turn the listed benefits into a rigorous KPI definition table that reporting teams could implement without further interpretation. Draft the table, then list measurement risks (gaming, lag, data quality) per KPI. Before drafting, ask me up to 5 clarifying questions about anything missing, then wait for my answers. Format: One table, one row per KPI: KPI name; plain-English definition; calculation formula; unit; baseline; target and target date; data source system; collection frequency; accountable owner (role, not name). Flag any KPI that cannot currently be measured. Do not invent facts or figures: mark anything you could not verify from my inputs as [TBC] and any value you propose yourself as [PROPOSED — VALIDATE]. Treat the output as a first draft for my review, not a finished artefact. Finish by listing your assumptions and which claims came from my inputs versus your own knowledge.
```

</details>
