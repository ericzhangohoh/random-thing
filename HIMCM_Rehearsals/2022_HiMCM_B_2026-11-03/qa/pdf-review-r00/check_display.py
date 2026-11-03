from pathlib import Path
import json,csv,hashlib,re
from pypdf import PdfReader
P=Path(__file__).resolve().parents[2];Q=Path(__file__).parent;R=P/'runs/T05-scientific-20261103-r03/outputs';M=json.loads((P/'paper/manuscript-complete-r03.json').read_text());checks=[]
def ck(n,v):assert v,n;checks.append(n)
def rows(n):return list(csv.DictReader((R/(n+'.csv')).open()))
def one(n,**kw):
 a=[r for r in rows(n) if all(r[k]==str(v) for k,v in kw.items())];assert len(a)==1,(n,kw,len(a));return a[0]
def tabs(p):return [b['rows'] for b in M['pages'][p-1]['blocks'] if b['type']=='table']
def fmt(v,n):return f'{float(v):.{n}f}'
def eq(p,actual,expected):ck('page '+str(p)+' '+str(actual),actual==expected)
for row in tabs(1)[0]:
 m=row[0].split()[0];eq(1,row[1:],[fmt(one('forecast_summary',fit_window='full',model_id=m,year=y)['value'],2) for y in [2050,2100]]+[one('thresholds',fit_window='full',model_id=m)['first_year']])
for row in tabs(5)[0]:
 d=one('production_fit_diagnostics',fit_window='full',model_id=row[0]);eq(5,row[1:],[d['train_start']+'-'+d['train_end'],d['n_train'],fmt(d['residual_rmse'],3),fmt(d['residual_lag1_correlation'],3)])
for row in tabs(6)[0]:
 d=one('development_metrics',grouping='overall',model_id=row[0]);f=one('final_metrics',grouping='overall',model_id=row[0]);eq(6,row[1:],[fmt(d['mae'],5),fmt(f['mae'],5),fmt(f['rmse'],5)])
for row in tabs(7)[0]:
 d=one('forecast_summary',fit_window='full',model_id=row[0],year=2050);f=one('forecast_summary',fit_window='full',model_id=row[0],year=2100);eq(7,row[1:],[fmt(d['value'],2),fmt(d['gap_from_685_ppm'],2),fmt(f['value'],2),one('thresholds',fit_window='full',model_id=row[0])['first_year']])
for row in tabs(8)[0]:eq(8,row[1:3],[fmt(one(n,grouping='overall',model_id=row[0])['mae'],6) for n in ['development_metrics','final_metrics']])
for row in tabs(9)[0]:
 m=row[0].split()[0];eq(9,row[1:],[one('thresholds',fit_window='full',model_id=m,threshold=h)['first_year'] for h in ['1.25','1.5','2.0']]+[fmt(one('forecast_summary',fit_window='full',model_id=m,year=y)['value'],2) for y in [2050,2100]])
for row,d in zip(tabs(10)[0],rows('relationship_diagnostics')):eq(10,row[-1],fmt(d['correlation'],6))
f=one('final_forecasts',model_id='T1-D',target_year=2016);e=one('historical_error_envelopes',target='temp',horizon=5)
eq(11,[r[1] for r in tabs(11)[0]],[fmt(v,6) for v in [f['predicted'],f['observed'],e['final_absolute_error'],e['radius'],e['final_excess']]])
for row in tabs(12)[0]:
 d=one('horizon_evidence',target='co2',horizon=row[0]);t=one('horizon_evidence',target='temp',horizon=row[0]);eq(12,row[1:],[fmt(d['development_mae'],5),fmt(d['final_absolute_error'],5),fmt(t['development_mae'],6),fmt(t['final_absolute_error'],6)])
for row in tabs(12)[1]:
 if 'anomaly' in row[0]:d=one('window_sensitivity',target='temp',year=row[0][:4]);n=5
 else:d=one('window_sensitivity',target='temp',threshold=str(float(row[0].split()[0])));n=0
 eq(12,row[1:],[fmt(d[k],n) for k in ['full_value','last30_value']])
r=PdfReader(P/'paper/exports/2022_HiMCM_B_practice-complete-r03.pdf');ck('16 pages',len(r.pages)==16)
for i,page in enumerate(M['pages'],1):
 text=re.sub(r'\s+',' ',r.pages[i-1].extract_text())
 for table in tabs(i):
  for row in table:
   for cell in row:ck('rendered table cell '+str(i)+' '+cell,re.sub(r'\s+',' ',cell) in text)
for p,h in M['artifact_hashes'].items():ck('manuscript asset '+p,hashlib.sha256((P/p).read_bytes()).hexdigest()==h)
reg=json.loads((P/'paper/figure-register-r02.json').read_text())
for fig in reg['figures']:
 for n,h in fig['sources'].items():ck('figure source '+fig['id']+n,hashlib.sha256((R/n).read_bytes()).hexdigest()==h)
release=json.loads((P/'control/accepted-writing-inputs-r01.json').read_text())
for p,h in release['sha256'].items():ck('release '+p,hashlib.sha256((P/p).read_bytes()).hexdigest()==h)
(Q/'display-checks.json').write_text(json.dumps({'status':'PASS','count':len(checks),'checks':checks},indent=2)+'\n');print('PASS',len(checks))
