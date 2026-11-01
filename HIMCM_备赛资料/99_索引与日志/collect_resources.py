#!/usr/bin/env python3
"""Archive public modeling resources; do not execute downloaded content."""
import concurrent.futures as cf
import csv
import hashlib
import io
import json
import re
import threading
import time
from datetime import datetime
from pathlib import Path
from urllib.parse import unquote, urldefrag, urljoin, urlparse
from zoneinfo import ZoneInfo

import requests
from bs4 import BeautifulSoup
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
LOG = ROOT / '99_索引与日志/manifest.jsonl'
STAMP = datetime.now(ZoneInfo('Australia/Sydney')).isoformat()
LOCK = threading.Lock()
RECORDS = {}
if LOG.exists():
    for line in LOG.read_text().splitlines():
        row = json.loads(line)
        RECORDS[row['url']] = row

def safe(s):
    return re.sub(r'[\\/:*?"<>|\x00-\x1f]', '_', unquote(s)).strip('. ')[:155] or 'resource'

def fetch(url, category, title='', name=None, note=''):
    url = urldefrag(url)[0].replace(' ', '%20')
    old = RECORDS.get(url)
    if old and old['status'] == 'ok' and (ROOT / old['local_path']).exists():
        return old
    row = dict(url=url, category=category, title=title, note=note, retrieved_at=STAMP,
               status='failed', local_path='', final_url='', bytes=0, sha256='', pages=None)
    try:
        r = requests.get(url, timeout=(12, 40), stream=True,
                         headers={'User-Agent':'HiMCM-Study-Archive/1.0 (personal educational resource collection)'})
        row['http_status'] = r.status_code
        row['final_url'] = r.url
        r.raise_for_status()
        chunks=[]; size=0
        for b in r.iter_content(131072):
            size += len(b)
            if size > 40*1024*1024:
                raise ValueError('resource exceeds 40 MB per-file limit')
            chunks.append(b)
        body = b''.join(chunks)
        typ = r.headers.get('content-type','').lower()
        is_pdf = body[:1024].lstrip().startswith(b'%PDF-')
        expected = unquote(urlparse(url).path).lower()
        if (expected.endswith('.pdf') or (name and name.endswith('.pdf'))) and not is_pdf:
            raise ValueError('not a PDF: server returned '+typ)
        if is_pdf:
            reader=PdfReader(io.BytesIO(body))
            row['pages']=len(reader.pages)
            if not row['pages']: raise ValueError('empty PDF')
            row['first_page_excerpt']=(reader.pages[0].extract_text() or '')[:600]
            ext='.pdf'
        elif 'html' in typ or body.lstrip().lower().startswith((b'<!doctype html', b'<html')):
            ext='.html'
        else:
            ext=Path(expected).suffix or '.bin'
        if not name:
            stem=safe(Path(unquote(urlparse(url).path)).stem)
            if stem in ('index','content','download',''): stem=safe(title or 'page')
            name=stem+ext
        dest=ROOT/category/safe(name)
        dest.parent.mkdir(parents=True,exist_ok=True)
        if dest.exists() and dest.read_bytes()!=body:
            dest=dest.with_name(dest.stem+'_'+hashlib.sha256(url.encode()).hexdigest()[:7]+dest.suffix)
        dest.write_bytes(body)
        row.update(status='ok', local_path=str(dest.relative_to(ROOT)), bytes=len(body),
                   sha256=hashlib.sha256(body).hexdigest(), content_type=typ)
        if ext=='.html':
            soup=BeautifulSoup(body,'html.parser')
            if not title: row['title']=soup.title.get_text(' ',strip=True) if soup.title else dest.stem
            for x in soup(['script','style','noscript']): x.decompose()
            text=soup.get_text('\n',strip=True)
            dest.with_suffix('.txt').write_text('Source: '+r.url+'\nRetrieved: '+STAMP+'\n\n'+text,encoding='utf-8')
            row['text_path']=str(dest.with_suffix('.txt').relative_to(ROOT))
    except Exception as e:
        row['error']=type(e).__name__+': '+str(e)[:350]
    with LOCK:
        RECORDS[url]=row
        with LOG.open('a',encoding='utf-8') as out: out.write(json.dumps(row,ensure_ascii=False)+'\n')
    return row

def batch(jobs):
    jobs=list(jobs)
    with cf.ThreadPoolExecutor(max_workers=4) as pool:
        results=list(pool.map(lambda j: fetch(*j), jobs))
    print(json.dumps({'requested':len(jobs),'ok':sum(r['status']=='ok' for r in results),
                      'failed':[{'url':r['url'],'error':r.get('error')} for r in results if r['status']!='ok']},ensure_ascii=False),flush=True)
    return results

def links(row):
    if row['status']!='ok' or not row.get('local_path','').endswith('.html'): return []
    soup=BeautifulSoup((ROOT/row['local_path']).read_bytes(),'html.parser')
    return [(urljoin(row['final_url'],a['href']).replace(' ','%20'),a.get_text(' ',strip=True))
            for a in soup.select('a[href]') if not a['href'].startswith(('mailto:','javascript:','#'))]

def export():
    rows=sorted(RECORDS.values(),key=lambda r:(r['category'],r.get('local_path',''),r['url']))
    (ROOT/'99_索引与日志/manifest.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
    fields=['category','title','status','local_path','url','final_url','retrieved_at','bytes','pages','sha256','note','error']
    with (ROOT/'99_索引与日志/资料来源清单.csv').open('w',encoding='utf-8-sig',newline='') as out:
        w=csv.DictWriter(out,fieldnames=fields,extrasaction='ignore');w.writeheader();w.writerows(rows)
    good=[r for r in rows if r['status']=='ok']
    print(json.dumps({'total_sources':len(rows),'downloaded':len(good),'pdf':sum(r['local_path'].endswith('.pdf') for r in good),
                      'MB':round(sum(r['bytes'] for r in good)/1048576,1)},ensure_ascii=False),flush=True)

def official():
    base='https://www.contest.comap.com/highschool/contests/himcm/'
    archive=fetch(base+'previous%20problems.html','02_历年真题','HiMCM 历年官方目录','历年官方目录.html')
    rules=fetch(base+'instructions.html','01_官方规则与模板','2026 HiMCM 官方规则','2026_官方规则.html')
    jobs=[]
    for u,t in links(archive):
        leaf=unquote(urlparse(u).path).rsplit('/',1)[-1]
        if re.fullmatch(r'(?:\d{4}|4th)(?:problems?|results)\.html',leaf,re.I):
            year=re.search(r'\d{4}',leaf)
            year=year.group() if year else '2001_November'
            cat=('02_历年真题/' if 'problem' in leaf.lower() else '03_论文与评审/历年官方结果/')+year
            jobs.append((u,cat,year+' '+t,leaf))
    yearrows=batch(dict((j[0],j) for j in jobs).values())
    docs=[]
    for row in [rules]+yearrows:
        for u,t in links(row):
            ext=Path(unquote(urlparse(u).path)).suffix.lower()
            if ext not in ('.pdf','.doc','.docx','.tex','.csv','.xlsx','.xls','.zip','.txt'):continue
            if 'im' in Path(urlparse(u).path).name.lower() and 'immc' in u.lower():continue
            if 'problem' in row['category'] or row['category'].startswith('02_'):
                cat=row['category']
                if 'midmcm' in u.lower():cat=cat.replace('02_历年真题/','02_历年真题/MidMCM_补充练习/')
            elif row==rules:
                cat='03_论文与评审/官方评审' if 'cons_' in u.lower() else '01_官方规则与模板'
            else:
                if not any(x in u.lower() for x in ['himcm','midmcm']):continue
                cat=row['category']
            docs.append((u,cat,t,None,'由 COMAP 官方页面直接链接；历史年份规则不代表现行规则'))
    latest=fetch(base+'2025problems.html','02_历年真题/2025')
    for u,t in links(latest):
        if any(u.lower().endswith(x) for x in ['.tex','.docx']): docs.append((u,'01_官方规则与模板',t))
    batch(dict((j[0],j) for j in docs).values())
    export()

if __name__=='__main__':
    import sys
    if len(sys.argv)>1 and sys.argv[1]=='official':official()
    else:export()
