#!/usr/bin/env python3
"""Add the five local module audio players to the generated learning map."""

from pathlib import Path
from html import escape
import re

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"

MODULE_AUDIO = {
    "07": "module_01_summary.mp3",
    "08": "module_02_summary.mp3",
    "09": "module_03_summary.mp3",
    "10": "module_04_summary.mp3",
    "11": "module_05_summary.mp3",
}

source = INDEX.read_text(encoding="utf-8")

def add_player(match):
    href = match.group(1)
    card = re.sub(r'<div class="module-audio">.*?</div>', '', match.group(0), flags=re.S)
    chapter = re.search(r"Chapter(\d+)", href).group(1)
    filename = MODULE_AUDIO[chapter]
    player = (
        f'<div class="module-audio">'
        f'<button class="audio-toggle" type="button" data-audio="audio_summaries/{filename}" '
        f'aria-label="播放本模組摘要" aria-pressed="false">'
        f'<span class="audio-label">播放摘要</span></button>'
        f'<audio controls preload="none" src="audio_summaries/{filename}"></audio></div>'
    )
    return card.replace("<span>開始本模組 →</span>", f"<span>開始本模組 →</span>{player}")

updated = re.sub(r'<a class="map-card" href="([^"]*Chapter(?:07|08|09|10|11)\.html)".*?</a>', add_player, source, flags=re.S)

style = """
.module-audio{display:flex;align-items:center;gap:8px;margin-top:18px;padding-top:14px;border-top:1px solid var(--line)}
.audio-toggle{display:inline-flex;align-items:center;gap:8px;padding:8px 11px;border:1px solid var(--sage);border-radius:999px;background:var(--paper);color:var(--ink);font:600 12px/1.2 "Noto Sans TC",Arial,sans-serif;cursor:pointer}
.audio-toggle:hover,.audio-toggle:focus-visible{border-color:var(--gold);outline:2px solid var(--gold);outline-offset:2px}
.audio-toggle[aria-pressed="true"]{background:var(--ink);color:white}
.module-audio audio{display:block;width:100%;max-width:260px;height:32px}
"""
script = """
<script>
document.querySelectorAll('.audio-toggle').forEach((button) => {
  const audio = button.parentElement.querySelector('audio');
  const label = button.querySelector('.audio-label');
  button.addEventListener('click', async (event) => {
    event.preventDefault();
    event.stopPropagation();
    if (audio.paused) {
      document.querySelectorAll('.module-audio audio').forEach((other) => { if (other !== audio) other.pause(); });
      await audio.play();
      label.textContent = '暫停摘要'; button.setAttribute('aria-pressed', 'true');
    } else { audio.pause(); }
  });
  audio.addEventListener('pause', () => { label.textContent = '播放摘要'; button.setAttribute('aria-pressed', 'false'); });
  audio.addEventListener('ended', () => { label.textContent = '重新播放摘要'; button.setAttribute('aria-pressed', 'false'); });
});
document.querySelectorAll('.module-audio audio').forEach((audio) => {
  audio.addEventListener('play', () => {
    document.querySelectorAll('.module-audio audio').forEach((other) => { if (other !== audio) other.pause(); });
  });
});
</script>
"""

# Keep the generator idempotent when the homepage is rebuilt.
updated = re.sub(r'<style>\s*\.module-audio\{.*?</style>', '', updated, count=1, flags=re.S)
updated = re.sub(r'<script>\s*document\.querySelectorAll\(\'.audio-toggle\'\).*?</script>', '', updated, count=1, flags=re.S)
updated = updated.replace("</style>", style + "</style>", 1).replace("</body>", script + "</body>")
INDEX.write_text(updated, encoding="utf-8")
print(INDEX)
