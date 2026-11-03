"""Author consistency check of retained adversarial outputs; no fitting or QA writes."""
from pathlib import Path
import hashlib,json
import numpy as np
p=Path(__file__).resolve().parents[1]
d=json.loads((p/'qa/adversarial_validation/development_probe_r01.json').read_text())
a=json.loads((p/'qa/adversarial_validation/assessment_r01.json').read_text())
s=json.loads((p/'qa/adversarial_structure/probe-results-r01.json').read_text())
checks={}
checks['A01_final_mae_matches_errors']=all(abs(v['MAE']-float(np.mean(np.abs(v['errors']))))<1e-12 for v in a['final'].values())
checks['A01_miss_lists_match_errors_radii']=all(v['miss_horizons']==(np.flatnonzero(np.abs(v['errors'])>np.array(v['radii']))+1).tolist() for v in a['final'].values())
checks['A01_D_all_final_errors_negative']=all(v<0 for v in a['final']['D']['errors'])
checks['A01_Q_final_MAE_lower_than_D']=a['final']['Q']['MAE']<a['final']['D']['MAE']
checks['A02_scores_match_stored_rows']=all(abs(v['mae']-np.mean([abs(r['error']) for r in s['rows'] if r['model']==m]))<1e-12 for m,v in s['metrics'].items())
origins=[1981,1986,1991,1996,2001]
winners=[min(['D','E','Q'],key=lambda m:d['origin_mae'][m][i]) for i in range(5)]
checks['A01_Q_wins_three_origins']=winners.count('Q')==3
files=[p/'qa/adversarial_validation/development_probe_r01.json',p/'qa/adversarial_validation/assessment_r01.json',p/'qa/adversarial_structure/probe-results-r01.json']
summary={'evidence_kind':'author consistency check of existing independent adversarial probe outputs; not primary-run validation','no_refitting':True,'checks':{k:bool(v) for k,v in checks.items()},'all_passed':all(checks.values()),'origin_winners':dict(zip(map(str,origins),winners)),'leave_one_origin_out_winners':d['leave_origin_out_winners'],'development_selected':d['selected'],'final_CO2_MAE':{k:a['final'][k]['MAE'] for k in ['D','Q','E']},'T1_D_miss_horizons':a['final']['T1-D']['miss_horizons'],'inputs':{str(f.relative_to(p)):hashlib.sha256(f.read_bytes()).hexdigest() for f in files},'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(p/'models/adversarial_evidence_check-r02.json').write_text(json.dumps(summary,indent=2)+'\n')
assert summary['all_passed']
print(json.dumps(dict(all_passed=summary['all_passed'],check_count=len(checks),no_refitting=True)))
