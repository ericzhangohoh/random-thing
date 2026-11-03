"""T02 synthetic modeler self-check; NOT computation validation or independent review."""
from pathlib import Path
import hashlib
import json
import math
import sys
import numpy as np

HERE = Path(__file__).resolve().parent
checks = []
def check(name, passed, actual, expected):
    checks.append(dict(name=name, passed=bool(passed), actual=actual, expected=expected))
    if not passed:
        raise AssertionError(name)

def first_year(f, threshold, origin, end):
    if f(origin) >= threshold - 1e-9:
        return ('AT_OR_BEFORE_ORIGIN', None)
    for y in range(origin + 1, end + 1):
        v = f(y)
        if not math.isfinite(v):
            return ('INVALID_PATH', None)
        if v >= threshold - 1e-9:
            return ('CROSSED', y)
    return ('NO_CROSSING_THROUGH_END', None)

def log_positive(v):
    if not math.isfinite(v) or v <= 0:
        raise ValueError('INVALID_UPSTREAM_PATH')
    return math.log(v)

linear = lambda y: 300.0 + 2.0 * (y - 2000)
deltas = [linear(y)-linear(y-10) for y in range(2010,2021)]
check('ten_elapsed_years', all(v == 20 for v in deltas), deltas, 'all 20 ppm')
check('not_unique_largest_when_tied', deltas[-1] == max(deltas[:-1]), deltas[-1], 20)
slope = (linear(2020)-linear(2010))/10
check('anchored_drift_exact', linear(2020)+slope*7 == linear(2027), linear(2020)+slope*7, 354.0)
x = np.arange(0,31,dtype=float)/10
Xq = np.column_stack([np.ones(len(x)),x,x*x])
qcoef = np.linalg.lstsq(Xq,300+5*x+2*x*x,rcond=None)[0]
check('quadratic_coefficients', np.allclose(qcoef,[300,5,2],atol=1e-9,rtol=0), qcoef.tolist(), [300,5,2])
X = np.column_stack([np.ones(len(x)),x])
C = 300*np.exp(0.02+0.04*x)
ecoef = np.linalg.lstsq(X,np.log(C/300),rcond=None)[0]
check('exponential_log_coefficients', np.allclose(ecoef,[0.02,0.04],atol=1e-12,rtol=0), ecoef.tolist(), [0.02,0.04])
tcoef = np.linalg.lstsq(X,0.1+0.2*x,rcond=None)[0]
check('temperature_time_coefficients', np.allclose(tcoef,[0.1,0.2],atol=1e-12,rtol=0), tcoef.tolist(), [0.1,0.2])
z = np.log(C/300)
Z = np.column_stack([np.ones(len(x)),z])
T = 0.2+1.5*z
acoef = np.linalg.lstsq(Z,T,rcond=None)[0]
check('association_coefficients', np.allclose(acoef,[0.2,1.5],atol=1e-12,rtol=0), acoef.tolist(), [0.2,1.5])
Z2 = np.column_stack([np.ones(len(x)),np.log(C/600)])
coef2 = np.linalg.lstsq(Z2,T,rcond=None)[0]
refdiff=float(np.max(np.abs(Z@acoef-Z2@coef2)))
check('log_reference_invariance', refdiff < 1e-12, refdiff, 'less than 1e-12 degrees C')
for name,func,H,o,e,expected in [
    ('fractional_root_to_integer',linear,305,2000,2010,('CROSSED',2003)),
    ('temperature_integer_crossing',lambda y:0.02*(y-2000),0.05,2000,2010,('CROSSED',2003)),
    ('exact_equality_crossing',linear,304,2000,2010,('CROSSED',2002)),
    ('constant_no_crossing',lambda y:300,305,2000,2010,('NO_CROSSING_THROUGH_END',None)),
    ('already_above_origin',linear,299,2000,2010,('AT_OR_BEFORE_ORIGIN',None)),
    ('nonmonotone_first_passage',lambda y:306-2*(y-2003)**2,305,2000,2010,('CROSSED',2003)),
]:
    actual=first_year(func,H,o,e)
    check(name,actual==expected,actual,expected)
for value in [0,-1,float('nan')]:
    rejected=False
    try:
        log_positive(value)
    except ValueError:
        rejected=True
    check('invalid_log_'+str(value),rejected,'rejected' if rejected else 'accepted','rejected')
result=dict(purpose='synthetic modeler self-check, not independent review or target implementation validation',
            source_data_used=False,python=sys.version,numpy=np.__version__,
            spec_sha256=hashlib.sha256((HERE/'model_spec-r01.md').read_bytes()).hexdigest(),
            script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            checks=checks,passed=all(c['passed'] for c in checks),check_count=len(checks))
(HERE/'toy_checks-r01.json').write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
print(json.dumps(dict(passed=result['passed'],check_count=len(checks),source_data_used=False)))
