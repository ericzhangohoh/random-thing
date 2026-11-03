"""Compare completed primary tables to retained independent A01/A02 evidence."""
import argparse,csv,hashlib,json,os,platform,shutil,subprocess,sys
from datetime import datetime,timezone
from pathlib import Path
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def now():return datetime.now(timezone.utc).isoformat()
def dump(p,d):Path(p).write_text(json.dumps(d,indent=2,allow_nan=False)+'\n')
def rows(p):
    with Path(p).open() as f:return list(csv.DictReader(f))

def evaluate(snapshot,out,source_run):
    s=Path(snapshot);p=s/'runs'/source_run/'outputs';checks=[]
    def check(name,a,b,tol=1e-9):
        numeric=isinstance(a,(int,float)) and isinstance(b,(int,float));delta=abs(a-b) if numeric else None
        checks.append({'check':name,'primary':a,'independent':b,'absolute_difference':delta,'tolerance':tol if numeric else None,'pass':delta<=tol if numeric else a==b})
    sel=json.loads((p/'selection_frozen.json').read_text());a01dev=json.loads((s/'qa/adversarial_validation/development_probe_r01.json').read_text());a01final=json.loads((s/'qa/adversarial_validation/assessment_r01.json').read_text());a02=json.loads((s/'qa/adversarial_structure/probe-results-r01.json').read_text())
    check('selected_ids',[sel['selected_co2_id'],sel['selected_temperature_id']],a01dev['selected'])
    dev_metrics=rows(p/'development_metrics.csv');final_metrics=rows(p/'final_metrics.csv');final_rows=rows(p/'final_forecasts.csv');summary=rows(p/'forecast_summary.csv');envelopes=rows(p/'historical_error_envelopes.csv')
    for mid,score in sel['development_mae'].items():
        check('A01developmentMAE/'+mid,score,a01dev['scores'][mid]);check('A02developmentMAE/'+mid,score,a02['metrics'][mid]['mae'])
        for i,origin in enumerate(sel['development_origins']):
            actual=float(next(r['mae'] for r in dev_metrics if r['model_id']==mid and r['grouping']=='origin' and int(r['group_value'])==origin));check('A01originMAE/'+mid+'/'+str(origin),actual,a01dev['origin_mae'][mid][i]);check('A02originMAE/'+mid+'/'+str(origin),actual,a02['metrics'][mid]['by_origin'][str(origin)])
        for h in range(1,11):
            actual=float(next(r['mae'] for r in dev_metrics if r['model_id']==mid and r['grouping']=='horizon' and int(r['group_value'])==h));check('A01horizonMAE/'+mid+'/'+str(h),actual,a01dev['horizon_mae'][mid][h-1])
            actual=float(next(r['error'] for r in final_rows if r['model_id']==mid and int(r['horizon'])==h));check('A01final_error/'+mid+'/'+str(h),actual,a01final['final'][mid]['errors'][h-1])
        actual=float(next(r['mae'] for r in final_metrics if r['model_id']==mid and r['grouping']=='overall'));check('A01finalMAE/'+mid,actual,a01final['final'][mid]['MAE'])
        for i,y in enumerate([2050,2100]):
            actual=float(next(r['value'] for r in summary if r['model_id']==mid and r['fit_window']=='full' and int(r['year'])==y));check('A01production/'+mid+'/'+str(y),actual,a01final['production_2050_2100'][mid][i])
    for mid in [sel['selected_co2_id'],sel['selected_temperature_id']]:
        selected=[r for r in envelopes if r['selected_model_id']==mid]
        for r in selected:check('A01radius/'+mid+'/'+r['horizon'],float(r['radius']),a01final['final'][mid]['radii'][int(r['horizon'])-1])
        check('A01miss_horizons/'+mid,[int(r['horizon']) for r in selected if r['final_contained']=='False'],a01final['final'][mid]['miss_horizons'])
    ranks=rows(p/'rank_stability.csv');loo=[next(r['diagnostic_winner'] for r in ranks if r['diagnostic']=='leave_one_origin_out' and int(r['omitted_origin'])==o) for o in sel['development_origins']];check('A01leave_one_origin_out',loo,a01dev['leave_origin_out_winners'])
    primary_rows={(r['model_id'],int(r['origin_year']),int(r['target_year'])):r for r in rows(p/'development_forecasts.csv')}
    for r in a02['rows']:
        key=(r['model'],r['origin'],r['year'])
        if key in primary_rows:check('A02row/'+str(key),float(primary_rows[key]['predicted']),r['pred'])
    result={'status':'PASS' if all(r['pass'] for r in checks) else 'FAIL','source_run':source_run,'comparison_count':len(checks),'max_numeric_difference':max(r['absolute_difference'] for r in checks if r['absolute_difference'] is not None),'checks':checks,'scope':'Author reconciliation of already independently computed outputs, not independent acceptance. No fitting or model retuning.','not_compared':'A02 exploratory omitted models and through2011 association use different scope; A01 exploratory29year hindcast is not an authorized primary experiment.'}
    dump(out,result);print(json.dumps({k:result[k] for k in ['status','comparison_count','max_numeric_difference']}));return result['status']=='PASS'

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--project-root');ap.add_argument('--run-id');ap.add_argument('--source-run',default='T05-scientific-20261103-r02');ap.add_argument('--evaluate',action='store_true');ap.add_argument('--snapshot');ap.add_argument('--out');a=ap.parse_args()
    if a.evaluate:sys.exit(0 if evaluate(a.snapshot,a.out,a.source_run) else 1)
    root=Path(a.project_root);run=root/'runs'/a.run_id;run.mkdir(parents=True,exist_ok=False);snapshot=run/'reproduction';snapshot.mkdir();log=run/'execution.log'
    manifest={'run_id':a.run_id,'status':'RUNNING','started_at':now(),'command':[sys.executable,*sys.argv],'working_directory':str(root),'retained_artifacts':[],'historical_fits_executed':False,'retention_check':{'status':'NOT_RUN'},'solver':{'status':'NOT_APPLICABLE_TABLE_COMPARISON'}}
    files=['code/qa/reconcile_adversarial_r01.py','code/qa/retrieve_retained_r01.py','qa/adversarial_validation/development_probe_r01.json','qa/adversarial_validation/assessment_r01.json','qa/adversarial_structure/probe-results-r01.json']+[f'runs/{a.source_run}/outputs/{name}' for name in ['selection_frozen.json','development_metrics.csv','development_forecasts.csv','final_metrics.csv','final_forecasts.csv','forecast_summary.csv','historical_error_envelopes.csv','rank_stability.csv']]
    for name in files:
        target=snapshot/name;target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(root/name,target);manifest['retained_artifacts'].append({'kind':'reconciliation_dependency','used_path':name,'sha256':sha(target),'retrieval_method':'retained_file','retained_path':str(target.relative_to(root))})
    manifest['environment']={'python':sys.version,'executable':sys.executable,'platform':platform.platform()};dump(run/'manifest.json',manifest);env=os.environ.copy();env['PYTHONDONTWRITEBYTECODE']='1'
    def cmd(argv,cwd):
        with log.open('a') as f:
            f.write('COMMAND '+json.dumps([str(x) for x in argv])+'\n');f.flush();r=subprocess.run([str(x) for x in argv],cwd=cwd,env=env,stdout=f,stderr=subprocess.STDOUT,timeout=60);f.write('EXIT '+str(r.returncode)+'\n')
        if r.returncode:raise RuntimeError('Reconciliation command failed')
    try:
        cmd([sys.executable,snapshot/'code/qa/reconcile_adversarial_r01.py','--evaluate','--snapshot',snapshot,'--source-run',a.source_run,'--out',run/'comparison.json'],run)
        recovery=run/'isolated-recovery';recover=[sys.executable,snapshot/'code/qa/retrieve_retained_r01.py','--project-root',root,'--manifest',run/'manifest.json','--destination',recovery];cmd(recover,run)
        cmd([sys.executable,recovery/'code/qa/reconcile_adversarial_r01.py','--evaluate','--snapshot',recovery,'--source-run',a.source_run,'--out',recovery/'comparison.json'],recovery)
        if sha(run/'comparison.json')!=sha(recovery/'comparison.json'):raise ValueError('Reconciliation rerun differs')
        manifest.update(status='SUCCEEDED',exit_code=0,outputs=[{'path':str((run/'comparison.json').relative_to(root)),'sha256':sha(run/'comparison.json')}],retention_check={'status':'PASS','method_or_command':[str(x) for x in recover],'isolated_directory':str(recovery.relative_to(root)),'receipt_path':str((recovery/'retrieval-receipt.json').relative_to(root)),'actual':'All13 dependencies recovered; comparison output reproduced byte-for-byte'})
    except BaseException:manifest.update(status='FAILED',exit_code=1);raise
    finally:manifest['finished_at']=now();manifest['log_path']=str(log.relative_to(root));dump(run/'manifest.json',manifest)
    print(json.dumps({'status':manifest['status'],'manifest_sha256':sha(run/'manifest.json'),'comparison':json.loads((run/'comparison.json').read_text())['comparison_count']}))
if __name__=='__main__':main()
