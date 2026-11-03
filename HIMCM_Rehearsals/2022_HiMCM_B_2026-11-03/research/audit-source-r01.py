"""Read-only admission audit. No model-ready data are created here."""
from pathlib import Path
import zipfile, json, xml.etree.ElementTree as ET, re
from decimal import Decimal
P=Path(__file__).resolve().parents[1]
N={'s':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
z=zipfile.ZipFile(P/'inputs/2022_HiMCM_Data.xlsx')
ss=[]
if 'xl/sharedStrings.xml' in z.namelist():
    ss=[''.join(n.itertext()) for n in ET.fromstring(z.read('xl/sharedStrings.xml'))]
workbook=ET.fromstring(z.read('xl/workbook.xml'))
sheet_meta=[dict(s.attrib) for s in workbook.findall('s:sheets/s:sheet',N)]
records=[]
for i,meta in enumerate(sheet_meta,1):
    xml=ET.fromstring(z.read(f'xl/worksheets/sheet{i}.xml'))
    cells=[]
    for c in xml.findall('.//s:c',N):
        v=c.find('s:v',N); f=c.find('s:f',N)
        value=v.text if v is not None else None
        if c.get('t')=='s': value=ss[int(value)]
        elif c.get('t')=='inlineStr': value=''.join(c.find('s:is',N).itertext())
        cells.append({'address':c.get('r'),'type':c.get('t','n'),'raw':value,'formula':f.text if f is not None else None,'style':c.get('s')})
    obs={int(re.sub('[A-Z]+','',c['address'])):{} for c in cells if c['raw'] is not None}
    for c in cells:
        if c['raw'] is not None: obs[int(re.sub('[A-Z]+','',c['address']))][re.sub('[0-9]+','',c['address'])]=c['raw']
    rows=[row for n,row in sorted(obs.items()) if n>1]
    years=[int(r['A']) for r in rows]
    vals=[Decimal(r['B']) for r in rows]
    records.append({'sheet':meta['name'],'metadata':meta,'xml_dimension':xml.find('s:dimension',N).get('ref'),'cells':cells,'stored_cell_count':len(cells),'nonempty_cell_count':sum(c['raw'] is not None for c in cells),'data_row_count':len(rows),'year_min':min(years),'year_max':max(years),'missing_years':sorted(set(range(min(years),max(years)+1))-set(years)),'duplicate_year_count':len(years)-len(set(years)),'missing_value_count':sum('B' not in r for r in rows),'value_min':str(min(vals)),'value_max':str(max(vals)),'zero_count':vals.count(Decimal(0)),'formula_count':sum(c['formula'] is not None for c in cells),'hidden_rows':[r.attrib for r in xml.findall('s:sheetData/s:row',N) if r.get('hidden')=='1'],'hidden_columns':[r.attrib for r in xml.findall('s:cols/s:col',N) if r.get('hidden')=='1'],'merged_cells':[r.attrib for r in xml.findall('s:mergeCells/s:mergeCell',N)],'hyperlinks':[r.attrib for r in xml.findall('s:hyperlinks/s:hyperlink',N)]})
note_parts={n:z.read(n).decode('utf-8') for n in z.namelist() if re.search(r'comment|thread|person',n,re.I)}
other_parts=[n for n in z.namelist() if re.search(r'table|drawing|externalLink',n,re.I)]
result={'sheets':records,'annotation_parts':note_parts,'other_object_parts':other_parts,'zip_parts':z.namelist(),'defined_names':[dict(n.attrib,text=n.text) for n in workbook.findall('s:definedNames/s:definedName',N)]}
(P/'research/workbook-xml-audit-r01.json').write_text(json.dumps(result,indent=2)+'\n')
artifact=json.loads((P/'research/workbook-artifact-allcells-r01.json').read_text())
for s,a in zip(records,artifact):
    assert s['sheet']==a['name']
    for c in s['cells']:
        if c['raw'] is None: continue
        col=ord(re.sub('[0-9]+','',c['address']))-ord('A'); row=int(re.sub('[A-Z]+','',c['address']))-1
        v=a['values'][row][col]
        assert str(v)==c['raw'] or (c['type']=='n' and abs(Decimal(str(v))-Decimal(c['raw']))<Decimal('1e-10')),(s['sheet'],c,v)
    print(s['sheet'], {k:v for k,v in s.items() if k not in ['cells','metadata']})
print('annotations',note_parts,'other_objects',other_parts)
print('Artifact Tool / OOXML value agreement: all populated cells match at 1e-10 absolute tolerance; string values exact')
print('All populated cells:')
for s in records:
    print(s['sheet'])
    print('\n'.join(c['address']+' '+str(c['raw']) for c in s['cells'] if c['raw'] is not None))
