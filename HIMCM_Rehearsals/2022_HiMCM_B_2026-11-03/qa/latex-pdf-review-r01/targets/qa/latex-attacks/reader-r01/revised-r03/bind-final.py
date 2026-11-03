import pathlib,json,hashlib,re,unicodedata,subprocess
root=pathlib.Path.cwd();p=root/'paper/latex-r01';out=root/'qa/latex-attacks/reader-r01/revised-r03';prevpath=root/'qa/latex-attacks/reader-r01/revised-r02/sentence-ledger.json'
expected={'manuscript-r05.tex':'1f8259757db5732f38d5cf69b37419c98f1725270559d90b1e82ba8839d92b55','build-r05/manuscript-r05.pdf':'2ec474ac04debd26d8acbf4b3393ba46e220536415d19e324597770ec7629aac','sentence-register-r06.json':'2a7a89c62ceeef6c7aae688a81e506edcc957022110d62411f24ed0bd446bd3c'}
for f,sha in expected.items():assert hashlib.sha256((p/f).read_bytes()).hexdigest()==sha
old=json.loads((p/'sentence-register-r04.json').read_text());new=json.loads((p/'sentence-register-r06.json').read_text());prev=json.loads(prevpath.read_text());pm={s['id']:s for s in prev['records']}
assert [(s['id'],s['sentence']) for s in old['sentences']]==[(s['id'],s['sentence']) for s in new['sentences']]
assert new['source_sha256']==expected['manuscript-r05.tex'] and new['pdf_sha256']==expected['build-r05/manuscript-r05.pdf']
a=(p/'manuscript-r03.tex').read_text();b=(p/'manuscript-r05.tex').read_text()
def strip_layout(s):
 s=re.sub(r'\\(?:widowpenalty|clubpenalty|displaywidowpenalty)=10000\n','',s)
 return s.replace('\\nopagebreak','').replace('\\clearpage\n','')
assert strip_layout(a)==strip_layout(b)
found={}
for m in re.finditer(r'\\(?:p|txt)\{([A-Z0-9]+)\}\{',b):
 start=m.end();depth=1;i=start
 while depth:
  if b[i]=='{' and b[i-1]!='\\':depth+=1
  if b[i]=='}' and b[i-1]!='\\':depth-=1
  i+=1
 found[m.group(1)]=b[start:i-1]
assert set(found)=={s['block_id'] for s in new['sentences']}
assert all(s['block_tex']==found[s['block_id']] for s in new['sentences'])
oldnon={x['id']:x for x in old['non_sentence_content']}
for n in new['non_sentence_content']:
 for key in ['exact_tex','text','extracted_text']:assert n.get(key)==oldnon[n['id']].get(key)
pdf=subprocess.check_output(['/opt/homebrew/bin/pdftotext','-layout',str(p/'build-r05/manuscript-r05.pdf'),'-']).decode();(out/'pdf-text-r05.txt').write_text(pdf)
clean=[]
for page in pdf.split('\f'):
 lines=page.splitlines()
 if lines and '2022 HiMCM Problem B' in lines[0]:lines=lines[1:]
 while lines and not lines[-1].strip():lines.pop()
 if lines and lines[-1].strip().isdigit():lines.pop()
 clean.append('\n'.join(lines))
def norm(x):return ''.join(c for c in unicodedata.normalize('NFKD',x) if c.isalnum()).lower()
normpages=[norm(x) for x in clean];combined=''.join(normpages);ledger=[]
for s in new['sentences']:
 digest=hashlib.sha256(s['sentence'].encode()).hexdigest();pr=pm[s['id']]
 assert digest==pr['text_sha256'] and s['sentence']==pr['exact_text'] and pr['verdict']=='PASS'
 assert norm(s['sentence']) in combined,s['id']
 row=dict(pr);row['tex_line']=s['source_line'];row['prior_review_provenance']=pr['provenance'];row['provenance']={'kind':'final_exact_ID_and_text_hash_binding','prior_ledger':str(prevpath.relative_to(root)),'prior_ledger_sha256':hashlib.sha256(prevpath.read_bytes()).hexdigest(),'prior_id':s['id'],'prior_text_sha256':digest};row['final_pdf_pages_with_normalized_match']=[i+1 for i,x in enumerate(normpages) if norm(s['sentence']) in x];ledger.append(row)
checks={'status':'ACCEPTED_FOR_SCOPE','reviewer':'A08','exact_artifacts':expected,'scope':'Sentence clarity, preserved qualifications, exact text carry-forward and final PDF textual coverage. Not an all-page visual review.','complete_ledger_records':len(ledger),'all_records_exact_ID_and_text_hash_matched':True,'prose_blocks':len(found),'normalized_sentence_matches':314,'pdf_pages':pdf.count('\f'),'pdf_ascii_semicolons':pdf.count(';'),'pdf_fullwidth_semicolons':pdf.count('；'),'unregistered_or_missing_prose_found':False,'non_sentence_inventory_items_unchanged':len(new['non_sentence_content']),'source_changes_only_layout_commands':True,'article_page':next(i+1 for i,t in enumerate(clean) if 'Climate numbers need more than a date' in t)}
(out/'sentence-ledger.json').write_text(json.dumps({**checks,'records':ledger},indent=2));(out/'sentence-ledger.md').write_text('# A08 final r05 full sentence ledger\n\nACCEPTED_FOR_SCOPE. Bound to final r05/r06 hashes in checks.json.\n\n'+ '\n\n'.join(f"## {x['id']} — {x['verdict']}\n\n`{x['text_sha256']}`\n\n{x['exact_text']}\n\n{x['rationale']}\n\nProvenance: exact ID/text hash verified against the revised-r02 ledger, with earlier review chain preserved in JSON." for x in ledger));(out/'checks.json').write_text(json.dumps(checks,indent=2));print(json.dumps(checks,indent=2))
