"""Audit supplied data, definitions and transcription without producing model inputs."""
from pathlib import Path
from decimal import Decimal
from pypdf import PdfReader
import json,re
P=Path(__file__).resolve().parents[1]
w=json.loads((P/'research/workbook-artifact-allcells-r01.json').read_text())
source=PdfReader(P/'inputs/2022_HiMCM_Problem_B.pdf')
out={'checks':[], 'numeric_interpretation':'Supplied hundredth-unit numbers; Decimal arithmetic on displayed precision.'}
ds=[]
for idx in range(2):
    x={int(r[0]):Decimal(str(r[1])).quantize(Decimal('.01')) for r in w[idx]['values'][1:] if r[0] is not None}
    text=source.pages[idx+2].extract_text()
    printed={}
    for line in text.splitlines():
        if re.match(r'^\d{4}\s',line.strip()):
            pairs=re.findall(r'(\d{4})\s+(-?\d+(?:\.\d+)?)',line)
            for yr,v in pairs: printed[int(yr)]=Decimal(v)
    assert printed==x,(idx,printed,x)
    out['checks'].append({'check':'All PDF table pairs match workbook', 'sheet':w[idx]['name'],'observations_compared':len(x),'pass':True})
    ds.append(x)
c,t=ds
growth=[{'start':y-10,'end':y,'increase_ppm':str(c[y]-c[y-10]),'average_growth_ppm_per_year':str((c[y]-c[y-10])/10)} for y in c if y-10 in c and y<=2004]
best=max(growth[:-1],key=lambda r:Decimal(r['increase_ppm']))
out.update({'join':{'overlap_years':[min(c),max(c)],'overlap_count':len(set(c)&set(t)),'temperature_only_years':sorted(set(t)-set(c)),'co2_only_years':sorted(set(c)-set(t))},'ten_year_definition':'C(y)-C(y-10); ten elapsed years, eleven annual endpoints; compare endings 1969–2003 against2004','ten_year_windows_through_2004':growth,'2004_window':growth[-1],'largest_prior_window':best,'2004_strictly_greater_than_all_prior':Decimal(growth[-1]['increase_ppm'])>Decimal(best['increase_ppm']),'gap_2004_minus_prior_max_ppm':str(Decimal(growth[-1]['increase_ppm'])-Decimal(best['increase_ppm']))})
for name,arr in [('CO2',c),('temperature',t)]:
    d=[arr[y]-arr[y-1] for y in arr if y-1 in arr]
    out[name+'_annual_change_range']={'min':str(min(d)),'max':str(max(d))}
ann=P/'data/raw/noaa-annual-definition-20261103.txt'
if ann.exists():
    current={int(f[0]):Decimal(f[1]) for line in ann.read_text().splitlines() if (f:=line.split()) and not line.startswith('#')}
    out['current_noaa_reference_only_differences']=[{'year':y,'supplied':str(v),'current_reference':str(current[y]),'supplied_minus_reference':str(v-current[y])} for y,v in c.items() if current[y]!=v]
    assert all(y<=2021 for y in c)
    out['current_noaa_reference_note']='These are revision differences only. Supplied2022 archive remains the sole modeling source.'
(P/'research/data-checks-r01.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='ten_year_windows_through_2004'},indent=2))
