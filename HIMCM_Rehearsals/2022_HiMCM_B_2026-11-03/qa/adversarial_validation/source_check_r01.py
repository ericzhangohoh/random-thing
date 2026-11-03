from pathlib import Path
import zipfile,xml.etree.ElementTree as ET,csv,json,hashlib
P=Path(__file__).resolve().parents[2]; O=Path(__file__).resolve().parent
ns={'s':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
with zipfile.ZipFile(P/'inputs/2022_HiMCM_Data.xlsx') as z:
 vals=[]
 for name in ['xl/worksheets/sheet1.xml','xl/worksheets/sheet2.xml']:
  root=ET.fromstring(z.read(name)); d={}
  for r in root.findall('.//s:sheetData/s:row',ns):
   cells={a.attrib['r'][0]:a.find('s:v',ns) for a in r.findall('s:c',ns)}
   if int(r.attrib['r'])>1: d[int(float(cells['A'].text))]=float(cells['B'].text)
  vals.append(d)
 rows=list(csv.DictReader((P/'data/processed/joined-r01.csv').open()))
 checks={'co2_rows':len(vals[0]),'temp_rows':len(vals[1]),'joined_rows':len(rows),'max_abs_source_difference':max(max(abs(float(r['co2_ppm'])-vals[0][int(r['year'])]),abs(float(r['temp_anomaly_c'])-vals[1][int(r['year'])])) for r in rows)}
 assert checks['max_abs_source_difference']<1e-10 and len(rows)==63
 (O/'source_check_r01.json').write_text(json.dumps(checks,indent=2)+'\n'); print(checks)
