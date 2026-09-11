# Scoring

Every prompt carries a mark out of 20 against
[`rubric/care-get-v1.yml`](../rubric/care-get-v1.yml): ten criteria, 0 (absent),
1 (partial) or 2 (met).

| Group | Criteria |
| --- | --- |
| CARE structure | 1 Context &middot; 2 Action &middot; 3 Result/Format &middot; 4 Example |
| G.E.T. validation | 5 Explain &middot; 6 Test &middot; 7 Anti-fabrication |
| Safety and reuse | 8 Data safety &middot; 9 Reusability &middot; 10 Right-sized |

**Bands.** 17-20 library-ready &middot; 12-16 usable, refine before sharing
&middot; 0-11 rework.

## The split: what a machine can decide

Six criteria are mechanically decidable, and `tools/lint.py` decides them:

| Criterion | The machine check |
| --- | --- |
| 4 Example | An `example` exists and contains a quoted sample, a delimiter or a figure — not a description of an example |
| 5 Explain | `validation: get` |
| 6 Test | `validation: get` |
| 7 Anti-fabrication | A guardrail both forbids invention *and* names a flag (`[TBC]`, `[PROPOSED — VALIDATE]`) |
| 8 Data safety | `data_safety` gives an explicit de-identification instruction, not just a mention of constraints |
| 9 Reusability | Two or more `[MARKED PLACEHOLDERS]`, and no hard-coded organisation name |

Four need judgement. The linter offers a provisional mark flagged `?` and leaves
the decision to a human or to
[`ba-prompt-scorer`](../skills/ba-prompt-scorer/SKILL.md):

- **1 Context** — cover the role and the audience with your thumb. Does the
  prompt still say who is writing and who reads it?
- **2 Action** — count the deliverables asked for. More than one is a menu, not a
  task.
- **3 Result/Format** — could a reviewer hold the output against the prompt and
  tick each requirement off?
- **10 Right-sized** — delete each sentence in turn; would the output change?

This split is the whole design. A score that claims machine precision on
judgement criteria is worse than no score, because it gets trusted.

## Why the declared score is checked, not taken

`tools/lint.py` compares the `score` block in the front-matter against its own
findings and **fails on any disagreement about a machine-decidable criterion**.
CI runs this on every pull request.

A self-awarded scorecard is worth nothing. Six of the ten cannot be self-awarded
here.

## Two disagreements worth knowing about

Building this repo surfaced two places where the machine and the source workbook
differ. Both are recorded rather than tuned away.

**`BB-03-M`, criterion 2.** The prompt opens "Help me define the real problem:
...". A naive check flags any "help me" as the rubric's vague 0-anchor. It is
not — there is a strong verb and an object. The check was narrowed to the vague
continuations (`help me with`, `help me out`). Worth knowing because the same
false positive will bite anyone else scoring by keyword.

**Six prompts, criterion 3.** The machine cannot see checkable structure in six
`output_format` fields that the author marked 2/2. They are flagged `?` for
review rather than resolved by either side.

## The caveat that matters most

> This library was written against this rubric. Its mean of 19.62/20 measures the
> author's discipline in applying a template, not the prompts' effect on real
> work.

Stronger evidence, in order:

1. **Dry run** on real de-identified work — did it produce the promised shape?
2. **Consistency** — run it twice. Does it give you the same structure?
3. **Hand-off** — give the output to someone who was not in the room. Can they
   use it without asking you what it means?

Log all three in [`field-reports/`](../field-reports/). One field report is worth
more than a point of rubric score.
