"""Immutable bounded execution and isolated-directory reproduction wrapper."""
import argparse
from datetime import datetime,timezone
import hashlib,importlib.metadata,json,os,platform,shutil,subprocess,sys,time,traceback
from pathlib import Path
def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def now():return datetime.now(timezone.utc).isoformat()
def dump(path,data):Path(path).write_text(json.dumps(data,indent=2,allow_nan=False)+'\n')

def main():
    p=argparse.ArgumentParser();p.add_argument('--project-root',required=True);p.add_argument('--run-id',required=True);args=p.parse_args();root=Path(args.project_root).resolve()
    if not args.run_id.startswith('T05-') or '/' in args.run_id or '..' in args.run_id:raise ValueError('Unsafe run ID')
    run=root/'runs'/args.run_id;run.mkdir(parents=True,exist_ok=False);snapshot=run/'reproduction';snapshot.mkdir();log=run/'execution.log';log.touch(exist_ok=False);start=time.monotonic()
    env=os.environ.copy();env.update({'PYTHONDONTWRITEBYTECODE':'1','OMP_NUM_THREADS':'1','OPENBLAS_NUM_THREADS':'1','MKL_NUM_THREADS':'1'})
    manifest={'run_id':args.run_id,'task_id':'T05','experiment_id':'T06-E01-through-E08-r02','status':'RUNNING','started_at':now(),'finished_at':None,'working_directory':str(root),'command':[sys.executable,*sys.argv],'status_meaning':'Execution only; no scientific acceptance','retained_artifacts':[],'outputs':[],'random_seeds':[],'solver':{'name':'numpy.linalg.lstsq SVD','status':'NOT_STARTED','tolerances':{'lstsq_rcond':None,'crossing_equality_absolute':1e-9,'selection_tie_absolute':1e-12}},'resource_limit':{'seconds_per_subprocess':60,'threads':1},'retention_check':{'status':'NOT_RUN'},'log_path':str(log.relative_to(root)),'exit_code':None,'limitations':['Python/package binaries not bundled; exact interpreter/package versions recorded.','Candidate evidence awaiting independent review and adversarial resolution.'],'retention_contract':'Retain exact dependencies while any associated run/review/claim exists, including failed/superseded runs; hashes alone are insufficient.'}
    def retain(source,used,kind):
        target=snapshot/used;target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(source,target);manifest['retained_artifacts'].append({'kind':kind,'used_path':str(used),'sha256':sha(target),'retrieval_method':'retained_file','retained_path':str(target.relative_to(root))})
    def command(argv,cwd=root):
        with log.open('a') as f:
            f.write('\nSTART '+now()+'\nCWD '+str(cwd)+'\nARGV '+json.dumps([str(a) for a in argv])+'\n');f.flush();result=subprocess.run([str(a) for a in argv],cwd=cwd,env=env,text=True,stdout=f,stderr=subprocess.STDOUT,timeout=60);f.write('EXIT '+str(result.returncode)+' '+now()+'\n')
        if result.returncode:raise RuntimeError(f'Subprocess failed with code{result.returncode}: {argv}')
    try:
        import numpy,scipy,pandas,openpyxl
        environment={'python':sys.version,'executable':sys.executable,'platform':platform.platform(),'packages':{name:importlib.metadata.version(name) for name in ['numpy','scipy','pandas','openpyxl']},'threads':{k:env[k] for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']}}
        dump(run/'environment.json',environment);(run/'requirements.txt').write_text('\n'.join(k+'=='+v for k,v in environment['packages'].items())+'\n');manifest['environment']=environment
        release=json.loads((root/'control/accepted-inputs-g2-r02.json').read_text())
        for path,expected in release['sha256'].items():
            if sha(root/path)!=expected:raise ValueError('Released artifact changed: '+path)
        files=['code/modeling/climate_models_r02.py','code/experiments/analysis_r02.py','code/experiments/run_analysis_r02.py','code/experiments/output_schema-r02.json','code/qa/test_models_r02.py','code/qa/preflight-review-r01.md','code/qa/retrieve_retained_r01.py','code/data/ingest_r01.py','code/data/ingestion_config-r01.json','code/data/ingestion_schema-r01.json','code/qa/test_ingestion_r01.py','inputs/2022_HiMCM_Data.xlsx','inputs/2022_HiMCM_Problem_B.pdf','research/data-dictionary-r01.md','research/data-quality-r01.md','research/problem-fulltext-r01.txt','data/processed/co2-r01.csv','data/processed/temperature-r01.csv','data/processed/joined-r01.csv','models/framing-r02.md','models/model_spec-r02.md','models/model_decision-r03.md','models/assumptions-r01.md','models/experiment_plan-r03.md','models/model_interface-r02.md','control/accepted-inputs-g2-r02.json','control/gates/G1-r01.md','control/gates/G2-r02.md','control/tasks/T05.md','handoffs/T05/computation-r03.md','qa/framing-r01/review.md']
        files=list(dict.fromkeys(files+list(release['sha256'])))
        for path in files:retain(root/path,Path(path),'source' if path.endswith('.py') else 'input_or_specification')
        config={'revision':'approved-r02-unchanged-forms-no-retuning','run_id':args.run_id,'development_origins':[1981,1986,1991,1996,2001],'final_origin':2011,'production_origin':2021,'display_end':2100,'search_end':2300,'selected_window_sensitivity_start':1992,'co2_tie_order':['D','E','Q'],'temperature_tie_first':'T0','information_cutoff':2021,'source_vintage':'supplied2022','max_horizon':10,'threshold_tolerance':1e-9,'selection_tolerance':1e-12}
        dump(run/'config.json',config);retain(run/'config.json',Path('config.json'),'configuration');retain(run/'environment.json',Path('environment.json'),'environment_record');retain(run/'requirements.txt',Path('requirements.txt'),'package_versions')
        manifest['model_specification']={'path':'models/model_spec-r02.md','sha256':sha(snapshot/'models/model_spec-r02.md'),'revision':'r02'};manifest['experiment_plan']={'path':'models/experiment_plan-r03.md','sha256':sha(snapshot/'models/experiment_plan-r03.md'),'revision':'r03'};manifest['output_schema']={'path':'code/experiments/output_schema-r02.json','sha256':sha(snapshot/'code/experiments/output_schema-r02.json')};manifest['configuration']=config;manifest['inputs']=[{'path':f,'sha256':sha(snapshot/f)} for f in files if f.startswith(('inputs/','data/processed/'))];manifest['code_files']=[{'path':r['used_path'],'sha256':r['sha256']} for r in manifest['retained_artifacts'] if r['kind']=='source'];dump(run/'manifest.json',manifest)
        command([sys.executable,snapshot/'code/qa/test_ingestion_r01.py']);command([sys.executable,snapshot/'code/qa/test_models_r02.py'])
        command([sys.executable,snapshot/'code/data/ingest_r01.py','--input',snapshot/'inputs/2022_HiMCM_Data.xlsx','--config',snapshot/'code/data/ingestion_config-r01.json','--output-dir',run/'input-reaudit'])
        for file in (run/'input-reaudit').glob('*.csv'):
            if sha(file)!=sha(snapshot/'data/processed'/file.name):raise ValueError('Original workbook reingestion mismatch')
        for phase in ['development','final','production']:command([sys.executable,snapshot/'code/experiments/analysis_r02.py','--phase',phase,'--snapshot',snapshot,'--output-dir',run/'outputs','--config',snapshot/'config.json'])
        manifest['solver']['status']='SUCCEEDED_FULL_RANK_ALL_EXECUTED_REGRESSIONS'
        recovery=run/'isolated-recovery';retrieve=[sys.executable,snapshot/'code/qa/retrieve_retained_r01.py','--project-root',root,'--manifest',run/'manifest.json','--destination',recovery];command(retrieve)
        for phase in ['development','final','production']:command([sys.executable,recovery/'code/experiments/analysis_r02.py','--phase',phase,'--snapshot',recovery,'--output-dir',recovery/'rerun-outputs','--config',recovery/'config.json'],cwd=recovery)
        comparisons=[]
        for file in sorted((run/'outputs').iterdir()):
            if file.name in ['selection_frozen.json','final_assessment_receipt.json','production_receipt.json']:continue
            actual=sha(recovery/'rerun-outputs'/file.name);expected=sha(file);comparisons.append({'file':file.name,'expected_sha256':expected,'actual_sha256':actual,'pass':actual==expected})
        selection=json.loads((run/'outputs/selection_frozen.json').read_text());reselected=json.loads((recovery/'rerun-outputs/selection_frozen.json').read_text());selection.pop('frozen_at');reselected.pop('frozen_at');selection_match=selection==reselected
        if not all(r['pass'] for r in comparisons) or not selection_match:raise ValueError('Recovered numerical reproduction differs')
        dump(run/'reproduction-check.json',{'status':'PASS','numeric_output_comparisons':comparisons,'selection_semantically_identical':selection_match,'metadata_exclusions':['freeze timestamp','final timestamps and hash of timestamped freeze','production timestamp and hash of timestamped final receipt'],'meaning':'Exact numerical output bytes and decisions; execution provenance naturally differs.'})
        manifest['retention_check']={'status':'PASS','method_or_command':[str(x) for x in retrieve],'isolated_directory':str(recovery.relative_to(root)),'expected':'Recover every inventory artifact with exact hash','actual':f"{len(manifest['retained_artifacts'])} dependencies recovered; {len(comparisons)} numerical outputs bitwise identical; same frozen decisions",'receipt_path':str((recovery/'retrieval-receipt.json').relative_to(root))}
        for f in sorted((run/'outputs').iterdir()):manifest['outputs'].append({'path':str(f.relative_to(root)),'sha256':sha(f),'description':'See retained output_schema-r02.json','units':'explicit CSV unit columns and schema'})
        manifest['checks']=[{'id':'own_implementation_tests','status':'PASS','evidence_path':str(log.relative_to(root))},{'id':'original_workbook_reingestion','status':'PASS','evidence_path':str((run/'input-reaudit/ingestion-checks-r01.json').relative_to(root))},{'id':'postrun_checks','status':'PASS','evidence_path':str((run/'outputs/numerical_checks.json').relative_to(root))},{'id':'isolated_reproduction','status':'PASS','evidence_path':str((run/'reproduction-check.json').relative_to(root))}]
        manifest['status']='SUCCEEDED';manifest['exit_code']=0
        (run/'completion-receipt.md').write_text('# T05 numerical execution receipt\n\nOwn synthetic/negative/leakage tests preceded historical fits. Original workbook reingestion matched admitted tables. Distinct development, final and production commands ran in order; final loaded saved development-only selection, then production refitted unchanged forms. Exact numerical outputs and frozen decisions reproduced from actual isolated recovered dependencies. See manifest, execution.log and reproduction-check.json. Execution success is candidate evidence; independent review/adversarial resolution remain required. No scientific acceptance or PDF success asserted.\n')
    except BaseException:
        manifest['status']='FAILED';manifest['exit_code']=1
        with log.open('a') as f:traceback.print_exc(file=f)
        raise
    finally:
        manifest['finished_at']=now();manifest['elapsed_seconds']=time.monotonic()-start;dump(run/'manifest.json',manifest)
    print(json.dumps({'run_id':args.run_id,'status':manifest['status'],'retention':manifest['retention_check'],'manifest_sha256':sha(run/'manifest.json')},indent=2))

if __name__=='__main__':main()
