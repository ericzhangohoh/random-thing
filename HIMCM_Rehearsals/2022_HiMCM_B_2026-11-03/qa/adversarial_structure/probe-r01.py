from pathlib import Path
import json,hashlib
import openpyxl,numpy as np
p=Path(__file__).resolve().parents[2]
w=openpyxl.load_workbook(p/'inputs/2022_HiMCM_Data.xlsx',data_only=True)
def vals(s):return {int(a):float(b) for a,b in w[s].iter_rows(min_row=2,max_col=2,values_only=True) if a is not None}
c=vals('CO2 Data Set 1'); t=vals('Temps Data Set 2'); cref=c[1959]
def fit(x,y,deg=1):return np.polynomial.polynomial.polyfit(x,y,deg)
def ev(b,x):return np.polynomial.polynomial.polyval(x,b)
rows=[]
for o in [1981,1986,1991,1996,2001]:
 y=np.arange(1959,o+1); x=(y-1959)/10; cf=np.array([c[v] for v in y]); tf=np.array([t[v] for v in y]); fut=np.arange(o+1,o+11); xf=(fut-1959)/10
 cp={'D':c[o]+(c[o]-c[o-10])/10*(fut-o),'Q':ev(fit(x,cf,2),xf),'E':cref*np.exp(ev(fit(x,np.log(cf/cref)),xf))}
 tp={'T0':ev(fit(x,tf),xf),'Tquad':ev(fit(x,tf,2),xf),'Tlinear20':ev(fit(x[-20:],tf[-20:]),xf)}
 b=fit(np.log(cf/cref),tf)
 tp.update({'T1-'+k:ev(b,np.log(v/cref)) for k,v in cp.items()})
 for target,preds,obs in [('co2',cp,c),('temp',tp,t)]:
  for m,pred in preds.items():
   for yy,pp in zip(fut,pred):rows.append(dict(origin=o,target=target,model=m,year=int(yy),pred=float(pp),observed=obs[yy],error=float(pp-obs[yy])))
metrics={}
for m in sorted(set(r['model'] for r in rows)):
 rr=[r for r in rows if r['model']==m]
 metrics[m]={'mae':float(np.mean([abs(r['error']) for r in rr])),'by_origin':{str(o):float(np.mean([abs(r['error']) for r in rr if r['origin']==o])) for o in [1981,1986,1991,1996,2001]}}
y=np.arange(1959,2012); x=(y-1959)/10; z=np.log(np.array([c[v] for v in y])/cref); tt=np.array([t[v] for v in y]); corr=lambda a,b:float(np.corrcoef(a,b)[0,1])
assoc={'raw':corr(z,tt),'first_difference':corr(np.diff(z),np.diff(tt))}
for d in [1,2]:assoc[f'detrend{d}']=corr(z-ev(fit(x,z,d),x),tt-ev(fit(x,tt,d),x))
result={'strategy':'predeclared development-only; no final holdout scoring','metrics':metrics,'association_through2011':assoc,'rows':rows}
(p/'qa/adversarial_structure/probe-results-r01.json').write_text(json.dumps(result,indent=2))
print(json.dumps({k:v for k,v in result.items() if k!='rows'},indent=2))
