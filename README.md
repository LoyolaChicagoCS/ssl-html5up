# SSL Website

[![Production Site](https://img.shields.io/badge/site-ssl.cs.luc.edu-1e88e5)](https://ssl.cs.luc.edu)
[![Build Status](https://img.shields.io/github/actions/workflow/status/LoyolaChicagoCS/ssl-html5up/build.yml?branch=main&label=build)](https://github.com/LoyolaChicagoCS/ssl-html5up/actions/workflows/build.yml)

The Software and Systems Laboratory (SSL) website is built with Sphinx and
deployed to GitHub Pages.

## Current Status

- Active documentation website project using Sphinx + `uv`
- CI deploys the site from `main` using `.github/workflows/build.yml`
- Build validation is in place; dedicated Python lint/unit-test tooling is not
  yet configured in this repository

## Production URL

- <https://ssl.cs.luc.edu>

## Repository Structure

- `src/`: Sphinx source files (`.rst`, `conf.py`, static assets)
- `src/_static/`: CSS and reusable profile fragments used by includes
- `src/publications/`: publication/blog post pages
- `build/`: generated site output (artifact/output directory)
- `.github/workflows/build.yml`: CI build and deploy workflow

## Prerequisites

- Python `3.14` (project target)
- `uv`
- `make` (optional convenience commands)

## Quick Start

```bash
uv sync
make build-proj
```

Open `build/index.html` after a successful build.

## Build and Preview

Build docs:

```bash
make build-proj
```

Equivalent direct command:

```bash
uv run sphinx-build -vvv --write-all --fresh-env src build
```

Live preview during edits:

```bash
make serve
```

Equivalent direct command:

```bash
uv run sphinx-autobuild src build
```

## Validation Before Opening a PR

Run strict docs validation (warnings as errors):

```bash
uv run sphinx-build -n -W --keep-going --write-all src build
```

Note: this repository currently uses Sphinx build checks as the primary quality
gate.

Run link validation when URLs are added or changed:

```bash
uv run sphinx-build -b linkcheck src build/linkcheck
```

## How to Contribute

1. Review contribution policy in `.github/CONTRIBUTING.md`.
1. Create a feature branch from `main`.
1. Make focused changes in `src/` (and `src/_static/` when needed).
1. Run the validation commands above.
1. Open a PR with a concise rationale and verification notes.

## Step-by-Step: Add or Edit a Member Profile

1. Identify which group card to update in `src/members.rst`.
1. Add or update the corresponding profile snippet in the correct file under
   `src/_static/` (for example `faculty_advisors.rst`, `phd_students.rst`,
   `masters_students.rst`, `undergraduate_students.rst`, `collaborators.rst`,
   `alumni.rst`).
1. Follow the existing marker pattern exactly:
   - Start each snippet block with `.. Full Name`
   - Keep the trailing `..` sentinel structure intact
1. If adding a new person card, add a matching `.. grid-item-card::` entry in
   `src/members.rst` with the proper `.. include::` slice.
1. Build locally (`make build-proj`) and verify the member appears correctly.
1. Run strict validation before opening the PR.

## Step-by-Step: Add a Publication/Blog Post

1. Create a new `.rst` file under `src/publications/`.
1. Use existing publication pages as templates for structure.
1. Ensure metadata/content is compatible with the `.. postlist::` block in
   `src/publications/index.rst`.
1. Build locally and verify the post appears on the publications page.
1. Run strict validation and linkcheck if external links were added.

## Step-by-Step: Update Projects Page

1. Edit `src/projects.rst`.
1. Keep headings and directive style consistent with surrounding content.
1. Build and verify page rendering.
1. Run strict validation before submitting the PR.

## Step-by-Step: Update Website Styles

1. Edit `src/_static/custom.css`.
1. Prefer scoped style changes over broad global overrides.
1. Verify desktop and mobile rendering.
1. Rebuild and confirm no regressions in core pages.

## Sphinx-Specific Authoring Notes

- Preserve heading hierarchy and adornment style within each `.rst` file.
- Reuse existing directives and patterns (`grid`, `include`, admonitions).
- Keep include slices exact (`:start-after:` / `:end-before:`) to avoid broken
  member cards.
- Keep prose concise and avoid redundant sections.

## Release Process

This project supports two release tracks.

### 1) Website release (deployment)

- Merge the approved PR to `main`.
- GitHub Actions builds and deploys the site via
  `.github/workflows/build.yml`.
- Confirm the production site reflects the new content at
  <https://ssl.cs.luc.edu>.

### 2) Versioned release (SemVer tags)

1. Ensure the desired changes are merged to `main`.
1. Create and push a semantic version tag, e.g. `v1.2.3`.
1. Create a GitHub Release for that tag.
1. Draft release notes from merged PRs and resolved issues since the previous
   tag.

## Contribution Guidelines

- Contribution process: `.github/CONTRIBUTING.md`

## Agent Guidance

- Agent-specific repository rules are documented in `AGENTS.md`.
- Recommended model: GPT-5.3-Codex in GitHub Copilot.
