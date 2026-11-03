"""Independent A05 exact-rational recheck of the A07 weighting clarification."""
import csv
import hashlib
import json
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path

root = Path(__file__).resolve().parents[3]
output = Path(__file__).resolve().parent
source = root/'runs/T05-scientific-20261103-r03/outputs/development_forecasts.csv'
expected_hash = 'd82a891af936cbe2865e99c90d3495df3b91311f8dadd5756a245ddfbb29ede4'
assert hashlib.sha256(source.read_bytes()).hexdigest() == expected_hash
with source.open() as f:
    rows = list(csv.DictReader(f))
result = {}
for model in ['D', 'Q', 'E']:
    subset = [r for r in rows if r['model_id']==model and r['phase']=='development' and r['target']=='co2']
    assert len(subset) == 50
    assert len({(r['origin_year'],r['horizon']) for r in subset}) == 50
    counts = Counter(int(r['target_year']) for r in subset)
    assert len(counts) == 30
    by_horizon = defaultdict(Fraction)
    by_origin = defaultdict(Fraction)
    joint = {}
    for row in subset:
        origin,horizon,year = [int(row[k]) for k in ['origin_year','horizon','target_year']]
        assert origin+horizon==year
        weight = Fraction(1,30*counts[year])
        by_horizon[horizon] += weight
        by_origin[origin] += weight
        joint[f'{origin},{horizon}'] = str(weight)
    assert sum(by_horizon.values()) == 1
    assert dict(by_horizon) == {h:Fraction(1,10) for h in range(1,11)}
    assert dict(by_origin) == {1981:Fraction(1,4),1986:Fraction(1,6),1991:Fraction(1,6),1996:Fraction(1,6),2001:Fraction(1,4)}
    result[model] = {'diagnostic_horizon_weights':{str(k):str(v) for k,v in sorted(by_horizon.items())},
                     'diagnostic_origin_weights':{str(k):str(v) for k,v in sorted(by_origin.items())},
                     'diagnostic_joint_weights':joint,
                     'original_horizon_weight':'1/10','original_origin_weight':'1/5','original_joint_weight':'1/50'}
assert hashlib.sha256(source.read_bytes()).hexdigest() == expected_hash
payload = {'input':str(source.relative_to(root)), 'sha256':expected_hash,
           'method':'independent Python Fraction aggregation from original CSV, no A07 or A05 r01 code imports',
           'passed':True, 'models':result}
(output/'marginal-weights-r02.json').write_text(json.dumps(payload,indent=2)+'\n')
print('PASS: all 3 models retain marginal horizon weights 1/10, origin weights change to 1/4 at 1981/2001 and 1/6 at 1986/1991/1996.')
