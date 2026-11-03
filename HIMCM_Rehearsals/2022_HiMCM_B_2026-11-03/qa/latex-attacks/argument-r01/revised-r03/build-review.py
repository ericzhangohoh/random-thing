from pathlib import Path
import collections,hashlib,json,re,subprocess,unicodedata,difflib

ROOT=Path(__file__).resolve().parents[4];OUT=Path(__file__).resolve().parent
PREV=OUT.parent/'revised-r02';P=ROOT/'paper/latex-r01'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
targets={P/'manuscript-r05.tex':'1f8259757db5732f38d5cf69b37419c98f1725270559d90b1e82ba8839d92b55',P/'build-r05/manuscript-r05.pdf':'2ec474ac04debd26d8acbf4b3393ba46e220536415d19e324597770ec7629aac',P/'sentence-register-r06.json':'2a7a89c62ceeef6c7aae688a81e506edcc957022110d62411f24ed0bd446bd3c'}
assert all(sha(p)==h for p,h in targets.items())
assert sha(PREV/'ledger.json')=='1cef09881b045272729d396769fe3d47bf58977e90ae894d96ada89e26a3e6fc'
reg=json.loads((P/'sentence-register-r06.json').read_text())
oldreg=json.loads((P/'sentence-register-r04.json').read_text())
prior=json.loads((PREV/'ledger.json').read_text());old={x['id']:x for x in prior['records']}
assert {x['id'] for x in reg['sentences']}==set(old)
assert len(reg['sentences'])==314
for option,name in [('-raw','rendered-raw.txt'),('-layout','rendered-layout.txt')]:
 subprocess.run(['pdftotext',option,str(P/'build-r05/manuscript-r05.pdf'),str(OUT/name)],check=True)
raw=(OUT/'rendered-raw.txt').read_text();layout=(OUT/'rendered-layout.txt').read_text()
def norm(t):return ''.join(c.lower() for c in unicodedata.normalize('NFKD',t) if c.isalnum())
clean=re.sub(r'2022 HiMCM Problem B\s*Retrospective practice','',raw)
clean=re.sub(r'(?m)^\d+\s*\f','',clean);rem=norm(clean)
rows=[]
for s in reg['sentences']:
 p=old[s['id']];h=hashlib.sha256(s['sentence'].encode()).hexdigest()
 assert p['exact_registered_text']==s['sentence'] and p['text_sha256']==h
 assert norm(s['sentence']) in rem
 rem=rem.replace(norm(s['sentence']),'',1)
 row=dict(p);row['source_line']=s['source_line'];row['independent_pdf_match']=True
 row['prior_provenance']=p['provenance']
 row['provenance']={'method':'exact_ID_text_SHA256_carry_forward_after_layout_only_source_diff_review','prior_ledger':str((PREV/'ledger.json').relative_to(ROOT)),'prior_ledger_sha256':sha(PREV/'ledger.json'),'prior_text_sha256':p['text_sha256'],'prior_verdict':p['verdict'],'new_target_source':'paper/latex-r01/manuscript-r05.tex','new_target_register':'paper/latex-r01/sentence-register-r06.json'}
 rows.append(row)
(OUT/'normalized-remainder.txt').write_text(rem)
oldrem=(PREV/'normalized-remainder.txt').read_text()
assert re.sub(r'\d','',rem)==re.sub(r'\d','',oldrem)
residue_changes=[]
for tag,a,b,c,d in difflib.SequenceMatcher(None,oldrem,rem,autojunk=False).get_opcodes():
 if tag!='equal':
  assert (not oldrem[a:b] or oldrem[a:b].isdigit()) and (not rem[c:d] or rem[c:d].isdigit())
  residue_changes.append({'old':oldrem[max(0,a-40):b+40],'new':rem[max(0,c-40):d+40]})
oldnp={x['id']:x for x in oldreg['non_sentence_content']}
for x in reg['non_sentence_content']:
 assert {k:v for k,v in x.items() if k!='source_line'}=={k:v for k,v in oldnp[x['id']].items() if k!='source_line'}
 if x['kind']=='plot_labels_annotations_legend_ticks':assert sha(Path(x['path']))==x['sha256']
tex=(P/'manuscript-r05.tex').read_text();oldtex=(P/'manuscript-r03.tex').read_text()
def unlayout(t):
 t=re.sub(r'\\(?:widowpenalty|clubpenalty|displaywidowpenalty)=10000\n','',t)
 t=t.replace('\\nopagebreak','')
 return t.replace('\\clearpage\n\\section{Conclusions}','\\section{Conclusions}')
assert unlayout(tex)==unlayout(oldtex)
blocks=re.findall(r'\\(?:p|txt)\{([^}]+)\}',tex[tex.index('\\begin{document}'):])
assert len(blocks)==93 and set(blocks)=={x['block_id'] for x in reg['sentences']}
stats={'canonical_verdict':'ACCEPTED_FOR_SCOPE','scope':'Argument, natural prose cadence, precision, registered text identity, omission search and semicolon compliance on exact r05/r06. Excludes all-page visual, font and numerical-run acceptance.','target_hashes':{str(p.relative_to(ROOT)):sha(p) for p in targets},'prior_accepted_ledger_sha256':sha(PREV/'ledger.json'),'records':314,'exact_ID_text_hash_matches':314,'changed':0,'added':0,'removed':0,'pdf_matches':314,'unmatched_ids':[],'prose_blocks':93,'nonprose_inventory_exact_content_matches':54,'source_difference':'Only three page-breaking penalties, nine nopagebreak commands after equation lead-ins, and a clearpage before Conclusions.','omission_check':'PDF residue differences independently inspected: only TOC page-number updates. No alphabetic change. Source equal after removing explicit layout-only changes.','pdf_residue_changes':residue_changes,'semicolons':{k:{'ascii':t.count(';'),'fullwidth':t.count('；')} for k,t in [('source',tex),('pdf_raw',raw),('pdf_layout',layout)]},'verdict_counts':dict(collections.Counter(x['verdict'] for x in rows))}
assert tex.count('\\nopagebreak')==9
assert all(v['ascii']==v['fullwidth']==0 for v in stats['semicolons'].values())
for name,obj in [('verification.json',stats),('ledger.json',{'review':stats,'records':rows})]:
 tmp=OUT/(name+'.tmp');tmp.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n');tmp.replace(OUT/name)
md=['# A06 final r05/r06 complete 314-record ledger','','All individual judgments carry forward only after exact ID, text and SHA-256 equality against the independently accepted r03 ledger. Layout-only source differences and final PDF text were checked again. Each JSON row preserves both immediate and earlier provenance.','','| ID | Exact registered text | Verdict | Individual rationale |','|---|---|---|---|']
for x in rows:md.append('| '+' | '.join(str(x[k]).replace('|','\\|') for k in ['id','exact_registered_text','verdict','specific_rationale_or_repair'])+' |')
tmp=OUT/'ledger.md.tmp';tmp.write_text('\n'.join(md)+'\n');tmp.replace(OUT/'ledger.md')
assert all(sha(p)==h for p,h in targets.items())
print(json.dumps({k:v for k,v in stats.items() if k!='pdf_residue_changes'},indent=2))
