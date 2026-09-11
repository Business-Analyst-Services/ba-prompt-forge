# Skills

Agent skills - a folder with a `SKILL.md` of instructions. Any agent runtime that
reads them (Claude Code, Claude Desktop, and most others) can use these directly.

## The three that matter

| Skill | Use it when |
| --- | --- |
| [`ba-prompt-router`](ba-prompt-router/SKILL.md) | You have BA work to do and want the right prompt, filled in. **Start here.** |
| [`ba-prompt-scorer`](ba-prompt-scorer/SKILL.md) | You want a prompt scored out of 20 and the deductions fixed |
| [`ba-prompt-forge`](ba-prompt-forge/SKILL.md) | You need a new prompt written, or an existing one converted |

These three are hand-written. They are the product: the router in particular
exists because a 126-item catalogue is unusable as a list, and the fix for that
is an agent that narrows, not a better index.

## `generated/`

All 126 library prompts pre-built as standalone skills:

```bash
python tools/convert.py --all --to-skill -o skills/generated
```

Useful when you want one BA service always available without the router in front
of it - install `generated/ba-agile-ceremony-facilitation-and-support/` on its
own and the agent picks it up when the work matches.

Regenerate rather than hand-edit: they are derived from `library/`, and a manual
edit will be overwritten. To change one, change the prompt.

Two things to check on a generated skill before relying on it:

- **The `description`** decides when the skill triggers. The generated one is
  derived from the prompt's task and deliverables; if it does not read like the
  words a BA would actually use, rewrite it in the library prompt.
- **The worked example** is inherited and may be wrong for a narrowed task.
