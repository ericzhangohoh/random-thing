"""Small audit-only recovery-contract probe; not a production validator or model run."""
from pathlib import Path
import hashlib
import json
import shutil

BASE = Path(__file__).resolve().parent / 'retention_probe_r01'
BASE.mkdir(exist_ok=False)

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def retrieve(entry, target):
    if entry.get('retrieval_method') != 'retained_file' or not entry.get('retained_path'):
        return {'accepted': False, 'reason': 'No retained-file retrieval location'}
    source = BASE / entry['retained_path']
    if not source.is_file():
        return {'accepted': False, 'reason': 'Retained bytes unavailable'}
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, target)
    actual = sha(target)
    return {'accepted': actual == entry['sha256'], 'retrieved_sha256': actual,
            'reason': 'Hash match' if actual == entry['sha256'] else 'Hash mismatch'}

working = BASE / 'working/source.py'
working.parent.mkdir()
working.write_text("VERSION = 'A'\n")
original_hash = sha(working)
retained = BASE / 'closed_r01/reproduction/source.py'
retained.parent.mkdir(parents=True)
shutil.copyfile(working, retained)
entry = {'kind': 'code', 'used_path': 'working/source.py', 'sha256': original_hash,
         'retrieval_method': 'retained_file',
         'retained_path': 'closed_r01/reproduction/source.py'}
(BASE / 'inventory.json').write_text(json.dumps([entry], indent=2) + '\n')
working.write_text("VERSION = 'B'\n")
working_b_hash = sha(working)
positive = retrieve(entry, BASE / 'recovered/source.py')
hash_only = retrieve({'kind': 'code', 'used_path': 'working/source.py', 'sha256': original_hash},
                     BASE / 'rejected_hash_only/source.py')
missing = retrieve({**entry, 'retained_path': 'nonexistent/source.py'},
                   BASE / 'rejected_missing/source.py')
wrong_bytes = retrieve({**entry, 'retained_path': 'working/source.py'},
                       BASE / 'rejected_wrong_bytes/source.py')
assert positive['accepted']
assert not hash_only['accepted'] and not missing['accepted'] and not wrong_bytes['accepted']
assert sha(working) == working_b_hash != original_hash
assert sha(retained) == original_hash
receipt = {'scope': 'Executed file retention/retrieval and SHA-256 checks only; no modeling or live agents',
           'original_A_sha256': original_hash, 'working_B_sha256': working_b_hash,
           'retained_A_recovered': positive, 'hash_only_rejected': hash_only,
           'missing_snapshot_rejected': missing, 'wrong_bytes_rejected': wrong_bytes,
           'working_B_unchanged_by_recovery': True, 'retained_A_unchanged': True,
           'status': 'PASSED'}
(BASE / 'receipt.json').write_text(json.dumps(receipt, indent=2) + '\n')
print(json.dumps(receipt, indent=2))
