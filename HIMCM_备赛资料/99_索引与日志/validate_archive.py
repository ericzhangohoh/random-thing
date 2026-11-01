#!/usr/bin/env python3
"""Check downloaded bytes and document structure without running attachments."""
import concurrent.futures as cf
import hashlib
import json
import subprocess
import zipfile
from collections import Counter
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
rows={}
for l in (ROOT/'99_索引与日志/manifest.jsonl').read_text().splitlines():
    r=json.loads(l);rows[r['url']]=r

def check(r):
    p=ROOT/r['local_path']
    out={'local_path':r['local_path'],'sha256_match':False,'status':'error'}
    try:
        body=p.read_bytes()
        out['sha256_match']=hashlib.sha256(body).hexdigest()==r['sha256']
        if len(body)!=r['bytes'] or not out['sha256_match']:raise ValueError('size/hash mismatch')
        if p.suffix.lower()=='.pdf':
            result=subprocess.run(['qpdf','--check',str(p)],capture_output=True,text=True,timeout=35)
            out['qpdf_exit_code']=result.returncode
            out['diagnostic']=(result.stdout+'\n'+result.stderr)[-4500:]
            if result.returncode not in (0,3):raise ValueError('qpdf reported a structural error')
            out['status']='warning' if result.returncode==3 else 'ok'
        elif p.suffix.lower() in ('.zip','.docx','.xlsx'):
            with zipfile.ZipFile(p) as z:
                bad=z.testzip()
                if bad:raise ValueError('ZIP CRC failed: '+bad)
                if p.suffix.lower()=='.docx' and 'word/document.xml' not in z.namelist():raise ValueError('not a Word document')
                if p.suffix.lower()=='.xlsx' and 'xl/workbook.xml' not in z.namelist():raise ValueError('not an Excel workbook')
            out['status']='ok'
        else:out['status']='ok'
    except Exception as e:out['error']=str(e)
    return out

with cf.ThreadPoolExecutor(max_workers=4) as pool:
    result=list(pool.map(check,[r for r in rows.values() if r['status']=='ok']))
summary={'sources':len(rows),'downloaded':len(result),'checks':dict(Counter(r['status'] for r in result)),
         'scope':'SHA-256/size for all files; qpdf --check for every PDF; ZIP CRC and format checks for DOCX/XLSX/ZIP; not a mathematical correctness review',
         'results':result}
(ROOT/'99_索引与日志/文件校验报告.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in summary.items() if k!='results'},ensure_ascii=False))
for r in result:
    if r['status']!='ok':print(json.dumps(r,ensure_ascii=False))
