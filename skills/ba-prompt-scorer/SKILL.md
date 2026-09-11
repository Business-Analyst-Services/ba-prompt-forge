---
name: ba-prompt-scorer
description: Score any prompt against the 10-criterion CARE + G.E.T. quality rubric and say exactly what to fix. Use when someone asks how good a prompt is, wants a prompt reviewed or improved before sharing it, or is submitting a prompt to the BA Prompt Forge library. Produces a criterion-by-criterion score out of 20, a verdict band, and a rewritten prompt that fixes the deductions.
license: CC-BY-4.0
---

# BA prompt scorer

Score a prompt out of 20 against the rubric in `rubric/care-get-v1.yml`, then fix
what you found. A score with no rewrite is half a job.

## Run the machine checks first

```bash
python tools/lint.py path/to/prompt.md
```

`tools/lint.py` decides six criteria mechanically and will not argue with you
about them: **Example, Explain, Test, Anti-fabrication, Data safety,
Reusability**. Take its marks for those.

It also gives a provisional mark on the four it cannot judge - **Context,
Action, Result/Format, Right-sized** - flagged `?`. Those four are yours. That
is the whole division of labour: the script counts, you judge.

If the prompt is loose prose rather than a library file, skip the script and
score all ten yourself.

## The ten criteria

Score each **0 (absent) / 1 (partial) / 2 (met)**.

| # | Criterion | 2 requires |
| --- | --- | --- |
| 1 | Context | Role *and* audience stated, plus the constraints that bind the work |
| 2 | Action | One task, strong verb, named inputs, explicit scope |
| 3 | Result / Format | A structure a reviewer could tick off - named sections, table columns, counts |
| 4 | Example | A real sample to imitate, not a description of one |
| 5 | Explain step | Asks for step-by-step synthesis logic tied to the inputs |
| 6 | Test step | Asks for sources **and** cross-referencing **and** assumptions |
| 7 | Anti-fabrication | Explicit prohibition **and** a flagging convention (`[TBC]`, `[PROPOSED - VALIDATE]`) |
| 8 | Data safety | Explicit de-identification instruction, not silence |
| 9 | Reusability | Marked `[PLACEHOLDERS]`, nothing hard-wired to one project |
| 10 | Right-sized | Every sentence changes the output; long is fine if load-bearing |

**Bands:** 17-20 library-ready &middot; 12-16 usable, refine before sharing
&middot; 0-11 rework.

## How to judge the four that need judgement

These are where scorers disagree, so apply the test, not the vibe.

- **Context (1).** Cover the role and the audience with your thumb. Does the
  prompt still say who is writing and who reads it? Both, or it is not a 2.
- **Action (2).** Count the deliverables the prompt asks for. More than one is a
  menu, not a task - cap at 1. This is the standard deduction on every Master
  prompt in the library, and it is deliberate there; it is rarely deliberate
  anywhere else.
- **Result/Format (3).** Could a reviewer hold the output against the prompt and
  tick each requirement off? "A summary" and "a table" are 1. "One row per KPI:
  name; definition; formula; baseline; target; source; frequency; owner" is a 2.
- **Right-sized (10).** Go sentence by sentence and ask: *would deleting this
  change the output?* If a whole sentence could go without loss, that is dead
  weight. Length itself is not the test.

## What to report

1. **The table** - all ten criteria, mark, and one line of reasoning each. Say
   which marks came from the script and which are your judgement.
2. **The total and band.**
3. **The fixes**, cheapest first. Name the criterion, quote the offending text,
   and give the replacement line. Not "improve the context" - give the sentence.
4. **The rewritten prompt** at the top of the band, in CARE + G.E.T. unless they
   asked for another framework.

## Be honest about what a score is worth

Say this when it matters, because it stops the number being over-trusted:

> This rubric rewards prompts written *against* this rubric. A 20/20 means the
> prompt is well-formed, not that it produces good output. The stronger evidence
> is a dry run on real de-identified work, the same prompt run twice for
> consistency, and handing the output to someone who was not in the room.

Where the repo's own library scores 19.67/20 on paper, that caveat is the reason
`field-reports/` exists. If the user has actually run the prompt, push them to
log the outcome there - that is the evidence the score is not.

## Scoring a contribution

For a pull request against this repo, add:

- Whether it duplicates an existing prompt (check `catalogue.json` by service and
  target deliverables before anything else).
- Whether the front-matter `score` block matches what you found, field by field.
  A mismatch on a machine-decided criterion is a hard fail - `tools/lint.py`
  will reject it in CI anyway.
- A recommendation: **merge**, **merge after the listed fixes**, or **decline**,
  with the reason in one sentence.

Anything below 17/20 does not enter the library. Say so kindly, give the fixes,
and invite the resubmission - the contributor keeps authorship credit either way.
