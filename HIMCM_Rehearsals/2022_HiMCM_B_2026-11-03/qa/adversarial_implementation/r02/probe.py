from pathlib import Path
import sys,json,shutil,subprocess,csv,hashlib,copy
import numpy as np
Q=Path(__file__).resolve().parent;S=Q/'snapshot';O=Q/'original-outputs';sys.path.insert(0,str(S/'code/experiments'));import analysis_r02 as a
m=a.m;py='/Users/ericzhang/.venvs/default/bin/python3';results={};logs=[]
def obj(out):return a.Analysis(S,out,S/'config.json')
def cp_stage(out,final=True):
 out.mkdir()
 for f in O.iterdir():
  if f.name.startswith('development_') or f.name=='selection_frozen.json' or (final and (f.name.startswith('final_'))):shutil.copyfile(f,out/f.name)
# Independent isolated full stage run.
R=Q/'rerun';R.mkdir()
for phase in ['development','final','production']:
 cmd=[py,str(S/'code/experiments/analysis_r02.py'),'--phase',phase,'--snapshot',str(S),'--output-dir',str(R),'--config',str(S/'config.json')]
 r=subprocess.run(cmd,cwd=S,text=True,capture_output=True,timeout=60);logs.append(phase+'\n'+r.stdout+r.stderr);assert r.returncode==0,r.stderr
excluded={'selection_frozen.json','final_assessment_receipt.json','production_receipt.json'}
comparison={f.name:hashlib.sha256(f.read_bytes()).hexdigest()==hashlib.sha256((O/f.name).read_bytes()).hexdigest() for f in R.iterdir() if f.name not in excluded};assert all(comparison.values());results['isolated_numerical_match']=comparison
# Frozen receipt semantic mutation, no changes to development evidence.
T=Q/'tampered-selection';cp_stage(T,False);rec=json.loads((T/'selection_frozen.json').read_text());rec['selected_co2_id']='Q';rec['selected_temperature_id']='T1-Q';(T/'selection_frozen.json').write_text(json.dumps(rec));ob=obj(T)
try:
 ob.final();results['tampered_selection']={'accepted':True,'final_receipt':json.loads((T/'final_assessment_receipt.json').read_text())}
except Exception as e:results['tampered_selection']={'accepted':False,'error':str(e)}
# Evidence-table tamper rejects.
for kind in ['development','final']:
 out=Q/('tampered-'+kind);cp_stage(out)
 f=out/(kind+'_forecasts.csv');f.write_text(f.read_text()+'\n')
 try:
  oo=obj(out);oo.load_frozen() if kind=='development' else oo.production();results[kind+'_table_tamper_rejected']=False
 except ValueError as e:results[kind+'_table_tamper_rejected']=str(e)
# Future-target invariance and actual forecastCO2 dependency.
ob=obj(Q/'functions');base={k:v.copy() for k,v in ob.data.items()};pert={k:v.copy() for k,v in base.items()};mask=base['year']>1991;pert['co2_ppm'][mask]+=1000;pert['temp_anomaly_c'][mask]-=100
p1=ob.fits(base,1991);p2=ob.fits(pert,1991)
results['future_perturbation_fit_invariant']=all(p1[k]==p2[k] for k in p1)
results['future_perturbation_prediction_invariant']=all(ob.predict(k,p1[k],2001)==ob.predict(k,p2[k],2001) for k in p1)
changed=copy.deepcopy(p1['T1-D']);changed['upstream']['parameters']['slope_ppm_per_year']+=1
results['pipeline_responds_to_predicted_CO2']=ob.predict('T1-D',changed,2001)!=ob.predict('T1-D',p1['T1-D'],2001)
cases={'cross_then_invalid':lambda y: -1 if y==2024 else 680+3*(y-2021),'invalid_then_cross':lambda y:-1 if y==2022 else 680+3*(y-2021),'negative_temperature':lambda y:-.2+.1*(y-2021)}
results['crossings']={k:m.crossing(f,685 if k!='negative_temperature' else .05,search_end=2026,positive_required=k!='negative_temperature') for k,f in cases.items()}
# Exercise actual production table assembly on synthetic nonpositive D prediction.
N=Q/'nonpositive-production';cp_stage(N)
class Injected(a.Analysis):
 def predict(self,mid,pack,year):
  if mid=='D' and year==2023:return -1.0
  return super().predict(mid,pack,year)
try:Injected(S,N,S/'config.json').production();results['nonpositive_production_completed']=True
except Exception as e:results['nonpositive_production_completed']=False;results['nonpositive_production_error']=repr(e)
with (N/'path_diagnostics.csv').open() as f:results['nonpositive_diagnostics']=[r for r in csv.DictReader(f) if r['model_id']=='D']
with (N/'threshold_search_paths.csv').open() as f:results['nonpositive_rows']=[r for r in csv.DictReader(f) if r['model_id']=='D' and r['year']=='2023']
(Q/'results.json').write_text(json.dumps(results,indent=2));(Q/'execution.log').write_text('\n'.join(logs))
print(json.dumps({k:v for k,v in results.items() if k not in ['isolated_numerical_match']},indent=2))
