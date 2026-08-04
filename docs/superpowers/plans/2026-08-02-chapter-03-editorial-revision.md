# Chapter 03 Editorial Revision Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 精修第三章深入閱讀文字稿，使案例、三個工具與管理主張形成同一條學習主線。

**Architecture:** 只更新 canonical Markdown；以既有六節為容器，把同一案例分散到各節，並透過三步路徑串起工具。HTML 與互動功能維持不變。

**Tech Stack:** Traditional Chinese Markdown、`deep_reading_renderer.py`、HBR content analyzer、management article checker。

## Global Constraints

- 導言 180–260 字、單一段落。
- 渲染文字至少 5,000 字。
- 保留 6 個主段落、3 個工具與 1 個總結提要。
- 不出現來源書名、作者或正式量表名稱。

---

### Task 1: 重建案例與工具主線

**Files:**
- Modify: `reference_materials/chapters/chapter_03/02_deep_reading_draft.md`

**Interfaces:**
- Consumes: `reference_materials/chapters/chapter_03/01_core_concepts.md`
- Produces: 可供 HTML renderer 使用的核准 Markdown

- [x] 將軟體公司案例延伸至訊號、期待、工作圖像、角色責任與回看結果。
- [x] 在第二節明示「看見訊號 → 找到共同期待 → 連回今日選擇」。
- [x] 讓三個工具分別對應三步並加入同一案例示範。
- [x] 重寫第四與第五節的重複段落，使其分別處理目的地與角色責任。
- [x] 將總結提要改成三項概念與兩項主管檢查。

### Task 2: 內容與結構驗證

**Files:**
- Test: `reference_materials/chapters/chapter_03/02_deep_reading_draft.md`

**Interfaces:**
- Consumes: Task 1 修訂稿
- Produces: 字數、結構、來源中立與語氣檢查結果

- [x] 執行 `python3 /Users/wes_mini/.codex/skills/hbr-review-skill/scripts/analyze_content.py reference_materials/chapters/chapter_03/02_deep_reading_draft.md`。
- [x] 執行 `python3 /Users/wes_mini/.codex/skills/write-management-article/scripts/check_article.py reference_materials/chapters/chapter_03/02_deep_reading_draft.md`。
- [x] 用 `deep_reading_renderer.py` 驗證導言、六節、三工具、總結與至少 5,000 字。
- [x] 更新 `TASK.md`、`HANDOFF.md` 與 `WORK_LOG.md`，記錄這一輪只改文字稿、未改 HTML。
