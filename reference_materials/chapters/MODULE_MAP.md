# 模組—來源—網頁對應索引

本索引是編輯與維護用的內部文件，說明網站使用者看到的模組編號，如何對應到來源章節、深入閱讀稿與生成後的網頁。

## 正式網站模組

| 網站模組 | 原始章節資料夾 | 深入閱讀稿 | 生成網頁 | 網站主題 |
|---|---|---|---|---|
| 模組 01 | `chapter_07` | `chapter_07/02_deep_reading_draft.md` | `LPI_Coach_Chapter07.html` | 走向成功的教練：先把成功說清楚，才知道如何陪伴 |
| 模組 02 | `chapter_08` | `chapter_08/02_deep_reading_draft.md` | `LPI_Coach_Chapter08.html` | 教練能力：在正確的時機，用正確的方式讓對話前進 |
| 模組 03 | `chapter_09` | `chapter_09/02_deep_reading_draft.md` | `LPI_Coach_Chapter09.html` | 教練流程：把一次對話變成一個可回看的學習循環 |
| 模組 04 | `chapter_10` | `chapter_10/02_deep_reading_draft.md` | `LPI_Coach_Chapter10.html` | 教練失去節奏時：把未完成的承諾重新接回工作 |
| 模組 05 | `chapter_11` | `chapter_11/02_deep_reading_draft.md` | `LPI_Coach_Chapter11.html` | 教練也要被教練：把專業精熟變成可持續的工作系統 |

## 編輯流程

每個模組的深入閱讀內容，應先編輯表格中的 `02_deep_reading_draft.md`，再透過建置工具產生對應的 HTML。生成後的 HTML 是網站輸出，不是文章內容的唯一來源。

```text
02_deep_reading_draft.md
        ↓ 建置工具
LPI_Coach_ChapterXX.html
        ↓ 首頁模組方塊
模組 01～05
```

## 舊資料夾說明

`chapter_01`、`chapter_02`、`chapter_03` 是早期內容資料，目前沒有對應到首頁正式的模組 01～05。除非重新指定內容用途，否則不要把它們當作現行網站模組的編輯來源。

## 相關工具

- 章節建置：`scripts/build_chapters.py`
- 深入閱讀轉換器：`scripts/deep_reading_renderer.py`
- 網站首頁：`index.html`
- 章節來源根目錄：`reference_materials/chapters/`
