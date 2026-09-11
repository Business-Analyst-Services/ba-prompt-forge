---
name: ba-prompt-forge
description: Author a new business-analysis prompt to library standard, or rebuild an existing one in a different prompt framework. Use when no library prompt fits the user's work and they need one written from scratch, when a rough prompt needs rebuilding to score 17+ on the CARE + G.E.T. rubric, or when a prompt has to be converted to CO-STAR, RISEN, TIDD-EC, RTF, RACE, CRISPE, APE, BAB or an agent skill. Produces a complete prompt file ready to submit to the library.
license: CC-BY-4.0
---

# BA prompt forge

Write a new prompt that would pass review, or rebuild an existing one. The target
is 17/20 minimum; the library mean is 19.67, so aim there.

Before writing anything, check the prompt does not already exist: search
`catalogue.json` by `service` and `deliverables`. Duplicating a 20/20 prompt
helps nobody.

## Authoring a new prompt

Work through the fields in this order. Each maps to a rubric criterion, so
filling them all is what produces the score.

**1. Who and for whom** (criterion 1)
Write `persona` and `audience` as separate fields. "I am an agile business
analyst (Agile BA)" and "Developers and testers picking the story up; product
owner confirming intent". The audience is what decides the format later, so be
specific about who reads it, not just that someone does.

**2. The one task** (criterion 2)
One artefact. Strong verb. Name the inputs it will receive. If you find yourself
writing "(1) ... (2) ... (3) ...", you are writing a Master prompt - that is a
legitimate thing to write, but it caps criterion 2 at 1/2 and it cannot carry a
regression test. Prefer a Deliverable prompt unless the user genuinely wants a
working session across the whole service.

**3. The checkable format** (criterion 3)
The test: could a reviewer hold the output against this and tick each item off?
Name the sections, the table columns, the counts. "Minimum 3 happy, 2 negative,
2 boundary" is checkable. "Comprehensive coverage" is not.

**4. A real example** (criterion 4)
This is the field that most changes output quality, and the one people skip.
Write an actual sample row or snippet the model can imitate - with realistic but
**synthetic** values. Never lift a real example from real work.

**5. The safety and honesty rules** (criteria 7 and 8)
Two non-negotiables, and the library template already carries both:

> My work must respect my organisation's privacy, information-security and
> data-residency obligations. Everything I paste is de-identified or synthetic -
> if any input appears to contain real personal or sensitive data, stop and alert
> me before proceeding.

> Do not invent facts or figures: mark anything you could not verify from my
> inputs as `[TBC]` and any value you propose yourself as `[PROPOSED - VALIDATE]`.

**6. The G.E.T. validation** (criteria 5 and 6)
Set `validation: get`. It renders the standard Generate -> Explain -> Test block.
Only write a custom one if the user has a specific reason.

**7. Placeholders** (criterion 9)
Everything project-specific becomes `[A MARKED PLACEHOLDER IN CAPITALS]`. No
organisation names, no sectors, no jurisdiction-specific legislation - the
library is deliberately portable so anyone can adopt it.

**8. Cut it back** (criterion 10)
Last pass. Delete each sentence in turn and ask whether the output would change.
If not, it stays deleted.

## Writing the file

Prompts live at `library/<role-slug>/<service-slug>/<ID>.md`. The YAML
front-matter is the prompt; the body is generated. Copy the field structure from
a neighbouring file, or start from `schema/prompt.schema.json`.

IDs are `<RR>-<NN>-<M|Dn>`: role prefix (`BB`, `BT`, `TB`, `AB`, `LB`, `PL`),
the service number within that role, then `M` for the Master or `D1`/`D2` for
deliverable prompts.

Then:

```bash
python tools/build.py                  # render the body, index, catalogue
python tools/lint.py library/.../NEW-ID.md   # score it
```

Fix anything the linter marks down, and use `ba-prompt-scorer` for the four
criteria the script cannot judge. Do not hand over a prompt you have not linted.

## Rebuilding in another framework

```bash
python tools/convert.py --formats                        # what's available
python tools/convert.py BB-01-D1 --format risen --fidelity
python tools/convert.py BB-01-D1 --to-skill
```

Ten frameworks are supported. What matters is that they are not equivalent:

- **Lossless** - CARE, CO-STAR, TIDD-EC. All ten criteria have somewhere to go.
  TIDD-EC is the best target when the guardrails matter most: it is the only
  common framework with an explicit DON'T slot.
- **Lossy** - RISEN and CRISPE have no Example slot. RACE drops the example and
  the whole G.E.T. step.
- **Very lossy** - RTF, APE, BAB and the compact chat build strip verification and
  safety entirely. A 20/20 CARE prompt lands at 10/20 as RTF.

Always run `--fidelity` and tell the user the cost before handing over a
converted prompt. Choosing a lossy framework is fine - choosing one without
knowing is not.

## Converting a prompt into an agent skill

`--to-skill` writes a `SKILL.md`. The conversion is not a copy-paste: a prompt is
one turn, a skill is a procedure. The modes become steps, the clarifying
questions become a gate before drafting, the G.E.T. block becomes a
hand-back checklist, and first-person text is shifted to address the agent about
the user.

Check two things in the generated file before using it:

- **The description.** It is what makes the skill trigger at the right moment.
  Rewrite it to say *when to use this*, in the words a BA would actually use.
- **The worked example.** It is inherited, and for a narrowed skill it is often
  the wrong example.

## Decomposing a Master into testable units

```bash
python tools/decompose.py BB-01-M        # preview
python tools/decompose.py --all --write  # write proposals
```

Each mode of a Master becomes a single-task unit prompt scoring 2/2 on Action -
and, unlike its parent, testable. Units land in `proposals/`, not `library/`:
they are drafts. Before promoting one, narrow the output format to that single
artefact, replace the inherited example, and run it once on real de-identified
work.

## Contributing it back

If the prompt is good and general, open a pull request. `CONTRIBUTING.md` has the
process; accepted prompts keep their author in the front-matter and in
`CONTRIBUTORS.md`. If you ran it for real, log what happened in `field-reports/` -
that evidence is worth more than the rubric score.
