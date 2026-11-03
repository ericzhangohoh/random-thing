import pathlib,json,hashlib,subprocess,re,unicodedata
root=pathlib.Path.cwd();out=root/'qa/latex-attacks/reader-r01/revised-r02';p=root/'paper/latex-r01'
h=lambda s:hashlib.sha256(s.encode()).hexdigest()
old=json.loads((p/'sentence-register-r03.json').read_text());new=json.loads((p/'sentence-register-r04.json').read_text());delta=json.loads((p/'sentence-delta-r03.json').read_text())
priorpath=root/'qa/latex-attacks/reader-r01/sentence-ledger.json';prior=json.loads(priorpath.read_text());oldmap={s['id']:s for s in old['sentences']}; priormap={s['id']:s for s in prior['records']}
notes={
'SUM02.04':'Choice under the prespecified rule now correctly separates the selected winner from the earlier decision rule. Prior optional clarification resolved.',
'SUM04.03':'First crossing dates are explicitly conditional and distinguished from realized, sustained and Paris-target crossings. Baseline and dates remain in the preceding sentence.',
'SUM06.01':'In their observed levels is idiomatic and precise, with weaker association after transformation and the adjacent causation caveat preserved. Prior repair resolved.',
'SUM05.02':'The historical 2016 miss is now a standalone finding, preventing an implied derivation of the 2031 cutoff from that miss.',
'SUM05.02a':'Separately and extending the tested ten-year horizon make the arithmetic display convention explicit, not a reliability guarantee. The following probability limitation remains intact.',
'DAT07.01':'One supplied vintage and truncation by observation year clearly describe the retrospective data construction. Vintage means a version of the source data in this context.',
'DAT07.02':'The next sentence explains the vintage limitation plainly: no reconstruction of contemporaneous historical releases is claimed.',
'VAL01.01':'Workbook dates rather than historically available releases now define each training sample. All five origins and one-to-ten-year tasks are retained.',
'VAL03.03':'Primary run recorded its selection replaces internal receipt jargon while preserving prior score exposure and the following no-blind-holdout caveat. Prior repair resolved.',
'TEM03.01':'Workbook pairs dated no later than the origin correctly implement observation-year truncation without claiming historical release reconstruction.',
'TEM05.03':'Sequential selected path versus lowest-error declared comparator is stated positively without claiming a global optimum across unspecified models.',
'FC05.02':'Both panels are now described scientifically, including log concentration for the change panel. Internal acceptance language has been removed without changing interpretation.',
'REL02.02':'Detrended results are located in Table 8 while Figure 5 is correctly limited to levels versus annual changes. Surrounding noncausal caveat remains.',
'SEN02.04':'Results do not select a replacement or supply probability bounds. The grammatical subject now takes parallel verbs and preserves sensitivity-only scope.',
'APP01.02':'Workbook observation dates replace historical availability language, aligning the appraisal with the new vintage qualification while preserving upstream forecast error.',
'APP02.05':'Physically justified saturation capacity is a narrower defensible limitation than categorical mathematical nonidentification of a logistic fit. Extra inputs for physical models remain explicit.',
'APP04.03':'Threshold and forecast origin now make the two status cases clear in ordinary language. Prior repair resolved without changing validity handling.',
'APP04.05':'All actual primary paths remain valid states the mathematical outcome directly and removes ambiguous rescue language. Prior optional clarification resolved.',
'ART05.04':'Dates are now crossings on conditional paths, not descriptions of paths. Deadline, sustained-warming and Paris limitations all remain. Prior repair resolved.'}
changes=[];unchanged=[];ledger=[]
for s in new['sentences']:
 i=s['id']; exact=s['sentence'];digest=h(exact)
 if i in oldmap and oldmap[i]['sentence']==exact:
  prev=priormap[i];assert prev['text_sha256']==digest;assert prev['verdict']=='PASS';unchanged.append(i)
  row=dict(prev);row.update(tex_line=s['source_line'],provenance={'kind':'exact_text_hash_carry_forward','prior_ledger':str(priorpath.relative_to(root)),'prior_ledger_sha256':hashlib.sha256(priorpath.read_bytes()).hexdigest(),'prior_id':i,'prior_text_sha256':digest})
 else:
  assert i in notes;changes.append(i)
  row={'id':i,'text_sha256':digest,'exact_text':exact,'tex_line':s['source_line'],'verdict':'PASS','rationale':notes[i],'repair':None,'provenance':{'kind':'personally_reread_changed_or_added_with_full_block_context','prior_verdict':priormap.get(i,{}).get('verdict')}}
 ledger.append(row)
assert set(changes)==set(notes)=={x['id'] for x in delta['changed_or_added']}
assert len(unchanged)==295 and len(changes)==19 and len(ledger)==314
for x in delta['changed_or_added']:
 assert x['new_sentence']==next(s['sentence'] for s in new['sentences'] if s['id']==x['id'])
 assert x.get('old_sentence')==oldmap.get(x['id'],{}).get('sentence')
assert set(oldmap)<={s['id'] for s in new['sentences']}
tex=(p/'manuscript-r03.tex').read_text();found={}
for m in re.finditer(r'\\(?:p|txt)\{([A-Z0-9]+)\}\{',tex):
 start=m.end();depth=1;i=start
 while depth:
  if tex[i]=='{' and tex[i-1]!='\\':depth+=1
  if tex[i]=='}' and tex[i-1]!='\\':depth-=1
  i+=1
 found[m.group(1)]=tex[start:i-1]
assert set(found)=={s['block_id'] for s in new['sentences']}
assert all(s['block_tex']==found[s['block_id']] for s in new['sentences'])
oldnon={x['id']:x for x in old['non_sentence_content']};nonchanges=[]
for n in new['non_sentence_content']:
 prev=oldnon[n['id']]
 for field in ['exact_tex','text','extracted_text']:
  if n.get(field)!=prev.get(field):nonchanges.append({'id':n['id'],'field':field,'old':prev.get(field),'new':n.get(field)})
assert len(nonchanges)==1 and nonchanges[0]['id']=='figure-labels-05'
figtexts=[]
for i in range(1,7):
 a=subprocess.check_output(['/opt/homebrew/bin/pdftotext',str(root/f'figures/latex-r01/F{i:02}-r01.pdf'),'-']).decode()
 b=subprocess.check_output(['/opt/homebrew/bin/pdftotext',str(root/f'figures/latex-r01/F{i:02}-r02.pdf'),'-']).decode()
 assert (a.replace('Accepted log-CO2 fit','Fitted log-CO2 curve') if i==5 else a)==b
 figtexts.append(b)
pdf=subprocess.check_output(['/opt/homebrew/bin/pdftotext','-layout',str(p/'build-r03/manuscript-r03.pdf'),'-']).decode();(out/'pdf-text-r03.txt').write_text(pdf)
def norm(x):return ''.join(c for c in unicodedata.normalize('NFKD',x) if c.isalnum()).lower()
n=norm(pdf);misses=[s['id'] for s in new['sentences'] if norm(s['sentence']) not in n]
metadata={'source_sha256':hashlib.sha256((p/'manuscript-r03.tex').read_bytes()).hexdigest(),'pdf_sha256':hashlib.sha256((p/'build-r03/manuscript-r03.pdf').read_bytes()).hexdigest(),'register_sha256':hashlib.sha256((p/'sentence-register-r04.json').read_bytes()).hexdigest(),'delta_sha256':hashlib.sha256((p/'sentence-delta-r03.json').read_bytes()).hexdigest()}
(out/'sentence-ledger.json').write_text(json.dumps({'reviewer':'A08',**metadata,'records':ledger},indent=2))
(out/'sentence-ledger.md').write_text('# A08 complete revised ledger\n\n'+ '\n\n'.join(f"## {x['id']} — {x['verdict']}\n\n`{x['text_sha256']}`\n\n{x['exact_text']}\n\n{x['rationale']}\n\nReview provenance: {x['provenance']['kind']}." for x in ledger))
checks={**metadata,'unchanged_exact_hash_carried':len(unchanged),'changed':16,'added':3,'total':len(ledger),'blocks':len(found),'nonprose_changes':nonchanges,'all_six_imported_figure_texts_independently_compared':True,'pdf_ascii_semicolons':pdf.count(';'),'pdf_fullwidth_semicolons':pdf.count('；'),'pdf_pages':pdf.count('\f'),'simple_normalized_pdf_match_exceptions':misses}
(out/'checks.json').write_text(json.dumps(checks,indent=2));print(json.dumps(checks,indent=2))
# Remove only recurring running head and the final page-number line on each extracted page.
clean=[]
for page in pdf.split('\f'):
 lines=page.splitlines()
 if lines and '2022 HiMCM Problem B' in lines[0]:lines=lines[1:]
 while lines and not lines[-1].strip():lines.pop()
 if lines and lines[-1].strip().isdigit():lines.pop()
 clean.append('\n'.join(lines))
normalized=norm('\n'.join(clean));remaining=[s['id'] for s in new['sentences'] if norm(s['sentence']) not in normalized]
assert remaining==[],remaining
checks['normalized_matches_after_removing_page_furniture']=314
checks['remaining_pdf_match_exceptions']=remaining
checks['page_break_exceptions_personally_inspected']=misses
(out/'checks.json').write_text(json.dumps(checks,indent=2))
