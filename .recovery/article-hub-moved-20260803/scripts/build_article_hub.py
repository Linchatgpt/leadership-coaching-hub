#!/usr/bin/env python3
"""Build Article Hub learner pages and the generated root map."""
from pathlib import Path
import html, json, re

ROOT=Path(__file__).resolve().parents[1]; ARTICLES=ROOT/'content/articles'; TEMPLATE=ROOT/'templates/article_learning_template.html'

def md_to_html(text):
    out=[]; para=[]; in_ul=False
    def flush():
        nonlocal para
        if para: out.append('<p>'+ '<br>'.join(para) +'</p>'); para=[]
    for raw in text.splitlines():
        line=raw.strip()
        if not line: flush(); continue
        if line.startswith('# '): flush(); out.append('<h1>'+html.escape(line[2:])+'</h1>'); continue
        if line.startswith('## '): flush(); out.append('<h2>'+html.escape(line[3:])+'</h2>'); continue
        if line.startswith('- '):
            if not in_ul: flush(); out.append('<ul>'); in_ul=True
            out.append('<li>'+html.escape(line[2:])+'</li>'); continue
        if in_ul: out.append('</ul>'); in_ul=False
        para.append(html.escape(line))
    flush()
    if in_ul: out.append('</ul>')
    return '\n'.join(out).replace('導言｜','<strong>導言｜</strong>')

def scan_html(items):
    blocks=[]
    for i,item in enumerate(items):
        opts=''.join(f'<button type="button" data-feedback="{html.escape(o["feedback"], quote=True)}">{html.escape(o["text"])}</button>' for o in item['options'])
        blocks.append(f'<div class="scan-question"><p>{i+1:02d} · {html.escape(item["question"])}</p><div class="scan-options">{opts}</div><p class="scan-feedback" aria-live="polite"></p></div>')
    return ''.join(blocks)

def questions_html(items):
    blocks=[]
    for i,item in enumerate(items):
        if isinstance(item, dict): label,q,options=item['label'],item['question'],item['options']
        else:
            label,q=item; options=["先記下這個線索","先試一個小改變"]
        buttons=''.join(f'<label class="assessment-option"><input type="radio" name="q{i}" value="{html.escape(label)}" data-option="{html.escape(text)}" data-key="q{i}"><span>{html.escape(text)}</span></label>' for text in options)
        blocks.append(f'<fieldset class="question"><legend><span class="question-number">{i+1}.</span> {html.escape(q)}</legend><div class="assessment-options">{buttons}</div><small class="question-label">{html.escape(label)}</small></fieldset>')
    return ''.join(blocks)

def build_article(d, md):
    t=TEMPLATE.read_text(); replacements={'TITLE':d['title'],'PROJECT_TITLE':'文章學習中心','NUMBER':d['id'].split('_')[-1],'CATEGORY':d['category'],'READING_MINUTES':str(d['reading_minutes']),'SUMMARY':d['summary'],'START_PROMPT':d['start_prompt'],'ORIENTATION':''.join('<li>'+html.escape(x)+'</li>' for x in d['orientation']),'QUICK_SCAN':scan_html(d['quick_scan']),'ARTICLE_HTML':md_to_html(md),'CASE':d['case'],'QUESTIONS':questions_html(d['questions']),'ARTICLE_DATA':json.dumps(d,ensure_ascii=False)}
    for k,v in replacements.items(): t=t.replace('{{'+k+'}}',v)
    return t

def main():
    cards=[]
    for folder in sorted(ARTICLES.iterdir()):
        if not folder.is_dir(): continue
        d=json.loads((folder/'article.json').read_text()); page=f'Article_Learning_{d["id"].replace("article_", "Article")}.html'; (ROOT/page).write_text(build_article(d,(folder/'article.md').read_text()))
        cards.append(f'<a class="map-card" href="{page}"><small>{html.escape(d["category"])} · {d["reading_minutes"]} MIN READ</small><h3>{html.escape(d["title"])}</h3><p>{html.escape(d["summary"])}</p><span>開始這篇學習 →</span></a>')
    index=f'''<!doctype html><html lang="zh-Hant"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>文章學習中心</title><link rel="stylesheet" href="assets/article-learning.css"><style>.home{{max-width:1180px;margin:auto;padding:70px 5vw 110px}}.home-hero{{max-width:800px;padding:20px 0 70px}}.home-hero h1{{font:clamp(48px,8vw,88px)/1.05 Georgia;margin:20px 0}}.home-hero em{{color:var(--sage);font-style:normal}}.home-hero p{{font:20px/1.9 Georgia;color:#456057;max-width:700px}}.map{{display:grid;grid-template-columns:repeat(2,1fr);gap:16px}}.map-card{{display:block;text-decoration:none;color:var(--ink);padding:28px;background:#fff;border:1px solid var(--line);transition:transform .2s,border-color .2s}}.map-card:hover{{transform:translateY(-3px);border-color:var(--gold)}}.map-card h3{{font:28px Georgia;margin:12px 0 8px}}.map-card p{{color:var(--muted);font-size:14px}}.home-note{{margin-top:70px;padding:24px 0;border-top:1px solid var(--line);max-width:760px}}@media(max-width:700px){{.map{{grid-template-columns:1fr}}}}</style></head><body><div class="top"><a class="brand" href="index.html" aria-label="返回文章學習地圖"><i>AL</i> 文章學習中心</a><span class="save">LOCAL LEARNING HUB</span></div><main class="home"><section class="home-hero"><small class="kicker">ONE PAGE · ONE PRACTICE</small><h1>把一篇文章，<em>讀成一個行動。</em></h1><p>每次只帶一個真實工作情境進來：先讀懂，再辨識，再試做。所有學習紀錄只留在目前瀏覽器，沒有登入，也不需要交出你的答案。</p></section><section><small class="kicker">LEARNING MAP</small><h2>選一篇，開始你的工作練習。</h2><div class="map">{"".join(cards)}</div></section><section class="home-note"><h2>使用前請知道</h2><p>案例人物與事件請自行去識別化。自我整理題目是發展工具，不是心理測驗、正式量表或人資決策工具；清除瀏覽器網站資料會刪除本機紀錄。</p></section></main><footer>文章學習中心 · 瀏覽器本機保存</footer></body></html>'''
    (ROOT/'index.html').write_text(index)
if __name__=='__main__': main()
