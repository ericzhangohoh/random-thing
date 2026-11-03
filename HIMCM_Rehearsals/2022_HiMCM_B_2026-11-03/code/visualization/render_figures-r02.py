#!/usr/bin/env python3
"""Display accepted tables only; no fitting, scoring, selection or crossings."""
from pathlib import Path
import hashlib,json,os
os.environ.setdefault('MPLCONFIGDIR','/private/tmp/himcm-2022b-mpl-final')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
ROOT=Path(__file__).resolve().parents[2]
RUN=ROOT/'runs/T05-scientific-20261103-r03'
EXPECTED='7bc6e1fe3498302d247b45fa97c4d13498edfbf5366cddd078ff7ebfaff4bc00'
assert hashlib.sha256((RUN/'manifest.json').read_bytes()).hexdigest()==EXPECTED
MAN=json.loads((RUN/'manifest.json').read_text())
HASHES={Path(x['path']).name:x['sha256'] for x in MAN['outputs']}
USED={};REGISTER=[];OUT=ROOT/'figures';OUT.mkdir(exist_ok=True)
def read(name):
 p=RUN/'outputs'/name
 assert hashlib.sha256(p.read_bytes()).hexdigest()==HASHES[name],name
 USED[name]=HASHES[name]
 return pd.read_csv(p)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'axes.titlesize':11,'axes.labelsize':10,'axes.spines.top':False,'axes.spines.right':False,'axes.edgecolor':'#81969A','axes.labelcolor':'#18383E','text.color':'#18383E','xtick.color':'#52666B','ytick.color':'#52666B','grid.color':'#DCE6E7','grid.linewidth':.6,'legend.frameon':False,'savefig.facecolor':'white'})
C={'D':'#176A73','Q':'#C96C26','E':'#785896','T0':'#7A8795','T1-D':'#176A73','T1-Q':'#C96C26','T1-E':'#785896'}
L={'D':'-','Q':'--','E':':','T0':'-.','T1-D':'-','T1-Q':'--','T1-E':':'}
def finish(fig,id,question,sources,transform):
 for ax in fig.axes:ax.grid(axis='y',alpha=.6);ax.set_axisbelow(True)
 fig.tight_layout(pad=1.1);files={}
 for ext in ['png','pdf']:
  p=OUT/f'{id}-r02.{ext}'
  if p.exists():raise FileExistsError(p)
  fig.savefig(p,dpi=220,bbox_inches='tight');files[str(p.relative_to(ROOT))]=hashlib.sha256(p.read_bytes()).hexdigest()
 plt.close(fig)
 REGISTER.append({'id':id,'question':question,'sources':{n:USED[n] for n in sources},'display_transform':transform,'files':files})

d=read('ten_year_changes.csv');fig,ax=plt.subplots(figsize=(7.1,2.6))
ax.plot(d.end_year,d.increase_ppm,color=C['D'],lw=1.8);ax.scatter(d.end_year,d.increase_ppm,color=C['D'],s=14)
for year,xytext,color in [(2003,(1985,19.4),C['Q']),(2004,(1990,17.6),C['E'])]:
 row=d[d.end_year==year].iloc[0];ax.scatter([year],[row.increase_ppm],s=50,color=color,zorder=5)
 ax.annotate(f'{year}: {row.increase_ppm:.2f} ppm',xy=(year,row.increase_ppm),xytext=xytext,arrowprops={'arrowstyle':'-','color':color},color=color,fontsize=10)
ax.set(xlabel='Ending year of a ten-elapsed-year window',ylabel='Ten-year increase (ppm)',xlim=(1968,2006),ylim=(7,20.7))
finish(fig,'F01','Was 2004 an annual ten-year record?',['ten_year_changes.csv'],'Plot accepted increase_ppm/end_year, highlight2003/2004. No recalculation.')

dev=read('development_metrics.csv');final=read('final_metrics.csv');fig,ax=plt.subplots(figsize=(7.1,2.6));xs=np.arange(3);w=.32
for off,frame,label,color in [(-w/2,dev,'Development','#6C9DA1'),(w/2,final,'Final 2012-2021','#D18A54')]:
 q=frame[(frame.target=='co2')&(frame.grouping=='overall')].set_index('model_id').loc[['D','Q','E']]
 bars=ax.bar(xs+off,q.mae,width=w,label=label,color=color);ax.bar_label(bars,labels=[f'{x:.3f}' for x in q.mae],fontsize=9,padding=3)
ax.set(xticks=xs,xticklabels=['D: recent drift','Q: quadratic','E: exponential'],ylabel='Mean absolute error (ppm)',ylim=(0,9.8));ax.legend(loc='upper left',ncol=2)
finish(fig,'F02','Does the ranking persist in later assessment?',['development_metrics.csv','final_metrics.csv'],'Select co2/overall; accepted mae, three-decimal labels. No new metrics.')

fore=read('production_forecasts.csv');res=read('production_residuals.csv');obs=res[(res.fit_window=='full')&(res.model_id=='Q')].sort_values('year')
fig,ax=plt.subplots(figsize=(7.1,3.0));ax.plot(obs.year,obs.observed,color='#5F6D70',lw=1.6,label='Supplied annual observations')
for m in ['D','Q','E']:
 d=fore[(fore.fit_window=='full')&(fore.model_id==m)].sort_values('year');ax.plot(d.year,d.value,color=C[m],ls=L[m],lw=2,label=m+(' (selected rule)' if m=='D' else ''))
ax.axvline(2021,color='#A1B0B2',ls=':',lw=1);ax.axhline(685,color='#777777',lw=1,ls='--');ax.text(1961,691,'685 ppm: pure-CO2 exercise',fontsize=9)
ax.text(2031,326,'Conditional extrapolations',color='#925D19',fontsize=10);ax.set(xlabel='Calendar year',ylabel='Annual CO2 concentration (ppm)',xlim=(1958,2102),ylim=(300,723));ax.legend(loc='upper left',bbox_to_anchor=(0,.9),fontsize=8.6)
finish(fig,'F03','How do concentration paths diverge through2100?',['production_forecasts.csv','production_residuals.csv'],'Full-window annual paths; observed values from Q residual table. Forecast starts2022; no fitting/interpolation.')

th=read('thresholds.csv');fig,ax=plt.subplots(figsize=(7.1,3.0));to=res[(res.fit_window=='full')&(res.model_id=='T0')].sort_values('year')
ax.plot(to.year,to.observed,color='#829295',lw=1.25,label='Supplied anomalies')
for m in ['T0','T1-D','T1-Q','T1-E']:
 d=fore[(fore.fit_window=='full')&(fore.model_id==m)].sort_values('year');ax.plot(d.year,d.value,color=C[m],ls=L[m],lw=2 if m=='T1-D' else 1.6,label=m)
for h in [1.25,1.5,2.0]:
 ax.axhline(h,color='#B8C3C4',ls=':',lw=1);row=th[(th.fit_window=='full')&(th.model_id=='T1-D')&(th.threshold==h)].iloc[0]
 ax.scatter(row.first_year,row.value_at_year,color=C['D'],s=30,zorder=5);ax.annotate(str(int(row.first_year)),(row.first_year,row.value_at_year),xytext=(3,-15),textcoords='offset points',fontsize=8,color=C['D'])
ax.axvline(2021,color='#A1B0B2',ls=':',lw=1);ax.set(xlabel='Calendar year',ylabel='Temperature anomaly (°C)\nrelative to 1951-1980',xlim=(1958,2102),ylim=(-.27,3.05));ax.legend(loc='upper left',fontsize=8.7,ncol=2)
finish(fig,'F04','How do temperature paths and crossings differ?',['production_forecasts.csv','production_residuals.csv','thresholds.csv'],'Full-window paths, accepted T1-D crossing years/raw values. No threshold recomputation.')

series=read('relationship_series.csv');diag=read('relationship_diagnostics.csv');fig,axs=plt.subplots(1,2,figsize=(7.1,2.8))
tres=res[(res.fit_window=='full')&(res.model_id=='T1-D')].sort_values('year');j=obs[['year','observed']].merge(tres[['year','observed','fitted']],on='year',suffixes=('_co2','_temp'),validate='one_to_one')
axs[0].scatter(j.observed_co2,j.observed_temp,color=C['D'],s=19,alpha=.7);axs[0].plot(j.observed_co2,j.fitted,color='#173B40',lw=1.3,label='Accepted log-CO2 fit')
axs[0].set(xlabel='CO2 concentration (ppm)',ylabel='Anomaly (°C)',title='Levels, 1959-2021');axs[0].text(.05,.9,f'r = {diag[diag.diagnostic=="levels_co2"].iloc[0].correlation:.3f}',transform=axs[0].transAxes,fontsize=9);axs[0].legend(loc='lower right',fontsize=8)
d=series[series.diagnostic=='first_differences_log_co2'];axs[1].scatter(d.x_value,d.y_value,color=C['Q'],s=19,alpha=.8);axs[1].axhline(0,color='#A0ADAF',lw=.7)
axs[1].set(xlabel='Annual change in log(C / Cref)',ylabel='Annual anomaly change (°C)',title='Changes, 1960-2021');axs[1].text(.05,.9,f'r = {diag[diag.diagnostic=="first_differences_log_co2"].iloc[0].correlation:.3f}',transform=axs[1].transAxes,fontsize=9)
finish(fig,'F05','How do level association and annual changes differ?',['production_residuals.csv','relationship_series.csv','relationship_diagnostics.csv'],'Join accepted observed/fitted rows byyear; first differences read directly. Diagnostic r labels. No refit/differencing.')

ff=read('final_forecasts.csv');env=read('historical_error_envelopes.csv');fig,axs=plt.subplots(1,2,figsize=(7.1,2.9))
for ax,target,m,yl in [(axs[0],'co2','D','CO2 (ppm)'),(axs[1],'temp','T1-D','Anomaly (°C), 1951-1980')]:
 d=ff[ff.model_id==m].sort_values('target_year');e=env[env.target==target].sort_values('final_target_year')
 ax.fill_between(e.final_target_year,e.final_lower,e.final_upper,color='#C9DFE1',alpha=.8,label='Historical error reference');ax.plot(d.target_year,d.predicted,color=C[m],lw=1.8,label=m+' prediction');ax.plot(d.target_year,d.observed,color='#3D4547',marker='o',markersize=3,lw=1,label='Observed')
 ax.set(xlabel='Target year (origin: 2011)',ylabel=yl,title=m+' later assessment',xticks=[2012,2016,2021])
 if target=='temp':
  miss=d[d.target_year==2016].iloc[0];ax.scatter([2016],[miss.observed],color='#C84735',s=50,zorder=5);ax.annotate('2016 miss',(2016,miss.observed),xytext=(2017,.53),arrowprops={'arrowstyle':'->','color':'#C84735'},color='#C84735',fontsize=9)
axs[0].legend(loc='upper left',fontsize=7.4)
finish(fig,'F06','Do fixed historical envelopes contain later observations?',['final_forecasts.csv','historical_error_envelopes.csv'],'Accepted lower/upper/predicted/observed values, accepted2016 miss. No widening or coverage probability inference.')

record={'run_id':MAN['run_id'],'manifest_sha256':EXPECTED,'purpose':'display only; no modeling','figures':REGISTER}
p=ROOT/'paper/figure-register-r02.json';tmp=p.with_suffix('.json.tmp');tmp.write_text(json.dumps(record,indent=2)+'\n');tmp.replace(p)
print(json.dumps({'figures':len(REGISTER),'register':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()},indent=2))
