# BA Prompt Forge

### → **[Read it as a website: business-analyst-services.github.io/ba-prompt-forge](https://business-analyst-services.github.io/ba-prompt-forge/)**

Every prompt, the full rubric, all ten framework renderings, the delivery
contexts and the skills are published as an accessible website — you never need
to open this repository to use any of it. This repo is the source that builds it.

---

**126 scored business-analysis prompts you don't browse.** You describe the work;
an agent finds the prompt, fills it in, and hands it back in whatever framework
you need.

Covering 42 BA services across 6 roles and 11 delivery contexts, every prompt
scored against a 10-criterion quality rubric — and every one convertible into
nine other prompt frameworks or into an agent skill.

[Index](INDEX.md) &middot; [Frameworks](formats/README.md) &middot;
[Scoring](docs/scoring.md) &middot; [Contributing](CONTRIBUTING.md) &middot;
[Statistics](docs/statistics.md)

---

## The problem this solves

A library of 126 prompts is not a resource, it is a homework assignment. Nobody
opens a catalogue and knows whether they want `BT-06-D2` or `BB-07-M`. The
choice is the cost.

So the primary interface here is not a list. It is
[`skills/ba-prompt-router`](skills/ba-prompt-router/SKILL.md) — you say *"I need
acceptance criteria a tester can actually work from"* and it routes, narrows,
recommends one prompt, interviews you for the placeholders, and returns something
you can paste. The index exists for when you already know what you want.

## Three ways in

**As an agent skill** — the intended route. Point any agent that reads
`SKILL.md` files (Claude Code, Claude Desktop, and most agent runtimes) at
`skills/`:

```bash
git clone https://github.com/Business-Analyst-Services/ba-prompt-forge
```

| Skill | What it does |
| --- | --- |
| [`ba-prompt-router`](skills/ba-prompt-router/SKILL.md) | Describe your work, get the right prompt, filled in |
| [`ba-prompt-scorer`](skills/ba-prompt-scorer/SKILL.md) | Score any prompt out of 20 and fix the deductions |
| [`ba-prompt-forge`](skills/ba-prompt-forge/SKILL.md) | Write a new prompt to library standard, or convert one |
| [`skills/generated/`](skills/generated/) | All 126 prompts pre-built as standalone skills |

**From the command line:**

```bash
pip install -r requirements.txt

python tools/convert.py BB-01-D1                        # CARE + G.E.T.
python tools/convert.py BB-01-D1 --format co-star       # another framework
python tools/convert.py BB-01-D1 --format rtf --fidelity # ...and what it costs
python tools/convert.py BB-01-D1 --to-skill             # as an agent skill
python tools/lint.py library/**/BB-01-D1.md             # score it
```

**By reading** — the
[website](https://business-analyst-services.github.io/ba-prompt-forge/prompts/)
is the readable form: every prompt with all ten framework renderings, a copy
button, its scorecard and its provenance. [INDEX.md](INDEX.md) is the in-repo
equivalent, and `catalogue.json` is there if you are building something on top.

```bash
python tools/build_site.py           # rebuild the site into site/
python tools/build_site.py --serve   # preview at http://localhost:8000
```

The site build fails if any colour pair drops below its WCAG 2.1 AA contrast
threshold in either theme, so an inaccessible palette cannot ship.

## How it works

Each prompt is stored as **fields, not as a blob of text**:

```yaml
persona:       a business analyst (Business BA)
audience:      Benefit owners and the reporting/data team who must build the measures
task:          Turn the listed benefits into a rigorous KPI definition table...
output_format: One table, one row per KPI: name; definition; formula; unit; baseline...
guardrails:    [Do not invent facts or figures..., Treat the output as a first draft...]
example:       'KPI: Cases resolved within 26 weeks | Formula: (cases closed <=26wks...'
score:         {total: 20, verdict: Library-ready, ...}
```

That single decision is what makes everything else possible. A blob of text
cannot be re-rendered into CO-STAR, scored criterion by criterion, diffed in a
pull request, or turned into a skill. Fields can.

```
library/**/*.md  ──►  tools/formats.py  ──►  CARE · CO-STAR · TIDD-EC · RISEN
 (YAML fields)         (10 renderers)         CRISPE · RACE · RTF · APE · BAB
       │                                      compact chat · SKILL.md
       ├──►  tools/lint.py       ──►  score out of 20, machine-verified floor
       ├──►  tools/decompose.py  ──►  single-task units you can regression-test
       └──►  tools/build.py      ──►  INDEX.md, catalogue.json, formats/README.md
```

## Scoring

Every prompt carries a mark against the ten criteria in
[`rubric/care-get-v1.yml`](rubric/care-get-v1.yml): Context, Action,
Result/Format, Example, Explain, Test, Anti-fabrication, Data safety,
Reusability, Right-sized. 0–2 each; 17+ is library-ready.

The scoring is split honestly. **Six criteria are machine-decidable** and
`tools/lint.py` decides them — is there a real example, does the anti-fabrication
flag convention exist, is there a marked placeholder. **Four need judgement** and
the script only offers a provisional mark, flagged `?`, for a human or
[`ba-prompt-scorer`](skills/ba-prompt-scorer/SKILL.md) to settle.

```
$ python tools/lint.py library/business-ba/benefits-realisation-and-kpi-management/BB-01-D1.md
PASS BB-01-D1  20/20  Library-ready (12/12 machine-verified)
  ? 2  Context          role, audience and constraints all stated
  ? 2  Action           one task with 2 named input(s)
    2  Example          concrete sample the model can imitate
    2  Anti-fabrication explicit prohibition plus a flagging convention
    ...
```

CI runs the linter over every prompt on every push, and rejects a pull request
whose declared score disagrees with the machine check.

> **A 20/20 means well-formed, not effective.** This library was written against
> this rubric, so its paper scores skew high (mean 19.62). The stronger evidence
> is a prompt run on real de-identified work — which is what
> [`field-reports/`](field-reports/) is for.

## Frameworks, and what conversion costs

CARE is a storage format, not a commitment. Ten frameworks are supported, and
because each renderer declares which rubric criteria its slots can carry, the
repo can tell you what you lose:

| Framework | `BB-01-D1` after conversion | Criteria lost |
| --- | --- | --- |
| CARE + G.E.T., CO-STAR, TIDD-EC | 20 / 20 | — |
| RISEN | 18 / 20 | Example |
| CRISPE | 16 / 20 | Example, Test |
| RACE | 14 / 20 | Example, Explain, Test |
| RTF, APE, BAB, compact chat | 10 / 20 | most of the verification and safety rules |

Picking a lossy framework is fine. Picking one without knowing is not. Full
detail and worked renderings in [formats/README.md](formats/README.md).

## Prompts as skills

`--to-skill` is not a copy-paste of the prompt text. A prompt is one turn; a
skill is a procedure — so the modes become steps, the clarifying questions become
a gate before drafting, the G.E.T. block becomes a hand-back checklist, and the
first-person text is shifted to address the agent about the user.

```bash
python tools/convert.py --all --to-skill -o skills/generated
```

## Smaller units, so prompts can be tested

Every Master prompt loses the same rubric point: it offers a menu of modes rather
than one task. Deliberate — a Master is a working session — but a menu cannot
carry a regression test, because a test needs one input and one expected shape.

```bash
$ python tools/decompose.py BB-01-M
BB-01-U1     20/20 (+1 vs BB-01-M)  A benefits map linking initiative outputs to outcomes to benefits
BB-01-U2     20/20 (+1 vs BB-01-M)  A KPI definition table (KPI, definition, formula, baseline...)
BB-01-U3     20/20 (+1 vs BB-01-M)  A value realisation assessment comparing actuals to targets...
```

Across the library that is **188 single-task units from 42 Masters**. They land
in `proposals/`, not `library/` — they are machine-derived drafts that each need
a narrowed format and a rewritten example before promotion. See
[docs/decomposition.md](docs/decomposition.md).

## Contribute a prompt, keep the credit

Prompts are better when the people doing the work write them. If you have one
that works:

1. Write it as a library file (or let
   [`ba-prompt-forge`](skills/ba-prompt-forge/SKILL.md) do it with you).
2. `python tools/lint.py` it. 17/20 is the bar.
3. Open a pull request.

Your name stays in the prompt's `provenance.author` field — which travels with it
into every converted format and every generated skill — and in
[CONTRIBUTORS.md](CONTRIBUTORS.md).

**Upvoting** is GitHub-native: each accepted prompt gets a Discussion thread, and
👍 reactions are the vote. **Impact** is [`field-reports/`](field-reports/) —
short structured notes on what happened when you actually used a prompt. A
rubric score says a prompt is well-formed; a field report says it worked. Full
process in [CONTRIBUTING.md](CONTRIBUTING.md), roadmap in
[docs/roadmap.md](docs/roadmap.md).

## Provenance

The library originates from the *BA Services AI Prompt Library (CARE + G.E.T.)
v1.0 — Portable edition* by [Business Analyst Services](https://business-analyst.services),
included at [`source/`](source/). It is deliberately organisation-neutral: no
client names, no sectors, no jurisdiction-specific rules. Two edits make it
yours — extend the `# CONTEXT` block with your organisation and sector, and
replace each worked example with one from your own domain. The example is what
most shapes output quality.

## Licence

Code (`tools/`, `schema/`) — [MIT](LICENSE).
Prompts, rubric and documentation — [CC BY 4.0](LICENSE), so use them at work,
adapt them, ship them in a product; keep the attribution.
