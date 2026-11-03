from pathlib import Path
import json,csv,hashlib,statistics
from datetime import datetime
P=Path(__file__).resolve().parents[2];Q=Path(__file__).resolve().parent;R=P/'runs/T05-scientific-20261103-r02';O=R/'outputs'
rr=json.loads((Q/'independent-temporal-predictions.json').read_text());checks=[]
def check(n,v):checks.append({'check':n,'passed':bool(v)});assert v,n
def rows(n):return list(csv.DictReader((O/n).open()))
def score(m,phase='development',origin=None,omitted=None):return statistics.mean(abs(r['error']) for r in rr if r['model']==m and r['phase']==phase and (origin is None or r['origin']==origin) and (omitted is None or r['origin']!=omitted))
ids=['D','E','Q'];origins=[1981,1986,1991,1996,2001];winners={o:min(ids,key=lambda m:score(m,origin=o)) for o in origins}
for r in rows('rank_stability.csv'):
 if r['diagnostic']=='per_origin_win_count':check('win_count_'+r['model_id'],int(r['win_count'])==list(winners.values()).count(r['model_id']));continue
 kw={'origin':int(r['origin_year'])} if r['diagnostic']=='per_origin' else {'omitted':int(r['omitted_origin'])};s={m:score(m,**kw) for m in ids}
 check('rankscore',abs(s[r['model_id']]-float(r['mae_ppm']))<1e-8);check('rankwinner',min(ids,key=s.get)==r['diagnostic_winner']);check('post_exposure_label',r['introduced_after_assessment']=='True' and r['selection_changed']=='False')
for r in rows('comparison_ranks.csv'):
 candidates=ids if r['target']=='co2' else ['T0','T1-D','T1-Q','T1-E'];s={m:score(m,r['phase']) for m in candidates}
 check('comparisonwinner',min(candidates,key=s.get)==r['best_declared_comparator_id']);check('comparisonrank',int(r['rank_among_declared_comparators'])==1+sum(v<s[r['model_id']]-1e-12 for v in s.values()))
sel=json.loads((O/'selection_frozen.json').read_text());fin=json.loads((O/'final_assessment_receipt.json').read_text());prod=json.loads((O/'production_receipt.json').read_text())
sha=lambda f:hashlib.sha256(f.read_bytes()).hexdigest()
check('ordered_timestamps',datetime.fromisoformat(sel['frozen_at'])<datetime.fromisoformat(fin['started_at'])<=datetime.fromisoformat(fin['finished_at'])<datetime.fromisoformat(prod['finished_at']))
check('loaded_selection_identity',sha(O/'selection_frozen.json')==fin['loaded_selection_sha256']==prod['loaded_selection_sha256'])
check('loaded_final_identity',sha(O/'final_assessment_receipt.json')==prod['final_assessment_sha256'])
check('exposure_not_hidden',sel['project_final_scores_previously_exposed_by_A01'] is True and sel['selection_rule_changed_after_exposure'] is False and sel['final_targets_used_for_selection'] is False)
release=json.loads((P/'control/accepted-inputs-g2-r02.json').read_text());check('all_release_bytes_unchanged',all(sha(P/f)==h for f,h in release['sha256'].items()))
for k,f in [('input_sha256','data/processed/joined-r01.csv'),('spec_sha256','models/model_spec-r02.md'),('code_sha256','code/experiments/analysis_r02.py'),('model_code_sha256','code/modeling/climate_models_r02.py'),('configuration_sha256','config.json')]:check('selection_'+k,sha(R/'reproduction'/f)==sel[k])
a=json.loads((P/'qa/adversarial_validation/assessment_r01.json').read_text());check('A01_final_reconciled',all(abs(score(m,'final')-v['MAE'])<1e-8 for m,v in a['final'].items()))
summary={'checks':checks,'all_passed':all(x['passed'] for x in checks),'origin_winners':winners,'leave_one_origin_out_winners':{o:min(ids,key=lambda m:score(m,omitted=o)) for o in origins},'local_order':'verified from actual receipt identities/timestamps and source inspection; does not prove global unseen scores','production_model_imported':False}
(Q/'trace-rank-checks.json').write_text(json.dumps(summary,indent=2)+'\n');print('Passed',len(checks),'trace/rank/evidence checks')
