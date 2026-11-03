"""Separate development freeze, final assessment and production commands."""
import argparse,csv,hashlib,json,math,sys
from datetime import datetime,timezone
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'modeling'))
import climate_models_r02 as m
import numpy as np
MODEL_IDS=['D','Q','E','T0','T1-D','T1-Q','T1-E']
def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def now():return datetime.now(timezone.utc).isoformat()
def savejson(path,value):
    with Path(path).open('x') as f:json.dump(value,f,indent=2,allow_nan=False);f.write('\n')
def absolute_or_none(value):return None if value is None else abs(value)
def difference_or_none(a,b):return None if a is None or b is None else a-b
def offset_or_none(value,offset):return None if value is None else value+offset
def verify_final_tables(directory,receipt):
    for name in ['final_forecasts','final_metrics']:
        if sha(Path(directory)/(name+'.csv'))!=receipt[name+'_sha256']:raise ValueError('Final evidence changed after assessment: '+name)

class Analysis:
    def __init__(self,snapshot,out,config_path):
        self.root=Path(snapshot);self.out=Path(out);self.config=json.loads(Path(config_path).read_text());self.out.mkdir(parents=True,exist_ok=True)
        self.identity={'input_sha256':sha(self.root/'data/processed/joined-r01.csv'),'spec_sha256':sha(self.root/'models/model_spec-r02.md'),'configuration_sha256':sha(config_path),'code_sha256':sha(Path(__file__)),'model_code_sha256':sha(self.root/'code/modeling/climate_models_r02.py')}
        self.trace={'run_id':self.config['run_id'],'data_sha256':self.identity['input_sha256'],'spec_sha256':self.identity['spec_sha256']}
        release=json.loads((self.root/'control/accepted-inputs-g2-r02.json').read_text())
        for name in ['data/processed/co2-r01.csv','data/processed/temperature-r01.csv','data/processed/joined-r01.csv','models/model_spec-r02.md','models/model_interface-r02.md','models/experiment_plan-r02.md']:
            if sha(self.root/name)!=release['sha256'][name]:raise m.ModelFailure('INPUT_CONTRACT_FAILURE','Released dependency changed: '+name)
        with (self.root/'data/processed/joined-r01.csv').open() as f:rows=list(csv.DictReader(f))
        self.data={k:np.array([float(r[k]) for r in rows]) for k in ['year','co2_ppm','temp_anomaly_c']}
        m.validate_data(self.data,np.arange(1959,2022));self.data['year']=self.data['year'].astype(int)
        for filename,field in [('co2-r01.csv','co2_ppm'),('temperature-r01.csv','temp_anomaly_c')]:
            with (self.root/'data/processed'/filename).open() as f:original={int(r['year']):float(r[field]) for r in csv.DictReader(f)}
            if any(original[int(y)]!=v for y,v in zip(self.data['year'],self.data[field])):raise m.ModelFailure('INPUT_CONTRACT_FAILURE','Positional/value-mismatched join')
        self.cref=float(self.data['co2_ppm'][0])
    def table(self,name,rows):
        if not rows:raise ValueError('Empty table '+name)
        rows=[{**self.trace,**r} for r in rows];keys=list(dict.fromkeys(k for r in rows for k in r))
        with (self.out/name).open('x',newline='') as f:
            w=csv.DictWriter(f,fieldnames=keys,lineterminator='\n');w.writeheader();w.writerows(rows)
    def fits(self,data,origin,start=1959):
        result={}
        for mid in MODEL_IDS:
            try:
                if mid in ['D','Q','E']:fit=m.fit_co2(data,mid,origin,start,self.cref);upstream=None
                else:
                    fit=m.fit_temperature(data,'T0' if mid=='T0' else 'T1',origin,start,self.cref)
                    if mid!='T0' and result[mid[-1]]['status']!='OK':raise m.ModelFailure('INVALID_UPSTREAM_PATH','CO2 fit failed')
                    upstream=None if mid=='T0' else result[mid[-1]]['fit']
                result[mid]={'fit':fit,'upstream':upstream,'status':'OK'}
            except m.ModelFailure as error:result[mid]={'fit':None,'upstream':None,'status':error.status,'reason':str(error)}
        return result
    def predict(self,mid,pack,year):
        if pack['status']!='OK':raise m.ModelFailure(pack['status'],pack.get('reason','Failed fit'))
        return float(m.predict_co2(pack['fit'],year)) if mid in ['D','Q','E'] else float(m.predict_temperature(pack['fit'],year,pack['upstream']))
    def fit_evidence(self,packs,phase,window):
        params=[];residuals=[];diagnostics=[]
        for mid,pack in packs.items():
            if pack['status']!='OK':params.append({'phase':phase,'fit_window':window,'model_id':mid,'status':pack['status'],'reason':pack.get('reason')});continue
            fit=pack['fit'];target='co2' if mid in ['D','Q','E'] else 'temp';unit='ppm' if target=='co2' else 'degrees_C_anomaly_1951_1980'
            meta={k:fit[k] for k in ['origin','train_start','train_end','n_train','rank','fit_method','status']};meta.update(phase=phase,fit_window=window,model_id=mid,target=target,unit=unit,upstream_model_id=None if pack['upstream'] is None else pack['upstream']['model_id'])
            for name,value in fit['parameters'].items():params.append({**meta,'coefficient':name,'value':value,'fixed_cref_ppm':fit['cref']})
            train=m.training(self.data,fit['origin'],fit['train_start']);obs=train['co2_ppm'] if target=='co2' else train['temp_anomaly_c']
            if mid.startswith('T1'):pred=m.temperature_from_co2(fit,train['co2_ppm'])
            elif mid=='T0':pred=m.predict_temperature(fit,train['year'])
            else:pred=m.predict_co2(fit,train['year'])
            residual=pred-obs
            for y,o,p,e in zip(train['year'],obs,pred,residual):residuals.append({**meta,'year':int(y),'observed':float(o),'fitted':float(p),'residual_fitted_minus_observed':float(e),'fit_input':'observed training CO2' if mid.startswith('T1') else 'training year','log_residual':float(np.log(p/o)) if mid=='E' else None})
            lag,status=m.correlation(residual[:-1],residual[1:]);diagnostics.append({**meta,'residual_mean':float(np.mean(residual)),'residual_rmse':float(np.sqrt(np.mean(residual**2))),'residual_lag1_correlation':lag,'lag1_status':status,'interpretation':'descriptive fit diagnostics; not selection criteria'})
        return params,residuals,diagnostics
    def forecasts(self,origins,phase,data):
        rows=[];params=[];residuals=[];diagnostics=[]
        for origin in origins:
            packs=self.fits(data,origin);p,r,d=self.fit_evidence(packs,phase,'full');params+=p;residuals+=r;diagnostics+=d
            for mid in MODEL_IDS:
                pack=packs[mid];fit=pack['fit'];target='co2' if mid in ['D','Q','E'] else 'temp'
                for horizon in range(1,11):
                    year=origin+horizon;idx=int(np.flatnonzero(data['year']==year)[0]);obs=float(data['co2_ppm' if target=='co2' else 'temp_anomaly_c'][idx])
                    row={'phase':phase,'target':target,'model_id':mid,'origin_year':origin,'train_start':None if fit is None else fit['train_start'],'train_end':None if fit is None else fit['train_end'],'n_train':None if fit is None else fit['n_train'],'target_year':year,'horizon':horizon,'observed':obs,'predicted':None,'error':None,'unit':'ppm' if target=='co2' else 'degrees_C_anomaly_1951_1980','status':pack['status'],'forecast_co2_input_ppm':None,'upstream_model_id':None if pack['upstream'] is None else pack['upstream']['model_id']}
                    try:
                        pred=self.predict(mid,pack,year);row.update(predicted=pred,error=pred-obs,status='OK')
                        if target=='co2' and pred<=0:row['status']='NONPOSITIVE_PATH'
                        if mid.startswith('T1'):row['forecast_co2_input_ppm']=float(m.predict_co2(pack['upstream'],year))
                    except m.ModelFailure as error:row.update(status=error.status,reason=str(error))
                    rows.append(row)
        return rows,params,residuals,diagnostics
    @staticmethod
    def metrics(rows):
        out=[]
        for mid in MODEL_IDS:
            candidate=[r for r in rows if r['model_id']==mid];groups=[('overall',None,candidate)]
            groups += [('origin',o,[r for r in candidate if r['origin_year']==o]) for o in sorted(set(r['origin_year'] for r in candidate))]
            groups += [('horizon',h,[r for r in candidate if r['horizon']==h]) for h in range(1,11)]
            for grouping,value,group in groups:
                ok=all(r['status']=='OK' for r in group);errors=np.array([r['error'] for r in group]) if ok else None
                out.append({'phase':group[0]['phase'],'target':group[0]['target'],'model_id':mid,'grouping':grouping,'group_value':value,'n':len(group),'valid_n':sum(r['status']=='OK' for r in group),'mae':float(np.mean(np.abs(errors))) if ok else None,'rmse':float(np.sqrt(np.mean(errors**2))) if ok else None,'bias':float(np.mean(errors)) if ok else None,'unit':group[0]['unit'],'status':'OK' if ok else 'INELIGIBLE_FAILED_ROWS'})
        return out
    def development(self):
        data={k:v[self.data['year']<=2011] for k,v in self.data.items()};rows,params,residuals,diagnostics=self.forecasts(self.config['development_origins'],'development',data);metrics=self.metrics(rows)
        for name,value in [('development_forecasts.csv',rows),('development_metrics.csv',metrics),('development_coefficients.csv',params),('development_residuals.csv',residuals),('development_fit_diagnostics.csv',diagnostics)]:self.table(name,value)
        scores={r['model_id']:r['mae'] for r in metrics if r['grouping']=='overall'};selected_co2=m.select_minimum(scores,['D','E','Q']);temp_candidates=['T0','T1-'+selected_co2];selected_temp=m.select_minimum(scores,temp_candidates)
        receipt={**self.identity,'run_id':self.config['run_id'],'status':'FROZEN_BEFORE_FINAL_ASSESSMENT','frozen_at':now(),'co2_candidates':['D','Q','E'],'temperature_comparators':['T0','T1-D','T1-Q','T1-E'],'temperature_selection_candidates':temp_candidates,'development_origins':self.config['development_origins'],'horizons':list(range(1,11)),'development_target_max_year':2011,'eligible_ids':[mid for mid in MODEL_IDS if scores[mid] is not None],'development_mae':scores,'selected_co2_id':selected_co2,'selected_temperature_id':selected_temp,'development_forecasts_sha256':sha(self.out/'development_forecasts.csv'),'development_metrics_sha256':sha(self.out/'development_metrics.csv'),'final_targets_used_for_selection':False,'project_final_scores_previously_exposed_by_A01':True,'selection_rule_changed_after_exposure':False,'note':'Local execution order for unchanged predeclared rules. A01 already consumed final scores; no project-wide unseen holdout claim.'}
        savejson(self.out/'selection_frozen.json',receipt);print(json.dumps({'phase':'development','status':'SUCCEEDED','scores':scores,'selected_co2':selected_co2,'selected_temperature':selected_temp}))
    def load_frozen(self):
        path=self.out/'selection_frozen.json';receipt=json.loads(path.read_text())
        if receipt['status']!='FROZEN_BEFORE_FINAL_ASSESSMENT':raise ValueError('Missing freeze status')
        for k,v in self.identity.items():
            if receipt[k]!=v:raise ValueError('Freeze dependency mismatch: '+k)
        for name in ['development_forecasts','development_metrics']:
            if sha(self.out/(name+'.csv'))!=receipt[name+'_sha256']:raise ValueError('Development evidence changed after freeze')
        return receipt
    def final(self):
        receipt=self.load_frozen();start=now();frozen_hash=sha(self.out/'selection_frozen.json');rows,params,residuals,diagnostics=self.forecasts([2011],'final',self.data);metrics=self.metrics(rows)
        for name,value in [('final_forecasts.csv',rows),('final_metrics.csv',metrics),('final_coefficients.csv',params),('final_residuals.csv',residuals),('final_fit_diagnostics.csv',diagnostics)]:self.table(name,value)
        if sha(self.out/'selection_frozen.json')!=frozen_hash:raise ValueError('Freeze receipt mutated')
        savejson(self.out/'final_assessment_receipt.json',{'status':'COMPLETED','started_at':start,'finished_at':now(),'loaded_selection_sha256':frozen_hash,'selection_frozen_at':receipt['frozen_at'],'selected_co2_id':receipt['selected_co2_id'],'selected_temperature_id':receipt['selected_temperature_id'],'final_forecasts_sha256':sha(self.out/'final_forecasts.csv'),'final_metrics_sha256':sha(self.out/'final_metrics.csv'),'selection_changed':False,'final_metrics':[r for r in metrics if r['grouping']=='overall']})
        print(json.dumps({'phase':'final','status':'SUCCEEDED','metrics':[r for r in metrics if r['grouping']=='overall'],'selection_changed':False}))
    def read_forecasts(self,name):
        with (self.out/name).open() as f:rows=list(csv.DictReader(f))
        for r in rows:
            for k in ['origin_year','horizon','target_year']:r[k]=int(r[k])
            for k in ['error','predicted','observed']:r[k]=None if r[k]=='' else float(r[k])
        return rows
    def production(self):
        receipt=self.load_frozen();assessment=json.loads((self.out/'final_assessment_receipt.json').read_text())
        if assessment['status']!='COMPLETED' or assessment['loaded_selection_sha256']!=sha(self.out/'selection_frozen.json'):raise ValueError('Final stage prerequisite mismatch')
        verify_final_tables(self.out,assessment)
        paths=[];search_paths=[];thresholds=[];summary=[];params=[];residuals=[];fit_diagnostics=[];path_diagnostics=[]
        selected=[receipt['selected_co2_id'],receipt['selected_temperature_id']]
        for window,start in [('full',1959),('last30',1992)]:
            packs=self.fits(self.data,2021,start);ids=MODEL_IDS if window=='full' else selected
            p,r,d=self.fit_evidence({mid:packs[mid] for mid in ids},'production',window);params+=p;residuals+=r;fit_diagnostics+=d
            for mid in ids:
                pack=packs[mid];target='co2' if mid in ['D','Q','E'] else 'temp';unit='ppm' if target=='co2' else 'degrees_C_anomaly_1951_1980'
                meta={'fit_window':window,'target':target,'model_id':mid,'origin':2021,'unit':unit,'selected_rule':mid in selected};values=[];invalid_from=None;prefix_reason=None
                for year in range(2021,2301):
                    row={**meta,'year':year,'value':None,'status':pack['status'],'interpretation':'conditional_central_path','forecast_co2_input_ppm':None}
                    try:
                        if invalid_from is not None:raise m.ModelFailure('INVALID_PATH','Invalid contiguous path prefix from '+str(invalid_from)+': '+str(prefix_reason))
                        v=self.predict(mid,pack,year);row.update(value=v,status='OK')
                        if target=='co2' and v<=0:row.update(value=None,status='NONPOSITIVE_CO2',reason='NONPOSITIVE_CO2')
                        if mid.startswith('T1'):row['forecast_co2_input_ppm']=float(m.predict_co2(pack['upstream'],year))
                    except m.ModelFailure as error:row.update(status=error.status,reason=str(error))
                    if row['status']!='OK' and invalid_from is None:invalid_from=year;prefix_reason=row.get('reason',row['status'])
                    values.append(row);search_paths.append(row)
                    if 2022<=year<=2100:paths.append(row)
                f=lambda year:self.predict(mid,pack,year)
                for threshold in ([685] if target=='co2' else [1.25,1.50,2.0]):
                    row={**meta,**m.crossing(f,threshold,positive_required=(target=='co2'))};observed=self.data['co2_ppm'] if target=='co2' else self.data['temp_anomaly_c'];hit=self.data['year'][observed>=threshold-m.TOL]
                    row['first_observed_historical_exceedance']=None if len(hit)==0 else int(hit[0])
                    if mid.startswith('T1') and pack['status']=='OK':
                        pp=pack['fit']['parameters'];beta=pp['beta_c_per_log_ratio']
                        try:row['equivalent_co2_threshold_ppm']=self.cref*math.exp((threshold-pp['alpha_c'])/beta) if beta>0 else None
                        except OverflowError:row['equivalent_co2_threshold_ppm']=None
                    thresholds.append(row)
                required={r['year']:r for r in values if r['year'] in [2050,2100]}
                for year in [2050,2100]:
                    row={**meta,'year':year,'value':required[year]['value'],'status':required[year]['status'],'reason':required[year].get('reason'),'interpretation':'conditional long extrapolation'}
                    if target=='co2':
                        v=row['value'];cross=next(r for r in thresholds if r['model_id']==mid and r['fit_window']==window)
                        row.update(gap_from_685_ppm=None if v is None else v-685,relative_gap_percent=None if v is None else 100*(v-685)/685,reaches_685_by_2050=(cross['status']=='AT_OR_BEFORE_ORIGIN' or (cross['first_year'] is not None and cross['first_year']<=2050)))
                    summary.append(row)
                valid=[r for r in values if r['value'] is not None];vv=np.array([r['value'] for r in valid]);dv=np.diff(vv)
                diag={**meta,'evaluated_start':2021,'evaluated_end':2300,'invalid_count':sum(r['status']!='OK' for r in values),'decreasing_segments':int(np.sum(dv < -m.TOL)),'minimum_value':float(min(vv)) if len(vv) else None,'nonpositive_co2_count':sum(r['value'] is not None and r['value']<=0 for r in values) if target=='co2' else None,'turning_year':None}
                if mid=='Q' and pack['status']=='OK':
                    pp=pack['fit']['parameters'];q=pp['c_ppm_per_decade_squared'];diag['turning_year']=None if q==0 else 1959+10*(-pp['b_ppm_per_decade']/(2*q));diag['growth_ppm_per_year_2021']=float((pp['b_ppm_per_decade']+2*q*m.xyears(2021))/10);diag['growth_ppm_per_year_2100']=float((pp['b_ppm_per_decade']+2*q*m.xyears(2100))/10)
                path_diagnostics.append(diag)
        for name,value in [('production_forecasts.csv',paths),('threshold_search_paths.csv',search_paths),('thresholds.csv',thresholds),('forecast_summary.csv',summary),('production_coefficients.csv',params),('production_residuals.csv',residuals),('production_fit_diagnostics.csv',fit_diagnostics),('path_diagnostics.csv',path_diagnostics)]:self.table(name,value)
        changes=m.ten_year_changes(self.data['year'],self.data['co2_ppm'],range(1969,2005));last=changes[-1]['increase_ppm'];prior=max(r['increase_ppm'] for r in changes[:-1]);self.table('ten_year_changes.csv',changes)
        comparison={'period':'supplied annual observations only','window_2004_increase_ppm':last,'prior_max_increase_ppm':prior,'prior_max_ending_years':[r['end_year'] for r in changes[:-1] if abs(r['increase_ppm']-prior)<=m.TOL],'rank_2004_among_36':1+sum(r['increase_ppm']>last+m.TOL for r in changes),'margin_2004_minus_prior_max_ppm':last-prior,'status':'TIED' if abs(last-prior)<=m.TOL else ('STRICTLY_LARGER' if last>prior else 'SMALLER')};savejson(self.out/'ten_year_comparison.json',{**self.trace,**comparison})
        relationship,diagnostic_series=m.relationship_diagnostics(self.data)
        for row in relationship:row.update(interpretation='descriptive association, not causal identification',x_unit='ppm' if row['diagnostic']=='levels_co2' else 'log concentration ratio',y_unit='degrees_C_anomaly_1951_1980',fitted_doubling_contrast_c=row['slope']*math.log(2) if row['diagnostic']=='levels_log_co2' and row['slope'] is not None else None)
        self.table('relationship_diagnostics.csv',relationship);self.table('relationship_series.csv',diagnostic_series)
        development=self.read_forecasts('development_forecasts.csv');final=self.read_forecasts('final_forecasts.csv');envelope=[];future_envelope=[];horizon_evidence=[];error_samples=[]
        for mid in selected:
            radius=m.historical_envelope(development,mid);target='co2' if mid in ['D','Q','E'] else 'temp';unit='ppm' if target=='co2' else 'degrees_C_anomaly_1951_1980'
            for row in development:
                if row['model_id']==mid:error_samples.append({'target':target,'model_id':mid,'origin_year':row['origin_year'],'horizon':row['horizon'],'error':row['error'],'unit':unit})
            for h in range(1,11):
                test=next(r for r in final if r['model_id']==mid and r['horizon']==h);dev=[r for r in development if r['model_id']==mid and r['horizon']==h]
                envelope.append({'target':target,'selected_model_id':mid,'horizon':h,'radius':radius[h],'unit':unit,'development_origin_count':5,'label':'historical_max_error_envelope','final_target_year':test['target_year'],'final_absolute_error':absolute_or_none(test['error']),'final_contained':None if test['error'] is None else abs(test['error'])<=radius[h]+m.TOL,'final_lower':offset_or_none(test['predicted'],-radius[h]),'final_upper':offset_or_none(test['predicted'],radius[h]),'final_status':test['status']})
                predicted=next(r['value'] for r in paths if r['fit_window']=='full' and r['model_id']==mid and r['year']==2021+h)
                future_envelope.append({'target':target,'selected_model_id':mid,'year':2021+h,'horizon':h,'central_path':predicted,'radius':radius[h],'lower':offset_or_none(predicted,-radius[h]),'upper':offset_or_none(predicted,radius[h]),'unit':unit,'label':'historical_max_error_envelope','coverage_guarantee':'none','status':'OK' if predicted is not None else 'INVALID_PATH'})
                horizon_evidence.append({'target':target,'selected_model_id':mid,'horizon':h,'development_mae':float(np.mean([abs(r['error']) for r in dev])),'development_origin_count':5,'final_absolute_error':absolute_or_none(test['error']),'future_year':2021+h,'unit':unit,'headline_horizon':h in [1,5,10],'final_status':test['status']})
        for row in envelope:row['final_excess']=None if row['final_absolute_error'] is None else max(0,row['final_absolute_error']-row['radius'])
        self.table('historical_error_envelopes.csv',envelope);self.table('production_error_envelopes.csv',future_envelope);self.table('horizon_evidence.csv',horizon_evidence);self.table('development_error_samples.csv',error_samples)
        self.rank_diagnostics(development,final,receipt)
        sensitivity=[]
        for row in summary:
            if row['fit_window']=='last30':
                baseline=next(r for r in summary if r['fit_window']=='full' and r['model_id']==row['model_id'] and r['year']==row['year']);sensitivity.append({'target':row['target'],'model_id':row['model_id'],'quantity':'forecast','year':row['year'],'threshold':None,'full_value':baseline['value'],'last30_value':row['value'],'difference':difference_or_none(row['value'],baseline['value']),'unit':row['unit'],'full_status':baseline['status'],'last30_status':row['status']})
        for row in thresholds:
            if row['fit_window']=='last30':
                baseline=next(r for r in thresholds if r['fit_window']=='full' and r['model_id']==row['model_id'] and r['threshold']==row['threshold']);a,b=baseline['first_year'],row['first_year'];sensitivity.append({'target':row['target'],'model_id':row['model_id'],'quantity':'threshold_year','year':None,'threshold':row['threshold'],'full_value':a,'last30_value':b,'difference':None if a is None or b is None else b-a,'unit':'calendar years','full_status':baseline['status'],'last30_status':row['status']})
        self.table('window_sensitivity.csv',sensitivity);full=[r for r in summary if r['fit_window']=='full'];structural=[]
        for target in ['co2','temp']:
            for year in [2050,2100]:
                rr=[r for r in full if r['target']==target and r['year']==year and r['value'] is not None];structural.append({'target':target,'year':year,'minimum':min(r['value'] for r in rr) if rr else None,'maximum':max(r['value'] for r in rr) if rr else None,'spread':max(r['value'] for r in rr)-min(r['value'] for r in rr) if rr else None,'model_count':len(rr),'unit':'ppm' if target=='co2' else 'degrees_C_anomaly_1951_1980','status':'OK' if rr else 'INVALID_PATH','interpretation':'model-form sensitivity, not probability interval'})
        self.table('structural_sensitivity.csv',structural);checks=self.check_outputs(receipt,paths,thresholds,development,final,envelope,future_envelope);savejson(self.out/'numerical_checks.json',checks)
        if not all(r['pass'] for r in checks['checks']):raise AssertionError('Post-computation validation failed')
        claims={'status':'COMPUTED_CANDIDATES_PENDING_INDEPENDENT_REVIEW','selected_co2':receipt['selected_co2_id'],'selected_temperature':receipt['selected_temperature_id'],'ten_year_comparison':comparison,'final_overall_metrics':assessment['final_metrics'],'forecast_summary':summary,'thresholds':thresholds,'relationship_diagnostics':relationship,'final_envelope_misses':{mid:sum(r['final_contained'] is False for r in envelope if r['selected_model_id']==mid) for mid in selected},'limitations':['Annual supplied series cannot test March claim.','685 ppm OECD source is CO2-equivalent; these models use pure CO2.','Temperature baseline1951–1980.','No causal identification, long-horizon accuracy guarantee or probability interval.','Final targets excluded from unchanged selector; A01 already exposed final scores before this primary execution.']}
        savejson(self.out/'claim_candidates.json',{**self.trace,**claims});savejson(self.out/'production_receipt.json',{'status':'COMPLETED','finished_at':now(),'loaded_selection_sha256':sha(self.out/'selection_frozen.json'),'final_assessment_sha256':sha(self.out/'final_assessment_receipt.json'),'checks_passed':len(checks['checks'])});print(json.dumps({'phase':'production','status':'SUCCEEDED','selected':selected,'checks_passed':len(checks['checks']),'envelope_misses':claims['final_envelope_misses']}))
    def check_outputs(self,receipt,paths,thresholds,development,final,envelope,future):
        checks=[]
        def check(name,ok,detail):checks.append({'check':name,'pass':bool(ok),'detail':detail})
        check('development_counts',all(sum(r['model_id']==mid for r in development)==50 for mid in MODEL_IDS),'50 rows per declared model');check('final_counts',all(sum(r['model_id']==mid for r in final)==10 for mid in MODEL_IDS),'10 rows per declared model')
        check('temporal_availability',all(r['train_end'] not in [None,''] and int(r['train_end'])<=r['origin_year'] and r['target_year']==r['origin_year']+r['horizon'] for r in development+final),'Every fit ends at/before origin; target=origin+h');check('development_cutoff',max(r['target_year'] for r in development)==2011,'Development outcomes end2011')
        check('frozen_receipt_unchanged',json.loads((self.out/'selection_frozen.json').read_text())==receipt,'Final and production loaded unchanged receipt');check('path_count',len(paths)==79*(7+2),'553 full plus158 selected last30 display rows')
        check('no_envelope_after_2031',max(r['year'] for r in future)==2031 and len(future)==20,'Only10-year empirical radii');check('nondecreasing_envelope',all(np.all(np.diff([r['radius'] for r in envelope if r['selected_model_id']==mid])>=0) for mid in [receipt['selected_co2_id'],receipt['selected_temperature_id']]),'Prefix maxima cannot shrink')
        check('threshold_boundaries',all(r['value_at_year']>=r['threshold']-m.TOL and r['value_previous_year']<r['threshold']-m.TOL for r in thresholds if r['status']=='CROSSED'),'Raw crossing and predecessor, tolerance1e-9');check('finite_valid_outputs',all(r['value'] is not None and math.isfinite(r['value']) for r in paths if r['status']=='OK'),'No NaN in successful row')
        check('all_required_forecast_years',all(any(r['model_id']==mid and r['fit_window']=='full' and r['year']==y for r in paths) for mid in MODEL_IDS for y in [2050,2100]),'All7 models retained2050/2100');check('forecast_CO2_pipeline',all(r['forecast_co2_input_ppm']!='' and float(r['forecast_co2_input_ppm'])>0 for r in development+final if r['model_id'].startswith('T1') and r['status']=='OK'),'All linked scores retain forecastCO2 input')
        return {'status':'PASS' if all(r['pass'] for r in checks) else 'FAIL','checks':checks}

    def rank_diagnostics(self,development,final,receipt):
        """Post-assessment summaries; these never feed the original selector."""
        rows=[];counts={mid:0 for mid in ['D','E','Q']};origins=self.config['development_origins']
        for kind in ['per_origin','leave_one_origin_out']:
            for origin in origins:
                subset=[r for r in development if (r['origin_year']==origin if kind=='per_origin' else r['origin_year']!=origin)]
                scores={mid:float(np.mean([abs(r['error']) for r in subset if r['model_id']==mid])) if all(r['error'] is not None for r in subset if r['model_id']==mid) else None for mid in ['D','E','Q']};winner=m.select_minimum(scores,['D','E','Q'])
                if kind=='per_origin':counts[winner]+=1
                for mid,score in scores.items():rows.append({'diagnostic':kind,'origin_year':origin if kind=='per_origin' else None,'omitted_origin':origin if kind=='leave_one_origin_out' else None,'model_id':mid,'mae_ppm':score,'diagnostic_rank':None if score is None else 1+sum(v is not None and v<score-1e-12 for v in scores.values()),'diagnostic_winner':winner,'win_count':None,'introduced_after_assessment':True,'selection_changed':False})
        for mid,count in counts.items():rows.append({'diagnostic':'per_origin_win_count','origin_year':None,'omitted_origin':None,'model_id':mid,'mae_ppm':None,'diagnostic_rank':None,'diagnostic_winner':None,'win_count':count,'introduced_after_assessment':True,'selection_changed':False})
        self.table('rank_stability.csv',rows);ranks=[]
        for phase,source in [('development',development),('final',final)]:
            for target,ids in [('co2',['D','E','Q']),('temp',['T0','T1-D','T1-Q','T1-E'])]:
                scores={mid:float(np.mean([abs(r['error']) for r in source if r['model_id']==mid])) if all(r['error'] is not None for r in source if r['model_id']==mid) else None for mid in ids}
                finite={k:v for k,v in scores.items() if v is not None};winner=min(finite,key=finite.get) if finite else None
                for mid,score in scores.items():ranks.append({'phase':phase,'target':target,'model_id':mid,'mae':score,'rank_among_declared_comparators':None if score is None else 1+sum(v<score-1e-12 for v in finite.values()),'best_declared_comparator_id':winner,'selected_by_original_rule':mid in [receipt['selected_co2_id'],receipt['selected_temperature_id']],'eligible_for_original_selection':mid in (ids if target=='co2' else receipt['temperature_selection_candidates']),'unit':'ppm' if target=='co2' else 'degrees_C_anomaly_1951_1980','introduced_after_assessment':True,'selection_changed':False})
        self.table('comparison_ranks.csv',ranks)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--phase',choices=['development','final','production'],required=True);p.add_argument('--snapshot',required=True);p.add_argument('--output-dir',required=True);p.add_argument('--config',required=True);args=p.parse_args();obj=Analysis(args.snapshot,args.output_dir,args.config);getattr(obj,args.phase)()
