"""Direct implementation of released T02 M00-M07. Units are explicit in fits."""
from dataclasses import dataclass
import math
import numpy as np

TOL = 1e-9


class ModelFailure(ValueError):
    def __init__(self, status, message):
        self.status = status
        super().__init__(message)


def validate_data(data, expected_years=None):
    year = np.asarray(data['year'])
    c, t = np.asarray(data['co2_ppm']), np.asarray(data['temp_anomaly_c'])
    if not (len(year) == len(c) == len(t)) or len(year) == 0:
        raise ModelFailure('INPUT_CONTRACT_FAILURE', 'Empty or unequal-length columns')
    if not all(np.all(np.isfinite(v)) for v in (year,c,t)):
        raise ModelFailure('INPUT_CONTRACT_FAILURE', 'Nonfinite observations')
    if np.any(year != year.astype(int)) or len(set(year)) != len(year):
        raise ModelFailure('INPUT_CONTRACT_FAILURE', 'Noninteger or duplicated years')
    if np.any(np.diff(year) != 1) or (expected_years is not None and not np.array_equal(year, expected_years)):
        raise ModelFailure('INPUT_CONTRACT_FAILURE', 'Noncontiguous or unexpected years')
    if np.any(c <= 0):
        raise ModelFailure('INPUT_CONTRACT_FAILURE', 'CO2 must be strictly positive')


def xyears(year):
    return (np.asarray(year,dtype=float)-1959.0)/10.0


def least_squares(design, outcome):
    design, outcome = np.asarray(design,dtype=float), np.asarray(outcome,dtype=float)
    if not np.all(np.isfinite(design)) or not np.all(np.isfinite(outcome)):
        raise ModelFailure('NONFINITE_FIT', 'Nonfinite regression arrays')
    beta, _, rank, singular = np.linalg.lstsq(design,outcome,rcond=None)
    if rank != design.shape[1]:
        raise ModelFailure('RANK_DEFICIENT', 'Design matrix lacks full column rank')
    if not np.all(np.isfinite(beta)):
        raise ModelFailure('NONFINITE_FIT', 'Nonfinite fitted parameters')
    return beta, int(rank), singular


def training(data, origin, start):
    mask=(data['year']>=start)&(data['year']<=origin)
    result={key:np.asarray(value)[mask] for key,value in data.items()}
    validate_data(result, np.arange(start,origin+1))
    return result


def fit_co2(data, model_id, origin, start=1959, cref=None):
    if cref is None:
        ix=np.flatnonzero(data['year']==1959)
        if len(ix)!=1:
            raise ModelFailure('INPUT_CONTRACT_FAILURE','Missing fixed 1959 reference')
        cref=float(data['co2_ppm'][ix[0]])
    if not math.isfinite(cref) or cref<=0:
        raise ModelFailure('INPUT_CONTRACT_FAILURE','Invalid positive CO2 reference')
    train=training(data,origin,origin-10 if model_id=='D' else start)
    years,c=train['year'],train['co2_ppm']; x=xyears(years)
    base={'model_id':model_id,'origin':int(origin),'train_start':int(years[0]),'train_end':int(years[-1]),'n_train':len(years),'cref':cref,'status':'OK'}
    if model_id=='D':
        base.update(parameters={'anchor_ppm':float(c[-1]),'slope_ppm_per_year':float((c[-1]-c[0])/10)},rank=None,fit_method='ten-year endpoint drift')
    elif model_id=='Q':
        beta,rank,s=least_squares(np.column_stack([np.ones(len(x)),x,x*x]),c)
        base.update(parameters=dict(zip(['a_ppm','b_ppm_per_decade','c_ppm_per_decade_squared'],map(float,beta))),rank=rank,singular_values=s.tolist(),fit_method='SVD least squares in ppm')
    elif model_id=='E':
        beta,rank,s=least_squares(np.column_stack([np.ones(len(x)),x]),np.log(c/cref))
        base.update(parameters=dict(zip(['a_log_ratio','b_log_ratio_per_decade'],map(float,beta))),rank=rank,singular_values=s.tolist(),fit_method='SVD least squares in log(C/C_ref)')
    else:
        raise ValueError('Unknown CO2 model '+model_id)
    return base


def fit_temperature(data,model_id,origin,start=1959,cref=None):
    if cref is None:
        cref=float(data['co2_ppm'][np.flatnonzero(data['year']==1959)[0]])
    train=training(data,origin,start)
    predictor=xyears(train['year']) if model_id=='T0' else np.log(train['co2_ppm']/cref)
    beta,rank,s=least_squares(np.column_stack([np.ones(len(predictor)),predictor]),train['temp_anomaly_c'])
    names=['alpha0_c','delta_c_per_decade'] if model_id=='T0' else ['alpha_c','beta_c_per_log_ratio']
    return {'model_id':model_id,'origin':int(origin),'train_start':int(train['year'][0]),'train_end':int(train['year'][-1]),'n_train':len(train['year']),
            'cref':cref,'parameters':dict(zip(names,map(float,beta))),'rank':rank,'singular_values':s.tolist(),'fit_method':'SVD least squares in degrees Celsius anomaly','status':'OK'}


def predict_co2(fit,years):
    t=np.asarray(years,dtype=float); x=xyears(t); p=fit['parameters']; m=fit['model_id']
    with np.errstate(over='ignore',invalid='ignore'):
        if m=='D': result=p['anchor_ppm']+p['slope_ppm_per_year']*(t-fit['origin'])
        elif m=='Q': result=p['a_ppm']+p['b_ppm_per_decade']*x+p['c_ppm_per_decade_squared']*x*x
        elif m=='E': result=fit['cref']*np.exp(p['a_log_ratio']+p['b_log_ratio_per_decade']*x)
        else: raise ValueError(m)
    if not np.all(np.isfinite(result)):
        raise ModelFailure('NONFINITE_PREDICTION','CO2 prediction overflow/nonfinite')
    return result


def temperature_from_co2(fit,co2):
    c=np.asarray(co2,dtype=float)
    if np.any(c<=0) or not np.all(np.isfinite(c)):
        raise ModelFailure('INVALID_UPSTREAM_PATH','Linked temperature needs finite positive forecast CO2')
    p=fit['parameters']
    result=p['alpha_c']+p['beta_c_per_log_ratio']*np.log(c/fit['cref'])
    if not np.all(np.isfinite(result)):
        raise ModelFailure('NONFINITE_PREDICTION','Temperature prediction nonfinite')
    return result


def predict_temperature(fit,years,upstream=None):
    if fit['model_id']=='T0':
        p=fit['parameters']; return p['alpha0_c']+p['delta_c_per_decade']*xyears(years)
    if upstream is None:
        raise ModelFailure('INVALID_UPSTREAM_PATH','Missing forecast CO2 producer')
    try:
        forecast_co2=predict_co2(upstream,years)
    except ModelFailure as error:
        raise ModelFailure('INVALID_UPSTREAM_PATH','CO2 producer failed: '+str(error)) from error
    return temperature_from_co2(fit,forecast_co2)


def ten_year_changes(years,co2,end_years):
    values=dict(zip(map(int,years),map(float,co2)))
    rows=[]
    for end in end_years:
        if any(y not in values for y in range(end-10,end+1)):
            raise ModelFailure('INPUT_CONTRACT_FAILURE','Ten-year interval lacks eleven observations')
        change=values[end]-values[end-10]
        rows.append({'start_year':end-10,'end_year':end,'start_co2_ppm':values[end-10],'end_co2_ppm':values[end],'increase_ppm':change,'average_growth_ppm_per_year':change/10})
    return rows


def select_minimum(scores,tie_order,tolerance=1e-12):
    finite={k:float(scores[k]) for k in tie_order if k in scores and scores[k] is not None and math.isfinite(scores[k])}
    if not finite:
        raise ModelFailure('NO_ELIGIBLE_MODEL','All candidates failed development')
    best=min(finite.values())
    return next(k for k in tie_order if k in finite and finite[k]<=best+tolerance)


def crossing(function,threshold,origin=2021,search_end=2300,positive_required=False):
    """Released r02: first passage on valid prefix plus full-domain validity."""
    values=[];first=None;invalid=None
    for year in range(origin,search_end+1):
        try:
            raw=function(year)
            if raw is None:raise ModelFailure('MISSING_REQUIRED_VALUE','MISSING_REQUIRED_VALUE')
            value=float(raw)
            if not math.isfinite(value):raise ModelFailure('INVALID_PATH','NONFINITE_CO2' if positive_required else 'NONFINITE_TARGET')
            if positive_required and value<=0:raise ModelFailure('INVALID_PATH','NONPOSITIVE_CO2')
        except (ModelFailure,OverflowError,ValueError,TypeError) as error:
            if invalid is None:invalid={'year':year,'reason':str(error) or 'EVALUATION_ERROR'}
            continue
        if invalid is not None:continue  # Re-entry never restores first-passage inference.
        values.append((year,value))
        if first is None and value>=threshold-TOL:first=(year,value,values[-2][1] if len(values)>1 else None)
    diff=np.diff([v for _,v in values]);monotone=None if len(values)<2 else bool(np.all(diff>=-TOL))
    recross=bool(first is not None and any(y>first[0] and v<threshold-TOL for y,v in values))
    if first is not None:status='AT_OR_BEFORE_ORIGIN' if first[0]==origin else 'CROSSED'
    elif invalid:status='INVALID_PATH'
    else:status='NO_CROSSING_THROUGH_2300'
    end_valid=values[-1][0] if values else None
    return {'threshold':float(threshold),'origin':origin,'search_end':search_end,'first_year':first[0] if status=='CROSSED' else None,
            'status':status,'value_at_year':None if first is None else first[1],'value_previous_year':None if first is None else first[2],
            'monotone_flag':monotone,'monotonicity_end_year':end_valid,'possible_recrossing':recross,
            'beyond_tested_horizon':first[0]>origin+10 if status=='CROSSED' else None,
            'search_domain_valid':invalid is None,'valid_through_year':end_valid,
            'invalid_from_year':None if invalid is None else invalid['year'],'invalid_reason':None if invalid is None else invalid['reason']}


def correlation(a,b):
    a,b=np.asarray(a,dtype=float),np.asarray(b,dtype=float)
    if len(a)<2 or np.var(a)<=np.finfo(float).eps**2 or np.var(b)<=np.finfo(float).eps**2:
        return None,'UNDEFINED_CORRELATION'
    return float(np.corrcoef(a,b)[0,1]),'OK'


def descriptive_regression(a,b):
    r,status=correlation(a,b)
    if status!='OK': return {'correlation':r,'slope':None,'intercept':None,'r_squared':None,'status':status}
    beta,_,_=least_squares(np.column_stack([np.ones(len(a)),a]),b)
    residual=np.asarray(b)-beta[0]-beta[1]*np.asarray(a)
    r2=1-float(residual@residual)/float(np.sum((np.asarray(b)-np.mean(b))**2))
    return {'correlation':r,'slope':float(beta[1]),'intercept':float(beta[0]),'r_squared':r2,'status':status}


def relationship_diagnostics(data):
    years=data['year'];c=data['co2_ppm'];t=data['temp_anomaly_c'];z=np.log(c/c[0]);x=xyears(years)
    rows=[];series=[]
    for name,a,b,period,order in [('levels_co2',c,t,(int(years[0]),int(years[-1])),None),('levels_log_co2',z,t,(int(years[0]),int(years[-1])),None)]:
        rows.append({'diagnostic':name,'start_year':period[0],'end_year':period[1],'n':len(a),'detrending_order':order,**descriptive_regression(a,b)})
    for order in (1,2):
        design=np.column_stack([x**i for i in range(order+1)])
        bz,_,_=least_squares(design,z);bt,_,_=least_squares(design,t)
        rz=z-design@bz;rt=t-design@bt
        rows.append({'diagnostic':f'detrended_order_{order}','start_year':int(years[0]),'end_year':int(years[-1]),'n':len(years),'detrending_order':order,**descriptive_regression(rz,rt)})
        for y,az,at in zip(years,rz,rt):series.append({'diagnostic':f'detrended_order_{order}','year':int(y),'x_value':float(az),'y_value':float(at)})
    dz=np.diff(z);dt=np.diff(t)
    rows.append({'diagnostic':'first_differences_log_co2','start_year':int(years[1]),'end_year':int(years[-1]),'n':len(dz),'detrending_order':None,**descriptive_regression(dz,dt)})
    for y,az,at in zip(years[1:],dz,dt):series.append({'diagnostic':'first_differences_log_co2','year':int(y),'x_value':float(az),'y_value':float(at)})
    return rows,series


def historical_envelope(forecast_rows,model_id):
    selected=[r for r in forecast_rows if r['model_id']==model_id]
    if len(selected)!=50 or any(r['status']!='OK' for r in selected):
        raise ModelFailure('INVALID_ENVELOPE','Need all fifty valid development errors')
    return {h:max(abs(r['error']) for r in selected if r['horizon']<=h) for h in range(1,11)}
