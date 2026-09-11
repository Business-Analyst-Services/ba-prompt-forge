# Contributing

Prompts are better when written by the people doing the work. This repo is built
so that a business analyst who has a prompt that genuinely works can get it in,
keep the credit, and find out whether it helped anyone else.

## The bar

**17/20 on the [rubric](rubric/care-get-v1.yml).** That is the published
threshold, not a preference — below it, outputs are unreliable enough that
sharing the prompt does more harm than good. Nothing else about your prompt has
to match house style.

A prompt below 17 is not rejected, it is returned with the specific fixes. You
keep authorship on the resubmission.

## Adding a prompt

**1. Check it doesn't exist.** Search `catalogue.json` by service and target
deliverable. 42 services are covered; duplicating a 20/20 prompt helps nobody.
The exception is a genuinely better prompt for the same job — say so explicitly
in the PR and we will compare them.

**2. Write it as fields, not prose.** Copy a neighbouring file in
`library/<role>/<service>/`, or start from
[`schema/prompt.schema.json`](schema/prompt.schema.json). The YAML front-matter
*is* the prompt; the body is generated. Writing it as one blob of text means it
cannot be converted, scored field by field, or diffed — so the schema forbids it.

Easiest route: ask an agent to run
[`skills/ba-prompt-forge`](skills/ba-prompt-forge/SKILL.md), which walks the
fields in rubric order.

**3. Pick an ID.** `<RR>-<NN>-<M|Dn>` — role prefix (`BB` Business BA, `BT`
Business/Tech BA, `TB` Technical BA, `AB` Agile BA, `LB` Lead BA, `PL` Practice
Lead), service number, then `M` for a Master or `D1`/`D2` for a deliverable
prompt. Use the next free number in that service.

**4. Build and score:**

```bash
pip install -r requirements.txt
python tools/build.py                        # render body, index, catalogue
python tools/lint.py library/.../YOUR-ID.md  # score it
```

Fix anything the linter marks down. For the four criteria it flags `?` — Context,
Action, Result/Format, Right-sized — use
[`skills/ba-prompt-scorer`](skills/ba-prompt-scorer/SKILL.md) or score them
yourself and put the marks in the `score` block.

**5. Open the pull request.** The template asks for the score, one sentence on
where it came from, and — the part reviewers care about most — whether you have
actually run it.

## What review checks

| | |
| --- | --- |
| **CI, automatically** | Schema valid; `tools/build.py --check` clean; `tools/lint.py` passes; declared score matches the machine check on all six machine-decidable criteria |
| **A human** | Not a duplicate; the four judgement criteria; the worked example is concrete and synthetic; the prompt is portable |

A mismatch between your declared score and the machine check fails CI. That is
deliberate: the scorecard is only worth something if it cannot be self-awarded.

## Three rules that are not negotiable

These are what make the library safe to hand to a stranger.

1. **No real data, anywhere.** Worked examples must be synthetic. Never paste a
   real case number, name, address, health or financial detail into an example —
   not even lightly disguised. Every prompt must keep its de-identification
   instruction.
2. **No invented facts.** Every prompt must forbid fabrication *and* give a
   flagging convention: `[TBC]` for unverified, `[PROPOSED — VALIDATE]` for
   values the model proposes.
3. **Portable.** No employer names, sectors, named legislation or
   jurisdiction-specific rules. Project specifics become `[MARKED PLACEHOLDERS]`.
   Someone in another country in another industry has to be able to use it.

## Credit

Your name goes in `provenance.author` (and `author_github` if you want it
linked). That field travels with the prompt into every converted framework and
every generated skill — so credit survives the conversion, which is the only
kind of credit worth having in a prompt library.

Accepted contributors are listed in [CONTRIBUTORS.md](CONTRIBUTORS.md).

If you would rather not be named, say so in the PR and we will use the handle you
choose, or none.

## Upvoting

Each accepted prompt gets a thread in
[Discussions](https://github.com/Business-Analyst-Services/ba-prompt-forge/discussions).
👍 on the thread is the vote; the comments are where
people say what they changed to make it work in their context. Reaction counts
feed the "most used" view, and they surface the gap between *scored well* and
*actually used* — which is the more interesting number.

## Impact

A rubric score says a prompt is well-formed. A field report says it worked.

If you have used a prompt on real work, add a short structured note to
[`field-reports/`](field-reports/) — which prompt, what you were doing, what it
produced, what you had to change, and whether you would use it again. Copy
[`field-reports/TEMPLATE.md`](field-reports/TEMPLATE.md).

Negative reports are more valuable than positive ones and are never edited out. A
prompt that scores 20/20 and fails in practice is the single most useful thing
this repo could learn.

**De-identify field reports the same way you de-identify prompt inputs.** No
client names, no real figures, no quotable extracts from real artefacts.

## Improving the tooling

Bug reports and PRs on `tools/` are welcome. Two things to know:

- `tools/build.py --check` must stay clean — CI fails if generated output has
  drifted from the front-matter.
- When adding a framework to `tools/formats.py`, register it in `FORMATS` with
  the honest set of criteria its slots can carry. Claiming a framework carries a
  criterion it has no slot for makes the fidelity report lie, and the fidelity
  report is the point.

## Code of conduct

Be decent. Critique prompts, not people. Reviewers: a prompt someone wrote at
work and offered for free deserves specific, fixable feedback, not a verdict.
