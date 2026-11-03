from pathlib import Path
import csv,json,hashlib
from datetime import datetime
P=Path(__file__).resolve().parents[2];Q=Path(__file__).resolve().parent
A=P/'runs/T05-scientific-20261103-r02';B=P/'runs/T05-scientific-20261103-r03'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(A/'manifest.json')=='33beee2a51123a789d83e60ae02f22c05b73acecc69e17d02168d455110e5870'
assert sha(B/'manifest.json')=='7bc6e1fe3498302d247b45fa97c4d13498edfbf5366cddd078ff7ebfaff4bc00'
for R in [A,B]:
 for item in json.loads((R/'manifest.json').read_text())['outputs']:assert sha(P/item['path'])==item['sha256'],item['path']
files=sorted(f.name for f in (A/'outputs').iterdir());assert files==sorted(f.name for f in (B/'outputs').iterdir()) and len(files)==35
exceptions={
 'selection_frozen.json':{'configuration_sha256','code_sha256','run_id','frozen_at','development_forecasts_sha256','development_metrics_sha256','selection_rule'},
 'final_assessment_receipt.json':{'started_at','finished_at','loaded_selection_sha256','selection_frozen_at','final_forecasts_sha256','final_metrics_sha256'},
 'production_receipt.json':{'finished_at','loaded_selection_sha256','final_assessment_sha256'},
 'claim_candidates.json':{'run_id'},'ten_year_comparison.json':{'run_id'},'numerical_checks.json':set()}
comparisons=[]
for n in files:
 if n.endswith('.csv'):
  def read(R):
   with (R/'outputs'/n).open() as f:
    rs=list(csv.DictReader(f));assert all(r.pop('run_id')==R.name for r in rs);return rs
  a,b=read(A),read(B);assert a==b,n;comparisons.append({'file':n,'exact_fields_equal':True,'excluded':['run_id'],'rows':len(a)})
 else:
  a=json.loads((A/'outputs'/n).read_text());b=json.loads((B/'outputs'/n).read_text());ex=exceptions[n]
  assert {k:v for k,v in a.items() if k not in ex}=={k:v for k,v in b.items() if k not in ex},n
  comparisons.append({'file':n,'exact_fields_equal':True,'excluded':sorted(ex)})
sel=json.loads((B/'outputs/selection_frozen.json').read_text());fin=json.loads((B/'outputs/final_assessment_receipt.json').read_text());prod=json.loads((B/'outputs/production_receipt.json').read_text())
assert sel['selection_rule']=={'score':'pooled_development_mae','co2_tie_order':['D','E','Q'],'temperature_tie_order':['T0','T1-D'],'absolute_tie_tolerance':1e-12}
assert sel['selected_co2_id']=='D' and sel['selected_temperature_id']=='T1-D'
assert sel['project_final_scores_previously_exposed_by_A01'] is True and sel['selection_rule_changed_after_exposure'] is False
for k,p in [('configuration_sha256','config.json'),('code_sha256','code/experiments/analysis_r03.py'),('model_code_sha256','code/modeling/climate_models_r02.py'),('input_sha256','data/processed/joined-r01.csv'),('spec_sha256','models/model_spec-r02.md')]:assert sel[k]==sha(B/'reproduction'/p)
for stem in ['development_forecasts','development_metrics']:assert sel[stem+'_sha256']==sha(B/'outputs'/(stem+'.csv'))
for stem in ['final_forecasts','final_metrics']:assert fin[stem+'_sha256']==sha(B/'outputs'/(stem+'.csv'))
assert fin['loaded_selection_sha256']==prod['loaded_selection_sha256']==sha(B/'outputs/selection_frozen.json')
assert prod['final_assessment_sha256']==sha(B/'outputs/final_assessment_receipt.json')
assert fin['selection_frozen_at']==sel['frozen_at']
assert datetime.fromisoformat(sel['frozen_at'])<datetime.fromisoformat(fin['started_at'])<=datetime.fromisoformat(fin['finished_at'])<datetime.fromisoformat(prod['finished_at'])
a=json.loads((A/'config.json').read_text());b=json.loads((B/'config.json').read_text());a.pop('run_id');b.pop('run_id');assert a==b
assert sha(A/'reproduction/code/modeling/climate_models_r02.py')==sha(B/'reproduction/code/modeling/climate_models_r02.py')
# Old reviewed targets, not merely producer's current file inventory.
old=json.loads((P/'qa/numerical-r00/target-inventory-initial.json').read_text());assert all(sha(Path(x['source']))==x['sha256'] for x in old)
result={'status':'PASS','independent_comparator':True,'production_comparator_imported':False,'comparison_count':35,'comparisons':comparisons,'numeric_or_scientific_fields_excluded':False,'new_selector_metadata_explicitly_verified':True,'all_excluded_current_hash_links_verified':True,'current_local_chronology_verified':True,'config_and_model_equations_unchanged':True,'previous_reviewed_targets_unchanged':True,'existing_independent_math_applies_by_exact_scientific_equivalence':True}
(Q/'equivalence-independent.json').write_text(json.dumps(result,indent=2)+'\n');print('PASS: all 35 scientific outputs identical; explicit selector metadata/hash links/chronology verified; no math rerun')
