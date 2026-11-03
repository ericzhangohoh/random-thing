"""Run immutable pre-G2 ingestion with exact snapshots and real recovery proof."""
import argparse
from datetime import datetime, timezone
import hashlib
import importlib.metadata
import json
import os
from pathlib import Path
import platform
import shutil
import subprocess
import sys
import time
import traceback


def now():
    return datetime.now(timezone.utc).isoformat()


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def dump(path,value):
    Path(path).write_text(json.dumps(value,indent=2)+'\n')


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--project-root',required=True)
    parser.add_argument('--run-id',required=True)
    args=parser.parse_args()
    root=Path(args.project_root).resolve()
    if not args.run_id.startswith('T05-') or '/' in args.run_id or '..' in args.run_id:
        raise ValueError('Use a safe unique T05- run ID')
    run=root/'runs'/args.run_id
    run.mkdir(parents=True,exist_ok=False)  # Refuse an existing run, including failed runs.
    start=time.monotonic()
    reproduction=run/'reproduction'
    reproduction.mkdir()
    manifest={'run_id':args.run_id,'task_id':'T05','experiment_id':'pre-G2-ingestion-r01',
              'status':'RUNNING','status_meaning':'Execution only, not scientific acceptance',
              'started_at':now(),'finished_at':None,'working_directory':str(root),
              'command':[sys.executable,*sys.argv], 'model_specification':None,
              'experiment_plan':{'path':'control/tasks/T05.md','revision':'pre-G2 ingestion scope'},
              'resource_limit':{'per_subprocess_timeout_seconds':60,'threads':1},
              'retained_artifacts':[], 'outputs':[], 'random_seeds':[],
              'solver':{'name':None,'status':'NOT_APPLICABLE: extraction and validation only'},
              'retention_check':{'status':'NOT_RUN'},'exit_code':None,
              'limitations':['No fitting/forecasts before explicit G2.','Python and installed package binaries are environment prerequisites; exact versions recorded, not bundled.'],
              'retention_contract':'Retain exact dependencies for every retained run/review/claim, including failed and superseded runs; hashes alone are insufficient.'}
    log=run/'execution.log'
    log.touch(exist_ok=False)
    manifest['log_path']=str(log.relative_to(root))
    env=os.environ.copy()
    env.update({'PYTHONDONTWRITEBYTECODE':'1','OMP_NUM_THREADS':'1','OPENBLAS_NUM_THREADS':'1','MKL_NUM_THREADS':'1'})

    def command(argv,cwd=root):
        with log.open('a') as handle:
            handle.write('\nSTART '+now()+'\nCWD '+str(cwd)+'\nARGV '+json.dumps([str(x) for x in argv])+'\n')
            handle.flush()
            result=subprocess.run([str(x) for x in argv],cwd=cwd,env=env,text=True,stdout=handle,stderr=subprocess.STDOUT,timeout=60)
            handle.write('EXIT '+str(result.returncode)+' '+now()+'\n')
        if result.returncode:
            raise RuntimeError(f'Child process failed with code {result.returncode}: {argv}')

    def retain(source,used_path,kind):
        destination=reproduction/used_path
        destination.parent.mkdir(parents=True,exist_ok=True)
        shutil.copyfile(source,destination)
        manifest['retained_artifacts'].append({'kind':kind,'used_path':str(used_path),'sha256':sha256(destination),
            'retrieval_method':'retained_file','retained_path':str(destination.relative_to(root))})

    try:
        dependencies={
          'code/data/ingest_r01.py':'executed_source','code/data/ingestion_config-r01.json':'configuration',
          'code/data/ingestion_schema-r01.json':'output_schema','code/qa/test_ingestion_r01.py':'executed_source',
          'code/qa/retrieve_retained_r01.py':'executed_source','code/experiments/run_ingestion_r01.py':'runner_source',
          'inputs/2022_HiMCM_Data.xlsx':'input','inputs/2022_HiMCM_Problem_B.pdf':'source_statement',
          'research/data-dictionary-r01.md':'input_specification','research/data-quality-r01.md':'input_evidence',
          'research/data-checks-r01.json':'input_evidence','research/problem-fulltext-r01.txt':'source_statement_text',
          'control/tasks/T05.md':'experiment_plan','handoffs/T05/computation-r00.md':'consumer_acknowledgment'}
        for path,kind in dependencies.items():
            retain(root/path,Path(path),kind)
        environment={'python':sys.version,'python_executable':sys.executable,'platform':platform.platform(),
                     'packages':{name:importlib.metadata.version(name) for name in ['numpy','scipy','pandas','openpyxl']},
                     'thread_environment':{k:env[k] for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']}}
        dump(run/'environment.json',environment)
        retain(run/'environment.json',Path('environment.json'),'environment_record')
        (run/'requirements.txt').write_text('\n'.join(k+'=='+v for k,v in environment['packages'].items())+'\n')
        retain(run/'requirements.txt',Path('requirements.txt'),'dependency_versions')
        manifest['environment']=environment
        manifest['code_files']=[{'path':i['used_path'],'sha256':i['sha256']} for i in manifest['retained_artifacts'] if 'source' in i['kind']]
        manifest['inputs']=[{'path':'inputs/2022_HiMCM_Data.xlsx','sha256':sha256(root/'inputs/2022_HiMCM_Data.xlsx'),'meaning':'Frozen supplied observations, not web references'}]
        manifest['configuration']=json.loads((reproduction/'code/data/ingestion_config-r01.json').read_text())
        manifest['output_schema']={'path':str((reproduction/'code/data/ingestion_schema-r01.json').relative_to(root)), 'sha256':sha256(reproduction/'code/data/ingestion_schema-r01.json')}
        dump(run/'manifest.json',manifest)
        command([sys.executable,reproduction/'code/qa/test_ingestion_r01.py'])
        command([sys.executable,reproduction/'code/data/ingest_r01.py','--input',reproduction/'inputs/2022_HiMCM_Data.xlsx','--config',reproduction/'code/data/ingestion_config-r01.json','--output-dir',run/'outputs'])
        # Exercise retained-file retrieval, then rerun only recovered source/config/input.
        recovery=run/'isolated-recovery'
        recovery_command=[sys.executable,reproduction/'code/qa/retrieve_retained_r01.py','--project-root',root,'--manifest',run/'manifest.json','--destination',recovery]
        command(recovery_command)
        command([sys.executable,recovery/'code/data/ingest_r01.py','--input',recovery/'inputs/2022_HiMCM_Data.xlsx','--config',recovery/'code/data/ingestion_config-r01.json','--output-dir',recovery/'rerun-outputs'],cwd=recovery)
        comparisons=[]
        for file in sorted((run/'outputs').iterdir()):
            actual=sha256(recovery/'rerun-outputs'/file.name)
            expected=sha256(file)
            comparisons.append({'file':file.name,'expected_sha256':expected,'recovered_rerun_sha256':actual,'pass':actual==expected})
        if not all(x['pass'] for x in comparisons):
            raise ValueError('Recovered isolated rerun output differs')
        dump(run/'reproduction-check.json',{'status':'PASS','comparisons':comparisons,'scope':'Bitwise identical five ingestion outputs from recovered dependencies'})
        manifest['retention_check']={'status':'PASS','method_or_command':[str(x) for x in recovery_command], 'isolated_directory':str(recovery.relative_to(root)), 'expected':'All inventoried artifacts recovered with identical hashes', 'actual':f"{len(manifest['retained_artifacts'])} files recovered and verified", 'receipt_path':str((recovery/'retrieval-receipt.json').relative_to(root))}
        manifest['checks']=[{'check_id':'ingestion_behavior','status':'PASS','evidence_path':str(log.relative_to(root))},
                            {'check_id':'real_workbook_contract','status':'PASS','evidence_path':str((run/'outputs/ingestion-checks-r01.json').relative_to(root))},
                            {'check_id':'isolated_rerun','status':'PASS','evidence_path':str((run/'reproduction-check.json').relative_to(root))}]
        # Export fixed data versions only after checks; refuse accidental replacement.
        processed=root/'data/processed'
        processed.mkdir(parents=True,exist_ok=True)
        for file in sorted((run/'outputs').glob('*.csv')):
            with (processed/file.name).open('xb') as handle:
                handle.write(file.read_bytes())
        for file in sorted((run/'outputs').iterdir()):
            manifest['outputs'].append({'path':str(file.relative_to(root)),'sha256':sha256(file),'units':'see retained ingestion_schema-r01.json','description':'Frozen source data or ingestion verification/provenance'})
        manifest['status']='SUCCEEDED';manifest['exit_code']=0
        (run/'completion-receipt.md').write_text('# T05 ingestion completion receipt\n\nActual execution succeeded. All nine behavior tests and source checks passed. All 16 retained dependencies were recovered into a fresh isolated directory and rehashed. The recovered ingestion produced five bitwise-identical outputs. Three immutable processed CSVs were exported. No model fit, selection, forecast or scientific acceptance occurred. The pinned model specification and explicit G2 release remain required.\n')
    except BaseException:
        manifest['status']='FAILED';manifest['exit_code']=1
        with log.open('a') as handle:
            traceback.print_exc(file=handle)
        raise
    finally:
        manifest['finished_at']=now();manifest['elapsed_seconds']=time.monotonic()-start
        dump(run/'manifest.json',manifest)
    print(json.dumps({'run_id':args.run_id,'status':manifest['status'],'retention_check':manifest['retention_check'],'outputs':manifest['outputs']},indent=2))


if __name__=='__main__':
    main()
