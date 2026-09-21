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
    ("start/", "Start here"),
    ("prompts/", "Find a prompt"),
    ("contexts/", "By project type"),
    ("glossary/", "Glossary"),
    ("advanced/", "Advanced"),
    ("contribute/", "Contribute"),
    ("about/", "About"),
]

# The fastest path in: what a BA is actually trying to write, in their words,
# mapped to one prompt. Hand-curated - the catalogue's own 226 deliverable names
# are too many and still written in catalogue language.
QUICK_PICKS = [
    ("Acceptance criteria for a user story", "AB-03-D1"),
    ("Break an epic into user stories", "BT-02-D1"),
    ("A map of how a process works today", "BB-07-D1"),
    ("A redesigned process, and the gaps to get there", "BB-07-D2"),
    ("Turn messy workshop notes into business needs", "BB-02-D2"),
    ("A problem statement — what is actually wrong", "BB-03-D1"),
    ("Functional requirements for a feature", "BB-06-D1"),
    ("Non-functional requirements (performance, security)", "BB-06-D2"),
    ("KPIs that prove the benefits", "BB-01-D1"),
    ("A stakeholder register and engagement plan", "BT-08-D1"),
    ("UAT scenarios and test scripts", "BT-09-D1"),
    ("An options paper for a decision", "BB-08-D2"),
]

# Plain-English definitions. Every term Chale flagged as unexplained, plus the
# ones the library itself introduces. Definitions must not use jargon that is
# not itself defined here.
GLOSSARY = [
    ("ai-assistant", "AI assistant", [
        "A tool you type a question into and get written text back: Microsoft "
        "Copilot, ChatGPT, Claude or Google Gemini are the common ones. If your "
        "employer gives you one, it is probably Copilot.",
        "Everything on this site works with any of them. You do not need a "
        "special one, a subscription tier, or anything installed.",
    ]),
    ("prompt", "Prompt", [
        "The instructions you give an AI assistant. That is all a prompt is — "
        "text you paste into the box.",
        "A good prompt says who you are, what you want, what shape the answer "
        "should take, and what the assistant must not do. Writing all that out "
        "every time is tedious, which is why this site exists: the prompts here "
        "are already written.",
    ]),
    ("placeholder", "Placeholder", [
        "The bits in [SQUARE BRACKETS AND CAPITALS] that you replace with your "
        "own details before you send the prompt — your project name, the "
        "process you are mapping, the notes you are working from.",
        "If you do not know one, leave it and say so; the assistant will ask.",
    ]),
    ("first-draft", "First draft", [
        "What an AI assistant gives you back. It is a starting point to edit, "
        "not something to forward to your sponsor.",
        "Every prompt here says this to the assistant explicitly, so the output "
        "arrives labelled as a draft rather than dressed up as finished work.",
    ]),
    ("hallucination", "Made-up facts (hallucination)", [
        "AI assistants will invent plausible-sounding detail — a figure, a "
        "date, a standard, a citation — rather than admit they do not know. "
        "This is the single biggest risk in using them for BA work.",
        "Every prompt here forbids it and tells the assistant to mark anything "
        "it could not verify as [TBC], and anything it suggested itself as "
        "[PROPOSED — VALIDATE]. When you see those tags, that is the prompt "
        "working. Check them before the document goes anywhere.",
    ]),
    ("de-identified", "De-identified / synthetic data", [
        "De-identified means you removed the details that identify a real "
        "person or case before pasting: names, case numbers, addresses, dates "
        "of birth. Synthetic means you made the example up entirely.",
        "Every prompt here tells the assistant to stop and warn you if what you "
        "pasted looks like real personal data. Treat that as a backstop, not a "
        "substitute for checking first — and follow your own organisation's "
        "rules about what may go into an AI tool at all.",
    ]),
    ("deliverable-prompt", "Deliverable prompt", [
        "A prompt that produces one specific thing — a traceability matrix, "
        "a set of acceptance criteria, a stakeholder register.",
        "Most of the time this is what you want. 84 of the 126 prompts here are "
        "deliverable prompts.",
    ]),
    ("master-prompt", "Master prompt", [
        "A prompt that sets an assistant up to work with you across a whole "
        "area for a while, offering several things it can produce, rather than "
        "producing one artefact and stopping.",
        "Useful when you are working a topic through over an afternoon. If you "
        "just need one document, use a deliverable prompt instead.",
    ]),
    ("ba-service", "BA service", [
        "A named area of business-analysis work — 'Process Analysis & "
        "Improvement', 'Requirements Governance & Traceability'. This site "
        "covers 42 of them.",
        "It is how the prompts are filed. If the names mean nothing to you, "
        "ignore them and search by what you are writing instead.",
    ]),
    ("delivery-context", "Delivery context", [
        "The kind of project you are on: an agile delivery, a procurement, a "
        "data warehouse build, a go-live. There are eleven here.",
        "Useful when you know your project type but not which document you "
        "need yet.",
    ]),
    ("prompt-framework", "Prompt framework", [
        "A standard running order for the parts of a prompt — context first, "
        "then the task, then the output format, and so on. CARE, CO-STAR, "
        "RISEN, TIDD-EC, RACE, CRISPE, RTF, APE and BAB are all just different "
        "running orders, usually named after their initials.",
        "They matter to people building prompt tooling. As someone using a "
        "prompt, you can ignore them completely — the ready-to-use version "
        "on every prompt page is already in a good one.",
    ]),
    ("care-get", "CARE + G.E.T.", [
        "The framework these prompts are written in. CARE is Context, Action, "
        "Result/Format, Example. G.E.T. is what the prompt asks the assistant "
        "to do afterwards: Generate the answer, Explain how it reached it, and "
        "Test it by listing its sources and assumptions.",
        "That last part is the useful bit for BA work — it is what turns "
        "output you have to trust into output you can check.",
    ]),
    ("rubric", "Rubric / quality score", [
        "A checklist used to mark each prompt out of 20 against ten criteria: "
        "does it say who the audience is, does it give a worked example, does "
        "it forbid made-up facts, and so on.",
        "You do not need to care about the number. Everything published here "
        "scored 17 or higher, which is the bar for being published at all. The "
        "score is there so contributors know the standard and reviewers can "
        "apply it consistently.",
    ]),
    ("agent", "AI agent", [
        "An AI assistant that can take several steps on its own — read a "
        "file, decide what to do next, come back to you — rather than "
        "answering one question at a time.",
        "Nothing on this site requires one.",
    ]),
    ("agent-skill", "Agent skill", [
        "A file of instructions (named SKILL.md) that you give to an AI agent "
        "once, so it knows how to do a job properly every time you ask, without "
        "you pasting a prompt.",
        "Think of it as a prompt you install rather than paste. Optional — "
        "the copy-and-paste route works perfectly well.",
    ]),
    ("router-skill", "Router skill", [
        "One particular agent skill on this site. You tell it what you are "
        "working on in your own words — 'I need acceptance criteria a "
        "tester can actually work from' — and it picks the right prompt out "
        "of the 126, asks you for the details it needs, and hands back a "
        "finished prompt.",
        "It exists because 126 is too many to browse. It is a convenience, not "
        "a requirement.",
    ]),
    ("agentic-ai", "Agentic AI", [
        "A way of building systems where AI agents carry out multi-step tasks "
        "with some independence, rather than just answering questions.",
        "It appears on this site only as the name of one delivery context — "
        "for BAs whose project happens to be building such a system. It is not "
        "something you need to understand to use the prompts.",
    ]),
    ("rag", "RAG (retrieval-augmented generation)", [
        "A technique for making an AI assistant answer from a specific set of "
        "documents — your policies, your knowledge base — rather than "
        "from whatever it learned in training. The system looks up relevant "
        "documents first, then answers using them.",
        "Same as above: it appears here only because some BAs are asked to "
        "write requirements for systems that use it.",
    ]),
    ("grounding", "Grounding", [
        "Tying an AI assistant's answers to real, checkable sources so it is "
        "less free to invent. RAG is one way of doing it.",
    ]),
    ("bdd", "BDD / Gherkin / Given-When-Then", [
        "A way of writing acceptance criteria as concrete scenarios in a fixed "
        "shape: Given some starting situation, When someone does something, Then "
        "this should happen. Gherkin is the name of that shape; BDD "
        "(behaviour-driven development) is the practice of using it.",
        "It is popular because the same scenario is readable by a business "
        "stakeholder and usable by a tester.",
    ]),
    ("dor", "Definition of Ready / Definition of Done", [
        "Two checklists an agile team agrees between themselves. Definition of "
        "Ready is what a piece of work needs before the team will start it; "
        "Definition of Done is what it needs before they will call it finished.",
    ]),
    ("uat", "UAT (user acceptance testing)", [
        "The testing done by the people who will actually use a system, to "
        "confirm it does what the business needed — as opposed to testing "
        "that it works technically.",
    ]),
    ("babok", "BABOK", [
        "A Guide to the Business Analysis Body of Knowledge, published by IIBA. "
        "The reference text most BA practice is described against.",
        "Some prompts mention it so the assistant writes in a style a BA "
        "audience will recognise. You do not need a copy.",
    ]),
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

    # The ready-to-use build is shown on its own. Every other framework lives
    # behind a disclosure: those labels are jargon, and putting ten of them on
    # the first screen is what made this page unreadable for a new reader.
    main_prompt = render(p, "care")
    others = [(k, m["label"], render(p, k), fidelity(p, k))
              for k, m in FORMATS.items() if k != "care"]
    others.append(("skill", "Agent skill file", to_skill(p), None))

    panels, tabs = [], []
    for i, (key, label, text, fid) in enumerate(others):
        panel_id, tab_id, code_id = f"panel-{key}", f"tab-{key}", f"code-{key}"
        if fid:
            lost = ", ".join(fid["criteria_lost"])
            cost = (f"Scores {fid['converted_total']}/20 after conversion, losing: "
                    f"{e(lost)}." if lost else "Carries everything the original does.")
            note = f'<p class="muted">{e(FORMATS[key]["note"])} {cost}</p>'
        else:
            note = ('<p class="muted">The same prompt rebuilt as an '
                    f'<a href="{rel(1, "glossary/")}#agent-skill">agent skill</a> '
                    "file, so an AI agent can follow it without you pasting "
                    "anything. Save it as <code>SKILL.md</code>.</p>")
        tabs.append(
            f'<button type="button" role="tab" id="{tab_id}" aria-controls="{panel_id}" '
            f'aria-selected="{"true" if i == 0 else "false"}" '
            f'tabindex="{"0" if i == 0 else "-1"}">{e(label)}</button>'
        )
        panels.append(
            f'\n<div class="tabpanel" role="tabpanel" id="{panel_id}" '
            f'aria-labelledby="{tab_id}" tabindex="0">\n'
            f'  <h3 class="panel-heading">{e(label)}</h3>\n'
            f"  {note}\n"
            f'  <div class="copy-row">\n'
            f'    <button type="button" class="btn" data-copy="{code_id}"\n'
            f'            data-copy-status="copy-status-{key}" hidden>Copy this version</button>\n'
            f'    <span class="copy-status" id="copy-status-{key}" role="status" '
            f'aria-live="polite"></span>\n'
            f"  </div>\n"
            f'  <pre id="{code_id}"><code>{e(text)}</code></pre>\n'
            f"</div>"
        )

    inputs = "\n".join(f"<li><code>[{e(i)}]</code></li>" for i in p.get("inputs", [])) \
        or "<li>Nothing &mdash; this one works as it is.</li>"
    contexts = "\n".join(
        f'<li><a href="{rel(1, "contexts/")}'
        f'#{e(re.sub(r"[^a-z0-9]+", "-", c.lower()).strip("-"))}">{e(c)}</a></li>'
        for c in p.get("delivery_contexts", [])
    ) or "<li>Not mapped to a particular project type.</li>"

    score_rows = [[e(label), str((p.get("score") or {}).get(key, "&ndash;")),
                   "Checked automatically" if key in {
                       "c4_example", "c5_explain", "c6_test", "c7_anti_fabrication",
                       "c8_data_safety", "c9_reusability"} else "Human judgement"]
                  for key, label in CRITERIA]
    notes = (p.get("score") or {}).get("notes")
    prov = p.get("provenance") or {}
    deliverables = ", ".join(p.get("deliverables", []))

    kind = (
        "Produces one document and stops."
        if p["type"] == "deliverable" else
        "Sets the assistant up to work with you across this whole area, offering "
        "several things it can produce. If you only need one document, use a "
        "deliverable prompt instead."
    )
    verdict = (p.get("score") or {}).get("verdict", "")

    body = f"""
<p class="muted"><a href="{rel(1, 'prompts/')}">&larr; All prompts</a></p>
<h1>{e(p['name'])}</h1>

<p class="lede">{e(p['task'])}</p>

<p class="meta">
  <span><strong>Writes:</strong> {e(deliverables or p['service'])}</span>
  <span><strong>For:</strong> {e(p['audience'])}</span>
</p>
<p class="muted small">{e(kind)} Filed under
<a href="{rel(1, 'glossary/')}#ba-service">{e(p['service'])}</a> for a
{e(p['role'])}. Reference <code>{e(pid)}</code>.
<a href="#quality">Quality score {e(total)}/20</a>.</p>

<h2 id="ready">1. Have these ready</h2>
<p>You will replace each of these in the prompt below:</p>
<ul>
{inputs}
</ul>
<p>Do not know one? Leave it as it is and say so &mdash; the assistant will ask.</p>

<div class="panel">
  <h3>Before you paste anything in</h3>
  <p>{e(p['data_safety'])}</p>
  <p class="small">In short: take out real names, case numbers and anything else
  identifying, or make up an example instead. See
  <a href="{rel(1, 'glossary/')}#de-identified">de-identified data</a>.</p>
</div>

<h2 id="prompt">2. Copy the prompt</h2>
<div class="copy-row">
  <button type="button" class="btn" data-copy="code-main"
          data-copy-status="copy-status-main" hidden>Copy the prompt</button>
  <span class="copy-status" id="copy-status-main" role="status" aria-live="polite"></span>
</div>
<pre id="code-main"><code>{e(main_prompt)}</code></pre>

<h2 id="next">3. Paste it into your AI assistant</h2>
<p>Copilot, ChatGPT, Claude or Gemini &mdash; any of them. Here is what should
happen:</p>
<ol>
  <li><strong>It asks you questions first</strong> (up to {p.get('clarifiers', 5)}).
  Answer them &mdash; this is what makes the draft about your project rather than
  a generic one.</li>
  <li><strong>It writes the document</strong> in the structure the prompt asked for.</li>
  <li><strong>It explains how it got there</strong> and lists the assumptions it
  made, so you can check its reasoning and not just its output.</li>
</ol>
<p>Anything tagged <code>[TBC]</code> it could not verify. Anything tagged
<code>[PROPOSED &mdash; VALIDATE]</code> it suggested itself.
<strong>Those tags are your to-do list.</strong> Treat the whole thing as a first
draft and read every line before it goes to anyone.</p>

<details class="advanced">
  <summary>Other formats of this prompt (optional)</summary>
  <p>The version above is ready to use and works everywhere. These are the same
  prompt written in other
  <a href="{rel(1, 'glossary/')}#prompt-framework">prompt frameworks</a>, for people
  whose tooling or house standard expects one &mdash; plus an
  <a href="{rel(1, 'glossary/')}#agent-skill">agent skill</a> version. Several drop
  parts of the original, and each one says what it loses.</p>
  <div class="tabs full">
    <div class="tablist" role="tablist" aria-label="Other prompt formats">
      {''.join(tabs)}
    </div>
    {''.join(panels)}
  </div>
</details>

<details class="advanced" id="quality">
  <summary>Quality score: {e(total)}/20 &mdash; {e(verdict)}</summary>
  <p>Every prompt here is marked against
  <a href="{rel(1, 'scoring/')}">ten criteria</a> before publication, and 17 out of
  20 is the minimum to be published at all. You do not need to care about the
  number &mdash; it exists so contributors know the standard.</p>
  {table(["Criterion", "Mark", "Decided by"], score_rows,
         "Marks out of 2 against the ten-criterion quality standard.")}
  {('<p>' + e(notes) + '</p>') if notes else ''}
  <p class="muted">A high score means the prompt is well built, not that it worked.
  If you use it for real, <a href="{rel(1, 'contribute/')}#field-reports">tell us
  what happened</a> &mdash; that is worth more than the score.</p>
</details>

<h2 id="contexts">Used on these kinds of project</h2>
<ul>
{contexts}
</ul>

<h2 id="provenance">Who wrote it</h2>
<ul>
  <li><strong>Author:</strong> {e(prov.get('author', 'Unknown'))}</li>
  <li><strong>Added:</strong> {e(prov.get('added', '&ndash;'))}</li>
  <li><strong>Licence:</strong> {e(prov.get('license', 'CC-BY-4.0'))} &mdash; use it
  at work, adapt it, keep the attribution.</li>
</ul>
<p>Improved it, or found that it did not work?
<a href="{rel(1, 'contribute/')}">Send it back</a> &mdash; you keep the credit.</p>
"""
    return page(title=p["name"], depth=1, current="prompts/",
                description=f"A ready-to-use AI prompt that writes: "
                            f"{deliverables or p['service']}. Copy it into Copilot, "
                            "ChatGPT or Claude.", body=body)


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
<p class="lede">Each prompt writes one thing. Search for what you need to
produce &mdash; &ldquo;acceptance criteria&rdquo;, &ldquo;process map&rdquo;,
&ldquo;business case&rdquo;, &ldquo;test scripts&rdquo;.</p>

<p>Once you have found one: copy it, replace the bits in [SQUARE BRACKETS] with
your own details, and paste it into Copilot, ChatGPT or Claude. New to this?
<a href="{rel(1, 'start/')}">Start here</a> first.</p>

<details class="advanced">
  <summary>What do &ldquo;Master&rdquo; and &ldquo;Deliverable&rdquo; mean in the table?</summary>
  <p><strong>Deliverable</strong> prompts produce one document and stop. That is
  almost always what you want, and 84 of the 126 are this kind.</p>
  <p><strong>Master</strong> prompts set the assistant up to work with you across a
  whole area of BA work over a longer session, offering several things it can
  produce rather than just one.</p>
  <p><strong>Area of work</strong> is how the prompts are filed &mdash; 42 named
  areas of business analysis. If the names mean nothing to you, ignore that column
  and search by what you are writing instead.</p>
</details>

<form class="filters full" role="search" aria-label="Filter prompts"
      onsubmit="return false;">
  <div class="field">
    <label for="filter-search">Search</label>
    <input type="search" id="filter-search" autocomplete="off"
           placeholder="acceptance criteria, process map, test scripts&hellip;">
  </div>
  <div class="field">
    <label for="filter-role">Your BA role</label>
    <select id="filter-role" data-filter="role"><option value="">All roles</option>{options(roles)}</select>
  </div>
  <div class="field">
    <label for="filter-type">Prompt type</label>
    <select id="filter-type" data-filter="type"><option value="">All types</option>{options(types)}</select>
  </div>
  <div class="field">
    <label for="filter-service">Area of work</label>
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
  <caption>Every prompt, with the role it suits, what kind it is, its area of work and its quality score.</caption>
  <thead><tr>
    <th scope="col">Prompt</th><th scope="col">Role</th><th scope="col">Type</th>
    <th scope="col">Area of work</th><th scope="col">Score</th>
  </tr></thead>
  <tbody>
{''.join(rows)}
  </tbody>
</table>
</div>

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
<h1>Find prompts by project type</h1>
<p class="lede">Know what kind of project you are on, but not which document you
need yet? Start from your project type and see the prompts BAs use most on it.</p>

<p>If you already know what you need to write,
<a href="{rel(1, 'prompts/')}">searching the prompts</a> is faster.</p>

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
    return page(title="Find prompts by project type", depth=1, current="contexts/",
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
<p class="lede">You can ignore this page. The ready-to-use version on every prompt
page already works in Copilot, ChatGPT and Claude &mdash; this is for people whose
tooling or house standard expects a particular format.</p>

<div class="panel">
  <p>A <a href="{rel(1, 'glossary/')}#prompt-framework">prompt framework</a> is just
  a standard running order for the parts of a prompt: context first, then the task,
  then the required output, and so on. CARE, CO-STAR, RISEN and the rest are
  different running orders, named after their initials. None of them is magic and
  the differences rarely matter to someone simply using a prompt.</p>
</div>

<p>This library is written in
<a href="{rel(1, 'glossary/')}#care-get">CARE + G.E.T.</a>, but that is a storage
decision, not a commitment: every prompt can be re-rendered in any of ten
frameworks, or as an agent skill.</p>

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
    return page(title="Prompt frameworks", depth=1, current="advanced/",
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
<h1>How prompts are quality checked</h1>
<p class="lede">Short answer: you can ignore the scores. Everything published here
passed the bar, and the number exists so contributors know the standard and
reviewers apply it consistently.</p>

<div class="panel">
  <h2>Why bother scoring prompts at all?</h2>
  <p>Because the difference between a prompt that gives you a usable draft and one
  that gives you confident nonsense is not obvious by reading it. The checklist below
  is the set of things that turned out to matter &mdash; does the prompt say who the
  audience is, does it give the assistant a worked example to copy, does it forbid
  made-up facts, does it stop you pasting real personal data.</p>
  <p>Every prompt on this site scored at least 17 out of 20 against it. That is the
  publication bar, not an aspiration.</p>
</div>

<p>What follows is the detail: the ten criteria, what a machine can and cannot
judge, and why a high score is weaker evidence than one person saying a prompt
actually worked.</p>

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
    return page(title="How prompts are quality checked", depth=1, current="advanced/",
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
                      page(title=title, depth=1, current="advanced/",
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
<h1>Use the library with an AI agent</h1>
<p class="lede">Optional, and for a narrower audience. Copying and pasting a prompt
works perfectly well &mdash; this page is for people who would rather install the
library once than search it each time.</p>

<div class="panel">
  <p>An <a href="{rel(1, 'glossary/')}#agent-skill">agent skill</a> is a file of
  instructions, named <code>SKILL.md</code>, that you hand to an AI assistant that
  supports them (Claude Code and Claude Desktop, among others). After that, the
  assistant knows how to do the job without you pasting anything.</p>
  <p>If your AI assistant is Microsoft Copilot or ChatGPT, this will not apply to
  you &mdash; <a href="{rel(1, 'prompts/')}">use the prompts directly</a> instead.</p>
</div>

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
                  page(title="Use the library with an AI agent", depth=1, current="advanced/",
                       description="Agent skills that route, score and author BA prompts, "
                                   "plus all 126 prompts as standalone skills.",
                       body=index_body)))
    return pages

def glossary_page() -> str:
    items = "\n".join(
        f'<h2 id="{e(slug)}">{e(term)}</h2>\n'
        + "\n".join(f"<p>{body}</p>" for body in paras)
        for slug, term, paras in GLOSSARY
    )
    toc = "\n".join(f'<li><a href="#{e(s)}">{e(t)}</a></li>' for s, t, _ in GLOSSARY)
    body = f"""
<h1>Glossary</h1>
<p class="lede">Every term this site uses, in plain English. If something here is
still unclear, that is a fault in the writing &mdash; please
<a href="{REPO}/issues/new">tell us</a>.</p>

<div class="panel">
  <p><strong>The short version:</strong> a <a href="#prompt">prompt</a> is text you
  paste into an <a href="#ai-assistant">AI assistant</a> like Copilot or ChatGPT.
  This site has 126 of them, already written, for documents business analysts
  produce. Everything else on this page is optional detail.</p>
</div>

<nav aria-labelledby="terms-heading">
  <h2 id="terms-heading">Terms</h2>
  <ul>
{toc}
  </ul>
</nav>

{items}
"""
    return page(title="Glossary", depth=1, current="glossary/",
                description="Plain-English definitions of every term used on this "
                            "site: prompt, AI assistant, agent skill, rubric, RAG and "
                            "the rest.", body=body)


def start_page(prompts: list[dict]) -> str:
    example = next((p for p in prompts if p["id"] == "BB-07-D1"), prompts[0])
    picks = "\n".join(
        f'<li><a href="{rel(1, "prompts/")}{e(pid)}.html">{e(label)}</a></li>'
        for label, pid in QUICK_PICKS[:6]
    )
    body = f"""
<h1>Start here</h1>
<p class="lede">If you have never used an AI assistant for work, this page is the
whole thing in about five minutes. No jargon, no setup, nothing to install.</p>

<h2>What this site is</h2>
<p>Business analysts write a lot of the same documents: requirements, acceptance
criteria, process maps, stakeholder registers, business cases. An AI assistant can
give you a decent first draft of any of them &mdash; but only if you ask well, and
asking well takes a page of careful instructions.</p>
<p><strong>This site is those instructions, already written.</strong> 126 of them,
one for each kind of document. You copy one, fill in a few blanks, paste it in, and
edit what comes back.</p>

<h2>What you need</h2>
<p>An <a href="{rel(1, 'glossary/')}#ai-assistant">AI assistant</a> &mdash; Microsoft
Copilot, ChatGPT, Claude or Google Gemini. If your employer provides one, it is
most likely Copilot. Any of them works; you do not need a paid tier.</p>
<p>Check your organisation's rules on using AI at work before you start, especially
about what information may go into one.</p>

<h2>Use it in three steps</h2>
<ol class="steps">
  <li>
    <h3>1. Find the thing you need to write</h3>
    <p>Start with <a href="{rel(1, 'prompts/')}">Find a prompt</a> and search for
    what you are producing &mdash; &ldquo;acceptance criteria&rdquo;, &ldquo;process
    map&rdquo;, &ldquo;business case&rdquo;. Or pick one of these common ones:</p>
    <ul>
{picks}
    </ul>
  </li>
  <li>
    <h3>2. Copy the prompt</h3>
    <p>Every prompt page has the full text and a <strong>Copy</strong> button. Before
    you paste it anywhere, replace the bits in
    <a href="{rel(1, 'glossary/')}#placeholder">[SQUARE BRACKETS]</a> with your own
    details. They are listed at the top of each page so you know what to have ready.</p>
    <p>Do not know one of them? Leave it as it is and say so &mdash; the assistant
    will ask you about it.</p>
  </li>
  <li>
    <h3>3. Paste it into your AI assistant</h3>
    <p>Paste the whole thing into the message box and send it. <strong>It will ask
    you questions before it writes anything</strong> &mdash; usually up to five. That
    is deliberate: answering them is what makes the draft useful rather than generic.</p>
    <p>Then it produces the document, explains how it put it together, and lists the
    assumptions it made.</p>
  </li>
</ol>

<h2>A worked example</h2>
<p>Say you need to document how a process works today. You open
<a href="{rel(1, 'prompts/')}{e(example['id'])}.html">{e(example['name'])}</a> and
see it needs two things from you: your project name, and a description of the
process. You paste the prompt with those filled in.</p>
<p>The assistant asks you a few questions &mdash; who performs each step, where the
process starts and stops, what the exceptions are. You answer. It gives you back a
structured process map you can put into your own template and take to a workshop.</p>

<h2>Three things to know before you trust the output</h2>
<div class="panel">
  <h3>It is a first draft, not a deliverable</h3>
  <p>Read every line before it goes anywhere near a stakeholder. The prompts tell the
  assistant to say so itself, but the judgement is yours.</p>
</div>
<div class="panel">
  <h3>It will make things up unless you stop it</h3>
  <p>AI assistants invent plausible detail &mdash; figures, dates, standards &mdash;
  rather than say they do not know. Every prompt here forbids that and makes the
  assistant tag anything unverified as <code>[TBC]</code> and anything it suggested
  itself as <code>[PROPOSED &mdash; VALIDATE]</code>.
  <strong>Those tags are your to-do list.</strong></p>
</div>
<div class="panel">
  <h3>Do not paste real personal or sensitive data</h3>
  <p>Take out names, case numbers, addresses and anything else that identifies a real
  person or matter, or make up an example instead. Every prompt tells the assistant to
  stop and warn you if it spots real data &mdash; but that is a backstop, not a
  substitute for checking.</p>
</div>

<h2>That is genuinely it</h2>
<p>You now know everything you need. <a href="{rel(1, 'prompts/')}">Find a prompt</a>
and try one.</p>
<p>If a word anywhere on this site is unfamiliar, the
<a href="{rel(1, 'glossary/')}">glossary</a> defines all of them. There is also an
<a href="{rel(1, 'advanced/')}">advanced section</a> for people building tooling on
top of this &mdash; you can ignore it entirely.</p>
"""
    return page(title="Start here", depth=1, current="start/",
                description="New to using AI at work? The whole thing in five "
                            "minutes: what you need, how to use a prompt, and what "
                            "to check before you trust the output.", body=body)


def advanced_page(prompts: list[dict]) -> str:
    body = f"""
<h1>Advanced</h1>
<p class="lede">Everything on this page is optional. If you came here to get a
document written, you do not need any of it &mdash;
<a href="{rel(1, 'prompts/')}">find a prompt</a> instead.</p>

<p>This section is for people who want to build on the library rather than just use
it: integrate it into tooling, re-render the prompts in a different format, apply the
quality standard to their own prompts, or contribute.</p>

<ul class="cards">
  <li class="card">
    <h2><a href="{rel(1, 'skills/')}">Use it with an AI agent</a></h2>
    <p>Install the library as <a href="{rel(1, 'glossary/')}#agent-skill">agent
    skills</a> so an assistant picks and fills the right prompt for you, instead of
    you copying and pasting.</p>
  </li>
  <li class="card">
    <h2><a href="{rel(1, 'frameworks/')}">Other prompt formats</a></h2>
    <p>Every prompt can be re-rendered in nine other
    <a href="{rel(1, 'glossary/')}#prompt-framework">prompt frameworks</a> &mdash;
    CO-STAR, RISEN, TIDD-EC and the rest &mdash; and the site reports what each
    conversion costs.</p>
  </li>
  <li class="card">
    <h2><a href="{rel(1, 'scoring/')}">The quality standard</a></h2>
    <p>The ten-criterion <a href="{rel(1, 'glossary/')}#rubric">rubric</a> every
    prompt is marked against, what a machine can and cannot judge, and why a high
    score is weaker evidence than one person saying it worked.</p>
  </li>
  <li class="card">
    <h2><a href="{rel(1, 'decomposition/')}">Testable prompt units</a></h2>
    <p>Why a prompt that offers several options cannot carry a regression test, and
    the 188 single-task units generated to fix that.</p>
  </li>
  <li class="card">
    <h2><a href="{rel(1, 'roadmap/')}">Roadmap</a></h2>
    <p>What is next, what is under consideration, and what is deliberately not
    planned.</p>
  </li>
  <li class="card">
    <h2><a href="{rel(1, 'catalogue.json')}">catalogue.json</a></h2>
    <p>The whole library as machine-readable data &mdash; every prompt with its
    identifier, area of work, target documents and score. Start here if you are
    building something on top.</p>
  </li>
</ul>

<h2>How the library is put together</h2>
<p>Each prompt is stored as <strong>separate fields</strong> &mdash; who is writing,
who the audience is, the one task, the required output structure, the rules, the
worked example &mdash; rather than as one block of text.</p>
<p>That is the decision everything else rests on. A block of text cannot be
re-rendered in another framework, marked criterion by criterion, compared in a pull
request, or converted into an agent skill. A set of fields can.</p>
<p>The source, the tooling that builds this site, and the full contribution process
are on <a href="{REPO}">GitHub</a>.</p>
"""
    return page(title="Advanced", depth=1, current="advanced/",
                description="Optional material for people building on the library: "
                            "agent skills, other prompt frameworks, the quality "
                            "standard, and the data.", body=body)


def home_page(prompts: list[dict], contexts: list[dict]) -> str:
    services = len({p["service"] for p in prompts})
    by_id = {p["id"]: p for p in prompts}

    picks = "\n".join(f"""<li class="card">
  <h3><a href="{rel(0, 'prompts/')}{e(pid)}.html">{e(label)}</a></h3>
  <p>{e(by_id[pid]['name'] if pid in by_id else '')}</p>
</li>""" for label, pid in QUICK_PICKS if pid in by_id)

    ctx_links = "\n".join(
        f"""<li><a href="{rel(0, 'contexts/')}#{re.sub(r'[^a-z0-9]+', '-', f"{c['id']}. {c['name']}".lower()).strip('-')}">{e(c['name'])}</a></li>"""
        for c in contexts
    )

    body = f"""
<h1>AI prompts for business analysts</h1>
<p class="lede">Ready-to-use prompts for the documents you already write &mdash;
requirements, acceptance criteria, process maps, business cases, test scripts.
Copy one, paste it into Copilot or ChatGPT, and edit the draft it gives you back.</p>

<p>Free, and free to adapt. {len(prompts)} prompts covering {services} areas of
business-analysis work. Nothing to install and no account needed.</p>

<h2>Use it in three steps</h2>
<ol class="steps">
  <li>
    <h3>1. Find the thing you need to write</h3>
    <p>Pick it from the list below, or
    <a href="{rel(0, 'prompts/')}">search all {len(prompts)} prompts</a>.</p>
  </li>
  <li>
    <h3>2. Copy the prompt</h3>
    <p>Replace the few bits in [SQUARE BRACKETS] with your own details. Each page
    lists exactly what to have ready.</p>
  </li>
  <li>
    <h3>3. Paste it into Copilot, ChatGPT or Claude</h3>
    <p>It asks you a handful of questions first, then writes the draft. Edit it
    like you would anyone else's first draft.</p>
  </li>
</ol>

<h2 id="what-are-you-writing">What are you writing today?</h2>
<ul class="cards">
{picks}
</ul>
<p><a href="{rel(0, 'prompts/')}">See all {len(prompts)} prompts</a>, or browse by
what kind of project you are on:</p>
<ul class="inline-list">
{ctx_links}
</ul>

<div class="panel">
  <h2>New to using AI at work?</h2>
  <p>You do not need to know anything about AI to use this. The
  <a href="{rel(0, 'start/')}">Start here</a> page covers the whole thing in about
  five minutes: what you need, how to use a prompt, and what to check before you
  trust what comes back.</p>
</div>

<h2>What you get that a blank chat box does not</h2>
<dl>
  <dt><strong>It asks before it writes</strong></dt>
  <dd>Every prompt makes the assistant ask you up to five questions first. That is
  the difference between a generic answer and one about your project.</dd>

  <dt><strong>It flags what it made up</strong></dt>
  <dd>AI assistants invent figures, dates and standards rather than admit they do
  not know. These prompts forbid that, and make the assistant tag anything
  unverified as <code>[TBC]</code> and anything it suggested itself as
  <code>[PROPOSED &mdash; VALIDATE]</code>. Those tags become your checklist.</dd>

  <dt><strong>It tells you where the answer came from</strong></dt>
  <dd>Each prompt ends by asking the assistant to explain how it reached its answer
  and list every assumption it made, so you can check it rather than trust it.</dd>

  <dt><strong>It reminds you about sensitive data</strong></dt>
  <dd>Each prompt tells the assistant to stop and warn you if what you pasted looks
  like real personal information.</dd>

  <dt><strong>The output has a shape you can check</strong></dt>
  <dd>Prompts specify the actual structure &mdash; named sections, table columns,
  how many test cases of each kind &mdash; so you can hold the draft up against
  what you asked for.</dd>
</dl>

<h2>Where these came from</h2>
<p>They were written by a working BA practice for its own use, then made
organisation-neutral so anyone can adopt them: no client names, no sector
assumptions, no country-specific rules. Every prompt was reviewed against a
published quality standard before it was published here.</p>
<p>Two edits make them yours: add your organisation and sector to the context
section, and swap each worked example for one from your own domain. The example is
the part that most changes the quality of what you get back.</p>

<h2>Help make them better</h2>
<p>If you write a prompt that works, or find that one of these does not, both are
worth more than anything else here. Contributors keep their name on their prompts.
<a href="{rel(0, 'contribute/')}">How to contribute</a>.</p>

<p class="muted">Building tooling on top of this library, or want the quality
standard and the other prompt formats? That is all in
<a href="{rel(0, 'advanced/')}">Advanced</a>.</p>
"""
    return page(title="AI prompts for business analysts", depth=0, current="",
                description=f"{len(prompts)} free, ready-to-use AI prompts for the "
                "documents business analysts write: requirements, acceptance "
                "criteria, process maps, business cases and more.", body=body)


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
    write("start/index.html", start_page(prompts)); written += 1
    write("glossary/index.html", glossary_page()); written += 1
    write("advanced/index.html", advanced_page(prompts)); written += 1
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
