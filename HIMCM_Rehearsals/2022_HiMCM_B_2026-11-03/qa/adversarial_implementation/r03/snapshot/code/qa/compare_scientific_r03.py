"""Strict r02/r03 comparison: scientific fields equal; enumerate provenance differences."""
import argparse,csv,hashlib,json
from pathlib import Path
BASELINE_MANIFEST_SHA256='33beee2a51123a789d83e60ae02f22c05b73acecc69e17d02168d455110e5870'
def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def compare(snapshot,current):
    snapshot,current=Path(snapshot),Path(current)
    baseline=snapshot/'runs/T05-scientific-20261103-r02';manifest=baseline/'manifest.json'
    if sha(manifest)!=BASELINE_MANIFEST_SHA256:raise ValueError('Changed closed r02 manifest')
    records=json.loads(manifest.read_text())['outputs'];results=[]
    exclusions={
        'selection_frozen.json':['configuration_sha256','code_sha256','run_id','frozen_at','development_forecasts_sha256','development_metrics_sha256','selection_rule'],
        'final_assessment_receipt.json':['started_at','finished_at','loaded_selection_sha256','selection_frozen_at','final_forecasts_sha256','final_metrics_sha256'],
        'production_receipt.json':['finished_at','loaded_selection_sha256','final_assessment_sha256'],
    }
    for record in records:
        old=snapshot/record['path'];new=current/old.name
        if sha(old)!=record['sha256']:raise ValueError('Changed r02 output: '+old.name)
        if old.suffix=='.csv':
            with old.open() as f:a=list(csv.DictReader(f))
            with new.open() as f:b=list(csv.DictReader(f))
            excluded=['run_id'];changes=[key for key in excluded if [r.get(key) for r in a]!=[r.get(key) for r in b]]
            for rows in [a,b]:
                for row in rows:row.pop('run_id',None)
        else:
            a=json.loads(old.read_text());b=json.loads(new.read_text());excluded=exclusions.get(old.name,['run_id'])
            changes=[key for key in excluded if a.get(key)!=b.get(key)]
            if old.name=='selection_frozen.json':
                expected={'score':'pooled_development_mae','co2_tie_order':['D','E','Q'],'temperature_tie_order':['T0','T1-D'],'absolute_tie_tolerance':1e-12}
                if b.get('selection_rule')!=expected or 'selection_rule' in a:raise ValueError('Unexpected selector metadata change')
            for key in excluded:a.pop(key,None);b.pop(key,None)
        results.append({'file':old.name,'before_sha256':sha(old),'after_sha256':sha(new),'scientific_fields_equal':a==b,'excluded_provenance_fields':excluded,'changed_provenance_fields':changes,'byte_identical':sha(old)==sha(new)})
    if not all(r['scientific_fields_equal'] for r in results):raise ValueError('Scientific output changed: '+str([r['file'] for r in results if not r['scientific_fields_equal']]))
    return {'status':'PASS','baseline_manifest_sha256':BASELINE_MANIFEST_SHA256,'comparison_count':len(results),'scientific_outputs_equal':True,'comparisons':results,'limits':'run IDs, code/config identities, timestamps, dependent hashes and explicit unchanged-selector metadata differ; no numerical field excluded. Does not assert independent acceptance.'}
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--snapshot',required=True);p.add_argument('--outputs',required=True);p.add_argument('--report',required=True);a=p.parse_args();result=compare(a.snapshot,a.outputs)
    with Path(a.report).open('x') as f:json.dump(result,f,indent=2);f.write('\n')
    print(json.dumps({'status':result['status'],'comparison_count':result['comparison_count']}))
