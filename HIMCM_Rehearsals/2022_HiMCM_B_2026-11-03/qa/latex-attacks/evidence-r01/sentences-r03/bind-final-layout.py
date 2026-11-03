from pathlib import Path
import hashlib,json,re,unicodedata
ROOT=Path(__file__).resolve().parents[4]
OUT=Path(__file__).resolve().parent
OLD=OUT.parent/'sentences-r02'
sha=lambda p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
htext=lambda s:hashlib.sha256(s.encode()).hexdigest()
pins={'paper/latex-r01/manuscript-r05.tex':'1f8259757db5732f38d5cf69b37419c98f1725270559d90b1e82ba8839d92b55','paper/latex-r01/build-r05/manuscript-r05.pdf':'2ec474ac04debd26d8acbf4b3393ba46e220536415d19e324597770ec7629aac','paper/latex-r01/sentence-register-r06.json':'2a7a89c62ceeef6c7aae688a81e506edcc957022110d62411f24ed0bd446bd3c'}
assert all(sha(p)==h for p,h in pins.items())
TEX,PDF,REG=list(pins)
previous=json.loads((OLD/'sentence-ledger.json').read_text())
assert all(sha(p)==h for p,h in previous['targets'].items())
old={r['id']:r for r in previous['records']}
reg=json.loads((ROOT/REG).read_text())
new={r['id']:r for r in reg['sentences']}
assert len(old)==len(new)==314 and old.keys()==new.keys()
assert all(old[i]['exact_text']==new[i]['sentence'] and old[i]['text_sha256']==htext(new[i]['sentence']) for i in old)
assert all(r['verdict']=='PASS_FOR_STATED_SCOPE' for r in old.values())
provenance={'immediate_prior_ledger':str((OLD/'sentence-ledger.json').relative_to(ROOT)),'immediate_prior_ledger_sha256':sha(str((OLD/'sentence-ledger.json').relative_to(ROOT))),'immediate_prior_review':str((OLD/'review.md').relative_to(ROOT)),'immediate_prior_review_sha256':sha(str((OLD/'review.md').relative_to(ROOT))),'original_full_review_chain':previous['provenance'],'prior_accepted_targets':previous['targets']}
records=[]
for s in reg['sentences']:
 before=old[s['id']]
 records.append({'id':s['id'],'exact_text':s['sentence'],'text_sha256':htext(s['sentence']),'source_line':s['source_line'],'block_id':s['block_id'],'block_tex_sha256':htext(s['block_tex']),'source_tex_sha256':pins[TEX],'evidence_refs':before['evidence_refs'],'rationale':before['rationale'],'verdict':'PASS_FOR_STATED_SCOPE','review_mode':'EXACT_TEXT_AND_CONTEXT_CARRY_FORWARD_AFTER_LAYOUT_ONLY_VERIFICATION','required_repair':None,'provenance':{'prior_record_id':before['id'],'prior_text_sha256':before['text_sha256'],'prior_ledger_sha256':provenance['immediate_prior_ledger_sha256'],'original_review_record':before['original_review_record'],'prior_review_mode':before['review_mode']}})
oldsource=json.loads((OLD/'evidence-sources.json').read_text())
checked=[]
for entries in oldsource.values():
 for e in entries:
  assert sha(e['path'])==e['sha256']
  checked.append(e)
sources=dict(oldsource)
sources['TEX']=[{'path':p,'sha256':sha(p)} for p in [TEX,PDF,'paper/latex-r01/build-r05/manuscript-r05.log','paper/latex-r01/build-r05/manuscript-r05.aux','paper/latex-r01/build-r05/manuscript-r05.toc']]
(OUT/'evidence-sources.json').write_text(json.dumps(sources,indent=2)+'\n')
final={'reviewer':'A07','verdict':'ACCEPTED_FOR_SCOPE','scope':'Complete sentence factual, numerical and evidence review, plus exact final source/PDF text binding. Not all-page visual/layout acceptance.','targets':pins,'counts':{'records':314,'exact_text_carry_forward':314,'changed_sentence_texts':0,'added_sentence_ids':0,'removed_sentence_ids':0,'outstanding_findings':0},'provenance':provenance,'records':records}
(OUT/'sentence-ledger.json').write_text(json.dumps(final,indent=2,ensure_ascii=False)+'\n')
md=['# A07 final layout-bound complete sentence ledger','','Canonical verdict: ACCEPTED_FOR_SCOPE. Scope: factual, numerical and evidentiary sentence review tied to exact r05 source/PDF and r06 register. Every sentence is text-identical to the accepted r03 candidate and carries its complete judgment with original-review provenance. All-page visual QA is separate.','']
for r in records:
 md += [f"## {r['id']} — {r['verdict']}",'',r['exact_text'],'',f"Text SHA-256: `{r['text_sha256']}`. Current TeX line {r['source_line']}.",'',f"Evidence: {', '.join(r['evidence_refs'])}. {r['rationale']}",'',f"Provenance: exact-text carry-forward from {r['provenance']['prior_record_id']} in ledger SHA-256 `{r['provenance']['prior_ledger_sha256']}`.",'']
(OUT/'sentence-ledger.md').write_text('\n'.join(md))
# Verify full TeX differs only by inspected layout controls.
previous_tex=(ROOT/'paper/latex-r01/manuscript-r03.tex').read_text()
tex=(ROOT/TEX).read_text()
expected=previous_tex.replace('\\setlength{\\emergencystretch}{1em}\n','\\setlength{\\emergencystretch}{1em}\n\\widowpenalty=10000\n\\clubpenalty=10000\n\\displaywidowpenalty=10000\n')
for block in ['DEC01','CO202','CO203','CO205','CO207','VAL02','TEM01','TEM03','ENV01']:
 expected=re.sub(r'(\\p\{'+block+r'\}[^\n]*)(\n)',lambda m:m[1]+r'\nopagebreak'+m[2],expected)
expected=expected.replace('\\section{Conclusions}\\label{sec:conclusion}',r'\clearpage'+'\n'+r'\section{Conclusions}\label{sec:conclusion}')
assert expected==tex
# All mathematical, tabular and separate label contents retain exact identities.
oldnon={r['id']:r for r in json.loads((OLD/'non-sentence-ledger.json').read_text())}
non=[]
for n in reg['non_sentence_content']:
 raw=n.get('exact_tex',n.get('extracted_text',n.get('text','')))
 prior=oldnon[n['id']]
 assert prior['content_sha256']==htext(raw)
 if n.get('path'):assert sha(str(Path(n['path']).relative_to(ROOT)))==n['sha256']
 non.append({**prior,'review_mode':'EXACT_CONTENT_CARRY_FORWARD_TO_LAYOUT_ONLY_FINAL','current_source_line':n.get('source_line'),'current_source_tex_sha256':pins[TEX]})
assert len(non)==54
(OUT/'non-sentence-ledger.json').write_text(json.dumps(non,indent=2,ensure_ascii=False)+'\n')
# Independent balanced-brace inventory protects against omitted or newly inserted prose.
def balanced(s,p):
 assert s[p]=='{'
 d=0
 for j in range(p,len(s)):
  if j and s[j-1]=='\\':continue
  if s[j]=='{':d+=1
  elif s[j]=='}':
   d-=1
   if d==0:return s[p+1:j],j+1
 raise ValueError('unbalanced source')
body=tex.split(r'\begin{document}',1)[1].split(r'\end{document}',1)[0]
blocks=[]
for m in re.finditer(r'\\(?:p|txt)\{',body):
 id,end=balanced(body,m.end()-1)
 content,finish=balanced(body,end)
 blocks.append((id,content))
registered={b['block_id']:b for b in reg['prose_blocks']}
assert len(blocks)==93 and set(registered)=={b[0] for b in blocks}
for id,content in blocks:
 assert registered[id]['exact_tex']==content
 assert ' '.join(s['sentence'] for s in reg['sentences'] if s['block_id']==id)==registered[id]['display_text']
canon=lambda s:''.join(c for c in unicodedata.normalize('NFKC',s).lower() if c.isalnum())
pdftext=(OUT/'pdf-text.txt').read_text()
pages=pdftext.split('\f')[:-1]
clean=[]
for i,p in enumerate(pages,1):clean.append('\n'.join(l for l in p.splitlines() if l.strip()!=str(i) and not ('2022 HiMCM Problem B' in l and 'Retrospective practice' in l)))
single_unmatched=[s['id'] for s in reg['sentences'] if not any(canon(s['sentence']) in canon(p) for p in pages)]
remaining=[s['id'] for s in reg['sentences'] if canon(s['sentence']) not in canon(' '.join(clean))]
assert len(pages)==16 and not remaining
assert tex.count(';')+tex.count('；')==pdftext.count(';')+pdftext.count('；')==0
article_ids=[s['id'] for s in reg['sentences'] if s['id'].startswith('ART')]
assert all(canon(new[i]['sentence']) in canon(pages[14]) for i in article_ids)
primary=json.loads((OUT.parent/'sentences-r01/independent-numeric-checks.json').read_text())['primary_source_hashes']
assert all(sha(p)==h for p,h in primary.items())
writer='handoffs/T15/writer-visuals-r02.md'
assert sha(writer)=='788a1d3690c484a7a56728f4814b1480ad84cf93e791e5d47aebcbd2d7d401c4'
checks={'verdict':'ACCEPTED_FOR_SCOPE','scope':final['scope'],'targets':pins,'source_delta':'Exactly three pagination penalties, nine no-page-break controls after equation lead-ins, and a page break before Conclusions. No other source change.','text_identities_verified':314,'blocks_verified':93,'non_sentence_content_identities_verified':54,'all_accepted_scientific_output_hashes_unchanged':True,'scientific_files_checked':len(primary),'prior_evidence_bindings_checked':len(checked),'pdf_pages':len(pages),'pdf_single_page_unmatched_ids':single_unmatched,'pdf_remaining_unmatched_ids':remaining,'article_page':15,'article_records_on_page_15':len(article_ids),'source_combined_semicolons':0,'PDF_combined_semicolons':0,'writer_visual_receipt':{'path':writer,'sha256':sha(writer),'role':'Author receipt identity only, not a substitute for A07 text checks or T16 visual review'},'provenance':provenance}
(OUT/'final-binding-checks.json').write_text(json.dumps(checks,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({k:checks[k] for k in ['verdict','text_identities_verified','blocks_verified','non_sentence_content_identities_verified','pdf_pages','pdf_single_page_unmatched_ids','pdf_remaining_unmatched_ids','article_page','source_combined_semicolons','PDF_combined_semicolons']},indent=2))
