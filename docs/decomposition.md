# Decomposition

## The problem

All 42 Master prompts in this library score 19/20, and they all lose the same
point — criterion 2, Action:

> Action 1/2: a menu of modes, not one task — deliberate flexibility, but costs
> single-task clarity.

That is an honest note from the source workbook, not a defect introduced here. A
Master prompt is a working session across a whole BA service, and offering three
modes is the right design for that.

But it has a consequence: **a menu cannot be tested.** A regression test needs
one input and one expected shape of output. A prompt that might produce a
benefits map, or a KPI table, or a value assessment, depending on what you ask
for next, has no single expected shape.

## Units

`tools/decompose.py` turns each mode into a single-task unit prompt:

```
$ python tools/decompose.py BB-01-M
BB-01-U1     20/20 (+1 vs BB-01-M)  A benefits map linking initiative outputs to outcomes to benefits
BB-01-U2     20/20 (+1 vs BB-01-M)  A KPI definition table (KPI, definition, formula, baseline...)
BB-01-U3     20/20 (+1 vs BB-01-M)  A value realisation assessment comparing actuals to targets...
```

The unit's task is rewritten as *"Produce exactly one artefact and nothing else:
..."*, which scores 2/2 on Action — and, more usefully, can carry a test.

Across the library: **188 candidate units from 42 Masters.**

## Why they are proposals, not library prompts

Generated units land in `proposals/`, which is gitignored. They are drafts, and
three fields are wrong on arrival:

| Field | Why it is wrong |
| --- | --- |
| `output_format` | Still the parent's — it describes artefacts this unit does not produce |
| `example` | Inherited from the parent, so usually the wrong example for a narrower task |
| `situation` / `inputs` | May carry inputs this single task does not need |

The second matters most. The worked example is the field that most shapes output
quality, so a unit with an inherited example is a prompt that scores 20/20 and
performs worse than its parent. Promoting these unreviewed would raise the mean
score and lower the library's quality — exactly the failure mode the rubric is
supposed to prevent.

`tools/decompose.py` writes the fixes into each proposal's `review_needed` list.

## The workflow

```bash
python tools/decompose.py BB-01-M --write
```

Then edit `proposals/business-ba/BB-01-U2.md`:

- narrow `output_format` to this one artefact
- write a new worked example, with synthetic values
- trim inputs the task does not need
- run it once on real de-identified work

Then promote it:

```bash
mv proposals/business-ba/BB-01-U2.md library/business-ba/<service>/
python tools/build.py
python tools/lint.py library/business-ba/<service>/BB-01-U2.md
```

Log what happened in [`field-reports/`](../field-reports/) — a unit's whole
reason for existing is that it can be evaluated, so evaluate it.

## Keep the Masters

Units do not replace Masters. They are different tools:

- **Master** — you are working the whole service and want a partner across it.
  Multi-mode is the feature.
- **Deliverable** — you know the artefact you need.
- **Unit** — you need the artefact *and* you want to test the prompt, measure it,
  or wire it into something automated.
