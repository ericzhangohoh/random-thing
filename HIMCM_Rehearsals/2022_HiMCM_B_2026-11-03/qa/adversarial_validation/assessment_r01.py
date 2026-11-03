# A01 independent assessment; consumes frozen development_probe_r01 receipt.
# This exposes 2012-2021 forecast errors. No tuning or primary rule change authorized.
from probe_r01 import P,O,preds,y,c,t,np,json,hashlib
receipt=json.loads((O/'development_probe_r01.json').read_text()); result={'holdout_consumed':True,'holdout_years':[2012,2021],'frozen_ids':receipt['selected'],'selection_basis':'development_probe_r01.json persisted before this script'}
err=np.load(O/'development_errors_r01.npz'); pp=preds(2011,np.arange(2012,2022)); result['final']={}
for k,v in pp.items():
 e=v-(t if k.startswith('T') else c)[y>=2012]; B=np.maximum.accumulate(np.max(abs(err[k]),axis=0))
 result['final'][k]={'MAE':float(np.mean(abs(e))),'errors':e.tolist(),'radii':B.tolist(),'miss_horizons':(np.where(abs(e)>B)[0]+1).tolist()}
# Pre-2012 29-year illustrative long-horizon hindcast; no 2021 final targets enter.
long=preds(1981,np.array([2010])); result['pre2012_29_year_hindcast']={k:{'prediction':float(v[0]),'absolute_error':float(abs(v[0]-(t if k.startswith('T') else c)[y==2010][0]))} for k,v in long.items()}
result['production_2050_2100']={k:v.tolist() for k,v in preds(2021,np.array([2050,2100])).items()}
(O/'assessment_r01.json').write_text(json.dumps(result,indent=2)+'\n'); print(json.dumps(result,indent=2))
