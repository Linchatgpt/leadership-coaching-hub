# Chapter 03 Royal Variant Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [x]`) syntax for tracking.

**Goal:** 建立完整、可獨立開啟的第三章皇家知識沙龍版本，同時保持原始第三章不變。

**Architecture:** 以 `LPI_Coach_Chapter03.html` 作為內容與互動基準，由一個小型建置器做可重複的字串轉換，產生 `LPI_Coach_Chapter03_Royal.html`。視覺覆寫集中於獨立 CSS；皇家版改用獨立 localStorage key，避免影響原版學習紀錄。

**Tech Stack:** Python 3.13、HTML5、CSS3、既有原生 JavaScript、unittest、BeautifulSoup、Chrome 實機驗證。

## Global Constraints

- 不修改或取代 `LPI_Coach_Chapter03.html`。
- 保留全文、工作案例、十二題自評、雷達結果、工作紀錄與行動承諾。
- 皇家版背景維持淺色，採象牙紙、孔雀綠、古金與酒紅。
- 所有互動目標至少 44px，提供可見焦點，支援 `prefers-reduced-motion`，390px 不得水平溢出。
- 皇家版 localStorage key 固定為 `LPI_CoachChapter3RoyalV2`；`V2` 命名空間用來隔離 Chrome 驗收期間留下的測試文字。

---

### Task 1: 可重建的皇家版產生器

**Files:**
- Create: `scripts/test_chapter03_royal.py`
- Create: `scripts/build_chapter03_royal.py`

**Interfaces:**
- Consumes: 原始 Chapter 03 HTML 字串。
- Produces: `build_royal_html(source: str) -> str` 與輸出檔 `LPI_Coach_Chapter03_Royal.html`。

- [x] **Step 1: Write the failing test**

測試使用最小 HTML fixture，要求轉換後保留章節文字、加入皇家版 body class 與 CSS、改用獨立儲存鍵，且重複執行得到相同結果。

- [x] **Step 2: Run test to verify it fails**

Run: `python3 scripts/test_chapter03_royal.py`

Expected: FAIL with `Royal builder has not been implemented`。

- [x] **Step 3: Write minimal implementation**

建置器驗證 `<title>`、`<body>`、`</head>` 與原始儲存鍵各存在一次，再執行固定替換；若輸入已是皇家版則直接回傳，確保冪等。

- [x] **Step 4: Run test to verify it passes**

Run: `python3 scripts/test_chapter03_royal.py`

Expected: 兩個單元測試通過。

### Task 2: 皇家知識沙龍視覺系統

**Files:**
- Create: `assets/chapter03-royal.css`
- Generate: `LPI_Coach_Chapter03_Royal.html`

**Interfaces:**
- Consumes: 現有 Chapter 03 DOM class 與互動狀態。
- Produces: 僅作用於 `body.royal-chapter` 的 CSS 覆寫。

- [x] **Step 1: Define tokens and signature**

使用 `--royal-ivory: #f7f2e8`、`--royal-paper: #fffdf8`、`--royal-peacock: #173f36`、`--royal-gold: #a77d32`、`--royal-wine: #7d2838`、`--royal-ink: #24322e`；Hero 以純 CSS 同心圓與刻度形成皇家天文儀。

- [x] **Step 2: Implement component overrides**

覆寫 topbar、目錄、Hero、導讀、快問、正文、案例、自評、結果、工作紀錄、承諾與 footer；保持既有 DOM 與 JavaScript 事件不變。

- [x] **Step 3: Implement accessibility and responsive states**

提供 `:focus-visible`、44px 控制高度、`@media (max-width: 800px)` 單欄、`@media (prefers-reduced-motion: reduce)` 靜態模式與列印樣式。

- [x] **Step 4: Generate the standalone page**

Run: `python3 scripts/build_chapter03_royal.py`

Expected: 產生皇家版 HTML；建置器會在每次執行前後即時計算原檔 SHA-256，若建置期間原檔被改動便立即失敗。

### Task 3: 完整功能與視覺驗收

**Files:**
- Verify: `LPI_Coach_Chapter03_Royal.html`
- Update: `TASK.md`
- Update: `HANDOFF.md`
- Update: `WORK_LOG.md`

**Interfaces:**
- Consumes: 皇家版頁面與既有互動 runtime。
- Produces: 桌面與 390px 手機驗證證據。

- [x] **Step 1: Run automated verification**

Run: `python3 scripts/test_chapter03_royal.py && python3 scripts/test_chapter_learning_page.py && node --check assets/chapter-runtime.js`

- [x] **Step 2: Verify content length and source integrity**

計算 `#s1 .reading-essay` 去空白後字數，要求至少 5,000；重新計算原檔 SHA-256。

- [x] **Step 3: Verify in Chrome**

桌面完成快問、十二題自評、結果、焦點、工作紀錄與行動承諾；重新載入確認皇家版 localStorage；390px 確認單欄與無水平溢出，並檢查 console。

- [x] **Step 4: Record the verified work**

只在完成驗證後更新 TASK、HANDOFF 與 WORK_LOG，記錄檔名、獨立 storage key、測試結果與原檔雜湊。
