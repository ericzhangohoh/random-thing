from pathlib import Path
import csv,json,hashlib,zipfile,xml.etree.ElementTree as ET
from decimal import Decimal
from functools import lru_cache
import numpy as np
P=Path(__file__).resolve().parents[2]; Q=Path(__file__).resolve().parent
R=P/'runs/T05-scientific-20261103-r02'; O=R/'outputs'
checks=[];diffs=[]
def verify(label,actual,expected,tol=1e-8):
 if isinstance(expected,(int,float,np.number)) and not isinstance(expected,bool):
  delta=abs(float(actual)-float(expected));ok=np.isfinite(delta) and delta<=tol;diffs.append(delta)
 else:ok=actual==expected
 checks.append({'label':label,'passed':bool(ok),'actual':actual if isinstance(actual,(str,int,float,bool,type(None))) else str(actual),'expected':float(expected) if isinstance(expected,np.floating) else expected})
 if not ok: print('FAIL',label,actual,expected)
def rows(n):return list(csv.DictReader((O/n).open()))
ns={'s':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
with zipfile.ZipFile(R/'reproduction/inputs/2022_HiMCM_Data.xlsx') as z:
 d=[]
 for i in [1,2]:
  root=ET.fromstring(z.read(f'xl/worksheets/sheet{i}.xml'));table={}
  for r in root.findall('s:sheetData/s:row',ns)[1:]:
   cells={c.attrib['r'].rstrip('0123456789'):c.findtext('s:v',namespaces=ns) for c in r.findall('s:c',ns)}
   if cells.get('A'):table[int(Decimal(cells['A']))]=float(Decimal(cells['B']).quantize(Decimal('.01')))
  d.append(table)
C,T=d; years=np.array(sorted(C));cv=np.array([C[y] for y in years]);tv=np.array([T[y] for y in years]);cref=C[1959]
verify('source_co2_count',len(C),63);verify('source_temp_count',len(T),64)
def linear(x,y):
 slope=np.dot(x-x.mean(),y-y.mean())/np.dot(x-x.mean(),x-x.mean())
 return np.array([y.mean()-slope*x.mean(),slope])
@lru_cache(None)
def fit(origin,start=1959):
 mask=(years>=start)&(years<=origin);ys=years[mask];x=(ys-1959)/10;c=cv[mask];t=tv[mask]
 q=np.polynomial.polynomial.polyfit(x,c,2);e=linear(x,np.log(c/cref));t0=linear(x,t);assoc=linear(np.log(c/cref),t)
 return {'D':np.array([C[origin],(C[origin]-C[origin-10])/10]),'Q':q,'E':e,'T0':t0,**{m:assoc for m in ['T1-D','T1-Q','T1-E']}}
def predict(m,origin,year,start=1959):
 p=fit(origin,start)[m];x=(year-1959)/10
 if m=='D':return p[0]+p[1]*(year-origin)
 if m=='Q':return p[0]+p[1]*x+p[2]*x*x
 if m=='E':return cref*np.exp(p[0]+p[1]*x)
 if m=='T0':return p[0]+p[1]*x
 return p[0]+p[1]*np.log(predict(m[3:],origin,year,start)/cref)
errors={}; temporal=[]
for phase,origins in [('development',[1981,1986,1991,1996,2001]),('final',[2011])]:
 rr=rows(phase+'_forecasts.csv');verify(phase+'_rows',len(rr),len(origins)*10*7)
 for r in rr:
  m=r['model_id'];o=int(r['origin_year']);y=int(r['target_year']);pred=predict(m,o,y);obs=C[y] if m in ['D','Q','E'] else T[y];key=(phase,m,o,y)
  errors[key]=pred-obs;temporal.append(dict(phase=phase,model=m,origin=o,year=y,predicted=pred,observed=obs,error=pred-obs))
  for field,val in [('predicted',pred),('observed',obs),('error',pred-obs),('horizon',y-o),('train_end',o),('train_start',o-10 if m=='D' else 1959),('n_train',11 if m=='D' else o-1958)]:verify(str(key)+field,r[field],val)
  verify(str(key)+'status',r['status'],'OK')
  if m.startswith('T1'):verify(str(key)+'forecast_co2_input',r['forecast_co2_input_ppm'],predict(m[3:],o,y))
 for r in rows(phase+'_metrics.csv'):
  vals=[v for (ph,m,o,y),v in errors.items() if ph==phase and m==r['model_id'] and (r['grouping']=='overall' or r['grouping']=='origin' and o==int(r['group_value']) or r['grouping']=='horizon' and y-o==int(r['group_value']))]
  for field,v in [('mae',np.mean(np.abs(vals))),('rmse',np.sqrt(np.mean(np.square(vals)))),('bias',np.mean(vals)),('n',len(vals))]:verify(phase+str((r['model_id'],r['grouping'],r['group_value']))+field,r[field],v)
sel=json.loads((O/'selection_frozen.json').read_text());devmae={m:np.mean([abs(v) for (ph,mm,o,y),v in errors.items() if ph=='development' and mm==m]) for m in ['D','Q','E','T0','T1-D','T1-Q','T1-E']}
chosen=min(['D','E','Q'],key=lambda m:devmae[m]);chosenT=min(['T0','T1-'+chosen],key=lambda m:devmae[m]);verify('selected_co2',sel['selected_co2_id'],chosen);verify('selected_temp',sel['selected_temperature_id'],chosenT)
for r in rows('forecast_summary.csv'):
 start=1992 if r['fit_window']=='last30' else 1959;m=r['model_id'];y=int(r['year']);v=predict(m,2021,y,start);verify('forecast_summary'+str((m,start,y)),r['value'],v)
 if m in ['D','Q','E']:
  verify('gap',r['gap_from_685_ppm'],v-685);verify('relative_gap',r['relative_gap_percent'],100*(v-685)/685)
thresholds=[]
for r in rows('thresholds.csv'):
 start=1992 if r['fit_window']=='last30' else 1959;m=r['model_id'];H=float(r['threshold']);path=np.array([predict(m,2021,y,start) for y in range(2021,2301)])
 assert np.all(np.isfinite(path)); assert m not in ['D','Q','E'] or np.all(path>0)
 idx=np.flatnonzero(path>=H);first=int(2021+idx[0]);verify('threshold'+str((start,m,H)),r['first_year'],first);verify('crossed',r['status'],'CROSSED');verify('whole_domain_valid',r['search_domain_valid'],'True');verify('boundary_current',r['value_at_year'],path[first-2021]);verify('boundary_previous',r['value_previous_year'],path[first-2022]);verify('strict_previous',bool(path[first-2022]<H),True)
 verify('threshold_monotone',r['monotone_flag'],str(bool(np.all(np.diff(path)>=-1e-9))));verify('valid_through',r['valid_through_year'],2300);verify('no_invalid_year',r['invalid_from_year'],'');thresholds.append({'model':m,'window':r['fit_window'],'threshold':H,'first_year':first})
miss=[]
for r in rows('historical_error_envelopes.csv'):
 m=r['selected_model_id'];h=int(r['horizon']);radius=max(abs(v) for (ph,mm,o,y),v in errors.items() if ph=='development' and mm==m and y-o<=h);ae=abs(errors[('final',m,2011,2011+h)])
 verify('radius'+m+str(h),r['radius'],radius);verify('envelope_error'+m+str(h),r['final_absolute_error'],ae);verify('envelope_contained'+m+str(h),r['final_contained'],str(ae<=radius));verify('envelope_excess'+m+str(h),r['final_excess'],max(0,ae-radius))
 if ae>radius:miss.append({'model':m,'year':2011+h,'error':ae,'radius':radius,'excess':ae-radius})
x=(years-1959)/10;z=np.log(cv/cref);pairs={'levels_co2':(cv,tv),'levels_log_co2':(z,tv),'first_differences_log_co2':(np.diff(z),np.diff(tv))}
for degree in [1,2]:
 rz=z-np.polynomial.polynomial.polyval(x,np.polynomial.polynomial.polyfit(x,z,degree));rt=tv-np.polynomial.polynomial.polyval(x,np.polynomial.polynomial.polyfit(x,tv,degree));pairs[f'detrended_order_{degree}']=(rz,rt)
for r in rows('relationship_diagnostics.csv'):
 xx,yy=pairs[r['diagnostic']];coef=linear(xx,yy);corr=np.corrcoef(xx,yy)[0,1]
 for k,v in [('correlation',corr),('slope',coef[1]),('intercept',coef[0]),('r_squared',corr*corr),('n',len(xx))]:verify(r['diagnostic']+k,r[k],v)
 if r['fitted_doubling_contrast_c']:verify('doubling_contrast',r['fitted_doubling_contrast_c'],coef[1]*np.log(2))
coefnames={'D':['anchor_ppm','slope_ppm_per_year'],'Q':['a_ppm','b_ppm_per_decade','c_ppm_per_decade_squared'],'E':['a_log_ratio','b_log_ratio_per_decade'],'T0':['alpha0_c','delta_c_per_decade']}
for phase in ['development','final','production']:
 for r in rows(phase+'_coefficients.csv'):
  m=r['model_id'];o=int(r['origin']);start=1992 if r.get('fit_window')=='last30' else 1959;names=coefnames.get(m,['alpha_c','beta_c_per_log_ratio']);verify(phase+'coef'+str((m,o,start,r['coefficient'])),r['value'],fit(o,start)[m][names.index(r['coefficient'])])
comp=json.loads((O/'ten_year_comparison.json').read_text());decs={y:Decimal(str(C[y]))-Decimal(str(C[y-10])) for y in range(1969,2005)};verify('2004 decade',comp['window_2004_increase_ppm'],float(decs[2004]));verify('prior decade max',comp['prior_max_increase_ppm'],float(max(v for k,v in decs.items() if k<2004)))
for r in rows('window_sensitivity.csv'):
 m=r['model_id']
 if r['quantity']=='forecast':
  a=predict(m,2021,int(r['year']));b=predict(m,2021,int(r['year']),1992)
 else:
  H=float(r['threshold']);a=next(t['first_year'] for t in thresholds if t['model']==m and t['window']=='full' and t['threshold']==H);b=next(t['first_year'] for t in thresholds if t['model']==m and t['window']=='last30' and t['threshold']==H)
 for k,v in [('full_value',a),('last30_value',b),('difference',b-a)]:verify('window_'+m+'_'+k,r[k],v)
fail=[c for c in checks if not c['passed']]
summary={'independence':'stdlib direct workbook parse; centered covariance linear regression and NumPy polynomial fitting; no production model imports','checked_scalar_conditions':len(checks),'failures':fail,'maximum_absolute_numeric_difference':max(diffs),'selected':[chosen,chosenT],'development_mae':devmae,'thresholds':thresholds,'envelope_misses':miss,'source_workbook_sha256':hashlib.sha256((R/'reproduction/inputs/2022_HiMCM_Data.xlsx').read_bytes()).hexdigest(),'run_manifest_sha256':hashlib.sha256((R/'manifest.json').read_bytes()).hexdigest()}
(Q/'independent-results.json').write_text(json.dumps(summary,indent=2)+'\n');(Q/'all-checks.json').write_text(json.dumps(checks,indent=2)+'\n');(Q/'independent-temporal-predictions.json').write_text(json.dumps(temporal,indent=2)+'\n');print(json.dumps(summary,indent=2));assert not fail
