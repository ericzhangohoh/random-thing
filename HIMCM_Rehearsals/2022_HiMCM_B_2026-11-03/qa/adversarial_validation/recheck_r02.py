from pathlib import Path
import hashlib,json,re
P=Path(__file__).resolve().parents[2]; O=Path(__file__).resolve().parent
handoff=(P/'handoffs/T06/modeler-r01.md').read_text()
pairs=re.findall(r'\| `(models/[^`]+)` \| `([0-9a-f]{64})` \|',handoff)
checks={}; targets={}
for name,expected in pairs:
 actual=hashlib.sha256((P/name).read_bytes()).hexdigest(); targets[name]=actual; checks['handoff_hash:'+name]=actual==expected
old=json.loads((O/'development_probe_r01.json').read_text())['hashes']
checks['original_source_and_model_hashes_preserved']=all(hashlib.sha256((P/name).read_bytes()).hexdigest()==sha for name,sha in old.items())
a=(P/'models/model_spec-r01.md').read_text(); b=(P/'models/model_spec-r02.md').read_text()
def part(s,title,end): return s.split(title,1)[1].split(end,1)[0]
for title,end in [('## M00','## M03'),('## M04','## M05'),('## M07','## Budget')]: checks['unchanged:'+title]=part(a,title,end)==part(b,title,end)
# Complete diff inspected manually; these focused strings ensure retained selection semantics.
for s in ['Fixed rolling origins: 1981, 1986, 1991, 1996, 2001','Select CO2 by minimum development MAE in ppm','fixed order D,E,Q','compare T0 with T1 driven by that selected rule','ties within 1e-12 to T0']:
 checks['retained:'+s]=s in a and s in b
for name in ['models/assumptions-r01.md','handoffs/T06/modeler-r01.md']:
 targets[name]=hashlib.sha256((P/name).read_bytes()).hexdigest()
result={'purpose':'A01 repair recheck; no fitting or final-score recomputation','checks':checks,'passed':all(checks.values()),'targets':targets}
assert result['passed']
(O/'recheck-results-r02.json').write_text(json.dumps(result,indent=2)+'\n'); print(json.dumps({'passed':result['passed'],'check_count':len(checks),'target_count':len(targets)}))
