from pathlib import Path
import ast,math,json,itertools,hashlib,difflib
P=Path(__file__).resolve().parents[2]; Q=Path(__file__).resolve().parent
src=(P/'models/boundary_selfcheck-r02.py').read_text()
node=next(n for n in ast.parse(src).body if isinstance(n,ast.FunctionDef) and n.name=='inspect_path')
# Execute only the inspected pure author helper; do not execute its top-level writes/tests.
g={'math':math,'TOL':1e-9};exec(compile(ast.Module(body=[node],type_ignores=[]),'<isolated author helper>','exec'),g)
count=0
for kind in ['co2','T0','T1']:
 for seq in itertools.product([None,-1.,0.,1.,2.],repeat=4):
  valid=[v is not None and (kind=='T0' or v>0) for v in seq]
  stop=next((i for i,v in enumerate(valid) if not v),4)
  vals=list(seq[:stop]);hit=next((i for i,v in enumerate(vals) if v>=1.5),None)
  if stop==0: status='INVALID_PATH'
  elif hit==0: status='AT_OR_BEFORE_ORIGIN'
  elif hit is not None: status='CROSSED'
  elif stop<4: status='INVALID_PATH'
  else: status='NO_CROSSING_THROUGH_2300'
  expected={'status':status,'first_year':2021+hit if status=='CROSSED' else None,'search_domain_valid':stop==4,'valid_through_year':None if stop==0 else 2020+stop,'invalid_from_year':None if stop==4 else 2021+stop,'monotone_flag':None if stop<2 else all(a<=b for a,b in zip(vals,vals[1:])),'monotonicity_end_year':None if stop==0 else 2020+stop}
  def f(y):
   v=seq[y-2021]
   return {'value':v,'co2':v} if kind=='T1' else {'value':v}
  actual=g['inspect_path'](f,1.5,kind,2021,2024)
  assert all(actual[k]==v for k,v in expected.items()),(kind,seq,expected,actual)
  count+=1
preserved=[]
for a in json.loads((P/'models/artifact-hashes-r01.json').read_text())['artifacts']:
 data=(P/a['path']).read_bytes();old=P/'qa/framing-r01/targets/project'/a['path']
 assert hashlib.sha256(data).hexdigest()==a['sha256'] and data==old.read_bytes()
 preserved.append(a['path'])
a=(P/'models/model_spec-r01.md').read_text();b=(P/'models/model_spec-r02.md').read_text()
for section,next_section in [('M00','M01'),('M01','M02'),('M02','M03'),('M04','M05')]:
 def part(text):return text[text.index('## '+section):text.index('## '+next_section)]
 assert part(a)==part(b),section
for name in ['framing','model_spec','model_decision','model_interface','experiment_plan']:
 old=(P/f'models/{name}-r01.md').read_text();new=(P/f'models/{name}-r02.md').read_text()
 (Q/f'{name}-diff.txt').write_text(''.join(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile=name+'-r01',tofile=name+'-r02')))
result={'scope':'independent finite-state semantic oracle against inspected pure author helper; not production validation','synthetic_cases':count,'all_passed':True,'original_T04_artifacts_byte_preserved':preserved,'unchanged_sections':['M00','M01','M02','M04'],'source_data_fits':False,'helper_sha256':hashlib.sha256(src.encode()).hexdigest()}
(Q/'contract-checks.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
