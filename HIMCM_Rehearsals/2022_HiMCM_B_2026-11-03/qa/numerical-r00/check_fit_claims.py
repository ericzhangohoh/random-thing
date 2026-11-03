from pathlib import Path
# Reuse only this reviewer's source parser/formulas, stopping before the previous audit loop.
q=Path(__file__).resolve().parent
prefix=(q/'recompute.py').read_text().split('errors={}; temporal=[]')[0]
exec(compile(prefix,'<independent reviewer formulas>','exec'))
for phase in ['development','final','production']:
 for r in rows(phase+'_fit_diagnostics.csv'):
  mid=r['model_id'];o=int(r['origin']);start=int(r['train_start']);base=1992 if r.get('fit_window')=='last30' else 1959
  yy=np.arange(start,o+1);obs=np.array([C[y] if mid in ['D','Q','E'] else T[y] for y in yy])
  if mid.startswith('T1'):
   a,b=fit(o,base)[mid];pred=a+b*np.log(np.array([C[y] for y in yy])/cref)
  else:pred=np.array([predict(mid,o,y,base) for y in yy])
  err=pred-obs
  for k,v in [('residual_mean',err.mean()),('residual_rmse',np.sqrt(np.mean(err**2))),('residual_lag1_correlation',np.corrcoef(err[:-1],err[1:])[0,1])]:verify(phase+str((mid,o,base))+k,r[k],v)
result={'scope':'new T12 C15 residual-fit claims; independent formulas reused without repeating temporal audit','checks':len(checks),'failures':[x for x in checks if not x['passed']],'maximum_difference':max(diffs)}
(Q/'fit-claim-checks.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result));assert not result['failures']
