#!/usr/bin/env python3
"""Create local navigation, provenance reports, and explicit coverage notes."""
import csv
import html
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import quote
from bs4 import BeautifulSoup
from collect_resources import ROOT, RECORDS, export

export()
rows=sorted(RECORDS.values(),key=lambda r:(r['category'],r.get('local_path',''),r['url']))
good=[r for r in rows if r['status']=='ok']
failed=[r for r in rows if r['status']!='ok']
groups=defaultdict(list)
for r in good:groups[r['category']].append(r)

def label(r):
    p=Path(r['local_path'])
    t=r.get('title','')
    if not t or t in ['PDF','here','Download Now'] or len(t)>160:t=p.stem
    return re.sub(r'\s+',' ',t).replace('|','／')

def target(r):return r.get('text_path') or r['local_path']
def mdlink(p,t):return '['+t+']('+quote(p,safe='/')+')'

counts=Counter(r['category'].split('/')[0] for r in good)
pdfcount=sum(r['local_path'].endswith('.pdf') for r in good)
mb=sum(r['bytes'] for r in good)/1048576
readme=f'''# HiMCM 备赛资料库

本轮整理日期：2026-11-02（Australia/Sydney）。共保存 **{len(good)} 项原始资源**，其中 **{pdfcount} 个 PDF**，原始下载内容约 **{mb:.1f} MiB**。网页另附可离线检索的 TXT，不重复计入资源数。

从这里查找：[可搜索的本地目录](00_可搜索目录.html) · [完整分类索引](目录索引.md) · [下载缺失清单](99_索引与日志/未下载与受限资源.md) · [来源清单](99_索引与日志/资料来源清单.csv)

## 分类

| 目录 | 已保存资源 | 内容 |
| --- | ---: | --- |
| 01_官方规则与模板 | {counts['01_官方规则与模板']} | 2026 官方规则页面、AI 政策、报名和提交说明、摘要页 Word/LaTeX 模板 |
| 02_历年真题 | {counts['02_历年真题']} | 官方目录覆盖 1999—2025，按年份保存题目网页、公开 PDF 和附件；2001 年两次比赛分开；MidMCM 补充题独立存放 |
| 03_论文与评审 | {counts['03_论文与评审']} | 55 篇 2017—2023 HiMCM 公开镜像论文、1 篇作者公开论文、官方评审文章、历年官方结果和会员论文目录 |
| 04_教材与训练 | {counts['04_教材与训练']} | SIAM 两本建模手册和速查卡、GAIMME、27 单元中英双语讲义及数据、Python 仿真教材、概率统计、复杂系统、凸优化、预测资料 |
| 05_算法与代码文档 | {counts['05_算法与代码文档']} | 优化、图论、微分方程、离散事件仿真、敏感性分析、交叉验证、绘图、LaTeX 的原始论文或官方文档 |
| 06_数据来源导航 | {counts['06_数据来源导航']} | 世界银行、联合国、OWID、中澳统计局、政府开放数据、NASA、NOAA、OpenStreetMap 的入口快照 |
| 07_同级竞赛练习 | {counts['07_同级竞赛练习']} | 19 篇 IMMC 公开镜像论文；M3 2023—2025 官方题目 PDF 与配套 Excel 数据 |
| 99_索引与日志 | — | 原始下载清单、网址、获取时间、SHA-256、文件检查、缺失说明和采集脚本 |

## 开始阅读

1. 先看 `01_官方规则与模板/2026_官方规则.txt`，比赛规则以 COMAP 当前页面为准。
2. 用 `04_教材与训练/SIAM建模手册/SIAM_2014_建模入门与求解.pdf` 建立读题、假设、变量、建模和验证的完整认识。
3. 用 `04_教材与训练/SIAM建模手册/SIAM_2018_计算与表达.pdf` 补充数据、仿真、计算和表达。
4. 阅读 `03_论文与评审/官方评审/Cons_HiMCM.pdf`，其中包含评审讨论和优秀作品节选；它是历史评审资料。
5. 挑一道历年题，再打开同年份、同题号的论文对照。不要把官方获奖名单 PDF 当成论文正文。
6. 算法、Python 章节和双语讲义按题目需要查阅。凸优化教材属于进阶参考，不要求通读。

## 覆盖范围与来源区分

- 这是一次有范围的公开资料归档，不代表穷尽互联网或所有年份的获奖论文。官方历年目录提供的早期题目有些仅为 HTML，本库同时保存 HTML 原件和 TXT 正文。
- HiMCM 论文镜像来自 [Beldore 的公开目录](https://beldore.club/competitions/papers)。原始链接及镜像属性逐项记录；获奖标签不作为数学正确性或全文真实性的保证。另见 `99_索引与日志/HiMCM论文来源核对.csv`。
- `03_论文与评审/历年官方结果/` 是成绩公告；`官方评审/` 是评审文章；`HiMCM公开论文/` 才是所下载的完整参赛论文。
- 最新完整论文和部分教学模块在 COMAP 网站需要会员或免费账户。这里保留公开目录/介绍，不把登录页冒充全文，也没有创建账户、购买或绕过访问限制。GAIMME 中文版目前保存的是入口，英文公开版已下载。
- M3 部分 HTML 页面和 IMSA 学校论文下载端点返回 403；官网历史附件中另有 404。对应链接、原因均保留在缺失清单中。M3 已保存的三年 PDF/数据来自官方页面提供的直接链接。
- `06_数据来源导航` 是找数据的入口，不是把这些网站的数据库全部下载；教学数据保留来源和人工合成标签。
- 网页的 TXT 可直接离线阅读。HTML 原件保留网页源文件，但外部图片、样式和动态组件可能需要联网。
- 本目录为新建；原有四个资料文件夹未移动、覆盖或混装。已有 MCM/ICM 大论文库没有重复下载。

## 文件检查与重现

所有下载都记录 URL、最终 URL、获取时间、大小和 SHA-256。PDF 已逐个做结构检查；XLSX、DOCX、ZIP 做容器格式和 CRC 检查。完整记录见 `99_索引与日志/文件校验报告.json`。这些检查确认文件传输和结构，不证明论文中的模型、数据和结论正确。

部分原始 PDF 有可恢复的结构/线性化警告，原始字节保持不变；警告文件在检查报告中单列。采集脚本只用于本次明确来源的保存，没有运行下载的程序或安装第三方仓库。

采集入口：`99_索引与日志/collect_resources.py`；补充来源分别记录在同目录的 `collect_supplement.py`、`collect_bilingual.py` 和 `collect_training.py`。重新联网获取是手动操作，不包含后台监控或自动更新。
'''
(ROOT/'00_开始阅读.md').write_text(readme,encoding='utf-8')

lines=['# 完整分类索引','',f'2026-11-02 保存 {len(good)} 项资源；TXT 为网页可读版，原始 HTML 和下载网址见来源清单。','']
for cat,items in sorted(groups.items()):
    lines+=['## '+cat,'']
    for r in items:
        info=(str(r['pages'])+' 页') if r.get('pages') else Path(r['local_path']).suffix.lstrip('.').upper()
        lines.append('- '+mdlink(target(r),label(r))+' — '+info+' · [来源]('+r['url']+')')
    lines.append('')
(ROOT/'目录索引.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')

missing=['# 未下载与受限资源','',f'本轮 {len(failed)} 个明确下载地址未取得文件；下表不是全部会员资料清单。HTTP 403 与 404 均按原样记录，没有绕过限制。','',
         '| 分类 | 资源/地址 | 结果 |','| --- | --- | --- |']
for r in failed:
    title=r.get('title') or r['url'].rsplit('/',1)[-1]
    missing.append('| '+r['category']+' | ['+title.replace('|','／')+']('+r['url']+') | '+r.get('error','unknown').replace('|','／')+' |')
missing+=['','## 已保存入口但全文受限','',
          '- COMAP Mathmodels 部分完整获奖论文：见 `03_论文与评审/官方会员入口/`。',
          '- GAIMME 中文版和 COMAP 部分“免费”教学模块仍要求先注册免费会员：本库只保存公开介绍，未注册或登录。',
          '- 最新年度 HiMCM 全文未找到合适的公开下载来源；官方评审文章中的优秀作品节选已保存在 `03_论文与评审/官方评审/`。']
(ROOT/'99_索引与日志/未下载与受限资源.md').write_text('\n'.join(missing)+'\n',encoding='utf-8')

# Award cross-reference: require the team number to occur in the official
# Outstanding block, ending at the statistics table, MidMCM, or a Finalist row.
verification=[]
for r in good:
    if not r['category'].startswith('03_论文与评审/HiMCM公开论文/'):continue
    year=r['category'].split('/')[2]; team=Path(r['local_path']).stem
    official=ROOT/'03_论文与评审/历年官方结果'/year/(year+'results.html')
    result='未通过官方编号核验（不代表未获奖）'
    if official.exists():
        text=BeautifulSoup(official.read_bytes(),'html.parser').get_text(' ',strip=True)
        start=text.lower().find('outstanding')
        block=text[start:] if start>=0 else ''
        end=re.search(r'20\s?\d{2}\s+HiMCM\s+Statistics|20\s?\d{2}\s+MidMCM|\bFinalist\b',block,re.I)
        if end:block=block[:end.start()]
        if re.search(r'(?<!\d)'+re.escape(team)+r'(?!\d)',block):result='队号在 COMAP 官方 Outstanding 名单中匹配'
    verification.append({'year':year,'team':team,'local_path':r['local_path'],'mirror_url':r['url'],
                         'award_cross_reference':result,'official_results':str(official.relative_to(ROOT)),
                         'scope':'仅核对队号与奖项；未验证全文版本、题号或模型结论'})
with (ROOT/'99_索引与日志/HiMCM论文来源核对.csv').open('w',encoding='utf-8-sig',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(verification[0]));w.writeheader();w.writerows(verification)

# Offline searchable catalog: no network requests, source scripts, or third-party assets.
trs=[]
for r in good:
    info=str(r['pages'])+' 页' if r.get('pages') else Path(r['local_path']).suffix.lstrip('.').upper()
    trs.append('<tr><td>'+html.escape(r['category'])+'</td><td><a href="'+quote(target(r),safe='/')+'">'+html.escape(label(r))+'</a></td><td>'+info+'</td><td><a href="'+html.escape(r['url'],quote=True)+'" target="_blank" rel="noopener noreferrer">原始来源</a></td></tr>')
options=''.join('<option>'+html.escape(c)+'</option>' for c in sorted(counts))
page='''<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>HiMCM 备赛资料目录</title>
<style>body{font:16px/1.6 system-ui,sans-serif;color:#182b38;background:#f6f8fa;margin:0}main{max-width:1250px;margin:auto;padding:36px 24px}h1{font-size:32px;margin:0 0 8px}p{color:#50616e}input,select{font:inherit;padding:10px;border:1px solid #bac8d1;border-radius:6px;background:white}input{width:min(550px,90%)}table{border-collapse:collapse;width:100%;margin-top:24px;background:white}td,th{padding:10px 14px;border-bottom:1px solid #dfe6eb;text-align:left;vertical-align:top}th{background:#eaf0f4;position:sticky;top:0}td:first-child{font-size:13px;width:30%}a{color:#006184}nav{display:flex;flex-wrap:wrap;gap:12px}.muted{font-size:14px}td:nth-child(3),td:nth-child(4){white-space:nowrap}</style>
<main><h1>HiMCM 备赛资料库</h1><p>2026-11-02 · '''+str(len(good))+''' 项资源 · '''+str(pdfcount)+''' 个 PDF · 按主题、年份和题号归档</p><p class="muted">网页链接打开离线 TXT；外部来源在单独页面打开。论文、评审与成绩公告分开归档。<a href="00_开始阅读.md">阅读说明</a> · <a href="99_索引与日志/未下载与受限资源.md">未下载与受限资料</a></p>
<nav><input id="q" aria-label="搜索资料" placeholder="搜索：年份、题号、模型、关键词…"><select id="cat" aria-label="类别"><option value="">全部类别</option>'''+options+'''</select><span id="count"></span></nav><table><thead><tr><th>分类</th><th>资料</th><th>格式 / 页数</th><th>来源</th></tr></thead><tbody>'''+''.join(trs)+'''</tbody></table></main>
<script>const q=document.getElementById('q'),cat=document.getElementById('cat'),rs=[...document.querySelectorAll('tbody tr')];function filter(){let n=0;const s=q.value.toLowerCase().trim();for(const r of rs){const visible=r.textContent.toLowerCase().includes(s)&&(!cat.value||r.cells[0].textContent.startsWith(cat.value));r.hidden=!visible;if(visible)n++;}document.getElementById('count').textContent=n+' 项';}q.addEventListener('input',filter);cat.addEventListener('change',filter);filter();</script></html>'''
(ROOT/'00_可搜索目录.html').write_text(page,encoding='utf-8')
summary={'date':'2026-11-02','downloaded_resources':len(good),'pdf':pdfcount,'download_bytes':sum(r['bytes'] for r in good),
         'failed_requests':len(failed),'by_category':dict(counts),'himcm_papers':56,'immc_papers':19,
         'award_team_numbers_matched':sum('匹配' in r['award_cross_reference'] for r in verification)}
(ROOT/'99_索引与日志/归档统计.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(summary,ensure_ascii=False))
