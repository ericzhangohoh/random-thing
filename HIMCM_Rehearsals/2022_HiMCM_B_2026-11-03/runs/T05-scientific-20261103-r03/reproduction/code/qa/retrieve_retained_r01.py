"""Actually copy an inventory into a new isolated directory and verify bytes."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def retrieve(project_root, manifest_path, destination):
    root, destination = Path(project_root), Path(destination)
    destination.mkdir(parents=True,exist_ok=False)
    inventory = json.loads(Path(manifest_path).read_text())['retained_artifacts']
    results = []
    for item in inventory:
        if item['retrieval_method'] != 'retained_file':
            raise ValueError('This retrieval checker supports retained_file only')
        source = root/item['retained_path']
        target = destination/item['used_path']
        target.parent.mkdir(parents=True,exist_ok=True)
        shutil.copyfile(source,target)
        actual = sha256(target)
        passed = actual == item['sha256']
        results.append({'path':item['used_path'],'expected_sha256':item['sha256'],'actual_sha256':actual,'pass':passed})
        if not passed:
            raise ValueError(f"Recovered artifact hash mismatch: {item['used_path']}")
    receipt = {'status':'PASS','retrieved_count':len(results),'checks':results,
               'meaning':'Actual isolated byte recovery, not proof of scientific correctness.'}
    (destination/'retrieval-receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps({'status':'PASS','retrieved_count':len(results)}))


if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--project-root',required=True)
    parser.add_argument('--manifest',required=True)
    parser.add_argument('--destination',required=True)
    args=parser.parse_args()
    retrieve(args.project_root,args.manifest,args.destination)
