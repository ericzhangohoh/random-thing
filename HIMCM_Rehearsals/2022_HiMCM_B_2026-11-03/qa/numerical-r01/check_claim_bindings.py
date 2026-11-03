from pathlib import Path
import json,hashlib,csv
P=Path(__file__).resolve().parents[2]
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
a=json.loads((P/'models/claim-evidence-r01.json').read_text()); b=json.loads((P/'models/claim-evidence-r02.json').read_text()); checks=[]
def ck(label, condition):
 assert condition,label
 checks.append(label)
ck('current manifest',sha(P/b['manifest_path'])==b['manifest_sha256']=='7bc6e1fe3498302d247b45fa97c4d13498edfbf5366cddd078ff7ebfaff4bc00')
for path,v in b['source_files'].items(): ck('source '+path,sha(P/path)==v['sha256'])
for name,v in b['primary_output_files'].items():
 ck('output '+name,sha(P/v['path'])==v['sha256'])
 if name.endswith('.csv'):
  rows=list(csv.DictReader((P/v['path']).open()));ck('row count '+name,len(rows)==v['row_count']);ck('columns '+name,list(rows[0])==v['columns'])
for x,y in zip(a['claims'],b['claims']):
 for k in ['id','requirements','claim','limit']:
  old,new=x[k],y[k]
  if k=='requirements':old=[v.strip() for v in old]
  if k=='limit' and y['id']=='C16':old=old.replace('T05 r04','T05 r05')
  ck(y['id']+' unchanged '+k,old==new)
 for e in y['evidence']:
  if e['sha256'] is None: continue
  ck(y['id']+' evidence '+e['path'],sha(P/e['path'])==e['sha256'])
  if e['path'].endswith('.csv'):
   cols=next(csv.reader((P/e['path']).open())); ck(y['id']+' columns '+e['file'],set(e['value_columns'])<=set(cols))
ck('17 claims',len(a['claims'])==len(b['claims'])==17)
for name,rows in b['evidence_tables'].items():
 p=P/'runs/T05-scientific-20261103-r03/outputs'/name
 actual=list(csv.DictReader(p.open())) if name.endswith('.csv') else json.loads(p.read_text())
 ck('embedded evidence '+name,all(row in actual for row in rows) if name.endswith('.csv') else rows==actual)
x=(P/'models/claim_proposals-r01.md').read_text();y=(P/'models/claim_proposals-r02.md').read_text()
start=x.index('## Suggested summary wording');end=x.index('## r02 binding check') if '## r02 binding check' in x else len(x)
ck('summary article prohibitions unchanged',x[start:end].strip()==y[y.index('## Suggested summary wording'):y.index('## r02 binding check')].strip())
(P/'qa/numerical-r01/claim-binding-checks.json').write_text(json.dumps({'status':'PASS','count':len(checks),'checks':checks},indent=2)+'\n')
print('PASS',len(checks))
