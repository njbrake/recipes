
from __future__ import annotations

import re
from pathlib import Path


INGREDIENTS_RE = re.compile(r"(?m)^\s*##\s+Ingredients\b")
INSTRUCTIONS_RE = re.compile(r"(?m)^\s*##\s+Instructions\b")


def collect_markdown_files(base_dir: Path) -> list[Path]:
    return [p for p in base_dir.rglob("*.md") if p.is_file()]


def file_has_required_sections(path: Path) -> tuple[bool, list[str]]:
    text = path.read_text(encoding="utf-8")
    missing: list[str] = []
    if not INGREDIENTS_RE.search(text):
        missing.append("Ingredients")
    if not INSTRUCTIONS_RE.search(text):
        missing.append("Instructions")
    return (len(missing) == 0, missing)


def test_recipes_markdown() -> None:
    root = Path(__file__).resolve().parent.parent / "recipes"
    assert root.exists(), f"Path not found: {root}"

    md_files = collect_markdown_files(root)
    assert md_files, f"No markdown files found under {root}"

    failures: list[tuple[Path, list[str]]] = []
    for md in sorted(md_files):
        ok, missing = file_has_required_sections(md)
        if not ok:
            failures.append((md, missing))

    if failures:
        details = "\n".join(
            f"- {path.relative_to(root)}: missing {', '.join(missing)}" for path, missing in failures
        )
        raise AssertionError(f"Missing required sections:\n{details}")


