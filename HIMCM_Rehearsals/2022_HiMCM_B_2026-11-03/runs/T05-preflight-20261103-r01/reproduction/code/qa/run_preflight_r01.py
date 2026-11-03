"""Preserved synthetic-only selfchecks while reviewed M06 clarification waits."""
import argparse,hashlib,json,os,platform,shutil,subprocess,sys
from datetime import datetime,timezone
from pathlib import Path
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def now():return datetime.now(timezone.utc).isoformat()
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--project-root',required=True);ap.add_argument('--run-id',required=True);a=ap.parse_args();root=Path(a.project_root);run=root/'runs'/a.run_id;run.mkdir(parents=True,exist_ok=False);snap=run/'reproduction';snap.mkdir()
    manifest={'run_id':a.run_id,'task_id':'T05','status':'RUNNING','started_at':now(),'command':[sys.executable,*sys.argv],'working_directory':str(root),'retained_artifacts':[],'retention_check':{'status':'NOT_RUN'},'solver':{'status':'NOT_APPLICABLE_SYNTHETIC_TESTS_ONLY'},'historical_fits_executed':False,'exit_code':None}
    files=['code/qa/run_preflight_r01.py','code/qa/test_models_r01.py','code/qa/test_ingestion_r01.py','code/qa/preflight-review-r01.md','code/qa/retrieve_retained_r01.py','code/modeling/climate_models_r01.py','code/experiments/analysis_r01.py','code/data/ingest_r01.py','models/model_spec-r01.md','models/experiment_plan-r01.md','models/model_interface-r01.md']
    for name in files:
        target=snap/name;target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(root/name,target);manifest['retained_artifacts'].append({'kind':'synthetic_test_dependency','used_path':name,'sha256':sha(target),'retrieval_method':'retained_file','retained_path':str(target.relative_to(root))})
    import numpy,openpyxl
    environment={'python':sys.version,'executable':sys.executable,'platform':platform.platform(),'numpy':numpy.__version__,'openpyxl':openpyxl.__version__};(snap/'environment.json').write_text(json.dumps(environment,indent=2)+'\n');manifest['environment']=environment;manifest['retained_artifacts'].append({'kind':'environment','used_path':'environment.json','sha256':sha(snap/'environment.json'),'retrieval_method':'retained_file','retained_path':str((snap/'environment.json').relative_to(root))})
    env=os.environ.copy();env['PYTHONDONTWRITEBYTECODE']='1';codes=[];log=run/'execution.log'
    with log.open('x') as out:
        for file in ['code/qa/test_ingestion_r01.py','code/qa/test_models_r01.py']:
            cmd=[sys.executable,str(snap/file)];out.write('COMMAND '+json.dumps(cmd)+'\n');out.flush();result=subprocess.run(cmd,cwd=run,env=env,stdout=out,stderr=subprocess.STDOUT,timeout=60);codes.append(result.returncode);out.write('EXIT '+str(result.returncode)+'\n')
    (run/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    recovery=run/'isolated-recovery';cmd=[sys.executable,str(snap/'code/qa/retrieve_retained_r01.py'),'--project-root',str(root),'--manifest',str(run/'manifest.json'),'--destination',str(recovery)]
    with log.open('a') as out:
        out.write('COMMAND '+json.dumps(cmd)+'\n');out.flush();r=subprocess.run(cmd,cwd=run,env=env,stdout=out,stderr=subprocess.STDOUT,timeout=60);codes.append(r.returncode)
        for file in ['code/qa/test_ingestion_r01.py','code/qa/test_models_r01.py']:
            cmd2=[sys.executable,str(recovery/file)];out.write('COMMAND '+json.dumps(cmd2)+'\n');out.flush();r2=subprocess.run(cmd2,cwd=recovery,env=env,stdout=out,stderr=subprocess.STDOUT,timeout=60);codes.append(r2.returncode)
    manifest.update(status='SUCCEEDED' if all(c==0 for c in codes) else 'FAILED',exit_code=0 if all(c==0 for c in codes) else 1,finished_at=now(),log_path=str(log.relative_to(root)),actual_exit_codes=codes)
    manifest['retention_check']={'status':'PASS' if r.returncode==0 else 'FAILED','method_or_command':cmd,'isolated_directory':str(recovery.relative_to(root)),'receipt_path':str((recovery/'retrieval-receipt.json').relative_to(root)),'actual':'Actual inventory recovery and isolated repeated synthetic tests'}
    (run/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n');print(json.dumps({'status':manifest['status'],'exit_codes':codes,'manifest_sha256':sha(run/'manifest.json')}));sys.exit(manifest['exit_code'])
if __name__=='__main__':main()
