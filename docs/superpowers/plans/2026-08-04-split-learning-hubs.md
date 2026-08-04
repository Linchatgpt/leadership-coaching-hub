# Split Learning Hubs Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Split the current 11-module site into an independent Module 01–06 principle hub and Module 07–11 coaching hub.

**Architecture:** Preserve canonical HTML filenames and localStorage keys for compatibility. Give each project its own root index, assets, editor, configuration, allowed module range, tests, server command, and handoff documentation.

**Tech Stack:** Static HTML/CSS/JavaScript, Python builders and local HTTP server, unittest, Chrome verification.

## Global Constraints

- Existing learner records and canonical module filenames must remain stable.
- `Leadership Principle hub` exposes only Module 01–06.
- `Leadership Coaching Hub` exposes only Module 07–11.
- Both sites must have independent relative-link indexes and return-home brand links.
- Website changes must pass automated checks and real Chrome operation before completion.

---

### Task 1: Create project boundaries

**Files:** Rename the current root; create the coaching root by copying shared infrastructure; remove out-of-scope canonical pages from each root.

- [ ] Rename `Leader Principle hub` to `Leadership Principle hub`.
- [ ] Copy the project infrastructure to `Leadership Coaching Hub`.
- [ ] Keep only Module 01–06 learner HTML in the principle root and Module 07–11 learner HTML in the coaching root.

### Task 2: Create independent indexes and configuration

**Files:** Modify `config.json`, `index.html`, `admin.html`, `scripts/build_chapters.py`, and project memory in both roots.

- [ ] Add each project's allowed module range to configuration.
- [ ] Limit builders and admin page lists to each configured range.
- [ ] Generate a six-card principle index and five-card coaching index with portable relative links.
- [ ] Write project-specific product, task, handoff, user-guide, and work-log notes.

### Task 3: Verify both products

**Files:** Add split-contract tests in each project's `scripts/` directory.

- [ ] Assert each root has exactly its expected canonical module HTML files and index links.
- [ ] Run Python and JavaScript checks in both roots.
- [ ] Start each project on a separate localhost port.
- [ ] In Chrome, test both indexes, card navigation, return-home links, visible Module labels, and horizontal overflow.
