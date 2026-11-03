from pathlib import Path
import collections, hashlib, json, re, subprocess, unicodedata

ROOT=Path(__file__).resolve().parents[4]
OUT=Path(__file__).resolve().parent
OLD=OUT.parent/'revised-r01'
P=ROOT/'paper/latex-r01'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
targets={
 P/'manuscript-r03.tex':'2c86588b978e271eaafae26f89a4adada724316981586051f5566d509c610685',
 P/'build-r03/manuscript-r03.pdf':'4b9457da90c3b7a91343a0570fe1072a5bd5f7ff52aa36ecae10d80b687c3ff4',
 P/'sentence-register-r04.json':'ef5ac7a999d90934b0e686cc0b36c80f6a69d6686f105f9c7431537b64c73f33',
 P/'sentence-delta-r03.json':'b7c46ade1e8d4cc6fc549906ce23d50749fa4c840dbf3cc2b9f1cc30703ccf72',
}
assert all(sha(p)==h for p,h in targets.items())
assert sha(OLD/'ledger.json')=='a154b07f075accf98b0df61c55e908f2d549c6f2cc2e07e49d2a2caea259baba'
oldreg=json.loads((P/'sentence-register-r03.json').read_text())
reg=json.loads((P/'sentence-register-r04.json').read_text())
old={r['id']:r for r in oldreg['sentences']}
new={r['id']:r for r in reg['sentences']}
prior={r['id']:r for r in json.loads((OLD/'ledger.json').read_text())['records']}
changed=[k for k in new if k in old and new[k]['sentence']!=old[k]['sentence']]
added=[k for k in new if k not in old]
same=[k for k in new if k in old and new[k]['sentence']==old[k]['sentence']]
removed=list(set(old)-set(new))
assert (len(changed),len(added),len(same),len(removed))==(16,3,295,0)
claimed=json.loads((P/'sentence-delta-r03.json').read_text())
assert {x['id'] for x in claimed['changed_or_added']}==set(changed+added)
assert {x['id'] for x in claimed['unchanged_by_exact_identity']}==set(same)
for x in claimed['changed_or_added']:
 assert x['new_sentence']==new[x['id']]['sentence']
 assert x['old_sentence']==old.get(x['id'],{}).get('sentence')
notes={}
for line in (OUT/'delta-notes.txt').read_text().splitlines():
 k,v,n=line.split('|',2);notes[k]=(v,n)
assert set(notes)==set(changed+added+['DAT02.05'])

for option,name in [('-raw','rendered-raw.txt'),('-layout','rendered-layout.txt')]:
 subprocess.run(['pdftotext',option,str(P/'build-r03/manuscript-r03.pdf'),str(OUT/name)],check=True)
raw=(OUT/'rendered-raw.txt').read_text();layout=(OUT/'rendered-layout.txt').read_text()
def norm(t): return ''.join(c.lower() for c in unicodedata.normalize('NFKD',t) if c.isalnum())
clean=re.sub(r'2022 HiMCM Problem B\s*Retrospective practice','',raw)
clean=re.sub(r'(?m)^\d+\s*\f','',clean)
remainder=norm(clean)
records=[]
for s in reg['sentences']:
 k=s['id'];text=s['sentence'];text_hash=hashlib.sha256(text.encode()).hexdigest()
 assert norm(text) in remainder,k
 remainder=remainder.replace(norm(text),'',1)
 if k in same:
  assert prior[k]['exact_registered_text']==text
  assert prior[k]['text_sha256']==text_hash
  row=dict(prior[k])
  method='exact_text_identity_carry_forward'
 else:
  row={'id':k,'register_kind':s['kind'],'reviewer_classification':'sentence','checked_dimensions':['argument_role','natural_cadence','precision_and_qualifiers','surrounding_TeX_context','rendered_text_presence']}
  method='fresh_changed_or_added_sentence_review'
 if k in notes:
  row['verdict'],row['specific_rationale_or_repair']=notes[k]
  if k=='DAT02.05':method='exact_text_identity_plus_fresh_adjacent_context_reassessment'
 row.update(exact_registered_text=text,text_sha256=text_hash,source_line=s['source_line'],block_id=s['block_id'],independent_pdf_match=True)
 row['provenance']={'method':method,'prior_ledger_path':str((OLD/'ledger.json').relative_to(ROOT)) if k in prior else None,'prior_ledger_sha256':sha(OLD/'ledger.json') if k in prior else None,'prior_text_sha256':prior[k]['text_sha256'] if k in prior else None,'prior_verdict':prior[k]['verdict'] if k in prior else None,'fresh_note_file':'delta-notes.txt' if k in notes else None}
 records.append(row)
assert len(records)==314 and not any(x['verdict'] in ['NOTE','REPAIR'] for x in records)
(OUT/'normalized-remainder.txt').write_text(remainder)

tex=(P/'manuscript-r03.tex').read_text();body=tex[tex.index('\\begin{document}'):]
def group(t,p):
 assert t[p]=='{'
 d=1;start=p+1;p+=1
 while d:
  if t[p]=='\\':p+=2;continue
  if t[p]=='{':d+=1
  elif t[p]=='}':d-=1
  p+=1
 return t[start:p-1],p
spans=[];blocks=[]
for m in re.finditer(r'\\(?:p|txt)\{',body):
 k,pos=group(body,m.end()-1);val,end=group(body,pos);blocks.append(k);spans.append((m.start(),end))
assert set(blocks)=={x['block_id'] for x in reg['sentences']}
masked=list(body)
for a,b in spans:masked[a:b]=['\n' if c=='\n' else ' ' for c in body[a:b]]
residue=re.sub(r'\\begin\{(equation|align|tabular)\}.*?\\end\{\1\}','',''.join(masked),flags=re.S)
(OUT/'unregistered-source-residue.tex').write_text('\n'.join(x.strip() for x in residue.splitlines() if x.strip())+'\n')
oldnp={x['id']:x for x in oldreg['non_sentence_content']}
changednp=[]
for x in reg['non_sentence_content']:
 fields=['exact_tex','text','extracted_text','kind']
 if any(x.get(f)!=oldnp[x['id']].get(f) for f in fields):changednp.append(x['id'])
 if x['kind']=='plot_labels_annotations_legend_ticks':assert sha(Path(x['path']))==x['sha256']
assert changednp==['figure-labels-05']
figtext=subprocess.check_output(['pdftotext','-raw',str(ROOT/'figures/latex-r01/F05-r02.pdf'),'-'],text=True)
assert 'Fitted log-CO2 curve' in figtext and 'Accepted log-CO2 fit' not in figtext
(OUT/'F05-text.txt').write_text(figtext)
stats={'canonical_verdict':'ACCEPTED_FOR_ARGUMENT_PROSE_PRECISION_AND_TEXT_COVERAGE_ON_EXACT_R03','target_hashes':{str(p.relative_to(ROOT)):sha(p) for p in targets},'records':314,'unchanged_exact_identity':295,'changed':16,'added':3,'removed':0,'straight_carry_forward':294,'unchanged_but_context_reassessed':['DAT02.05'],'fresh_changed_or_added_reviews':19,'verdict_counts':dict(collections.Counter(x['verdict'] for x in records)),'prose_blocks':len(blocks),'unmatched_pdf_records':[],'nonprose_entries':len(reg['non_sentence_content']),'changed_nonprose_content':changednp,'semicolons':{name:{'ascii':t.count(';'),'fullwidth':t.count('；')} for name,t in [('source',tex),('pdf_raw',raw),('pdf_layout',layout)]},'prior_ledger_sha256':sha(OLD/'ledger.json'),'scope_limits':'Text presence is not visual or font acceptance. No target edits or numerical rerun. Acceptance does not extend to later bytes.'}
for name,obj in [('ledger.json',{'review':stats,'records':records}),('verification.json',stats),('independent-delta.json',{'changed':changed,'added':added,'unchanged':same,'removed':removed})]:
 tmp=OUT/(name+'.tmp');tmp.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n');tmp.replace(OUT/name)
md=['# A06 final 314-record ledger for exact r03','','Every carried judgment requires exact ID/text/hash identity. Changed/new records were freshly read with their complete paragraphs. DAT02.05 is unchanged but was reassessed beside the added vintage paragraph.','','| ID | Exact text | Verdict | Specific rationale | Provenance |','|---|---|---|---|---|']
for r in records:
 md.append('| '+' | '.join(str(r[k]).replace('|','\\|') for k in ['id','exact_registered_text','verdict','specific_rationale_or_repair'])+' | '+r['provenance']['method']+' |')
tmp=OUT/'ledger.md.tmp';tmp.write_text('\n'.join(md)+'\n');tmp.replace(OUT/'ledger.md')
assert all(sha(p)==h for p,h in targets.items())
print(json.dumps(stats,indent=2))
