from pathlib import Path
import json,hashlib,re,shutil
P=Path(__file__).resolve().parents[2];Q=Path(__file__).parent;R=P/'runs/T09-recovery-20261103-r02';S=P/'runs/T05-scientific-20261103-r03';F=P/'runs/T09-recovery-20261103-r01'
def j(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
checks=[]
def ck(n,v):assert v,n;checks.append(n)
ck('dispatch handoff identity',sha(P/'handoffs/T09/computation-r01.md')=='5548ca63d2e67a246245aa498d66c53adb0b022f9ca5b0145052077daefe77ad')
ck('dispatch manifest identity',sha(R/'manifest.json')=='ebd484ba9a80113aaff0f3eee6c19aa23e180336b1a92751828479d0892f6bc4')
m=j(R/'manifest.json');ck('278 retained identities',len(m['file_inventory'])==278)
for x in m['file_inventory']:
 p=R/x['path'];ck('inventory '+x['path'],sha(p)==x['sha256'] and p.stat().st_size==x['bytes'])
primary=j(S/'manifest.json')
for x in primary['retained_artifacts']:ck('recovered '+x['used_path'],sha(R/'recovered'/x['used_path'])==x['sha256'])
release=j(R/'recovered/control/accepted-inputs-g2-r02.json')
for p,h in release['sha256'].items():ck('G2 '+p,sha(R/'recovered'/p)==h)
old=j(R/'original_hashes_before.json');new=j(R/'original_hashes_after.json');ck('before after125',old==new and len(old)==125)
for x in new:ck('original now '+x['path'],sha(Path(x['path']))==x['sha256']==x['expected_sha256'])
ex={'selection_frozen.json':['frozen_at'],'final_assessment_receipt.json':['started_at','finished_at','selection_frozen_at','loaded_selection_sha256'],'production_receipt.json':['finished_at','loaded_selection_sha256','final_assessment_sha256']}
for o in [R/'outputs',R/'probes/valid-output-reference-v02/outputs']:
 ck('35 output names '+str(o),{p.name for p in o.iterdir()}=={Path(x['path']).name for x in primary['outputs']})
 for x in primary['outputs']:
  n=Path(x['path']).name;ref=R/'reference/outputs'/n;ck('reference '+n,sha(ref)==x['sha256'])
  if n not in ex:ck('exact '+str(o/n),sha(o/n)==x['sha256'])
  else:
   a,b=j(ref),j(o/n);ck('semantic '+str(o/n),{k:v for k,v in a.items() if k not in ex[n]}=={k:v for k,v in b.items() if k not in ex[n]})
 s,f,p=[j(o/n) for n in ex]
 ck('receipt chain '+str(o),f['loaded_selection_sha256']==p['loaded_selection_sha256']==sha(o/'selection_frozen.json') and p['final_assessment_sha256']==sha(o/'final_assessment_receipt.json'))
 ck('time order '+str(o),s['frozen_at']==f['selection_frozen_at'] and s['frozen_at']<=f['started_at']<=f['finished_at']<=p['finished_at'])
 ck('final output links '+str(o),all(f[n+'_sha256']==sha(o/(n+'.csv')) for n in ['final_forecasts','final_metrics']))
 ck('postrun12 '+str(o),len(j(o/'numerical_checks.json')['checks'])==12 and all(x['pass'] for x in j(o/'numerical_checks.json')['checks']))
report=j(R/'execution_report.json');ck('13commands',len(report['commands'])==13)
for c in report['commands']:
 ck('command '+c['label'],c['argv'][0]=='/Users/ericzhang/.venvs/default/bin/python3' and c['started_at']<=c['finished_at'] and c['expected_outcome_observed'])
 ck('isolated cwd '+c['label'],Path(c['working_directory']).is_relative_to(R))
 reject=c['expected_rejection_substring'];out=(R/c['stderr_path']).read_text()+(R/c['stdout_path']).read_text()
 ck('exit '+c['label'],c['exit_code']==(1 if reject else 0) and (not reject or reject in out))
 if c['label'].startswith('test_'):
  count={'test_ingestion_r01':9,'test_models_r03':28,'test_repair_r03':7}[c['label']];ck('test count '+c['label'],re.search(r'Ran '+str(count)+r' tests',out) is not None and '\nOK\n' in out)
wrong=R/'probes/wrong-output-reference-v01/outputs';ck('wrong metrics identity',j(wrong/'selection_frozen.json')['development_metrics_sha256']=='0'*64);ck('no rejected final outputs',not list(wrong.glob('final_*')))
ck('tampered dependency no receipt',not (R/'probes/tampered-dependency-v01/retrieval-attempt/retrieval-receipt.json').exists())
base=R/'recovered/data/processed/joined-r01.csv';bad=R/'probes/tampered-dependency-v01/repository-copy/fixture/joined-r01.csv';ck('actual changed bytes',sha(base)!=sha(bad));ck('valid dependency restored',sha(base)==sha(R/'probes/valid-dependency-v02/retrieved/data/processed/joined-r01.csv'))
for n in ['co2-r01.csv','temperature-r01.csv','joined-r01.csv']:ck('reingest '+n,sha(R/'input-reaudit'/n)==sha(R/'recovered/data/processed'/n))
ck('failed attempt retained',j(F/'failure_closure.json')['status']=='FAILED_HARNESS_RESTORATION_ATTEMPT_PRESERVED' and (F/'driver_failure.txt').exists())
c=j(F/'commands/13-recover-valid-reference-production.json');ck('r01 command13 failed',c['exit_code']!=0 and 'development_error_samples.csv' in (F/c['stderr_path']).read_text())
(Q/'checks.json').write_text(json.dumps({'status':'PASS','count':len(checks),'checks':checks,'scope':'Independent receipt/hash/equivalence verification; no reexecution of production or probes'},indent=2)+'\n')
# Pin all closed recovery files plus whole failed attempt; preserve exact versions.
paths=[R/'manifest.json',P/'handoffs/T09/computation-r01.md']+[R/x['path'] for x in m['file_inventory']]+[p for p in F.rglob('*') if p.is_file()]
inv=[]
for p in paths:
 t=Q/'targets'/p.relative_to(P);t.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,t);inv.append({'source':str(p),'retained':str(t),'sha256':sha(p)})
(Q/'target-inventory.json').write_text(json.dumps(inv,indent=2)+'\n');print('PASS',len(checks),'checks;',len(inv),'pinned files')
