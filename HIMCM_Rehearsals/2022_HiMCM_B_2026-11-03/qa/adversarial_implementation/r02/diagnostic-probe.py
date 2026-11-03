from pathlib import Path
import sys,json,shutil,csv
Q=Path(__file__).resolve().parent;S=Q/'snapshot';O=Q/'original-outputs';sys.path.insert(0,str(S/'code/experiments'));import analysis_r02 as a
N=Q/'nonpositive-complete';N.mkdir()
for name in ['selection_frozen.json','final_assessment_receipt.json','development_forecasts.csv','development_metrics.csv','final_forecasts.csv','final_metrics.csv']:shutil.copyfile(O/name,N/name)
class Injected(a.Analysis):
 def predict(self,mid,pack,year):
  if mid=='D' and year==2023:return -1.0
  return super().predict(mid,pack,year)
x=Injected(S,N,S/'config.json');x.production()
with (N/'path_diagnostics.csv').open() as f:diags=[r for r in csv.DictReader(f) if r['model_id']=='D']
with (N/'threshold_search_paths.csv').open() as f:rows=[r for r in csv.DictReader(f) if r['model_id']=='D' and r['year']=='2023']
assert all(r['nonpositive_co2_count']=='0' and r['invalid_count']=='278' for r in diags)
assert all(r['status']=='NONPOSITIVE_CO2' for r in rows)
(Q/'diagnostic-results.json').write_text(json.dumps({'production_completed':True,'diagnostics':diags,'first_invalid_rows':rows},indent=2))
