"""T06 author-only synthetic r02 boundary check; not production validation."""
from pathlib import Path
import hashlib
import json
import math
import sys

HERE=Path(__file__).resolve().parent
TOL=1e-9

def inspect_path(fn, threshold, kind='co2', origin=2021, end=2300):
    values={}; invalid={}
    for year in range(origin,end+1):
        try:
            record=fn(year)
            value=record.get('value')
            co2=value if kind=='co2' else record.get('co2')
            if kind in ('co2','T1'):
                if co2 is None: reason='MISSING_REQUIRED_VALUE'
                elif not math.isfinite(co2): reason='NONFINITE_CO2'
                elif co2<=0: reason='NONPOSITIVE_CO2'
                else: reason=None
            else: reason=None
            if reason is None:
                if value is None: reason='MISSING_REQUIRED_VALUE'
                elif not math.isfinite(value): reason='NONFINITE_TARGET'
            if reason is None: values[year]=value
            else: invalid[year]=reason
        except (ValueError,OverflowError,ArithmeticError,TypeError,AttributeError):
            invalid[year]='EVALUATION_ERROR'
    first_invalid=min(invalid) if invalid else None
    valid_end=end if first_invalid is None else (None if first_invalid==origin else first_invalid-1)
    first=None
    if valid_end is None: status='INVALID_PATH'
    elif values[origin]>=threshold-TOL: status='AT_OR_BEFORE_ORIGIN'
    else:
        first=next((y for y in range(origin+1,valid_end+1) if values[y]>=threshold-TOL),None)
        status='CROSSED' if first is not None else ('INVALID_PATH' if first_invalid is not None else 'NO_CROSSING_THROUGH_2300')
    mono=None if valid_end is None or valid_end==origin else all(values[y]>=values[y-1]-TOL for y in range(origin+1,valid_end+1))
    return dict(status=status,first_year=first,search_domain_valid=not invalid,
        valid_through_year=valid_end,invalid_from_year=first_invalid,
        invalid_reason=invalid[first_invalid] if first_invalid is not None else None,
        monotone_flag=mono,monotonicity_end_year=valid_end,
        value_at_year=values[first] if first is not None else None,
        value_previous_year=values[first-1] if first is not None else None,
        beyond_tested_horizon=(first>2031) if first is not None else None)

base=lambda y:680+2*(y-2021)
plain=lambda y:{'value':base(y)}
cases=[]
def check(name, fn, H, expected, kind='co2'):
    actual=inspect_path(fn,H,kind)
    passed=all(actual[k]==v for k,v in expected.items())
    cases.append(dict(name=name,passed=passed,expected=expected,actual=actual))
    assert passed,name

check('fractional_crossing',plain,685,dict(status='CROSSED',first_year=2024,search_domain_valid=True))
check('exact_crossing',plain,684,dict(status='CROSSED',first_year=2023))
check('crossing_then_nonpositive',lambda y:{'value':-1 if y==2030 else base(y)},685,dict(status='CROSSED',first_year=2024,invalid_from_year=2030,invalid_reason='NONPOSITIVE_CO2',valid_through_year=2029,search_domain_valid=False))
check('crossing_then_nonfinite',lambda y:{'value':float('nan') if y==2030 else base(y)},685,dict(status='CROSSED',first_year=2024,invalid_from_year=2030,invalid_reason='NONFINITE_CO2'))
check('crossing_then_missing',lambda y:{'value':None if y==2030 else base(y)},685,dict(status='CROSSED',first_year=2024,invalid_from_year=2030,invalid_reason='MISSING_REQUIRED_VALUE'))
check('invalid_before_crossing_and_recovery',lambda y:{'value':-1 if y==2023 else base(y)},685,dict(status='INVALID_PATH',first_year=None,invalid_from_year=2023,valid_through_year=2022))
check('invalid_at_apparent_hit',lambda y:{'value':1+0.1*(y-2021),'co2':-1 if y==2024 else 400},1.3,dict(status='INVALID_PATH',first_year=None,invalid_from_year=2024),'T1')
check('invalid_origin',lambda y:{'value':-1 if y==2021 else base(y)},685,dict(status='INVALID_PATH',first_year=None,valid_through_year=None,invalid_from_year=2021))
check('already_above_then_invalid',lambda y:{'value':-1 if y==2030 else 700},685,dict(status='AT_OR_BEFORE_ORIGIN',first_year=None,invalid_from_year=2030,search_domain_valid=False))
check('valid_no_crossing',lambda y:{'value':680},685,dict(status='NO_CROSSING_THROUGH_2300',first_year=None,search_domain_valid=True,valid_through_year=2300,invalid_from_year=None))
check('negative_temperature_valid',lambda y:{'value':-0.1+0.05*(y-2021)},0.05,dict(status='CROSSED',first_year=2024,search_domain_valid=True),'T0')
check('nonmonotone_first_hit',lambda y:{'value':690 if y==2022 else 680},685,dict(status='CROSSED',first_year=2022,monotone_flag=False,search_domain_valid=True))
def evaluation_failure(y):
    if y==2030: raise OverflowError('synthetic overflow')
    return {'value':base(y)}
check('crossing_then_evaluation_error',evaluation_failure,685,dict(status='CROSSED',first_year=2024,invalid_from_year=2030,invalid_reason='EVALUATION_ERROR'))
x=[0,1,3,10]
algebra_error=max(abs((0.2+2*math.log((300*math.exp(0.1+0.03*t))/300))-(0.2+2*0.1+2*0.03*t)) for t in x)
cases.append(dict(name='T1_E_time_linear_identity',passed=algebra_error<1e-12,actual=algebra_error,expected='less than 1e-12'))
assert cases[-1]['passed']
out=dict(purpose='synthetic modeler self-check; not primary implementation validation or independent review',source_data_used=False,python=sys.version,passed=all(c['passed'] for c in cases),check_count=len(cases),checks=cases,hashes={f.name:hashlib.sha256(f.read_bytes()).hexdigest() for f in [HERE/'model_spec-r02.md',HERE/'model_interface-r02.md',Path(__file__)]})
(HERE/'boundary_checks-r02.json').write_text(json.dumps(out,indent=2,allow_nan=False)+'\n')
print(json.dumps(dict(passed=out['passed'],check_count=len(cases),source_data_used=False)))
