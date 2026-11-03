"""Independent A07 verification. No production or A05 code is imported."""
import csv
import hashlib
import json
from collections import Counter, defaultdict
from decimal import Decimal, getcontext
from pathlib import Path

getcontext().prec = 50
ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / 'qa/latex-attacks/evidence-r01'
SOURCE = 'runs/T05-scientific-20261103-r03/outputs/development_forecasts.csv'
PIN = 'd82a891af936cbe2865e99c90d3495df3b91311f8dadd5756a245ddfbb29ede4'
paths = [SOURCE, 'runs/T05-scientific-20261103-r03/outputs/selection_frozen.json',
         'models/model_spec-r02.md', 'control/accepted-claims-g3-r01.json',
         'qa/latex-attacks/model-r01/review-r01.md',
         'qa/latex-attacks/model-r01/probe-results-r01.json']
hashes = {p: hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}
assert hashes[SOURCE] == PIN
rows = list(csv.DictReader((ROOT/SOURCE).open()))
frozen = json.loads((ROOT/paths[1]).read_text())
results = {}
evidence = []
expected_keys = {(o,h) for o in (1981,1986,1991,1996,2001) for h in range(1,11)}
for model in ['D','Q','E']:
    subset = [r for r in rows if r['target']=='co2' and r['model_id']==model]
    assert len(subset) == 50
    keys = [(int(r['origin_year']),int(r['horizon'])) for r in subset]
    assert len(set(keys)) == 50 and set(keys) == expected_keys
    by_year = defaultdict(list)
    errors = []
    max_error_field_difference = Decimal(0)
    for r in subset:
        assert r['phase']=='development' and r['status']=='OK' and r['unit']=='ppm'
        y,o,h = map(int,(r['target_year'],r['origin_year'],r['horizon']))
        assert y == o+h
        signed = Decimal(r['predicted'])-Decimal(r['observed'])
        error = abs(signed)
        max_error_field_difference = max(max_error_field_difference,abs(signed-Decimal(r['error'])))
        errors.append(error)
        by_year[y].append((o,h,error))
    assert set(by_year)==set(range(1982,2012))
    assert all(len(v)==(2 if 1987<=y<=2006 else 1) for y,v in by_year.items())
    year_means = {y:sum(e for o,h,e in v)/len(v) for y,v in by_year.items()}
    pair_score = sum(errors)/50
    year_score = sum(year_means.values())/30
    inverse_count_score = sum(e/len(by_year[y])/30 for y,v in by_year.items() for o,h,e in v)
    assert abs(year_score-inverse_count_score)<Decimal('1e-45')
    assert abs(pair_score-Decimal(str(frozen['development_mae'][model])))<Decimal('1e-12')
    origin_weights = defaultdict(Decimal)
    horizon_weights = defaultdict(Decimal)
    for y,v in sorted(by_year.items()):
        for o,h,e in v:
            weight = Decimal(1)/30/len(v)
            origin_weights[o] += weight
            horizon_weights[h] += weight
            evidence.append({'model':model,'target_year':y,'origin_year':o,'horizon':h,
                             'absolute_error_from_prediction':str(e),'year_multiplicity':len(v),
                             'equal_pair_weight':'0.02','equal_year_pair_weight':str(weight),
                             'year_mean_absolute_error':str(year_means[y])})
    results[model] = {'n_pairs':50,'n_distinct_target_years':len(by_year),
                      'target_years':sorted(by_year),
                      'target_year_multiplicity':{str(y):len(v) for y,v in sorted(by_year.items())},
                      'equal_pair_mae_ppm':str(pair_score),'equal_target_year_mae_ppm':str(year_score),
                      'inverse_multiplicity_crosscheck_ppm':str(inverse_count_score),
                      'max_stored_error_vs_decimal_reconstruction_difference':str(max_error_field_difference),
                      'equal_year_origin_total_weights':{str(k):str(v) for k,v in sorted(origin_weights.items())},
                      'equal_year_horizon_total_weights':{str(k):str(v) for k,v in sorted(horizon_weights.items())}}
pair_winner = min(results,key=lambda k:Decimal(results[k]['equal_pair_mae_ppm']))
year_winner = min(results,key=lambda k:Decimal(results[k]['equal_target_year_mae_ppm']))
assert pair_winner=='D' and year_winner=='Q' and frozen['selected_co2_id']=='D'
for p,h in hashes.items():
    assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
output = {'reviewer':'A07','scope':'Post-assessment weighting diagnostic only, not full revised-text acceptance',
          'method':'Decimal arithmetic from CSV predicted minus observed, grouping errors by target year, no A05 script reuse',
          'source_hashes':hashes,'scores':results,'equal_pair_winner':pair_winner,'equal_year_winner':year_winner,
          'pair_D_advantage_ppm':str(Decimal(results['Q']['equal_pair_mae_ppm'])-Decimal(results['D']['equal_pair_mae_ppm'])),
          'year_Q_advantage_ppm':str(Decimal(results['D']['equal_target_year_mae_ppm'])-Decimal(results['Q']['equal_target_year_mae_ppm'])),
          'verdict':'PASS_WITH_INTERPRETATION_CLARIFICATION'}
(OUT/'weighting-verification-r01.json').write_text(json.dumps(output,indent=2)+'\n')
with (OUT/'weighting-row-evidence-r01.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(evidence[0]))
    w.writeheader()
    w.writerows(evidence)
print(json.dumps({k:{'pairs':v['n_pairs'],'years':v['n_distinct_target_years'],'pair_mae':v['equal_pair_mae_ppm'],'year_mae':v['equal_target_year_mae_ppm'],'origin_weights':v['equal_year_origin_total_weights'],'horizon_weights':v['equal_year_horizon_total_weights']} for k,v in results.items()},indent=2))
