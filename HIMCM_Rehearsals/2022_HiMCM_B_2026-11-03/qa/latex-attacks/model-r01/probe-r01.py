"""New reviewer diagnostics; accepted-output inputs, no fit or reselection.

The realized-CO2 substitution is an ex-post error decomposition, NOT an
eligible forecast, oracle benchmark, new model, or assessment refresh.
"""
import csv
import hashlib
import json
import math
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
RUN = ROOT / 'runs/T05-scientific-20261103-r03/outputs'

def read(name):
    with (RUN / name).open() as f:
        return list(csv.DictReader(f))

def mean(xs):
    return sum(xs) / len(xs)

targets = [
    'models/model_spec-r02.md', 'models/model_decision-r03.md',
    'models/experiment_plan-r03.md', 'models/interpretation-r02.md',
    'control/accepted-claims-g3-r01.json', 'paper/manuscript-complete-r03.md',
    'paper/exports/2022_HiMCM_B_practice-complete-r03.pdf',
    'runs/T05-scientific-20261103-r03/manifest.json',
    'qa/adversarial_structure/review-r01.md',
    'qa/adversarial_validation/review-r02.md',
    'qa/numerical-r01/review.md', 'qa/adversarial_paper/r01/review.md',
]
targets += ['runs/T05-scientific-20261103-r03/outputs/' + f for f in [
    'development_forecasts.csv', 'final_forecasts.csv',
    'development_coefficients.csv', 'final_coefficients.csv',
    'production_coefficients.csv', 'forecast_summary.csv', 'thresholds.csv',
    'selection_frozen.json', 'historical_error_envelopes.csv']]
hashes = {p: hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in targets}
(OUT/'target-hashes-r01.json').write_text(json.dumps(hashes, indent=2)+'\n')

summary = {'scope': 'post-assessment diagnostics on accepted outputs; no refit or selector change',
           'error_decomposition': [], 'co2_horizon_scores': {}, 'calibration_beta': []}
details = []
for phase in ['development', 'final']:
    forecasts = read(phase + '_forecasts.csv')
    coefficients = read(phase + '_coefficients.csv')
    cmap = defaultdict(dict)
    for r in coefficients:
        cmap[int(r['origin']),r['model_id']][r['coefficient']] = float(r['value'])
    observed_c = {(int(r['origin_year']),int(r['target_year'])):float(r['observed'])
                  for r in forecasts if r['target']=='co2'}
    for model in ['T1-D','T1-Q','T1-E']:
        rows = [r for r in forecasts if r['model_id']==model]
        comp = []
        for r in rows:
            origin,year = int(r['origin_year']),int(r['target_year'])
            cf = cmap[origin,model]
            cobs = observed_c[origin,year]
            pobs = cf['alpha_c']+cf['beta_c_per_log_ratio']*math.log(cobs/315.98)
            calibration = pobs-float(r['observed'])
            upstream = cf['beta_c_per_log_ratio']*math.log(float(r['forecast_co2_input_ppm'])/cobs)
            residual = float(r['error'])-calibration-upstream
            assert abs(residual)<1e-12
            item = dict(phase=phase,model=model,origin=origin,year=year,
                        calibration_error=calibration,upstream_contribution=upstream,
                        total_error=float(r['error']),decomposition_residual=residual)
            comp.append(item)
            details.append(item)
        summary['error_decomposition'].append(dict(
            phase=phase,model=model,n=len(comp),
            total_mae=mean([abs(r['total_error']) for r in comp]),
            conditional_realized_c_mae=mean([abs(r['calibration_error']) for r in comp]),
            total_bias=mean([r['total_error'] for r in comp]),
            calibration_bias=mean([r['calibration_error'] for r in comp]),
            upstream_bias=mean([r['upstream_contribution'] for r in comp]),
            opposite_sign_count=sum(r['calibration_error']*r['upstream_contribution']<0 for r in comp),
            upstream_reduces_abs_error_count=sum(abs(r['total_error'])<abs(r['calibration_error']) for r in comp)))
    for (origin,model),cf in cmap.items():
        if model=='T1-D': summary['calibration_beta'].append(dict(origin=origin,beta=cf['beta_c_per_log_ratio']))
    summary['co2_horizon_scores'][phase] = {}
    for ids,horizon in [('all',range(1,11)),('h1_3',range(1,4)),('h8_10',range(8,11)),('h10',[10])]:
        summary['co2_horizon_scores'][phase][ids] = {
            model: mean([abs(float(r['error'])) for r in forecasts
                         if r['model_id']==model and int(r['horizon']) in horizon])
            for model in ['D','Q','E']}

rows = read('production_coefficients.csv')
for r in rows:
    if r['model_id']=='T1-D' and r['coefficient']=='beta_c_per_log_ratio':
        summary['calibration_beta'].append(dict(origin=2021,window=r['fit_window'],beta=float(r['value'])))

development = read('development_forecasts.csv')
summary['target_weights'] = dict(sorted((str(y),sum(int(r['target_year'])==y for r in development if r['model_id']=='D'))
                                      for y in set(int(r['target_year']) for r in development)))
summary['equal_target_weighted_mae'] = {}
for model in ['D','Q','E']:
    by_year=defaultdict(list)
    for r in development:
        if r['model_id']==model: by_year[int(r['target_year'])].append(abs(float(r['error'])))
    summary['equal_target_weighted_mae'][model]=mean([mean(v) for v in by_year.values()])

with (OUT/'decomposition-r01.csv').open('w') as f:
    writer=csv.DictWriter(f,fieldnames=list(details[0])); writer.writeheader(); writer.writerows(details)
(OUT/'probe-results-r01.json').write_text(json.dumps(summary,indent=2)+'\n')
assert all(hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==v for p,v in hashes.items())
print(json.dumps(summary,indent=2))
