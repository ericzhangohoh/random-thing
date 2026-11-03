from pathlib import Path
import json, hashlib, zipfile, xml.etree.ElementTree as E
from decimal import Decimal
P=Path(__file__).resolve().parents[2]
Q=Path(__file__).resolve().parent
ns={'s':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
with zipfile.ZipFile(P/'inputs/2022_HiMCM_Data.xlsx') as z:
    data=[]
    for i in (1,2):
        root=E.fromstring(z.read(f'xl/worksheets/sheet{i}.xml'))
        rows=[]
        for row in root.findall('s:sheetData/s:row',ns)[1:]:
            vals={c.attrib['r'].rstrip('0123456789'):c.findtext('s:v',namespaces=ns) for c in row.findall('s:c',ns)}
            if vals.get('A') is not None:
                rows.append((int(Decimal(vals['A'])),Decimal(vals['B']).quantize(Decimal('.01'))))
        data.append(dict(rows))
        assert len(rows)==len(data[-1])
c,t=data
assert sorted(c)==list(range(1959,2022))
assert sorted(t)==list(range(1958,2022))
windows=[{'start':y-10,'end':y,'change_ppm':str(c[y]-c[y-10])} for y in range(1969,2005)]
prior=max(windows[:-1],key=lambda x:Decimal(x['change_ppm']))
manifest=json.loads((P/'research/artifact-hashes-r01.json').read_text())
checks=[]
for a in manifest['artifacts']:
    b=(P/a['path']).read_bytes()
    checks.append({'path':a['path'],'hash_match':hashlib.sha256(b).hexdigest()==a['sha256'],'size_match':len(b)==a['bytes']})
assert all(x['hash_match'] and x['size_match'] for x in checks)
result={'independent_parser':'stdlib ZIP/OOXML, no producer code imported','co2_rows':len(c),'temperature_rows':len(t),'joined_rows':len(c.keys()&t.keys()),'windows_through_2004':windows,'prior_max':prior,'2004':windows[-1],'producer_inventory_checks':checks}
(Q/'independent-data-checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ('windows_through_2004','producer_inventory_checks')},indent=2))
