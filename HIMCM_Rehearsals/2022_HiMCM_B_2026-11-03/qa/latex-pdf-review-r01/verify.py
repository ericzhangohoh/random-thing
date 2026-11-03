from pathlib import Path
import json,hashlib,subprocess,re,unicodedata,shutil
from PIL import Image
import numpy as np
import pdfplumber
P=Path(__file__).resolve().parents[2];Q=Path(__file__).parent;L=P/'paper/latex-r01';PDF=L/'build-r05/manuscript-r05.pdf';checks=[]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def j(p):return json.loads(p.read_text())
def ck(n,v):assert v,n;checks.append(n)
def norm(s):return ''.join(c for c in unicodedata.normalize('NFKD',s).lower() if c.isalnum())
reg=j(L/'sentence-register-r06.json');author=j(L/'author-receipt-r05.json')
for path,h in (author['files']|author['additional_sources']).items():ck('author binding '+path,sha(P/path)==h)
ck('closed author handoff',sha(P/'handoffs/T15/writer-visuals-r02.md')=='788a1d3690c484a7a56728f4814b1480ad84cf93e791e5d47aebcbd2d7d401c4')
ck('closed author receipt',sha(L/'author-receipt-r05.json')=='852a2ed6006e5b257de2839d402959065783d8a4e94931ee3a5ccd9e374b8a93')
ck('314 register records',len(reg['sentences'])==314 and len({x['id'] for x in reg['sentences']})==314)
ck('93blocks54nonprose',len(reg['prose_blocks'])==93 and len(reg['non_sentence_content'])==54)
tex=(L/'manuscript-r05.tex').read_text()
for block in reg['prose_blocks']:ck('exact prose block '+block['block_id'],block['exact_tex'] in tex)
ledger_paths=['qa/latex-attacks/argument-r01/revised-r03/ledger.json','qa/latex-attacks/evidence-r01/sentences-r03/sentence-ledger.json','qa/latex-attacks/reader-r01/revised-r03/sentence-ledger.json']
for path in ledger_paths:
 led=j(P/path);rs=led['records'];ck('314 ordered IDs '+path,[x['id'] for x in rs]==[x['id'] for x in reg['sentences']])
 for a,b in zip(reg['sentences'],rs):
  text=b.get('exact_text',b.get('exact_registered_text'));ck(path+' '+a['id'],text==a['sentence'] and b['text_sha256']==hashlib.sha256(text.encode()).hexdigest() and b['verdict'] in ['PASS','FRAGMENT_PASS','PASS_FOR_STATED_SCOPE'] and not b.get('required_repair') and not b.get('repair'))
 # Verify immediate prior ledger binding for every carried record.
 for b in rs:
  prov=b.get('provenance',{});pp=prov.get('prior_ledger');ph=prov.get('prior_ledger_sha256')
  if pp and ph:ck('prior ledger '+path+' '+b['id'],sha(P/pp)==ph)
 texts=json.dumps(led);ck('final target binding '+path,reg['source_sha256'] in texts and reg['pdf_sha256'] in texts and sha(L/'sentence-register-r06.json') in texts)
extracts=[]
for name,pdf in [('final',PDF),('rebuild',Q/'rebuild/manuscript-r05.pdf')]:
 r=subprocess.run(['/opt/homebrew/bin/pdftotext','-layout',str(pdf),'-'],capture_output=True,text=True,check=True);(Q/(name+'-text.txt')).write_text(r.stdout);extracts.append(r.stdout)
 ck(name+'16 pages',r.stdout.count('\f')==16)
 ck(name+'0 semicolons',r.stdout.count(';')+r.stdout.count('；')==0)
fonts=subprocess.run(['/opt/homebrew/bin/pdffonts',str(PDF)],capture_output=True,text=True,check=True).stdout;(Q/'pdffonts.txt').write_text(fonts)
ck('font inventory actual TNR', 'TimesNewRomanPSMT' in fonts and 'TimesNewRomanPS-BoldMT' in fonts and 'TimesNewRomanPS-ItalicMT' in fonts)
ck('no font fallback',not any(x in fonts for x in ['LatinModern','LMRoman','DejaVu','Helvetica']))
ck('all fonts embedded',all(re.search(r'\s+yes\s+yes\s+(yes|no)\s+\d+',line) for line in fonts.splitlines()[2:] if line.strip()))
ck('identical extracted rebuilt content',extracts[0]==extracts[1])
ck('zero source semicolons',tex.count(';')+tex.count('；')==0)
body='\n'.join(line for line in extracts[0].splitlines() if not re.fullmatch(r'\s*\d+\s*',line) and not ('2022 HiMCM Problem B' in line and 'Retrospective practice' in line))
missing=[x['id'] for x in reg['sentences'] if norm(x['sentence']) not in norm(body)];ck('314 final PDF text matches',not missing)
log=(Q/'rebuild/manuscript-r05.log').read_text();ck('clean independent final log',not re.search(r'Warning|Overfull|Underfull|Missing character|undefined',log))
ck('same resolved toc',(Q/'rebuild/manuscript-r05.toc').read_bytes()==(L/'build-r05/manuscript-r05.toc').read_bytes())
pagefonts=[]
with pdfplumber.open(PDF) as pdf:
 for i,p in enumerate(pdf.pages,1):
  fs=sorted({c['fontname'] for c in p.chars});pagefonts.append({'page':i,'fonts':fs});ck('TNR present page'+str(i),any('TimesNewRoman' in f for f in fs))
for i in range(1,17):
 a=np.asarray(Image.open(Q/f'render/page-{i:02}.png').convert('RGB'));ck('monochrome page'+str(i),np.array_equal(a[:,:,0],a[:,:,1]) and np.array_equal(a[:,:,1],a[:,:,2]))
for i in range(1,7):
 fp=P/f'figures/latex-r01/F{i:02}-r02.pdf';f=subprocess.run(['/opt/homebrew/bin/pdffonts',str(fp)],capture_output=True,text=True,check=True).stdout;ck('TNR plot labels '+str(i),'TimesNewRomanPSMT' in f and not any(x in f for x in ['DejaVu','Helvetica','LatinModern']));(Q/f'figure-{i}-fonts.txt').write_text(f)
c=j(P/'control/accepted-claims-latex-r01.json')
for path,h in c['additional_claims'][0]['evidence_sha256'].items():ck('C18 evidence '+path,sha(P/path)==h)
manifest=j(P/'runs/T05-scientific-20261103-r03/manifest.json')
for x in manifest['outputs']:ck('unchanged primary '+x['path'],sha(P/x['path'])==x['sha256'])
(Q/'checks.json').write_text(json.dumps({'status':'PASS','count':len(checks),'checks':checks,'all314_pdf_matches':not missing,'semicolon_count':0,'rebuild_text_exact_equal':True,'binary_pdf_identity_not_claimed':True,'page_fonts':pagefonts},indent=2)+'\n');print('PASS',len(checks))
