# Home and Chapters 01–03 Normalization Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Normalize the learning-map homepage and Chapters 01–03 to the latest `build-source-book-learning-hub` content, source, layout, accessibility, and verification contract without overwriting approved learner work.

**Architecture:** Keep canonical Markdown and chapter JSON as editable sources, use the existing deterministic update/build scripts to produce learner HTML, and keep the Royal Chapter 03 variant outside the canonical root output set. Add regression tests before changing builders so future regeneration cannot restore source-book names, legacy typography, or incomplete chapter shells.

**Tech Stack:** Python 3 standard library, static HTML/CSS/JavaScript, unittest, localStorage, localhost Chrome verification.

## Global Constraints

- Preserve stable learner storage keys for Chapters 01–03.
- Learner-facing pages must not mention `本書`, the source title, or author names.
- Each deep-reading section must contain at least 5,000 rendered non-whitespace characters for this project.
- Use `Noto Sans TC` as the default Traditional Chinese body font.
- Canonical generated HTML remains in the project root; noncanonical visual experiments do not.
- Modify canonical Markdown/configuration before regenerating HTML.
- Do not report completion until all four pages are personally tested in Chrome.

---

### Task 1: Lock the normalization contract with tests

**Files:**
- Create: `scripts/test_home_and_chapters_01_03.py`
- Modify: none

**Interfaces:**
- Consumes: root `index.html`, Chapters 01–03 HTML, canonical drafts and current builder output.
- Produces: regression checks for source-neutral copy, canonical links, shared CSS, entry contract, transfer contract, and rendered reading length.

- [ ] Write tests for homepage source neutrality and exactly one canonical link per Chapter 01–03.
- [ ] Write tests for shared chapter styles, required DOM markers, stable storage keys, and 5,000-character reading minimum.
- [ ] Run the test and confirm it fails on the current Chapter 01 length and noncanonical Royal root output.

### Task 2: Normalize the homepage source and generated output

**Files:**
- Modify: `scripts/build_chapters.py`
- Modify: `templates/index_template.html`
- Generate: `index.html`

**Interfaces:**
- Consumes: `config.json` and chapter metadata in `scripts/build_chapters.py`.
- Produces: deterministic, source-neutral learning map with matching typography, responsive links, and privacy/assessment boundaries.

- [ ] Replace generator-only source-book naming with source-neutral learner copy.
- [ ] Align the index template language, Noto Sans TC fallback stack, header semantics, focus styles, and footer with the chapter shell.
- [ ] Rebuild the homepage without rebuilding Chapters 04–11.
- [ ] Run the homepage regression checks.

### Task 3: Normalize Chapters 01–03 from canonical sources

**Files:**
- Modify: `reference_materials/chapters/chapter_01/02_deep_reading_draft.md`
- Modify: `scripts/update_chapter_learning_page.py` only if required by a failing regression test
- Generate: `LPI_Coach_Chapter01.html`
- Generate: `LPI_Coach_Chapter02.html`
- Generate: `LPI_Coach_Chapter03.html`

**Interfaces:**
- Consumes: chapter drafts, callout JSON, learning JSON, shared CSS and runtime.
- Produces: three idempotently generated canonical learner pages.

- [ ] Add one substantive Chapter 01 passage that strengthens evidence collection and management boundaries.
- [ ] Run the character test and confirm Chapter 01 exceeds 5,000 rendered characters.
- [ ] Regenerate Chapters 01–03 twice and confirm the second run creates no structural drift.
- [ ] Run chapter and source-neutral regression tests.

### Task 4: Move the Chapter 03 Royal experiment out of canonical output

**Files:**
- Modify: `scripts/build_chapter03_royal.py`
- Modify: `scripts/test_chapter03_royal.py`
- Move: `LPI_Coach_Chapter03_Royal.html` to `experiments/chapter03-royal/LPI_Coach_Chapter03_Royal.html`
- Move: `assets/chapter03-royal.css` to `experiments/chapter03-royal/chapter03-royal.css`
- Modify: `USER_GUIDE.md`

**Interfaces:**
- Consumes: canonical Chapter 03 HTML as read-only input.
- Produces: an isolated experimental page that does not pollute root canonical validation.

- [ ] Update the Royal regression test to expect an experiment output path and working relative links.
- [ ] Run the test and confirm it fails before moving the output.
- [ ] Update the builder and move the current experiment assets.
- [ ] Run the Royal regression test and canonical validator.

### Task 5: Verify and document

**Files:**
- Modify: `TASK.md`
- Modify: `HANDOFF.md`
- Modify: `USER_GUIDE.md`
- Modify: `WORK_LOG.md`

**Interfaces:**
- Consumes: final generated pages and test output.
- Produces: reproducible verification record and user handoff.

- [ ] Run all Python tests, Python compile checks, JavaScript syntax checks, structural validation, link checks, forbidden-term checks, and rendered character counts.
- [ ] In Chrome, test index navigation and Chapters 01–03 on desktop and 390px mobile; operate quick scan, incomplete assessment, completed assessment, clear, focus selection, record persistence, and return navigation.
- [ ] Clear test data, reload each page, and check console errors.
- [ ] Update project memory with exact commands, counts, and any unverified items.

