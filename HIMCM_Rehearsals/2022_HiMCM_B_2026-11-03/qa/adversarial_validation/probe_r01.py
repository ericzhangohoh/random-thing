from pathlib import Path
import numpy as np, json, hashlib, csv
P=Path(__file__).resolve().parents[2]; O=Path(__file__).resolve().parent
raw=list(csv.DictReader((P/'data/processed/joined-r01.csv').open()))
y=np.array([int(r['year']) for r in raw]); c=np.array([float(r['co2_ppm']) for r in raw]); t=np.array([float(r['temp_anomaly_c']) for r in raw]); ref=c[0]
def preds(o, years, cv=c, tv=t):
 m=y<=o; x=(y[m]-1959)/10; u=(np.asarray(years)-1959)/10; X=np.c_[np.ones(sum(m)),x]
 q=np.linalg.lstsq(np.c_[X,x*x],cv[m],rcond=None)[0]; e=np.linalg.lstsq(X,np.log(cv[m]/ref),rcond=None)[0]
 d=cv[y==o][0]+(cv[y==o][0]-cv[y==o-10][0])/10*(np.asarray(years)-o)
 cp={'D':d,'Q':np.c_[np.ones(len(u)),u,u*u]@q,'E':ref*np.exp(np.c_[np.ones(len(u)),u]@e)}
 b=np.linalg.lstsq(np.c_[np.ones(sum(m)),np.log(cv[m]/ref)],tv[m],rcond=None)[0]
 return {**cp,'T0':np.c_[np.ones(len(u)),u]@np.linalg.lstsq(X,tv[m],rcond=None)[0],**{'T1-'+k:b[0]+b[1]*np.log(v/ref) for k,v in cp.items()}}
orig=[1981,1986,1991,1996,2001]; errors={k:[] for k in preds(1981,np.arange(1982,1992))}
for o in orig:
 ys=np.arange(o+1,o+11)
 for k,v in preds(o,ys).items(): errors[k].append(v-(t if k.startswith('T') else c)[np.isin(y,ys)])
errors={k:np.array(v) for k,v in errors.items()}
scores={k:float(np.mean(abs(v))) for k,v in errors.items()}; winner=min(['D','E','Q'],key=lambda k:scores[k]); twinner=min(['T0','T1-'+winner],key=lambda k:scores[k])
result={'phase':'development_only; no final forecast errors calculated','scores':scores,'selected':[winner,twinner], 'origin_mae':{k:np.mean(abs(v),axis=1).tolist() for k,v in errors.items()}, 'horizon_mae':{k:np.mean(abs(v),axis=0).tolist() for k,v in errors.items()},'leave_origin_out_winners':[min(['D','Q','E'],key=lambda k:np.mean(abs(np.delete(errors[k],i,0)))) for i in range(5)]}
# Leak perturbation uses altered post-origin fixtures, never final score.
cc=c.copy(); tt=t.copy(); cc[y>1981]*=3; tt[y>1981]+=99
result['future_fixture_invariance']=all(np.array_equal(v,preds(1981,np.arange(1982,1992),cc,tt)[k]) for k,v in preds(1981,np.arange(1982,1992)).items())
result['unique_development_target_years']=len(set(o+h for o in orig for h in range(1,11)))
result['hashes']={str(p.relative_to(P)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [P/'inputs/2022_HiMCM_Data.xlsx',P/'data/processed/joined-r01.csv',*sorted((P/'models').glob('*r01*'))]}
(O/'development_probe_r01.json').write_text(json.dumps(result,indent=2)+'\n')
np.savez(O/'development_errors_r01.npz',**errors)
print(json.dumps(result,indent=2))
