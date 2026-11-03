from pathlib import Path
import hashlib,json,shutil,subprocess,importlib.util,copy
import openpyxl
P=Path(__file__).resolve().parents[2]; Q=P/'qa/adversarial_implementation'; R=P/'runs/T05-ingestion-20261103-r02'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
manifest=json.loads((R/'manifest.json').read_text()); initial={str(R/'manifest.json'):sha(R/'manifest.json')}
I=Q/'isolated-r01'; I.mkdir()
for item in manifest['retained_artifacts']:
 s=P/item['retained_path']; assert sha(s)==item['sha256']; initial[str(s)]=sha(s)
 d=I/item['used_path'];d.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(s,d)
(Q/'target-hashes-r01.json').write_text(json.dumps(initial,indent=2))
shutil.copyfile(R/'manifest.json',Q/'ingestion-manifest-r01.json')
py='/Users/ericzhang/.venvs/default/bin/python3'
cmd=[py,str(I/'code/data/ingest_r01.py'),'--input',str(I/'inputs/2022_HiMCM_Data.xlsx'),'--config',str(I/'code/data/ingestion_config-r01.json'),'--output-dir',str(I/'fresh-output')]
r=subprocess.run(cmd,cwd=I,text=True,capture_output=True,timeout=60);assert r.returncode==0,r.stderr
comparisons={Path(o['path']).name:sha(I/'fresh-output'/Path(o['path']).name)==o['sha256'] for o in manifest['outputs']};assert all(comparisons.values())
spec=importlib.util.spec_from_file_location('copied_ingest',I/'code/data/ingest_r01.py'); mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
config=json.loads((I/'code/data/ingestion_config-r01.json').read_text()); fixtures=Q/'fixtures-r01';fixtures.mkdir()
checks=[]
for kind in ['shuffle','duplicate','missing','formula','outofrange','hash_mismatch']:
 w=openpyxl.load_workbook(I/'inputs/2022_HiMCM_Data.xlsx')
 s=w['CO2 Data Set 1']
 if kind=='shuffle':
  for ss in w:
   rows=list(ss.iter_rows(min_row=2,max_col=2,values_only=True))[::-1]
   for j,row in enumerate(rows,2):
    for k,v in enumerate(row,1):ss.cell(j,k).value=v
 elif kind=='duplicate':s['A3']=s['A2'].value
 elif kind=='missing':s['B3']=None
 elif kind=='formula':s['B3']='=300+16.91'
 elif kind=='outofrange':s['Z100']=1
 else:s['B3']=300
 fp=fixtures/(kind+'.xlsx');w.save(fp);w.close();cfg=copy.deepcopy(config)
 if kind!='hash_mismatch':cfg['input_sha256']=sha(fp)
 try:
  parsed,prov=mod.parse_workbook(fp,cfg)
  assert kind=='shuffle','Invalid fixture accepted: '+kind
  orig,_=mod.parse_workbook(I/'inputs/2022_HiMCM_Data.xlsx',config);assert parsed==orig
  checks.append({'test':kind,'pass':True,'outcome':'same keyed series after independent row reversal'})
 except ValueError as e:
  assert kind!='shuffle',str(e)
  checks.append({'test':kind,'pass':True,'outcome':str(e)})
before={f.name:sha(f) for f in (I/'fresh-output').iterdir()};rerun=subprocess.run(cmd,cwd=I,text=True,capture_output=True,timeout=60);assert rerun.returncode!=0;assert before=={f.name:sha(f) for f in (I/'fresh-output').iterdir()}
# Hash tamper failure through recovered retrieval checker; manifest points only to fixture paths.
tam=Q/'tampered-source-r01';tam.mkdir();(tam/'one.txt').write_text('changed')
tm={'retained_artifacts':[{'used_path':'one.txt','retained_path':'one.txt','sha256':hashlib.sha256(b'original').hexdigest(),'retrieval_method':'retained_file'}]};(tam/'manifest.json').write_text(json.dumps(tm))
tr=subprocess.run([py,str(I/'code/qa/retrieve_retained_r01.py'),'--project-root',str(tam),'--manifest',str(tam/'manifest.json'),'--destination',str(Q/'tamper-recovery-r01')],cwd=I,text=True,capture_output=True,timeout=60);assert tr.returncode!=0 and 'hash mismatch' in tr.stderr
assert all(sha(Path(f))==h for f,h in initial.items())
result={'status':'PASS','retained_artifacts_verified':len(manifest['retained_artifacts']),'isolated_command':cmd,'isolated_cwd':str(I),'output_comparisons':comparisons,'fixture_checks':checks,'existing_output_refused_and_unchanged':True,'tampered_recovery_rejected':True,'target_hashes_unchanged':True,'scope':'closed ingestion only; no full model verdict'}
(Q/'ingestion-results-r01.json').write_text(json.dumps(result,indent=2));(Q/'ingestion-execution-r01.log').write_text(r.stdout+'\nOVERWRITE REFUSAL\n'+rerun.stderr+'\nTAMPER REFUSAL\n'+tr.stderr);print(json.dumps(result,indent=2))
