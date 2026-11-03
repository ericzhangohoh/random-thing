import fs from 'node:fs/promises';
import { FileBlob, SpreadsheetFile } from '@oai/artifact-tool';
const root = '/Users/ericzhang/Desktop/himcm/HIMCM_Rehearsals/2022_HiMCM_B_2026-11-03';
const wb = await SpreadsheetFile.importXlsx(await FileBlob.load(`${root}/inputs/2022_HiMCM_Data.xlsx`));
const overview = await wb.inspect({kind:'workbook,sheet,table,thread,definedName,drawing', maxChars:18000,tableMaxRows:8,tableMaxCols:10});
await fs.writeFile(`${root}/research/workbook-artifact-overview-r01.ndjson`,overview.ndjson);
console.log(overview.ndjson);
const sheets = [];
for(let i=0;i<2;i++) {
  const s=wb.worksheets.getItemAt(i);
  const range=s.getRange('A1:Z100');
  sheets.push({name:s.name,values:range.values,formulas:range.formulas});
}
await fs.writeFile(`${root}/research/workbook-artifact-allcells-r01.json`,JSON.stringify(sheets,null,2)+'\n');
