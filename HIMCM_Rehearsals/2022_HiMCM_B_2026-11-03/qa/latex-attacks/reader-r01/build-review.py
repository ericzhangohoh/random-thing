import json,hashlib,re,collections,pathlib,subprocess
root=pathlib.Path.cwd(); out=root/'qa/latex-attacks/reader-r01'
r=json.loads((root/'paper/latex-r01/sentence-register-r03.json').read_text())
notes={}
for line in (out/'manual-reasons.txt').read_text().splitlines():
    cols=line.split('|');notes[cols[0]]=cols[1:]
blocks=collections.defaultdict(list)
for s in r['sentences']:blocks[s['block_id']].append(s)
assert set(blocks)==set(notes),(set(blocks)-set(notes),set(notes)-set(blocks))
for b,ss in blocks.items():assert len(ss)==len(notes[b]),(b,len(ss),len(notes[b]))
repairs={
'SUM02.04':('SUGGEST','We retain D as the choice under the prespecified selection rule without treating it as a universal future winner.'),
'SUM06.01':('REPAIR','Concentration and temperature are strongly associated in their observed levels, but the association weakens after trend removal and differencing.'),
'VAL03.03':('REPAIR','The local computation preserves this order, but another reviewer had already exposed the final-period scores before the primary run recorded its selection.'),
'APP04.03':('REPAIR','Paths already above the threshold at the forecast origin are distinguished from valid paths that do not cross it by 2300.'),
'APP04.05':('SUGGEST','All actual primary paths remain valid throughout the search domain.'),
'ART05.04':('REPAIR','These are crossing dates on conditional annual paths, not established deadlines, sustained warming dates or Paris targets.')}
ledger=[]
for b,ss in blocks.items():
    for s,reason in zip(ss,notes[b]):
        verdict,repair=repairs.get(s['id'],('PASS',None))
        ledger.append({'id':s['id'],'text_sha256':hashlib.sha256(s['sentence'].encode()).hexdigest(),'exact_text':s['sentence'],'tex_line':s['source_line'],'verdict':verdict,'rationale':reason,'repair':repair})
(out/'sentence-ledger.json').write_text(json.dumps({'reviewer':'A08','source_sha256':r['source_sha256'],'pdf_sha256':r['pdf_sha256'],'register_sha256':hashlib.sha256((root/'paper/latex-r01/sentence-register-r03.json').read_bytes()).hexdigest(),'records':ledger},indent=2))
(out/'sentence-ledger.md').write_text('# A08 exact-version sentence ledger\n\n'+ '\n\n'.join(f"## {x['id']} — {x['verdict']}\n\nText SHA-256: `{x['text_sha256']}`\n\n{x['exact_text']}\n\nReason: {x['rationale']}"+(f"\n\nRepair: {x['repair']}" if x['repair'] else '') for x in ledger))
# Independent balanced-brace inventory, not the register producer's reconciliation.
tex=(root/'paper/latex-r01/manuscript-r02.tex').read_text()
found={}
for m in re.finditer(r'\\(?:p|txt)\{([A-Z0-9]+)\}\{',tex):
    start=m.end();depth=1;i=start
    while depth:
        if tex[i]=='{' and tex[i-1]!='\\':depth+=1
        if tex[i]=='}' and tex[i-1]!='\\':depth-=1
        i+=1
    found[m.group(1)]=tex[start:i-1]
assert set(found)==set(blocks)
assert all(found[b]==ss[0]['block_tex'] for b,ss in blocks.items())
non=r['non_sentence_content']
for n in non:
    if 'exact_tex' in n:assert n['exact_tex'] in tex,n['id']
figs=re.findall(r'\\includegraphics\[[^]]*\]\{([^}]+)\}',tex)
assert len(figs)==6
pdf=(out/'pdf-text.txt').read_text()
checks={'reviewer':'A08','source_blocks_independently_found':len(found),'registered_blocks':len(blocks),'registered_sentences_reviewed':len(ledger),'non_sentence_items_inspected':len(non),'included_figures':figs,'unregistered_prose_blocks':[],'exact_block_tex_mismatches':[],'pdf_pages':len(pdf.split('\f'))-1,'ascii_semicolons_pdf':pdf.count(';'),'fullwidth_semicolons_pdf':pdf.count('；'),'ascii_semicolons_tex':tex.count(';'),'fullwidth_semicolons_tex':tex.count('；'),'verdict_counts':dict(collections.Counter(x['verdict'] for x in ledger)),'method':'Personally read prose, caption/reference fragments and surrounding TeX, plus PDF extracted pages. Independently parsed every p/txt block with balanced braces. Inspected 54 additional items: 9 math environments, 12 tables, 26 headings, 6 figure-label inventories and furniture. No missing prose found. No claim that 54 items are 54 sentences. PDF count includes rendered imported figure text.'}
(out/'completeness-and-punctuation.json').write_text(json.dumps(checks,indent=2));print(json.dumps(checks,indent=2))
