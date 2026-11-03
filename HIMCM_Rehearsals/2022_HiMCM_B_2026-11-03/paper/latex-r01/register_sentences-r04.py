from pathlib import Path
import re,json,hashlib,unicodedata
from pypdf import PdfReader
R=Path(__file__).resolve().parent;T=R/'manuscript-r04.tex';P=R/'build-r04/manuscript-r04.pdf'
s=T.read_text();aux=(R/'build-r04/manuscript-r04.aux').read_text();sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
refs=dict(re.findall(r'\\newlabel\{([^}]+)\}\{\{([^}]+)\}',aux));cites=dict(re.findall(r'\\bibcite\{([^}]+)\}\{([^}]+)\}',aux))
def arg(t,pos):
 assert t[pos]=='{';n=1;i=pos+1
 while n:
  if t[i]=='{' and t[i-1]!='\\':n+=1
  if t[i]=='}' and t[i-1]!='\\':n-=1
  i+=1
 return t[pos+1:i-1],i
def repl(t,name,n,fn):
 pat=re.compile(r'\\'+re.escape(name)+r'\s*\{')
 while m:=pat.search(t):
  vals=[];end=m.end()-1
  for _ in range(n):
   while t[end].isspace():end+=1
   v,end=arg(t,end);vals.append(v)
  t=t[:m.start()]+fn(*vals)+t[end:]
 return t
def plain(t):
 t=repl(t,'href',2,lambda u,l:l);t=repl(t,'cite',1,lambda k:'['+', '.join(cites[a] for a in k.split(','))+']');t=repl(t,'ref',1,lambda k:refs[k])
 for k in ['emph','textbf','textit','textrm','mathrm','textsubscript','ensuremath']:t=repl(t,k,1,lambda v:v)
 for a,b in [(r'\CO{}','CO2'),(r'\CO','CO2'),(r'\degC{}','°C'),(r'\degC','°C'),(r'\alpha','α'),(r'\beta','β'),(r'\mathcal O','O'),(r'\%','%'),(r'\_','_')]:t=t.replace(a,b)
 t=t.replace('---','—').replace('--','–').replace('~',' ').replace('$','').replace('{','').replace('}','')
 return re.sub(r'\s+',' ',t).strip()
def canon(t):return ''.join(c.lower() for c in unicodedata.normalize('NFKC',t) if c.isalnum())
pages=[p.extract_text() for p in PdfReader(P).pages];pc=[canon(p) for p in pages]
sections=[(s.index('\\begin{document}'),'Summary Sheet'),(s.index('\\tableofcontents'),'Contents'),(s.index('\\begin{thebibliography}'),'References')]
for m in re.finditer(r'\\(?:sub)?section\*?\{',s):
 title,_=arg(s,m.end()-1);sections.append((m.start(),plain(title)))
sections.sort();records=[];blocks=[]
for m in re.finditer(r'\\(p|txt)\{',s):
 if m.start()<s.index('\\begin{document}'):continue
 bid,end=arg(s,m.end()-1);content,end=arg(s,end);section=max((x for x in sections if x[0]<m.start()))[1];text=plain(content);line=s.count('\n',0,m.start())+1
 blocks.append({'block_id':bid,'section':section,'source_line':line,'exact_tex':content,'display_text':text})
 for j,part in enumerate(re.split(r'(?<=[.!?])\s+(?=[A-Z0-9])',text),1):
  kind='sentence' if part.endswith(('.','?','!')) else 'prose_fragment_connected_to_display'
  if bid.startswith('REF') and len(part.split())<6:kind='bibliographic_fragment'
  records.append({'id':f'{bid}.{j:02d}','block_id':bid,'section':section,'kind':kind,'sentence':part,'source':T.name,'source_line':line,'block_tex':content,'pdf_pages_with_normalized_match':[i+1 for i,p in enumerate(pc) if canon(part) in p]})
for record in records:
 if record['block_id']=='SUM05':
  num=int(record['id'].split('.')[-1])
  if num==3:record['id']='SUM05.02a'
  elif num>3:record['id']=f'SUM05.{num-1:02d}'
clean=['\n'.join([line for line in p.splitlines() if not line.startswith('2022 HiMCM Problem B') and not line.strip().isdigit()]) for p in pages]
for record in records:
 if not record['pdf_pages_with_normalized_match']:
  for i in range(len(clean)-1):
   if canon(record['sentence']) in canon(clean[i]+clean[i+1]):
    record['pdf_pages_with_normalized_match']=[i+1,i+2]
    record['match_note']='Sentence crosses page boundary, headers and page numbers excluded.'
    break
non=[]
for env in ['equation','align','tabular']:
 for i,m in enumerate(re.finditer(r'\\begin\{'+env+r'\}(.*?)\\end\{'+env+r'\}',s,re.S),1):non.append({'id':f'{env}-{i:02d}','kind':'table_cells_and_headers' if env=='tabular' else 'numbered_mathematics','source_line':s.count('\n',0,m.start())+1,'exact_tex':m.group(0)})
for i,(pos,title) in enumerate(sections,1):non.append({'id':f'heading-{i:02d}','kind':'heading','source_line':s.count('\n',0,pos)+1,'text':title})
for i in range(1,7):
 f=R.parent.parent/'figures/latex-r01'/f'F{i:02d}-r02.pdf';non.append({'id':f'figure-labels-{i:02d}','kind':'plot_labels_annotations_legend_ticks','path':str(f),'sha256':sha(f),'extracted_text':'\n'.join(p.extract_text() for p in PdfReader(f).pages)})
non.append({'id':'furniture','kind':'title_headers_footers_contents','text':'Carbon Dioxide and Temperature | Evidence, Extrapolation and Limits | Climate numbers need more than a date | Summary Sheet | Contents | 2022 HiMCM Problem B | Retrospective practice | page numbers | repeated TOC headings and page numbers | caption and equation numbers | bibliography item numbers'})
result={'source':str(T),'source_sha256':sha(T),'pdf':str(P),'pdf_sha256':sha(P),'pages':len(pages),'sentence_record_count':len(records),'prose_block_count':len(blocks),'sentences':records,'prose_blocks':blocks,'non_sentence_content':non,'reconciliation':{'method':'Balanced-brace extraction of every p/txt prose macro. Full exact TeX and prose blocks retained alongside split records. Actual-PDF matching normalizes whitespace, punctuation, hyphens, ligatures and script position. Cross-page matches omit headers and page numbers. Non-prose tables, equations, headings and plot text inventoried separately. Unmatched entries are explicit and require manual reconciliation.','unmatched_ids':[x['id'] for x in records if not x['pdf_pages_with_normalized_match']],'ascii_semicolons_pdf':sum(p.count(';') for p in pages),'fullwidth_semicolons_pdf':sum(p.count('；') for p in pages),'ascii_semicolons_source':s.count(';'),'fullwidth_semicolons_source':s.count('；')}}
out=R/'sentence-register-r05.json';assert not out.exists();out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
(R/'sentence-register-r05.md').write_text('\n\n'.join(f"{x['id']} | {x['section']} | {x['source']}:{x['source_line']}\n\n{x['sentence']}" for x in records)+'\n')
print(json.dumps({'records':len(records),'blocks':len(blocks),'unmatched':result['reconciliation']['unmatched_ids'],'sha256':sha(out)},indent=2))
