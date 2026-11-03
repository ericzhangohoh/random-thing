from pathlib import Path
import csv,hashlib,json,re,math,unicodedata
from collections import Counter,defaultdict
ROOT=Path(__file__).resolve().parents[4]
OUT=Path(__file__).resolve().parent
RUND='runs/T05-scientific-20261103-r03/'
RUN=RUND+'outputs/'
sha=lambda p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
TEX='paper/latex-r01/manuscript-r02.tex'
PDF='paper/latex-r01/build-r02/manuscript-r02.pdf'
REG='paper/latex-r01/sentence-register-r03.json'
pins={TEX:'f9f60adb63996ae83d2bffeec43e4e3b9e04cc10d9e85cbd1c3f452db8bed35b',PDF:'c0e4a245b2b5013effbd7fcca5262db2114ab5b48e3162b5a7482707e2137e8e',REG:'80e9e581927f4483cf99a3038dea6fb387ba9a903edec7b9b36cd69b8e940e7e'}
assert all(sha(p)==h for p,h in pins.items())
S={
'DATA':['research/data-dictionary-r01.md','research/data-quality-r01.md',RUND+'input-reaudit/ingestion-checks-r01.json','data/processed/co2-r01.csv','data/processed/temperature-r01.csv'],
'SRC':['research/source-register-r01.md','research/web-snapshot-manifest-r01.json','data/raw/oecd-climate-selected-evidence-20261103.txt','data/raw/noaa-news-web-extract-20261103.txt','data/raw/nasa-gistemp-faq-20261103.html','data/raw/noaa-data-20261103.html','data/raw/noaa-annual-definition-20261103.txt'],
'PROBLEM':['research/problem-fulltext-r01.txt','inputs/2022_HiMCM_Problem_B.pdf'],
'DEC':[RUN+'ten_year_comparison.json',RUN+'ten_year_changes.csv'],
'SPEC':['models/model_spec-r02.md','models/assumptions-r01.md'],
'MET':[RUN+'development_metrics.csv',RUN+'final_metrics.csv'],
'FROZE':[RUN+'selection_frozen.json',RUN+'final_assessment_receipt.json'],
'FINAL':[RUN+'final_forecasts.csv'],
'RANK':[RUN+'rank_stability.csv'],
'WEIGHT':['qa/latex-attacks/evidence-r01/weighting-verification-r01.json','qa/latex-attacks/evidence-r01/weighting-review-r01.md','control/accepted-claims-latex-r01.json',RUN+'development_forecasts.csv'],
'FORE':[RUN+'forecast_summary.csv',RUN+'production_forecasts.csv'],
'THR':[RUN+'thresholds.csv',RUN+'threshold_search_paths.csv'],
'COEF':[RUN+'production_coefficients.csv'],
'FIT':[RUN+'production_fit_diagnostics.csv'],
'REL':[RUN+'relationship_diagnostics.csv',RUN+'relationship_series.csv'],
'HORIZ':[RUN+'horizon_evidence.csv',RUN+'development_forecasts.csv'],
'ENV':[RUN+'historical_error_envelopes.csv',RUN+'final_forecasts.csv'],
'WIN':[RUN+'window_sensitivity.csv'],
'PATH':[RUN+'path_diagnostics.csv'],
'INTAKE':['control/intake.md','control/latex-revision-r01.md'],
'MANIFEST':[RUND+'manifest.json',RUND+'reproduction-check.json',RUND+'execution.log',RUND+'completion-receipt.md'],
'FIG':['code/visualization/latex-r01/render_figures-r01.py','paper/latex-r01/figure-register-r01.json']+[f'figures/latex-r01/F{i:02d}-r01.pdf' for i in range(1,7)],
'TEX':[TEX,PDF,'paper/latex-r01/build-r02/manuscript-r02.log','paper/latex-r01/build-r02/manuscript-r02.aux','paper/latex-r01/build-r02/manuscript-r02.toc'],
'CODE':['code/modeling/climate_models_r02.py','code/experiments/analysis_r03.py'],
'DECISION':['models/model_decision-r01.md','models/model_decision-r03.md','models/experiment_plan-r03.md'],
'CLAIMS':['control/accepted-claims-g3-r01.json','control/accepted-claims-latex-r01.json']}
sources={key:[{'path':p,'sha256':sha(p)} for p in paths] for key,paths in S.items()}
(OUT/'evidence-sources.json').write_text(json.dumps(sources,indent=2)+'\n')
reg=json.loads((ROOT/REG).read_text())
notes={}
for line in (OUT/'manual-assessments.txt').read_text().splitlines():
 id,refs,reason=line.split('|',2)
 assert id not in notes
 notes[id]={'evidence_refs':refs.split(','),'rationale':reason}
assert set(notes)=={s['id'] for s in reg['sentences']}
repairs={
'VAL01.01':('A07-F01','Add an explicit sentence that these backtests use the single supplied vintage, not versions available at each historical date.'),
'APP01.02':('A07-F01','Clarify historical year cutoffs using the same single-vintage qualification, or replace availability wording with observations dated no later than their origin.'),
'APP02.05':('A07-F02','Replace unsupported identification claim with: The supplied record does not establish a physically justified saturation capacity. Retain need for additional physical-model inputs.')}
ledger=[]
for s in reg['sentences']:
 n=notes[s['id']]
 assert all(k in sources for k in n['evidence_refs'])
 record={'id':s['id'],'exact_text':s['sentence'],'text_sha256':hashlib.sha256(s['sentence'].encode()).hexdigest(),'source_line':s['source_line'],'block_id':s['block_id'],'source_tex_sha256':pins[TEX],'block_tex_sha256':hashlib.sha256(s['block_tex'].encode()).hexdigest(),**n,'verdict':'REPAIR_REQUIRED' if s['id'] in repairs else 'PASS_FOR_STATED_SCOPE','finding':repairs.get(s['id'],(None,None))[0],'required_repair':repairs.get(s['id'],(None,None))[1]}
 ledger.append(record)
(OUT/'sentence-ledger.json').write_text(json.dumps({'reviewer':'A07','targets':pins,'scope':'Every registered record read and assessed against exact source and surrounding argument. Two wording issues require repair before final release.','counts':dict(Counter(r['verdict'] for r in ledger)),'records':ledger},indent=2,ensure_ascii=False)+'\n')
md=['# A07 complete evidence sentence ledger','', 'Each evidence key resolves to exact file SHA-256 identities in evidence-sources.json. These judgments apply only to the pinned r02 source and r03 register. Numerical correctness does not transfer to later source bytes without recheck.','']
for r in ledger:
 md += [f"## {r['id']} — {r['verdict']}",'',f"Text: {r['exact_text']}",'',f"Text SHA-256: `{r['text_sha256']}`. TeX line {r['source_line']}.",'',f"Evidence: {', '.join(r['evidence_refs'])}. {r['rationale']}",'']
 if r['required_repair']:md += [f"Repair {r['finding']}: {r['required_repair']}",'']
(OUT/'sentence-ledger.md').write_text('\n'.join(md))
nonnotes={}
for l in (OUT/'non-sentence-assessments.txt').read_text().splitlines():
 id,refs,reason=l.split('|',2)
 nonnotes[id]={'evidence_refs':refs.split(','),'rationale':reason}
assert set(nonnotes)=={n['id'] for n in reg['non_sentence_content']}
non=[]
for n in reg['non_sentence_content']:
 raw=n.get('exact_tex',n.get('extracted_text',n.get('text','')))
 non.append({'id':n['id'],'kind':n['kind'],'exact_content':raw,'content_sha256':hashlib.sha256(raw.encode()).hexdigest(),**nonnotes[n['id']],'verdict':'PASS_FOR_STATED_SCOPE'})
(OUT/'non-sentence-ledger.json').write_text(json.dumps(non,indent=2,ensure_ascii=False)+'\n')
# Independent source scan, not the writer's registration program.
tex=(ROOT/TEX).read_text()
start=tex.index(r'\begin{document}')+len(r'\begin{document}')
body=tex[start:tex.index(r'\end{document}')]
def balanced(text,pos):
 assert text[pos]=='{'
 level=0
 for end in range(pos,len(text)):
  if end>0 and text[end-1]=='\\':continue
  if text[end]=='{':level+=1
  elif text[end]=='}':
   level-=1
   if level==0:return text[pos+1:end],end+1
 raise ValueError('unbalanced')
found=[]
for m in re.finditer(r'\\(?:p|txt)\{',body):
 block_id,e=balanced(body,m.end()-1)
 content,e2=balanced(body,e)
 found.append((block_id,content,m.start(),e2))
assert len(found)==92
registered={b['block_id']:b for b in reg['prose_blocks']}
assert {f[0] for f in found}==set(registered)
assert all(content==registered[id]['exact_tex'] for id,content,_,_ in found)
joined_checks=[]
for id,content,_,_ in found:
 joined=' '.join(s['sentence'] for s in reg['sentences'] if s['block_id']==id)
 joined_checks.append({'block':id,'joined_sentences_equal_display_text':joined==registered[id]['display_text']})
assert all(r['joined_sentences_equal_display_text'] for r in joined_checks)
residue=body
for _,_,a,b in reversed(found):residue=residue[:a]+'[REVIEWED PROSE BLOCK]'+residue[b:]
# Remove independently enumerated mathematical/table environments, retaining title/headings/control residue for manual omission inspection.
for env in ['equation','align','tabular']:
 residue=re.sub(r'\\begin\{'+env+r'\}.*?\\end\{'+env+r'\}','[REVIEWED '+env+']',residue,flags=re.S)
(OUT/'independent-source-residue.txt').write_text(residue)
canonical=lambda s:''.join(ch for ch in unicodedata.normalize('NFKC',s).lower() if ch.isalnum())
pdftext=(OUT/'pdf-text.txt').read_text()
pages=pdftext.split('\f')[:-1]
unmatched=[s['id'] for s in reg['sentences'] if not any(canonical(s['sentence']) in canonical(p) for p in pages)]
clean_pages=[]
for number,page in enumerate(pages,1):
 clean_pages.append('\n'.join(line for line in page.splitlines() if line.strip()!=str(number) and not ('2022 HiMCM Problem B' in line and 'Retrospective practice' in line)))
spanning=[s['id'] for s in reg['sentences'] if s['id'] in unmatched and canonical(s['sentence']) in canonical(' '.join(clean_pages))]
assert set(spanning)==set(unmatched)

accepted=json.loads((ROOT/'control/accepted-claims-g3-r01.json').read_text())
accepted_hash_checks=[]
for claim in accepted['claims']:
 for e in claim.get('evidence',[]):
  p=e['path']
  if not (ROOT/p).is_file():
   assert p=='reasoned implication'
   continue
  accepted_hash_checks.append({'claim':claim['id'],'path':p,'matches':sha(p)==e['sha256']})
assert all(c['matches'] for c in accepted_hash_checks)
coverage={'targets':pins,'independent_p_or_txt_macro_count':len(found),'registered_blocks':len(registered),'all_source_macro_ids_and_exact_tex_match':True,'all_sentence_joins_equal_block_display_text':True,'registered_record_count':len(ledger),'non_sentence_items':len(non),'independent_pdf_pages':len(pages),'source_ASCII_plus_fullwidth_semicolons':tex.count(';')+tex.count('；'),'PDF_ASCII_plus_fullwidth_semicolons':pdftext.count(';')+pdftext.count('；'),'independent_pdf_single_page_unmatched_ids':unmatched,'independent_pdf_cross_page_matches':spanning,'remaining_unmatched_after_header_footer_removal':[],'base_claim_evidence_hash_checks':accepted_hash_checks,'residual_text_inspection':'independent-source-residue.txt includes only reviewed headings, furniture, labels and layout commands after the inventoried blocks/equations/tables are removed'}
(OUT/'coverage-and-hashes.json').write_text(json.dumps(coverage,indent=2)+'\n')
# Recompute selected descriptive quantities directly from accepted rows, without model refits.
def rows(name):return list(csv.DictReader((ROOT/RUN/name).open()))
num={}
for phase in ['development','final']:
 forecasts=rows(phase+'_forecasts.csv')
 measured=[]
 for metric in rows(phase+'_metrics.csv'):
  if metric['grouping']!='overall':continue
  e=[float(r['predicted'])-float(r['observed']) for r in forecasts if r['model_id']==metric['model_id']]
  calc={'mae':sum(abs(x) for x in e)/len(e),'rmse':math.sqrt(sum(x*x for x in e)/len(e)),'bias':sum(e)/len(e)}
  assert all(abs(calc[k]-float(metric[k]))<1e-12 for k in calc)
  measured.append({'model_id':metric['model_id'],'n':len(e),**calc})
 num[phase+'_metrics']=measured
forecast=rows('forecast_summary.csv')
num['co2_spreads']={str(y):max(float(r['value']) for r in forecast if r['fit_window']=='full' and r['target']=='co2' and r['year']==str(y))-min(float(r['value']) for r in forecast if r['fit_window']=='full' and r['target']=='co2' and r['year']==str(y)) for y in [2050,2100]}
env=rows('historical_error_envelopes.csv')
num['containment']={m:sum(r['final_contained']=='True' for r in env if r['selected_model_id']==m) for m in ['D','T1-D']}
assert num['containment']=={'D':10,'T1-D':9}
num['misses']=[{k:r[k] for k in ['selected_model_id','horizon','final_target_year','radius','final_absolute_error','final_excess']} for r in env if r['final_contained']=='False']
paths=rows('path_diagnostics.csv')
assert len(paths)==9 and all(r['invalid_count']=='0' and r['decreasing_segments']=='0' for r in paths)
num['actual_paths_finite_nondecreasing_count']=len(paths)
thresholds=rows('thresholds.csv')
assert all(float(r['value_previous_year'])<float(r['threshold'])<=float(r['value_at_year']) for r in thresholds)
num['all_threshold_boundaries_strictly_bracket_without_tolerance']=True
num['primary_source_hashes']={str(p.relative_to(ROOT)):sha(str(p.relative_to(ROOT))) for p in (ROOT/RUN).glob('*') if p.is_file()}
(OUT/'independent-numeric-checks.json').write_text(json.dumps(num,indent=2)+'\n')
print(json.dumps({'ledger':len(ledger),'verdicts':dict(Counter(r['verdict'] for r in ledger)),'non_sentence':len(non),'independent_blocks':len(found),'pdf_pages':len(pages),'pdf_unmatched':unmatched,'semicolons':coverage['PDF_ASCII_plus_fullwidth_semicolons'],'accepted_source_hashes_checked':len(accepted_hash_checks)},indent=2))
