# AGENTS.md

Repository operating guide for coding agents in `ssl-website`.

## 1) Project Overview

- Project type: Sphinx documentation website (Python)
- Dependency manager: `uv`
- Python version target: `3.14` (`.python-version`)
- Source directory: `src/`
- Build output directory: `build/`
- Main Sphinx config: `src/conf.py`
- CI workflow: `.github/workflows/build.yml`

## 2) Rule Files (Cursor / Copilot)

Checked paths:

- `.cursor/rules/` -> not present
- `.cursorrules` -> not present
- `.github/copilot-instructions.md` -> not present

If these files are added later, treat them as higher-priority instructions and
update this document.

## 2.1) Recommended Agent Model

- Recommended model for agentic edits in this repo: `GPT-5.3-Codex`
- Preferred access path: GitHub Copilot

## 3) Environment Setup

Preferred setup:

```bash
uv sync
```

Make helper:

```bash
make create-dev
```

Notes:

- `make create-dev` runs `uv sync` and `uv build`
- Prefer `uv run <command>` for tools inside the managed environment

## 4) Build / Lint / Test Commands

There is no dedicated lint/test framework configured in repo config files
(no project-level `pytest`, `ruff`, `mypy`, `black`, `flake8`, or `pylint`
configuration detected).
The Sphinx build is the effective validation gate.

Build site:

```bash
make build-proj
```

Equivalent direct command:

```bash
uv run sphinx-build -vvv --write-all --fresh-env src build
```

Local live preview:

```bash
make serve-site
```

Equivalent direct command:

```bash
uv run sphinx-autobuild src build
```

Strict docs validation (recommended before PR):

```bash
uv run sphinx-build -n -W --keep-going --write-all src build
```

Link validation (recommended when URLs change):

```bash
uv run sphinx-build -b linkcheck src build/linkcheck
```

## 5) Single-Test / Targeted Validation

There is currently no unit-test suite, so no true single-test command exists.
Use targeted checks instead:

1. Run strict Sphinx build
1. Verify only the changed pages in `build/`
1. Run linkcheck if links were added/updated

If `pytest` is introduced later, use this single-test pattern:

```bash
uv run pytest tests/path/test_file.py::test_name
```

## 6) Repository Layout Conventions

- Keep documentation source under `src/`
- Keep generated artifacts under `build/` only
- Keep reusable profile snippets in `src/_static/*.rst`
- Keep style overrides in `src/_static/custom.css`
- Keep publication pages in `src/publications/`

## 7) Python Style Guidelines

Applies to `src/conf.py` and any new Python code.

- Follow PEP 8 with 4-space indentation
- Use explicit imports; avoid wildcard imports
- Group imports: standard library, third-party, local
- Remove unused imports
- Use `snake_case` for functions/variables/modules
- Use `UPPER_SNAKE_CASE` for constants
- Prefer descriptive names over abbreviations
- Add type hints for new code when practical
- Keep functions focused and side effects explicit

## 8) Error Handling Guidelines

- Fail early with clear, actionable messages
- Raise specific exceptions
- Avoid broad `except Exception` unless re-raising/context wrapping
- Do not silently swallow exceptions
- Validate paths and required keys before processing
- Preserve root cause on re-raise (`raise ... from err`)

## 9) RST and Sphinx Style

- Preserve existing heading hierarchy/adornment style per file
- Keep prose concise, factual, and non-redundant
- Keep line wrapping readable and consistent
- Reuse directives already used in this repo (`grid`, `include`, admonitions)
- Keep include boundaries exact for `:start-after:` and `:end-before:`
- Do not rename sentinel markers in `_static/*.rst` casually
- Avoid broad rewrites unless explicitly requested

## 10) Imports, Formatting, Naming Expectations

- Match surrounding quote and formatting style in touched files
- Avoid formatting-only churn in unrelated sections
- Keep names and capitalization consistent with existing member entries
- Preserve existing Unicode names where already present
- Keep changes small, localized, and reviewable

## 11) CSS / Frontend Guidance

- Make scoped edits in `src/_static/custom.css`
- Prefer extending existing styles over global overrides
- Avoid changes that can destabilize Sphinx Book Theme defaults
- Validate rendering on desktop and mobile

## 12) CI Compatibility

Current workflow behavior:

1. Setup Python (workflow currently uses 3.13)
1. Install `uv` and run `uv sync`
1. Build docs with `sphinx-build --write-all src build`
1. Publish built site

Agent changes should remain compatible with this flow.

## 13) Pre-PR Checklist

- Run `uv sync` if dependencies/config changed
- Run strict docs build
- Run linkcheck for URL changes
- Verify changed pages render correctly
- Confirm include slices still resolve
- Keep commit/PR message focused on why

## 14) Do Not Assume

- Do not assume `pytest` exists today
- Do not assume a linter/formatter is configured today
- Do not assume Node/npm tooling exists
- Do not assume markdown-first docs (this repo is RST-first)

## 15) Maintenance Rule

When tests/linters/tooling/CI/rule files change, update `AGENTS.md` immediately
so future agents get accurate guidance.
