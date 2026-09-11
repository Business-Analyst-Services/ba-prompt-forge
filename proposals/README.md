# Proposals

Machine-generated prompt drafts. **Nothing here is part of the library.**

`tools/decompose.py` writes single-task unit prompts derived from the modes of a
multi-mode Master prompt:

```bash
python tools/decompose.py BB-01-M          # preview
python tools/decompose.py --all --write    # write all 188 candidates
```

The contents of this folder are gitignored, because a generated draft has not
been reviewed and an unreviewed prompt does not belong in a quality library.

## Promoting one

Each proposal carries a `review_needed` list. Work through it:

1. **Narrow `output_format`** - it is still the parent's, and describes an
   artefact the unit does not produce.
2. **Replace `example`** - inherited from the parent, and usually wrong for the
   narrower task. This is the field that most changes output quality, so it is
   the one that most needs rewriting.
3. **Trim `situation` and `inputs`** the single task does not need.
4. **Run it once** on real de-identified work.

Then move the file into `library/<role>/<service>/`, drop `status` and
`review_needed`, set `provenance.author` to yourself, and:

```bash
python tools/build.py
python tools/lint.py library/.../BB-01-U2.md
```

See [docs/decomposition.md](../docs/decomposition.md) for why units exist at all.
