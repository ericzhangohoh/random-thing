from pathlib import Path
import hashlib,json,re,unicodedata,subprocess
from collections import Counter
ROOT=Path(__file__).resolve().parents[4]
OUT=Path(__file__).resolve().parent
OLD=OUT.parent/'sentences-r01'
sha=lambda p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
hashtext=lambda s:hashlib.sha256(s.encode()).hexdigest()
pins={'paper/latex-r01/manuscript-r03.tex':'2c86588b978e271eaafae26f89a4adada724316981586051f5566d509c610685','paper/latex-r01/build-r03/manuscript-r03.pdf':'4b9457da90c3b7a91343a0570fe1072a5bd5f7ff52aa36ecae10d80b687c3ff4','paper/latex-r01/sentence-register-r04.json':'ef5ac7a999d90934b0e686cc0b36c80f6a69d6686f105f9c7431537b64c73f33','paper/latex-r01/sentence-delta-r03.json':'b7c46ade1e8d4cc6fc549906ce23d50749fa4c840dbf3cc2b9f1cc30703ccf72'}
assert all(sha(p)==h for p,h in pins.items())
TEX,PDF,REG,DELTA=list(pins)
previous=json.loads((OLD/'sentence-ledger.json').read_text())
assert all(sha(p)==h for p,h in previous['targets'].items())
oldreg=json.loads((ROOT/'paper/latex-r01/sentence-register-r03.json').read_text())
newreg=json.loads((ROOT/REG).read_text())
a={x['id']:x for x in oldreg['sentences']}
b={x['id']:x for x in newreg['sentences']}
changed=[i for i in b if i in a and a[i]['sentence']!=b[i]['sentence']]
added=[i for i in b if i not in a]
unchanged=[i for i in b if i in a and a[i]['sentence']==b[i]['sentence']]
removed=[i for i in a if i not in b]
assert (len(changed),len(added),len(unchanged),len(removed))==(16,3,295,0)
author=json.loads((ROOT/DELTA).read_text())
assert {x['id'] for x in author['changed_or_added']}==set(changed+added)
for x in author['changed_or_added']:
 assert x['new_sentence']==b[x['id']]['sentence']
 if x['id'] in a:assert x['old_sentence']==a[x['id']]['sentence']
manual={}
for line in (OUT/'manual-delta-assessments.txt').read_text().splitlines():
 id,refs,rationale=line.split('|',2)
 manual[id]={'evidence_refs':refs.split(','),'rationale':rationale}
assert set(manual)==set(changed+added)
oldledger={x['id']:x for x in previous['records']}
oldsources=json.loads((OLD/'evidence-sources.json').read_text())
source_checks=[]
for entries in oldsources.values():
 for entry in entries:
  assert sha(entry['path'])==entry['sha256']
  source_checks.append(entry)
sources=dict(oldsources)
sources['TEX']=[{'path':p,'sha256':sha(p)} for p in [TEX,PDF,'paper/latex-r01/build-r03/manuscript-r03.log','paper/latex-r01/build-r03/manuscript-r03.aux','paper/latex-r01/build-r03/manuscript-r03.toc']]
sources['FIG']=[{'path':p,'sha256':sha(p)} for p in ['code/visualization/latex-r01/render_figures-r02.py','paper/latex-r01/figure-register-r02.json']+[f'figures/latex-r01/F{i:02d}-r02.pdf' for i in range(1,7)]]
(OUT/'evidence-sources.json').write_text(json.dumps(sources,indent=2)+'\n')
provenance={'original_review_path':str((OLD/'review.md').relative_to(ROOT)),'original_review_sha256':sha(str((OLD/'review.md').relative_to(ROOT))),'original_ledger_path':str((OLD/'sentence-ledger.json').relative_to(ROOT)),'original_ledger_sha256':sha(str((OLD/'sentence-ledger.json').relative_to(ROOT))),'original_target_hashes':previous['targets'],'current_target_hashes':pins}
ledger=[]
for s in newreg['sentences']:
 id=s['id']
 kind='unchanged' if id in unchanged else 'changed' if id in changed else 'added'
 note=manual[id] if kind!='unchanged' else {k:oldledger[id][k] for k in ['evidence_refs','rationale']}
 if kind=='unchanged':
  assert oldledger[id]['verdict']=='PASS_FOR_STATED_SCOPE'
  assert oldledger[id]['text_sha256']==hashtext(s['sentence'])
 record={'id':id,'exact_text':s['sentence'],'text_sha256':hashtext(s['sentence']),'source_line':s['source_line'],'block_id':s['block_id'],'source_tex_sha256':pins[TEX],'block_tex_sha256':hashtext(s['block_tex']),**note,'verdict':'PASS_FOR_STATED_SCOPE','required_repair':None,'review_mode':'EXACT_TEXT_CARRY_FORWARD_AFTER_CONTEXT_DELTA_CHECK' if kind=='unchanged' else 'NEW_MANUAL_REVIEW_OF_TEXT_AND_CONTEXT','change_kind':kind,'original_review_record':None if kind=='added' else {'id':id,'text_sha256':oldledger[id]['text_sha256'],'verdict':oldledger[id]['verdict'],'ledger_sha256':provenance['original_ledger_sha256']}}
 ledger.append(record)
final={'reviewer':'A07','verdict':'ACCEPTED_FOR_EXACT_REVISED_TEXT_EVIDENCE_SCOPE','targets':pins,'provenance':provenance,'counts':{'records':314,'exact_text_carried':295,'manually_reread_changed':16,'manually_read_added':3,'unresolved_findings':0},'resolved_findings':['A07-F01','A07-F02'],'records':ledger}
(OUT/'sentence-ledger.json').write_text(json.dumps(final,indent=2,ensure_ascii=False)+'\n')
md=['# A07 complete final evidence sentence ledger','', 'Exact revised source is manuscript-r03.tex and exact register is sentence-register-r04.json. Evidence-source hashes are in evidence-sources.json. 295 exact-text judgments carry forward from the complete first review after delta/context verification. All 19 changed or new records have fresh manual judgments.','']
for r in ledger:
 md += [f"## {r['id']} — {r['verdict']}",'',f"Text: {r['exact_text']}",'',f"Text SHA-256: `{r['text_sha256']}`. TeX line {r['source_line']}. Review mode: {r['review_mode']}.",'',f"Evidence: {', '.join(r['evidence_refs'])}. {r['rationale']}",'']
(OUT/'sentence-ledger.md').write_text('\n'.join(md))
# Independent exact-content changes for all non-sentence items.
nonold={r['id']:r for r in oldreg['non_sentence_content']}
nonprior={r['id']:r for r in json.loads((OLD/'non-sentence-ledger.json').read_text())}
nonledger=[]
nonchanged=[]
for n in newreg['non_sentence_content']:
 id=n['id']
 content=n.get('exact_tex',n.get('extracted_text',n.get('text','')))
 before=nonold[id]
 oldcontent=before.get('exact_tex',before.get('extracted_text',before.get('text','')))
 if content!=oldcontent:nonchanged.append(id)
 note=nonprior[id]
 reason=note['rationale']
 if id=='figure-labels-05':
  assert content==oldcontent.replace('Accepted log-CO2 fit','Fitted log-CO2 curve')
  reason='Fresh review: only legend changes from Accepted log-CO2 fit to Fitted log-CO2 curve. It accurately names the stored fitted relationship. Axes, correlation labels and numeric data remain unchanged.'
 nonledger.append({'id':id,'kind':n['kind'],'exact_content':content,'content_sha256':hashtext(content),'evidence_refs':note['evidence_refs'],'rationale':reason,'verdict':'PASS_FOR_STATED_SCOPE','review_mode':'FRESH_LEGEND_REVIEW' if content!=oldcontent else 'EXACT_CONTENT_CARRY_FORWARD','artifact_path':n.get('path'),'artifact_sha256':n.get('sha256')})
assert nonchanged==['figure-labels-05']
(OUT/'non-sentence-ledger.json').write_text(json.dumps(nonledger,indent=2,ensure_ascii=False)+'\n')
# Check actual source environments rather than relying on content inventories.
oldtex=(ROOT/'paper/latex-r01/manuscript-r02.tex').read_text()
tex=(ROOT/TEX).read_text()
envchecks={}
for env in ['equation','align','tabular']:
 pat=r'\\begin\{'+env+r'\}.*?\\end\{'+env+r'\}'
 aa=re.findall(pat,oldtex,re.S)
 bb=re.findall(pat,tex,re.S)
 assert aa==bb
 envchecks[env]={'count':len(bb),'exactly_unchanged':True}
# Independently enumerate all tagged prose blocks with balanced braces.
def balanced(text,pos):
 assert text[pos]=='{'
 depth=0
 for j in range(pos,len(text)):
  if j>0 and text[j-1]=='\\':continue
  if text[j]=='{':depth+=1
  if text[j]=='}':
   depth-=1
   if depth==0:return text[pos+1:j],j+1
 raise ValueError('unbalanced')
body=tex.split(r'\begin{document}',1)[1].split(r'\end{document}',1)[0]
blocks=[]
for m in re.finditer(r'\\(?:p|txt)\{',body):
 id,end=balanced(body,m.end()-1)
 content,last=balanced(body,end)
 blocks.append((id,content,m.start(),last))
registered={r['block_id']:r for r in newreg['prose_blocks']}
assert len(blocks)==93 and set(registered)=={x[0] for x in blocks}
for id,content,_,_ in blocks:
 assert content==registered[id]['exact_tex']
 assert ' '.join(r['sentence'] for r in newreg['sentences'] if r['block_id']==id)==registered[id]['display_text']
residue=body
for _,_,start,end in reversed(blocks):residue=residue[:start]+'[REVIEWED BLOCK]'+residue[end:]
for env in ['equation','align','tabular']:
 residue=re.sub(r'\\begin\{'+env+r'\}.*?\\end\{'+env+r'\}','[REVIEWED '+env+']',residue,flags=re.S)
(OUT/'independent-source-residue.txt').write_text(residue)
canon=lambda s:''.join(c for c in unicodedata.normalize('NFKC',s).lower() if c.isalnum())
pdftext=(OUT/'pdf-text.txt').read_text()
pages=pdftext.split('\f')[:-1]
clean=[]
for i,page in enumerate(pages,1):clean.append('\n'.join(line for line in page.splitlines() if line.strip()!=str(i) and not ('2022 HiMCM Problem B' in line and 'Retrospective practice' in line)))
onepage_unmatched=[s['id'] for s in newreg['sentences'] if not any(canon(s['sentence']) in canon(p) for p in pages)]
unmatched=[s['id'] for s in newreg['sentences'] if canon(s['sentence']) not in canon(' '.join(clean))]
assert not unmatched
assert tex.count(';')+tex.count('；')==0 and pdftext.count(';')+pdftext.count('；')==0
assert len(pages)==15
c18_ids=[s['id'] for s in newreg['sentences'] if s['block_id']=='VAL06' or s['id']=='DIS04.03']
assert all(i in unchanged for i in c18_ids)
figchecks=[]
for i in range(1,7):
 p=f'figures/latex-r01/F{i:02d}-r02.pdf'
 h=sha(p)
 same=h==sha(f'figures/latex-r01/F{i:02d}-r01.pdf')
 assert same==(i!=5)
 figchecks.append({'path':p,'sha256':h,'bytes_identical_to_previous':same})
f5text=(OUT/'F05-text.txt').read_text()
assert 'Fitted log-CO2 curve' in f5text and 'Accepted log-CO2 fit' not in f5text
oldcode=(ROOT/'code/visualization/latex-r01/render_figures-r01.py').read_text()
newcode=(ROOT/'code/visualization/latex-r01/render_figures-r02.py').read_text()
assert newcode==oldcode.replace("f'{id}-r01.{ext}'","f'{id}-r02.{ext}'").replace('Accepted log-CO2 fit','Fitted log-CO2 curve').replace("figure-register-r01.json","figure-register-r02.json")
primary=json.loads((OLD/'independent-numeric-checks.json').read_text())['primary_source_hashes']
assert all(sha(p)==h for p,h in primary.items())
coverage={'targets':pins,'provenance':provenance,'independent_delta':{'unchanged_ids':unchanged,'changed_ids':changed,'added_ids':added,'removed_ids':removed,'author_delta_matches':True},'prose_blocks':93,'records':314,'independent_source_and_register_exactly_reconciled':True,'non_sentence_count':54,'non_sentence_content_changed':nonchanged,'mathematics_and_tables':envchecks,'C18_records_exactly_unchanged':c18_ids,'scientific_primary_files_checked_unchanged':len(primary),'prior_evidence_bindings_verified':len(source_checks),'figure_files':figchecks,'figure_code_only_changes':'Output r02 naming, register filename and F05 legend label. No data selection, metric, fit or plot coordinate code changed.','pdf_pages':len(pages),'pdf_single_page_unmatched':onepage_unmatched,'pdf_remaining_unmatched_after_header_footer_removal':unmatched,'source_combined_semicolons':0,'pdf_combined_semicolons':0}
(OUT/'delta-coverage-and-hashes.json').write_text(json.dumps(coverage,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({k:coverage[k] for k in ['prose_blocks','records','non_sentence_count','non_sentence_content_changed','pdf_pages','pdf_single_page_unmatched','pdf_remaining_unmatched_after_header_footer_removal','source_combined_semicolons','pdf_combined_semicolons']},indent=2))
