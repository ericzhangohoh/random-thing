from pathlib import Path
import sys,shutil,json,csv,hashlib
Q=Path(__file__).resolve().parent;S=Q/'snapshot';O=Q/'original-outputs';sys.path.insert(0,str(S/'code/experiments'));import analysis_r03 as a
sha=lambda f:hashlib.sha256(f.read_bytes()).hexdigest()
def stage(name,final=False):
 d=Q/name;d.mkdir()
 names=['selection_frozen.json','development_forecasts.csv','development_metrics.csv']
 if final:names+=['final_assessment_receipt.json','final_forecasts.csv','final_metrics.csv']
 for f in names:shutil.copyfile(O/f,d/f)
 return d
results={'semantic_cases':[],'diagnostic_cases':[]}
mutators={'selected_ids':lambda r:r.update(selected_co2_id='Q',selected_temperature_id='T1-Q'),'eligible_pair':lambda r:r.update(temperature_selection_candidates=['T0','T1-Q']),'score':lambda r:r['development_mae'].update(D=0),'tie':lambda r:r['selection_rule'].update(absolute_tie_tolerance=1),'exposure':lambda r:r.update(project_final_scores_previously_exposed_by_A01=False),'ids_production':lambda r:r.update(selected_co2_id='Q',selected_temperature_id='T1-Q'),'rehashed_metric':lambda r:None}
for name,mut in mutators.items():
 d=stage('tamper-'+name,name=='ids_production');r=json.loads((d/'selection_frozen.json').read_text());mut(r)
 if name=='rehashed_metric':
  f=d/'development_metrics.csv'
  with f.open() as h:reader=csv.DictReader(h);fields=reader.fieldnames;rows=list(reader)
  for row in rows:
   if row['model_id']=='D' and row['grouping']=='overall':row['mae']='0'
  with f.open('w',newline='') as h:w=csv.DictWriter(h,fieldnames=fields,lineterminator='\n');w.writeheader();w.writerows(rows)
  r['development_metrics_sha256']=sha(f)
 (d/'selection_frozen.json').write_text(json.dumps(r));before={f.name:sha(f) for f in d.iterdir()};obj=a.Analysis(S,d,S/'config.json')
 try:obj.production() if name=='ids_production' else obj.final();raise AssertionError('Mutation accepted: '+name)
 except ValueError as e:err=str(e)
 after={f.name:sha(f) for f in d.iterdir()};assert before==after,'Outputs changed on rejected '+name
 results['semantic_cases'].append({'case':name,'rejected':True,'error':err,'no_new_or_changed_stage_outputs':True})
# Successful control exercises changed semantic validation in both stages.
d=stage('valid-control');before=sha(d/'selection_frozen.json');obj=a.Analysis(S,d,S/'config.json');obj.final();obj.production();assert sha(d/'selection_frozen.json')==before
with (d/'path_diagnostics.csv').open() as h:assert all(r['nonpositive_co2_count']=='0' for r in csv.DictReader(h) if r['target']=='co2')
results['valid_control']={'completed':True,'frozen_receipt_unchanged':True,'positive_path_count_zero':True}
for name in ['negative','zero','repeat_negative','nonfinite']:
 d=stage('diagnostic-'+name,True)
 class Injected(a.Analysis):
  def predict(self,mid,pack,year):
   if mid=='D' and (year==2023 or (name=='repeat_negative' and year==2024)):
    if name=='nonfinite':raise a.m.ModelFailure('NONFINITE_PREDICTION','synthetic nonfinite')
    return 0.0 if name=='zero' else -1.0
   return super().predict(mid,pack,year)
 Injected(S,d,S/'config.json').production()
 with (d/'path_diagnostics.csv').open() as h:rows=[r for r in csv.DictReader(h) if r['model_id']=='D']
 expected=0 if name=='nonfinite' else 1
 assert len(rows)==2 and all(int(r['nonpositive_co2_count'])==expected and int(r['invalid_count'])==278 for r in rows)
 results['diagnostic_cases'].append({'case':name,'completed':True,'expected_direct_nonpositive_count':expected,'observed_counts':[int(r['nonpositive_co2_count']) for r in rows],'invalid_counts':[int(r['invalid_count']) for r in rows]})
pins=json.loads((Q/'pins.json').read_text());P=Q.parents[2];assert all(sha(P/f)==v for f,v in pins.items());results['original_targets_unchanged']=True
(Q/'results.json').write_text(json.dumps(results,indent=2));print(json.dumps(results,indent=2))
