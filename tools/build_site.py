"""Build the whole library as a static, accessible website into site/.

The site is the deliverable, not a shop window for the repository: every prompt,
every framework rendering, the full rubric, the delivery contexts, the skills and
all the guidance are pages here. Nothing requires the reader to open GitHub.

Accessibility is built in and checked, not asserted:
  - every colour pair in site.css is contrast-tested against WCAG 2.1 AA below,
    and the build fails if one drops under threshold
  - pages are complete without JavaScript (all format panels render in the HTML;
    script only hides, filters and copies)
  - one h1 per page, ordered headings, landmarks, skip link, visible focus
  - tables carry scope, forms carry real labels, filter results are announced

    python tools/build_site.py
    python tools/build_site.py --serve   # preview at http://localhost:8000
"""
from __future__ import annotations

import html

import re
import shutil
import sys
from pathlib import Path

import markdown
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from convert import to_skill  # noqa: E402
from formats import FORMATS, fidelity, render  # noqa: E402
from lib_ir import CRITERIA, ROOT, all_prompts  # noqa: E402

SITE = ROOT / "site"
ASSETS = Path(__file__).resolve().parent / "site_assets"
REPO = "https://github.com/Business-Analyst-Services/ba-prompt-forge"
BLOB = f"{REPO}/blob/main/"
BASE = "/ba-prompt-forge/"  # project-site path, used only by 404.html

NAV = [
    ("prompts/", "Find a prompt"),
    ("contexts/", "Delivery contexts"),
    ("frameworks/", "Frameworks"),
    ("scoring/", "Scoring"),
    ("skills/", "Skills"),
    ("contribute/", "Contribute"),
    ("about/", "About"),
]

# Repo paths that have a home on the site. Anything unmapped falls through to
# the GitHub blob URL so no link in the imported markdown ever dies.
LINK_MAP = {
    "README.md": "",
    "INDEX.md": "prompts/",
    "CONTRIBUTING.md": "contribute/",
    "CONTRIBUTORS.md": "about/#contributors",
    "LICENSE": "about/#licence",
    "catalogue.json": "catalogue.json",
    "formats/README.md": "frameworks/",
    "rubric/care-get-v1.yml": "scoring/",
    "contexts/delivery-contexts.yml": "contexts/",
    "docs/scoring.md": "scoring/",
    "docs/decomposition.md": "decomposition/",
    "docs/roadmap.md": "roadmap/",
    "docs/statistics.md": "about/#statistics",
    "field-reports/": "contribute/#field-reports",
    "field-reports/README.md": "contribute/#field-reports",
    "proposals/README.md": "decomposition/",
    "skills/README.md": "skills/",
    "skills/generated/": "skills/#generated",
    "skills/ba-prompt-router/SKILL.md": "skills/ba-prompt-router.html",
    "skills/ba-prompt-scorer/SKILL.md": "skills/ba-prompt-scorer.html",
    "skills/ba-prompt-forge/SKILL.md": "skills/ba-prompt-forge.html",
}

# --------------------------------------------------------------------------- #
# WCAG contrast checking
# --------------------------------------------------------------------------- #

def _luminance(hex_colour: str) -> float:
    r, g, b = (int(hex_colour[i:i + 2], 16) / 255 for i in (1, 3, 5))
    def channel(c: float) -> float:
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = channel(r), channel(g), channel(b)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b

def contrast(fg: str, bg: str) -> float:
    a, b = _luminance(fg), _luminance(bg)
    lo, hi = min(a, b), max(a, b)
    return (hi + 0.05) / (lo + 0.05)

# (foreground, background, minimum, what it is) - checked for both themes.
CONTRAST_CHECKS = [
    ("--text", "--bg", 4.5, "body text"),
    ("--text", "--surface", 4.5, "text on header/footer"),
    ("--muted", "--bg", 4.5, "muted text"),
    ("--muted", "--surface", 4.5, "muted text on surface"),
    ("--link", "--bg", 4.5, "links"),
    ("--link", "--surface", 4.5, "links on surface"),
    ("--link-hover", "--bg", 4.5, "hovered links"),
    ("--focus", "--bg", 3.0, "focus ring"),
    ("--border-strong", "--bg", 3.0, "control borders"),
    ("--border-strong", "--surface", 3.0, "control borders on surface"),
    ("--good-fg", "--good-bg", 4.5, "library-ready badge"),
    ("--warn-fg", "--warn-bg", 4.5, "refine badge"),
    ("--bad-fg", "--bad-bg", 4.5, "rework badge"),
    ("--text", "--code-bg", 4.5, "code blocks"),
]

def _tokens(css: str, selector_body: str) -> dict[str, str]:
    return dict(re.findall(r"(--[a-z0-9-]+):\s*(#[0-9a-fA-F]{6})", selector_body))

def check_contrast(css: str) -> list[str]:
    """Parse the two palettes out of site.css and test every declared pair."""
    light_block = css.split(":root {", 1)[1].split("}", 1)[0]
    dark_block = css.split(':root[data-theme="dark"] {', 1)[1].split("}", 1)[0]
    problems = []
    for theme, block in (("light", light_block), ("dark", dark_block)):
        tokens = _tokens(css, block)
        for fg, bg, minimum, label in CONTRAST_CHECKS:
            if fg not in tokens or bg not in tokens:
                problems.append(f"{theme}: token {fg} or {bg} missing")
                continue
            ratio = contrast(tokens[fg], tokens[bg])
            if ratio < minimum:
                problems.append(
                    f"{theme}: {label} ({fg} on {bg}) is {ratio:.2f}:1, needs {minimum}:1"
                )
    return problems

# --------------------------------------------------------------------------- #
# HTML helpers
# --------------------------------------------------------------------------- #

def e(text) -> str:
    return html.escape(str(text if text is not None else ""), quote=True)

def rel(depth: int, path: str = "") -> str:
    prefix = "../" * depth
    if not path:
        return prefix or "./"
    return prefix + path

def verdict_class(total) -> str:
    if total is None:
        return "badge-warn"
    return "badge-good" if total >= 17 else "badge-warn" if total >= 12 else "badge-bad"

def page(*, title: str, description: str, depth: int, current: str, body: str,
         absolute: bool = False) -> str:
    """The shell every page shares. `absolute` is for 404.html, which GitHub
    serves from arbitrary URLs where relative links would not resolve."""
    def href(path: str) -> str:
        return (BASE + path) if absolute else rel(depth, path)

    body = harden(body)
    nav = "\n".join(
        f'          <li><a href="{href(path)}"'
        + (' aria-current="page"' if path == current else "")
        + f">{e(label)}</a></li>"
        for path, label in NAV
    )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)} &middot; BA Prompt Forge</title>
<meta name="description" content="{e(description)}">
<meta name="color-scheme" content="light dark">
<link rel="stylesheet" href="{href('assets/site.css')}">
</head>
<body>
<a class="skip-link" href="#main">Skip to main content</a>
<header class="site-header">
  <div class="wrap">
    <a class="brand" href="{href('')}">BA Prompt Forge</a>
    <nav class="site-nav" aria-label="Main">
      <ul>
{nav}
      </ul>
    </nav>
    <button type="button" class="theme-toggle" aria-pressed="false" hidden>Dark theme</button>
  </div>
</header>
<main id="main" class="wrap" tabindex="-1">
{body}
</main>
<footer class="site-footer">
  <div class="wrap">
    <p><strong>BA Prompt Forge</strong> &mdash; 126 scored business-analysis prompts,
    convertible into ten prompt frameworks or into agent skills.</p>
    <p>Prompts, rubric and documentation are licensed
    <a href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a>; the tooling is MIT.
    Each prompt names its own author &mdash; see <a href="{href('about/')}">About</a>.
    Source on <a href="{REPO}">GitHub</a>.</p>
    <p>Built to WCAG 2.1 AA. Found something unusable?
    <a href="{REPO}/issues/new">Tell us</a> &mdash; accessibility defects are treated as bugs.</p>
  </div>
</footer>
<script src="{href('assets/site.js')}"></script>
</body>
</html>
"""

def write(path: str, content: str) -> None:
    target = SITE / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8")

_scroll_id = [0]

def scroll_region(inner: str, label: str) -> str:
    """A horizontally scrollable box must be reachable by keyboard, and a
    focusable box must have a name. Both, or axe's scrollable-region-focusable
    fires - and a keyboard-only user genuinely cannot scroll the thing."""
    _scroll_id[0] += 1
    return (f'<div class="table-scroll" role="region" tabindex="0" '
            f'aria-label="{e(label)}">{inner}</div>')

def table(headers: list[str], rows: list[list[str]], caption: str = "") -> str:
    head = "".join(f'<th scope="col">{h}</th>' for h in headers)
    body = "\n".join(
        "<tr>" + "".join(
            (f'<th scope="row">{cell}</th>' if i == 0 else f"<td>{cell}</td>")
            for i, cell in enumerate(row)
        ) + "</tr>"
        for row in rows
    )
    cap = f"<caption>{caption}</caption>" if caption else ""
    label = re.sub(r"<[^>]+>", "", caption) or f"Table of {headers[0].lower()}"
    return scroll_region(
        f"<table>{cap}<thead><tr>{head}</tr></thead><tbody>\n{body}\n</tbody></table>",
        label,
    )

# --------------------------------------------------------------------------- #
# Markdown import
# --------------------------------------------------------------------------- #

def _rewrite_link(link: str, source_dir: str, depth: int) -> str:
    if link.startswith(("http://", "https://", "mailto:", "#")):
        return link
    anchor = ""
    if "#" in link:
        link, anchor = link.split("#", 1)
        anchor = "#" + anchor
    parts: list[str] = []
    for part in (source_dir + "/" + link if source_dir else link).split("/"):
        if part in ("", "."):
            continue
        if part == "..":
            if parts:
                parts.pop()
        else:
            parts.append(part)
    normalised = "/".join(parts)
    if normalised in LINK_MAP:
        mapped = LINK_MAP[normalised]
        if "#" in mapped:
            mapped, mapped_anchor = mapped.split("#", 1)
            anchor = anchor or "#" + mapped_anchor
        return rel(depth, mapped) + anchor
    if normalised + "/" in LINK_MAP:
        return rel(depth, LINK_MAP[normalised + "/"]) + anchor
    return BLOB + normalised + anchor

def md_to_html(source: Path, depth: int) -> str:
    """Render a repo markdown file as site prose, with links rewritten and
    tables given the scope attributes python-markdown omits."""
    text = source.read_text(encoding="utf-8")
    if text.startswith("---\n"):  # SKILL.md front-matter
        text = text.split("---\n", 2)[2]
    text = re.sub(r"^#\s+.+\n+", "", text, count=1)  # h1 comes from the page shell

    out = markdown.markdown(
        text, extensions=["tables", "fenced_code", "sane_lists", "attr_list"]
    )
    source_dir = source.parent.relative_to(ROOT).as_posix()
    source_dir = "" if source_dir == "." else source_dir
    out = re.sub(
        r'href="([^"]+)"',
        lambda m: f'href="{e(_rewrite_link(html.unescape(m.group(1)), source_dir, depth))}"',
        out,
    )
    out = out.replace("<th>", '<th scope="col">')

    # Wrap each markdown table in a labelled, focusable scroll region, naming it
    # from the nearest preceding heading so the label is never generic.
    heading = ["Table"]

    def note_heading(match: re.Match) -> str:
        heading[0] = re.sub(r"<[^>]+>", "", match.group(2)).strip() or "Table"
        return match.group(0)

    def wrap_table(match: re.Match) -> str:
        return scroll_region(match.group(0), f"Table: {heading[0]}")

    out = re.sub(r"<(h[23])[^>]*>(.*?)</\1>", note_heading, out, flags=re.S)
    pieces, last = [], 0
    for m in re.finditer(r"<(?:h[23])[^>]*>.*?</(?:h[23])>|<table>.*?</table>", out, re.S):
        pieces.append(out[last:m.start()])
        chunk = m.group(0)
        if chunk.startswith("<table"):
            pieces.append(scroll_region(chunk, f"Table: {heading[0]}"))
        else:
            heading[0] = re.sub(r"<[^>]+>", "", chunk).strip() or "Table"
            pieces.append(chunk)
        last = m.end()
    pieces.append(out[last:])
    out = "".join(pieces)

    return f'<div class="prose">{out}</div>'

def harden(body: str) -> str:
    """A <pre> can scroll horizontally, so it must be keyboard-reachable too."""
    return re.sub(r"<pre(?![^>]*tabindex)", '<pre tabindex="0"', body)

# --------------------------------------------------------------------------- #
# Pages
# --------------------------------------------------------------------------- #

def prompt_page(p: dict) -> str:
    total = (p.get("score") or {}).get("total")
    pid = p["id"]
    panels, tabs = [], []

    variants = [(key, meta["label"], render(p, key), fidelity(p, key))
                for key, meta in FORMATS.items()]
    variants.append(("skill", "Agent skill", to_skill(p), None))

    for i, (key, label, text, fid) in enumerate(variants):
        panel_id, tab_id, code_id = f"panel-{key}", f"tab-{key}", f"code-{key}"
        note = ""
        if fid:
            lost = ", ".join(fid["criteria_lost"])
            note = (
                f'<p class="muted">{e(FORMATS[key]["note"])} '
                + (f'Converting costs {fid["original_total"] - fid["converted_total"]} '
                   f'rubric point(s) &mdash; this rendering scores '
                   f'{fid["converted_total"]}/20, losing: {e(lost)}.'
                   if lost else "Lossless: every rubric criterion has somewhere to go.")
                + "</p>"
            )
        else:
            note = ('<p class="muted">The prompt rebuilt as an agent skill: the modes become '
                    "steps, the clarifying questions become a gate before drafting, and the "
                    "validation block becomes a hand-back checklist. Save as "
                    "<code>SKILL.md</code>.</p>")
        tabs.append(
            f'<button type="button" role="tab" id="{tab_id}" aria-controls="{panel_id}" '
            f'aria-selected="{"true" if i == 0 else "false"}" '
            f'tabindex="{"0" if i == 0 else "-1"}">{e(label)}</button>'
        )
        panels.append(f"""
<div class="tabpanel" role="tabpanel" id="{panel_id}" aria-labelledby="{tab_id}" tabindex="0">
  <h3 class="panel-heading">{e(label)}</h3>
  {note}
  <div class="copy-row">
    <button type="button" class="btn" data-copy="{code_id}"
            data-copy-status="copy-status-{key}" hidden>Copy {e(label)} prompt</button>
    <span class="copy-status" id="copy-status-{key}" role="status" aria-live="polite"></span>
  </div>
  <pre id="{code_id}"><code>{e(text)}</code></pre>
</div>""")

    inputs = "\n".join(f"<li><code>[{e(i)}]</code></li>" for i in p.get("inputs", [])) \
        or "<li>None &mdash; this prompt takes no placeholders.</li>"
    contexts = "\n".join(
        f'<li><a href="{rel(1, "contexts/")}#{e(re.sub(r"[^a-z0-9]+", "-", c.lower()).strip("-"))}">'
        f"{e(c)}</a></li>" for c in p.get("delivery_contexts", [])
    ) or "<li>Not mapped to a delivery context.</li>"

    score_rows = [[e(label), str((p.get("score") or {}).get(key, "&ndash;")),
                   "Machine-checked" if key in {
                       "c4_example", "c5_explain", "c6_test", "c7_anti_fabrication",
                       "c8_data_safety", "c9_reusability"} else "Judgement"]
                  for key, label in CRITERIA]
    notes = (p.get("score") or {}).get("notes")
    prov = p.get("provenance") or {}

    body = f"""
<p class="muted"><a href="{rel(1, 'prompts/')}">&larr; All prompts</a></p>
<h1>{e(p['name'])}</h1>
<p class="meta">
  <code>{e(pid)}</code>
  <span>{e(p['role'])}</span>
  <span>{e(p['service'])}</span>
  <span>{e(p['type'].title())} prompt</span>
  <span class="badge {verdict_class(total)}">{e(total)}/20 {e((p.get('score') or {}).get('verdict', ''))}</span>
</p>
<p class="lede">{e(p['task'])}</p>

<h2>Who it is for</h2>
<p><strong>You are:</strong> {e(p['persona'])}.<br>
<strong>The audience for the output:</strong> {e(p['audience'])}.</p>
<p><strong>Target deliverables:</strong> {e(', '.join(p.get('deliverables', [])) or '&ndash;')}</p>

<h2 id="fill-in">What you need to fill in</h2>
<ul>
{inputs}
</ul>
<div class="panel">
  <p><strong>Before you paste anything in:</strong> {e(p['data_safety'])}</p>
</div>

<h2 id="prompt">The prompt</h2>
<p>Pick the framework your tool expects. The first is the library's native
CARE + G.E.T. build; the others are conversions, and each says what it costs.</p>
<div class="tabs full">
  <div class="tablist" role="tablist" aria-label="Prompt framework">
    {''.join(tabs)}
  </div>
  {''.join(panels)}
</div>

<h2 id="scorecard">Scorecard</h2>
{table(["Criterion", "Mark", "Decided by"], score_rows,
       "Marks out of 2 against the ten-criterion CARE + G.E.T. rubric.")}
<p><strong>Total: {e(total)}/20 &mdash; {e((p.get('score') or {}).get('verdict', ''))}.</strong>
{('<br>' + e(notes)) if notes else ''}</p>
<p class="muted">A high score means the prompt is well-formed, not that it is effective.
<a href="{rel(1, 'scoring/')}">How scoring works</a>.</p>

<h2 id="contexts">Used in these delivery contexts</h2>
<ul>
{contexts}
</ul>

<h2 id="provenance">Provenance</h2>
<ul>
  <li><strong>Author:</strong> {e(prov.get('author', 'Unknown'))}</li>
  <li><strong>Source:</strong> {e(prov.get('source', '&ndash;'))}</li>
  <li><strong>Added:</strong> {e(prov.get('added', '&ndash;'))}</li>
  <li><strong>Licence:</strong> {e(prov.get('license', 'CC-BY-4.0'))}</li>
</ul>
<p>Improved this prompt, or used it on real work?
<a href="{rel(1, 'contribute/')}">Contribute it back</a> &mdash; you keep the credit.</p>
"""
    return page(title=p["name"], depth=1, current="prompts/",
                description=f"{p['id']}: {p['task'][:150]}", body=body)

def prompts_index(prompts: list[dict]) -> str:
    roles = sorted({p["role"] for p in prompts})
    services = sorted({p["service"] for p in prompts})
    types = sorted({p["type"] for p in prompts})

    rows = []
    for p in prompts:
        total = (p.get("score") or {}).get("total")
        hay = " ".join([
            p["id"], p["name"], p["service"], p["role"], p["task"],
            " ".join(p.get("deliverables", [])), " ".join(p.get("delivery_contexts", [])),
        ]).lower()
        rows.append(f"""<tr data-prompt data-role="{e(p['role'])}" data-type="{e(p['type'])}"
 data-service="{e(p['service'])}" data-haystack="{e(hay)}">
<th scope="row"><a href="{e(p['id'])}.html">{e(p['name'])}</a><br>
<small class="muted"><code>{e(p['id'])}</code></small></th>
<td>{e(p['role'])}</td><td>{e(p['type'].title())}</td><td>{e(p['service'])}</td>
<td><span class="badge {verdict_class(total)}">{e(total)}/20</span></td></tr>""")

    def options(items):
        return "".join(f'<option value="{e(x)}">{e(x.title() if x.islower() else x)}</option>'
                       for x in items)

    body = f"""
<h1>Find a prompt</h1>
<p class="lede">{len(prompts)} prompts across {len(services)} business-analysis services.
Filter below &mdash; or, better, don't.</p>

<div class="panel">
  <h2>Reading a list of 126 is the slow way</h2>
  <p>Nobody knows in advance whether they want <code>BT-06-D2</code> or <code>BB-07-M</code>.
  If you know the <em>artefact</em> you need, filter by service below. If you only know what
  kind of project you are on, start from
  <a href="{rel(1, 'contexts/')}">delivery contexts</a> instead. And if you have an AI
  assistant to hand, the <a href="{rel(1, 'skills/ba-prompt-router.html')}">prompt router
  skill</a> does the narrowing for you &mdash; you describe the work in your own words and it
  returns one filled-in prompt.</p>
</div>

<form class="filters full" role="search" aria-label="Filter prompts"
      onsubmit="return false;">
  <div class="field">
    <label for="filter-search">Search</label>
    <input type="search" id="filter-search" autocomplete="off"
           placeholder="acceptance criteria, business case, cutover&hellip;">
  </div>
  <div class="field">
    <label for="filter-role">Role</label>
    <select id="filter-role" data-filter="role"><option value="">All roles</option>{options(roles)}</select>
  </div>
  <div class="field">
    <label for="filter-type">Type</label>
    <select id="filter-type" data-filter="type"><option value="">All types</option>{options(types)}</select>
  </div>
  <div class="field">
    <label for="filter-service">BA service</label>
    <select id="filter-service" data-filter="service"><option value="">All services</option>{options(services)}</select>
  </div>
  <div class="field">
    <span aria-hidden="true"></span>
    <button type="button" class="btn" id="filter-reset" hidden>Clear filters</button>
  </div>
</form>

<p class="result-count" id="result-count" role="status" aria-live="polite">Showing all {len(prompts)} prompts.</p>
<p id="no-results" hidden>No prompts match those filters. Try clearing one, or
<a href="{rel(1, 'contribute/')}">propose the prompt that is missing</a>.</p>

<div class="table-scroll full">
<table id="prompt-list">
  <caption>Every prompt, with its role, type, service and rubric score.</caption>
  <thead><tr>
    <th scope="col">Prompt</th><th scope="col">Role</th><th scope="col">Type</th>
    <th scope="col">BA service</th><th scope="col">Score</th>
  </tr></thead>
  <tbody>
{''.join(rows)}
  </tbody>
</table>
</div>

<h2>Master, Deliverable, Unit</h2>
<dl>
  <dt><strong>Master</strong></dt>
  <dd>A working session across a whole BA service. Offers several modes, which is why
  every Master scores 19 rather than 20 &mdash; a menu is not a single task.</dd>
  <dt><strong>Deliverable</strong></dt>
  <dd>One artefact, one task. Use these when you know what you need.</dd>
  <dt><strong>Unit</strong></dt>
  <dd>A Master split down to a single task so it can be tested.
  <a href="{rel(1, 'decomposition/')}">How decomposition works</a>.</dd>
</dl>
"""
    return page(title="Find a prompt", depth=1, current="prompts/",
                description="Filter 126 scored business-analysis prompts by role, "
                            "type and service.", body=body)

def contexts_page(contexts: list[dict], by_id: dict[str, dict]) -> str:
    sections = []
    for ctx in contexts:
        anchor = re.sub(r"[^a-z0-9]+", "-", f"{ctx['id']}. {ctx['name']}".lower()).strip("-")
        starts = [by_id[pid] for pid in ctx["start_with"] if pid in by_id]
        seen, first = set(), []
        for p in starts:
            if p["service"] not in seen:
                seen.add(p["service"])
                first.append(p)
        links = "\n".join(
            f'<li><a href="{rel(1, "prompts/")}{e(p["id"])}.html">{e(p["name"])}</a> '
            f'<span class="muted">&mdash; {e(p["service"])}</span></li>' for p in first[:8]
        )
        more = (f'<p class="muted">{len(starts)} prompts are mapped to this context in total.</p>'
                if len(starts) > len(first[:8]) else "")
        gaps = ""
        if ctx["gaps"]:
            items = "".join(f"<li>{e(g)}</li>" for g in ctx["gaps"])
            gaps = f"""<div class="panel">
  <h3>Known gaps in this context</h3>
  <p>The source catalogue flags these as not yet decomposed into prompts:</p>
  <ul>{items}</ul>
  <p>If you need one of these, it does not exist yet &mdash;
  <a href="{rel(1, 'contribute/')}">writing it is a genuinely useful contribution</a>.</p>
</div>"""
        sections.append(f"""
<h2 id="{anchor}">{ctx['id']}. {e(ctx['name'])}</h2>
<p>{e(ctx['when'])}</p>
<h3>Start with these prompts</h3>
<ul>
{links}
</ul>
{more}
<h3>BA services engaged</h3>
<p class="muted">{e('; '.join(ctx['services']))}</p>
{gaps}""")

    toc = "\n".join(
        f'<li><a href="#{re.sub(r"[^a-z0-9]+", "-", f"{c["id"]}. {c["name"]}".lower()).strip("-")}">'
        f'{c["id"]}. {e(c["name"])}</a></li>' for c in contexts
    )
    total_gaps = sum(len(c["gaps"]) for c in contexts)
    body = f"""
<h1>Delivery contexts</h1>
<p class="lede">Know your project type but not which prompt you need? Start here.
Eleven contexts, each mapped to the BA services and prompts most used in it.</p>

<nav aria-labelledby="toc-heading">
  <h2 id="toc-heading">On this page</h2>
  <ol>
{toc}
  </ol>
</nav>

<p>{total_gaps} decomposition gaps are flagged across these contexts &mdash; places the
source catalogue knows it does not yet cover. They are listed in context below rather than
hidden, because a known gap is more useful than a forced match.</p>
{''.join(sections)}
"""
    return page(title="Delivery contexts", depth=1, current="contexts/",
                description="Eleven BA delivery contexts mapped to the services and "
                            "prompts most used in each.", body=body)

def frameworks_page(prompts: list[dict]) -> str:
    ref = next((p for p in prompts if p["id"] == "BB-01-D1"), prompts[0])
    rows, sections = [], []
    for key, meta in FORMATS.items():
        f = fidelity(ref, key)
        lost = ", ".join(f["criteria_lost"]) or "&mdash;"
        rows.append([f"<code>{e(key)}</code>", e(meta["label"]),
                     f"{f['converted_total']} / 20", lost])
        sections.append(f"""
<h2 id="{e(key)}">{e(meta['label'])}</h2>
<p>{e(meta['note'])}</p>
<p><strong>{ref['id']} rendered as {e(meta['label'])}</strong> &mdash; scores
{f['converted_total']}/20{'' if not f['criteria_lost'] else ', losing ' + e(lost)}.</p>
<details>
  <summary>Show the rendering</summary>
  <pre><code>{e(render(ref, key))}</code></pre>
</details>""")

    body = f"""
<h1>Prompt frameworks</h1>
<p class="lede">The library is written in CARE + G.E.T., but CARE is a storage format,
not a commitment. Every prompt can be re-rendered into any of ten frameworks &mdash;
or into an agent skill.</p>

<h2>Why that is possible</h2>
<p>Each prompt is stored as <strong>fields, not as a blob of text</strong>: who is writing,
who reads it, the one task, the checkable output format, the guardrails, the worked example.
A blob cannot be re-rendered into another framework, scored criterion by criterion, or turned
into a skill. Fields can.</p>

<h2>Conversion is lossy, and we say by how much</h2>
<p>A framework with no Example slot cannot carry the worked example. A framework with no place
for verification rules drops them. Each renderer declares which of the
<a href="{rel(1, 'scoring/')}">ten rubric criteria</a> its slots can actually carry, so the
cost of a conversion is a number rather than a shrug.</p>
{table(["Flag", "Framework", "Score after conversion", "Criteria lost"], rows,
       f"{ref['id']} scores {(ref.get('score') or {}).get('total')}/20 in CARE. "
       "Its score in each other framework:")}
<p>Picking a lossy framework is fine &mdash; for a short input box, or a house standard.
Picking one without knowing is not.</p>

<h2>Converting a prompt into an agent skill</h2>
<p>A prompt is one turn; a skill is a procedure. The conversion is not a copy-paste: the modes
become steps, the clarifying questions become a gate before drafting, the validation block
becomes a hand-back checklist, and first-person wording is shifted to address the agent about
the user. Every prompt page carries its skill build under the
<strong>Agent skill</strong> tab, and <a href="{rel(1, 'skills/')}">all 126 are listed
here</a>.</p>

{''.join(sections)}
"""
    return page(title="Prompt frameworks", depth=1, current="frameworks/",
                description="Ten prompt frameworks - CARE, CO-STAR, TIDD-EC, RISEN, "
                            "CRISPE, RACE, RTF, APE, BAB - and what each conversion costs.",
                body=body)

def scoring_page(rubric: dict, prompts: list[dict]) -> str:
    machine = {"c4_example", "c5_explain", "c6_test", "c7_anti_fabrication",
               "c8_data_safety", "c9_reusability"}
    rows = [[f"{c['number']}. {e(c['name'])}", e(c["group"]), e(c["good"]), e(c["anchors"]),
             "Machine" if c["key"] in machine else "Judgement"]
            for c in rubric["criteria"]]
    bands = [[f"{b['min']}&ndash;{b['max']}", e(b["verdict"]), e(b["action"])]
             for b in rubric["bands"]]
    mean = sum((p.get("score") or {}).get("total", 0) for p in prompts) / len(prompts)

    body = f"""
<h1>Scoring</h1>
<p class="lede">Every prompt carries a mark out of 20 against a ten-criterion rubric.
Six of those criteria a machine can decide; four need judgement. The difference matters
more than the number.</p>

<h2 id="criteria">The ten criteria</h2>
<p>Each is scored 0 (absent), 1 (partial) or 2 (met).</p>
{table(["Criterion", "Group", "What good looks like", "Scoring anchors", "Decided by"], rows,
       "The CARE + G.E.T. quality scorecard, version 1.0.")}

<h2 id="bands">Bands</h2>
{table(["Score", "Verdict", "What to do"], bands)}

<h2 id="split">What a machine can and cannot decide</h2>
<p>Six criteria are mechanically decidable, and the repository's linter decides them: is there
a real worked example, does the anti-fabrication rule name a flagging convention, is there a
marked placeholder, does the prompt carry an explicit de-identification instruction.</p>
<p>Four need a human: <strong>Context</strong>, <strong>Action</strong>,
<strong>Result/Format</strong> and <strong>Right-sized</strong>. For these the linter offers
only a provisional mark and flags it for review.</p>
<p>That split is the whole design. A score claiming machine precision on judgement criteria is
worse than no score, because it gets trusted. Four useful tests for the judgement four:</p>
<ul>
  <li><strong>Context</strong> &mdash; cover the role and the audience with your thumb. Does
  the prompt still say who is writing and who reads it?</li>
  <li><strong>Action</strong> &mdash; count the deliverables asked for. More than one is a
  menu, not a task.</li>
  <li><strong>Result/Format</strong> &mdash; could a reviewer hold the output against the
  prompt and tick each requirement off?</li>
  <li><strong>Right-sized</strong> &mdash; delete each sentence in turn. Would the output
  change?</li>
</ul>

<h2 id="self-award">Scores are checked, not taken</h2>
<p>The repository's continuous integration compares each prompt's declared score against the
machine findings and <strong>fails on any disagreement about a machine-decidable
criterion</strong>. A self-awarded scorecard is worth nothing; six of the ten cannot be
self-awarded here.</p>

<h2 id="caveat">What a 20/20 does not mean</h2>
<div class="panel">
  <p>This library was written against this rubric. Its mean of {mean:.2f}/20 measures the
  author's discipline in applying a template &mdash; not the prompts' effect on real work.</p>
</div>
<p>Stronger evidence, in order:</p>
<ol>
  <li><strong>Dry run</strong> on real de-identified work. Did it produce the promised shape?</li>
  <li><strong>Consistency.</strong> Run it twice. Does it give you the same structure?</li>
  <li><strong>Hand-off.</strong> Give the output to someone who was not in the room. Can they
  use it without asking you what it means?</li>
</ol>
<p>That is what <a href="{rel(1, 'contribute/')}#field-reports">field reports</a> are for.
One field report is worth more than a point of rubric score.</p>

<h2 id="disagreements">Two disagreements on the record</h2>
<p>Building the tooling surfaced two places where the machine and the original author differ.
Both are recorded rather than tuned away.</p>
<ul>
  <li><strong>One prompt, criterion 2.</strong> <code>BB-03-M</code> opens &ldquo;Help me
  define the real problem&hellip;&rdquo;. A naive check flags any &ldquo;help me&rdquo; as the
  rubric's vague 0-anchor. It is not &mdash; there is a strong verb and an object. The check
  was narrowed. The same false positive will bite anyone scoring by keyword.</li>
  <li><strong>Six prompts, criterion 3.</strong> The machine cannot see checkable structure in
  six output formats the author marked 2/2. They are left flagged for review rather than
  resolved by either side.</li>
</ul>
"""
    return page(title="Scoring", depth=1, current="scoring/",
                description="The ten-criterion CARE + G.E.T. rubric, the scoring bands, "
                            "and what a high score does and does not mean.", body=body)

def skills_pages(prompts: list[dict]) -> list[tuple[str, str]]:
    hand = [
        ("ba-prompt-router", "Prompt router",
         "Describe your work; get the right prompt, filled in."),
        ("ba-prompt-scorer", "Prompt scorer",
         "Score any prompt out of 20 and fix the deductions."),
        ("ba-prompt-forge", "Prompt forge",
         "Write a new prompt to library standard, or convert one."),
    ]
    pages = []
    for slug, title, blurb in hand:
        source = ROOT / "skills" / slug / "SKILL.md"
        front = yaml.safe_load(source.read_text(encoding="utf-8").split("---\n")[1])
        body = f"""
<p class="muted"><a href="{rel(1, 'skills/')}">&larr; All skills</a></p>
<h1>{e(title)}</h1>
<p class="lede">{e(blurb)}</p>
<div class="panel">
  <p><strong>Skill name:</strong> <code>{e(front['name'])}</code></p>
  <p><strong>Description</strong> (this is what makes an agent trigger it):
  {e(front['description'])}</p>
  <p>Save the text below as <code>SKILL.md</code> inside a folder named
  <code>{e(front['name'])}</code>, and point your agent at it. It works with any runtime that
  reads agent skills.</p>
</div>
<div class="copy-row">
  <button type="button" class="btn" data-copy="skill-source"
          data-copy-status="copy-status-skill" hidden>Copy the full SKILL.md</button>
  <span class="copy-status" id="copy-status-skill" role="status" aria-live="polite"></span>
</div>
<details>
  <summary>Show the raw SKILL.md (with front-matter, ready to save)</summary>
  <pre id="skill-source"><code>{e(source.read_text(encoding='utf-8'))}</code></pre>
</details>
<h2>What it says</h2>
{md_to_html(source, 1)}
"""
        pages.append((f"skills/{slug}.html",
                      page(title=title, depth=1, current="skills/",
                           description=front["description"][:180], body=body)))

    generated = "\n".join(
        f'<li><a href="{rel(1, "prompts/")}{e(p["id"])}.html#prompt">{e(p["name"])}</a> '
        f'<span class="muted">&mdash; {e(p["role"])}</span></li>'
        for p in prompts if p["type"] == "master"
    )
    cards = "\n".join(f"""<li class="card">
  <h3><a href="{e(slug)}.html">{e(title)}</a></h3>
  <p>{e(blurb)}</p>
</li>""" for slug, title, blurb in hand)

    index_body = f"""
<h1>Skills</h1>
<p class="lede">An agent skill is a folder of instructions &mdash; a <code>SKILL.md</code> file
an AI assistant reads and follows. These turn the library into something that works
<em>with</em> you rather than something you have to search.</p>

<h2>The three that matter</h2>
<ul class="cards">
{cards}
</ul>

<div class="panel">
  <h2>Start with the router</h2>
  <p>A catalogue of 126 prompts is a homework assignment. The router is the answer to that:
  you describe the work in your own words &mdash; &ldquo;I need acceptance criteria a tester
  can actually work from&rdquo; &mdash; and it narrows, recommends one prompt, asks you for the
  placeholders, and hands back something you can paste. It is told, in as many words, never to
  show you a list of 126 anything.</p>
</div>

<h2 id="generated">Every prompt is also a skill</h2>
<p>All {len(prompts)} prompts convert to standalone skills. Open any prompt and choose the
<strong>Agent skill</strong> tab to get its <code>SKILL.md</code>. Useful when you want one BA
service always available without the router in front of it.</p>
<p>Two things to check before relying on a generated skill: the <strong>description</strong>
decides when it triggers, so make sure it reads like the words you would actually use; and the
<strong>worked example</strong> is inherited from the prompt, so it may need swapping for one
from your own domain.</p>
<h3>The 42 service-level skills</h3>
<ul>
{generated}
</ul>
"""
    pages.append(("skills/index.html",
                  page(title="Skills", depth=1, current="skills/",
                       description="Agent skills that route, score and author BA prompts, "
                                   "plus all 126 prompts as standalone skills.",
                       body=index_body)))
    return pages

def home_page(prompts: list[dict], contexts: list[dict]) -> str:
    mean = sum((p.get("score") or {}).get("total", 0) for p in prompts) / len(prompts)
    services = len({p["service"] for p in prompts})
    ctx_cards = "\n".join(f"""<li class="card">
  <h3><a href="{rel(0, 'contexts/')}#{re.sub(r'[^a-z0-9]+', '-', f"{c['id']}. {c['name']}".lower()).strip('-')}">{e(c['name'])}</a></h3>
  <p>{e(c['when'][:120])}{'&hellip;' if len(c['when']) > 120 else ''}</p>
</li>""" for c in contexts)

    body = f"""
<h1>Business-analysis prompts you don't have to browse</h1>
<p class="lede">{len(prompts)} prompts across {services} BA services, every one scored against
a published quality rubric, every one convertible into ten prompt frameworks or into an agent
skill.</p>

<div class="panel">
  <h2>Start where you actually are</h2>
  <p>You almost never know which prompt you want &mdash; you know what you have to produce by
  Friday. So pick whichever of these matches what is in your head right now:</p>
  <ul>
    <li><strong>I know the artefact I need</strong> (acceptance criteria, a KPI table, a
    cutover plan) &rarr; <a href="{rel(0, 'prompts/')}">search the prompts</a>.</li>
    <li><strong>I know my project type but not the artefact</strong> (agile delivery,
    procurement, a data warehouse) &rarr; <a href="{rel(0, 'contexts/')}">start from a delivery
    context</a>.</li>
    <li><strong>I have an AI assistant open right now</strong> &rarr; give it the
    <a href="{rel(0, 'skills/ba-prompt-router.html')}">router skill</a> and just describe the
    work.</li>
  </ul>
</div>

<h2>What makes these different from a list of prompts</h2>
<dl>
  <dt><strong>They are scored, and the scoring is honest about itself</strong></dt>
  <dd>Ten criteria, 0&ndash;2 each. Six can be checked by machine and are; four need judgement
  and are labelled as such. The library averages {mean:.2f}/20 &mdash; and the
  <a href="{rel(0, 'scoring/')}">scoring page</a> explains at length why that number is weaker
  evidence than one person saying it worked.</dd>

  <dt><strong>They carry safety rules you would otherwise forget</strong></dt>
  <dd>Every prompt tells the model to stop if you paste real personal data, forbids invented
  facts, and gives a flagging convention &mdash; <code>[TBC]</code> for unverified,
  <code>[PROPOSED &mdash; VALIDATE]</code> for anything it made up itself.</dd>

  <dt><strong>They are stored as fields, not as text</strong></dt>
  <dd>Which is why any prompt can be rebuilt as CO-STAR, RISEN, TIDD-EC or six others, or
  turned into an agent skill &mdash; and why the site can tell you what each conversion
  <a href="{rel(0, 'frameworks/')}">costs you</a>.</dd>

  <dt><strong>They are organisation-neutral</strong></dt>
  <dd>No client names, no sector assumptions, no jurisdiction-specific rules. Two edits make
  them yours: add your organisation to the context, and swap each worked example for one from
  your own domain.</dd>
</dl>

<h2>Browse by delivery context</h2>
<ul class="cards">
{ctx_cards}
</ul>

<h2>Contribute</h2>
<p>Prompts are better when the people doing the work write them. The bar is 17/20 on the
rubric; below that you get the specific fixes back, not a rejection. Your name stays in the
prompt's author field &mdash; which travels with it into every converted framework and every
generated skill. <a href="{rel(0, 'contribute/')}">How to contribute</a>.</p>
"""
    return page(title="Business-analysis prompts you don't have to browse", depth=0,
                current="", description=f"{len(prompts)} scored business-analysis prompts "
                f"across {services} BA services, convertible into ten prompt frameworks or "
                "agent skills.", body=body)

def contribute_page() -> str:
    body = f"""
<h1>Contribute</h1>
<p class="lede">Prompts are better when written by the people doing the work. If you have one
that works, it can get in &mdash; and you keep the credit.</p>

<div class="panel">
  <h2>The bar is 17/20</h2>
  <p>That is the published threshold on the <a href="{rel(1, 'scoring/')}">rubric</a>, not a
  preference: below it, outputs are unreliable enough that sharing the prompt does more harm
  than good. A prompt under 17 is not rejected &mdash; it comes back with the specific fixes,
  and you keep authorship on the resubmission.</p>
</div>

{md_to_html(ROOT / "CONTRIBUTING.md", 1)}

<h2 id="field-reports">Field reports</h2>
<p>A rubric score says a prompt is <strong>well-formed</strong>. A field report says it
<strong>worked</strong>. The second is harder to get and worth more.</p>
{md_to_html(ROOT / "field-reports" / "README.md", 1)}
"""
    return page(title="Contribute", depth=1, current="contribute/",
                description="How to contribute a prompt, keep the credit, upvote others, "
                            "and report what happened when you used one.", body=body)

def about_page(prompts: list[dict]) -> str:
    from collections import Counter
    roles = Counter(p["role"] for p in prompts)
    scores = Counter((p.get("score") or {}).get("total") for p in prompts)
    mean = sum((p.get("score") or {}).get("total", 0) for p in prompts) / len(prompts)
    multimode = [p for p in prompts if len(p.get("modes") or []) > 1]

    body = f"""
<h1>About</h1>
<p class="lede">Where this library came from, what is in it, who wrote it, and what you may
do with it.</p>

<h2 id="provenance">Provenance</h2>
<p>The library originates from the <em>BA Services AI Prompt Library (CARE + G.E.T.) v1.0 &mdash;
Portable edition</em> by <a href="https://business-analyst.services">Business Analyst
Services</a>: 126 prompts across 42 level-3 BA services and six roles, each scored by its
author against the ten-criterion scorecard.</p>
<p>It is deliberately organisation-neutral &mdash; no client names, no sector framing, no
jurisdiction-specific legislation, and every worked example rewritten in a generic
case-management domain. Two edits make it yours: extend the context block with your own
organisation and sector, and replace each worked example with one from your own domain. The
example is the field that most shapes output quality.</p>

<h2 id="statistics">Statistics</h2>
{table(["Measure", "Value"], [
    ["Prompts", str(len(prompts))],
    ["BA services", str(len({p['service'] for p in prompts}))],
    ["Roles", str(len(roles))],
    ["Mean rubric score", f"{mean:.2f} / 20"],
    ["Prompt frameworks supported", str(len(FORMATS))],
    ["Multi-mode prompts awaiting decomposition",
     f"{len(multimode)} ({sum(len(p['modes']) for p in multimode)} candidate single-task units)"],
])}
{table(["Role", "Prompts"], [[e(k), str(v)] for k, v in sorted(roles.items())],
       "Prompts by role.")}
{table(["Score", "Prompts"], [[f"{k}/20", str(v)] for k, v in sorted(scores.items(), reverse=True)],
       "Score distribution. Paper scores skew high - the library was written against the "
       "rubric that scores it.")}

<h2 id="contributors">Contributors</h2>
{md_to_html(ROOT / "CONTRIBUTORS.md", 1)}

<h2 id="licence">Licence</h2>
<p>The prompts, rubric and documentation are licensed
<a href="https://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0</a>:
use them at work, adapt them, ship them inside a product &mdash; keep the attribution. Each
prompt names its own author in its provenance, and that is the attribution to keep.</p>
<p>The tooling that builds this site is MIT licensed. Everything is on
<a href="{REPO}">GitHub</a>.</p>

<h2 id="accessibility">Accessibility</h2>
<p>This site targets <strong>WCAG 2.1 level AA</strong>. In practice that means:</p>
<ul>
  <li>Every page works with JavaScript disabled &mdash; all prompt framework renderings are in
  the HTML, and script only hides, filters and copies.</li>
  <li>Colour pairs are contrast-tested at build time in both light and dark themes; the build
  fails if a pair drops below its threshold.</li>
  <li>Semantic landmarks, one <code>h1</code> per page, ordered headings, a skip link, and a
  visible focus ring on every interactive element.</li>
  <li>Framework tabs follow the ARIA tabs pattern with full arrow-key, Home and End support.
  Filter results are announced to screen readers.</li>
  <li>Tables carry header scope; form controls carry real labels; nothing relies on colour
  alone &mdash; score badges always carry their number.</li>
  <li>Content reflows to 320&nbsp;px, respects <code>prefers-reduced-motion</code>, and follows
  your system light or dark setting unless you override it.</li>
</ul>
<p>If something here is unusable for you, that is a bug and will be treated as one:
<a href="{REPO}/issues/new">open an issue</a>.</p>

<h2 id="further">Further reading</h2>
<ul>
  <li><a href="{rel(1, 'decomposition/')}">Decomposition</a> &mdash; why Master prompts cannot
  be tested, and the 188 single-task units that fix it.</li>
  <li><a href="{rel(1, 'roadmap/')}">Roadmap</a> &mdash; what is next, what is under
  consideration, and what is deliberately not planned.</li>
</ul>
"""
    return page(title="About", depth=1, current="about/",
                description="Provenance, statistics, contributors, licence and the "
                            "accessibility commitments of BA Prompt Forge.", body=body)

def simple_doc(source: Path, title: str, lede: str, slug: str) -> tuple[str, str]:
    body = f"<h1>{e(title)}</h1>\n<p class=\"lede\">{e(lede)}</p>\n" + md_to_html(source, 1)
    return f"{slug}/index.html", page(title=title, depth=1, current="about/",
                                      description=lede, body=body)

def not_found() -> str:
    body = f"""
<h1>That page doesn't exist</h1>
<p class="lede">The link may be out of date, or the prompt may have been renamed.</p>
<ul>
  <li><a href="{BASE}prompts/">Search all 126 prompts</a></li>
  <li><a href="{BASE}contexts/">Start from your delivery context</a></li>
  <li><a href="{BASE}">Go to the home page</a></li>
</ul>
"""
    return page(title="Page not found", depth=0, current="", absolute=True,
                description="Page not found.", body=body)

# --------------------------------------------------------------------------- #

def main(argv: list[str]) -> int:
    css = (ASSETS / "site.css").read_text(encoding="utf-8")
    problems = check_contrast(css)
    if problems:
        print("Contrast failures - fix site.css before shipping:", file=sys.stderr)
        for p in problems:
            print("  " + p, file=sys.stderr)
        return 1

    prompts = all_prompts()
    by_id = {p["id"]: p for p in prompts}
    contexts = yaml.safe_load(
        (ROOT / "contexts" / "delivery-contexts.yml").read_text(encoding="utf-8")
    )["contexts"]
    rubric = yaml.safe_load(
        (ROOT / "rubric" / "care-get-v1.yml").read_text(encoding="utf-8")
    )["rubric"]

    if SITE.exists():
        shutil.rmtree(SITE)
    (SITE / "assets").mkdir(parents=True)
    shutil.copy2(ASSETS / "site.css", SITE / "assets" / "site.css")
    shutil.copy2(ASSETS / "site.js", SITE / "assets" / "site.js")
    shutil.copy2(ROOT / "catalogue.json", SITE / "catalogue.json")
    (SITE / ".nojekyll").write_text("", encoding="utf-8")

    written = 0
    write("index.html", home_page(prompts, contexts)); written += 1
    write("prompts/index.html", prompts_index(prompts)); written += 1
    for p in prompts:
        write(f"prompts/{p['id']}.html", prompt_page(p)); written += 1
    write("contexts/index.html", contexts_page(contexts, by_id)); written += 1
    write("frameworks/index.html", frameworks_page(prompts)); written += 1
    write("scoring/index.html", scoring_page(rubric, prompts)); written += 1
    for path, content in skills_pages(prompts):
        write(path, content); written += 1
    write("contribute/index.html", contribute_page()); written += 1
    write("about/index.html", about_page(prompts)); written += 1
    for source, title, lede, slug in [
        (ROOT / "docs" / "decomposition.md", "Decomposition",
         "Why a multi-mode prompt cannot be tested, and the 188 single-task units that fix it.",
         "decomposition"),
        (ROOT / "docs" / "roadmap.md", "Roadmap",
         "What is shipped, what is next, and what is deliberately not planned.", "roadmap"),
    ]:
        path, content = simple_doc(source, title, lede, slug)
        write(path, content); written += 1
    write("404.html", not_found()); written += 1

    print(f"Built {written} pages into {SITE.relative_to(ROOT)}/ "
          f"(contrast: {len(CONTRAST_CHECKS) * 2} pairs checked, all pass)")

    if "--serve" in argv:
        import http.server, socketserver, functools
        handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(SITE))
        with socketserver.TCPServer(("", 8000), handler) as httpd:
            print("Serving at http://localhost:8000 - Ctrl+C to stop")
            httpd.serve_forever()
    return 0

if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
