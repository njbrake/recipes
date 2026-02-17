# AGENTS.md

This file provides guidance to AI coding agents when working with code in this repository.

> **Note:** `CLAUDE.md` is a symlink pointing to this file. Do not edit `CLAUDE.md` directly — edit `AGENTS.md` instead.

## Project Overview

This is the Brake Family Recipes repository - a personal recipe collection containing 90+ recipes organized as Markdown files. The repository uses a structured format with YAML front matter and automated testing to ensure recipe completeness.

## Recipe Format Requirements

Every recipe must be a Markdown file with:

**YAML Front Matter** (required fields):
```yaml
---
meal_type: dinner | breakfast | side | dessert
cooking_method: ['stovetop'] | ['oven'] | ['slow-cooker'] | ['grill'] | etc.
difficulty: easy | medium | hard
title: Recipe Name
dates_made: [YYYY-MM-DD, ...]
prep_time: <minutes>
cook_time: <minutes>
servings: <number>
dietary: ['vegetarian'] | ['gluten-free'] | etc. (optional)
---
```

**Required Sections** (validated by tests):
- `## Ingredients` - ingredient list
- `## Instructions` - step-by-step instructions
- `## Notes` - optional section for tips and source attribution

The test suite (`tests/test_recipes.py`) validates required sections using regex: `^\s*##\s+Ingredients\b` and `^\s*##\s+Instructions\b`.

**File naming convention**: `snake_case.md` (e.g., `beef_kofta_meatballs.md`)

## Directory Structure

```
recipes/
├── breakfast/
├── desserts/
├── dinner/
│   ├── beef-pork/
│   ├── chicken/      (largest category)
│   ├── one-pot/
│   ├── pizza/
│   ├── seafood/
│   └── vegetarian/
└── sides/
```

## Development Commands

This project uses **uv** (not pip) for package management:

```bash
# Install dependencies
uv sync

# Run tests (validates recipe completeness)
uv run pytest

# Run tests with verbose output
uv run pytest -v

# Run a single test
uv run pytest tests/test_recipes.py::test_recipes_markdown -v
```

## Architecture Notes

- **File-based database**: Each recipe is a standalone markdown file
- **Convention enforcement**: Test suite ensures all recipes have required sections and proper formatting
- **Python 3.12** specified in `.python-version`
- **CI/CD**: GitHub Actions runs tests on every push to main branch (`.github/workflows/tests.yml`)
- **Meal planning**: `meals.md` contains weekly meal schedules with recipe links

## Code Style

- Python 3.12+ with `from __future__ import annotations` for forward references
- Use `pathlib.Path` for path handling; UTF-8 encoding for all file operations
- Type hints on all public functions; descriptive assertion messages including file paths
- Follow existing patterns in `tests/test_recipes.py` for consistency
