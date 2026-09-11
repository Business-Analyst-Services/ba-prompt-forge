"""Build the site and publish it to the gh-pages branch.

GitHub Pages serves this repository from the `gh-pages` branch root, not from a
workflow, so publishing is a branch push rather than a deploy action. That needs
no extra token scopes and works from any clone.

    python tools/publish_site.py            # build, then show what would change
    python tools/publish_site.py --push     # build and publish

The built site is gitignored on `main`: it is output, and keeping it out of the
source branch means a stale build can never masquerade as the library.
"""
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib_ir import ROOT  # noqa: E402

BRANCH = "gh-pages"
LIVE = "https://business-analyst-services.github.io/ba-prompt-forge/"


def run(cmd: list[str], cwd: Path, check: bool = True) -> str:
    result = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    if check and result.returncode != 0:
        raise SystemExit(f"$ {' '.join(cmd)}\n{result.stdout}{result.stderr}")
    return result.stdout.strip()


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--push", action="store_true", help="actually publish")
    args = ap.parse_args()

    if subprocess.run([sys.executable, "tools/build_site.py"], cwd=ROOT).returncode:
        return 1

    site = ROOT / "site"
    if not (site / "index.html").exists():
        raise SystemExit("site/index.html missing - the build did not produce a site")

    remote = run(["git", "remote", "get-url", "origin"], ROOT)
    source_commit = run(["git", "rev-parse", "--short", "HEAD"], ROOT)

    with tempfile.TemporaryDirectory() as tmp:
        work = Path(tmp) / "pages"
        work.mkdir()
        run(["git", "init", "-q", "-b", BRANCH], work)
        run(["git", "remote", "add", "origin", remote], work)
        shutil.copytree(site, work, dirs_exist_ok=True)
        (work / ".gitattributes").write_text("* text=auto eol=lf\n", encoding="utf-8")

        run(["git", "add", "-A"], work)
        files = len(run(["git", "diff", "--cached", "--name-only"], work).splitlines())

        if not args.push:
            print(f"\nWould publish {files} files to {BRANCH} (built from {source_commit}).")
            print("Re-run with --push to publish.")
            return 0

        run(["git", "commit", "-q", "-m",
             f"Publish site\n\nBuilt from main@{source_commit} by tools/build_site.py."], work)
        run(["git", "push", "--force", "-q", "origin", BRANCH], work)

    print(f"\nPublished {files} files to {BRANCH} from main@{source_commit}.")
    print(f"Live within a minute or so at {LIVE}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
