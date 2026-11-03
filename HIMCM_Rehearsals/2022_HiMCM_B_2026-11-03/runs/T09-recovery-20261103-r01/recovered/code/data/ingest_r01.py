"""Frozen supplied-workbook ingestion. No fitting, imputation, or live sources."""
import argparse
import csv
from decimal import Decimal
import hashlib
import json
import math
from pathlib import Path
import openpyxl


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def normalize_rows(rows, expected_years, label):
    """Validate keys independently of row position; retain supplied hundredths."""
    result = {}
    provenance = []
    for cell_row, year, value in rows:
        if isinstance(year, bool) or not isinstance(year, (int, float)) or not math.isfinite(year) or int(year) != year:
            raise ValueError(f"{label}: invalid integer year at row {cell_row}")
        year = int(year)
        if year in result:
            raise ValueError(f"{label}: duplicate year {year}")
        if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
            raise ValueError(f"{label}: non-finite or nonnumeric value for {year}")
        supplied = Decimal(str(value)).quantize(Decimal('0.01'))
        error = abs(float(supplied) - float(value))
        if error > 1e-10:
            raise ValueError(f"{label}: value has unsupported extra precision for {year}")
        result[year] = supplied
        provenance.append({'sheet': label, 'source_row': cell_row, 'year': year,
                           'reader_value_repr': repr(value), 'supplied_hundredths': str(supplied),
                           'serialization_delta': error})
    if set(result) != set(expected_years):
        raise ValueError(f"{label}: year coverage mismatch; missing={sorted(set(expected_years)-set(result))}, unexpected={sorted(set(result)-set(expected_years))}")
    return dict(sorted(result.items())), provenance


def keyed_join(co2, temperature):
    return [(year, co2[year], temperature[year]) for year in sorted(set(co2) & set(temperature))]


def parse_workbook(path, config):
    observed_hash = sha256(path)
    if observed_hash != config['input_sha256']:
        raise ValueError('Input SHA-256 mismatch: frozen source identity failed')
    book = openpyxl.load_workbook(path, read_only=True, data_only=False)
    if book.sheetnames != [s['sheet'] for s in config['series']]:
        raise ValueError('Unexpected workbook sheets/order')
    parsed, provenance = {}, []
    try:
        for spec in config['series']:
            sheet = book[spec['sheet']]
            if [sheet.cell(1, i).value for i in (1, 2)] != spec['headers']:
                raise ValueError(f"{spec['sheet']}: header mismatch")
            expected_years = list(range(spec['first_year'], spec['last_year'] + 1))
            last_row = 1 + len(expected_years)
            for row in sheet.iter_rows():
                for cell in row:
                    if cell.value is not None and (cell.column > 2 or cell.row > last_row):
                        raise ValueError(f"Unexpected populated cell: {spec['sheet']}!{cell.coordinate}")
                    if cell.data_type == 'f':
                        raise ValueError(f"Formula forbidden: {spec['sheet']}!{cell.coordinate}")
            rows = [(r, sheet.cell(r, 1).value, sheet.cell(r, 2).value) for r in range(2, last_row + 1)]
            parsed[spec['field']], source_rows = normalize_rows(rows, expected_years, spec['sheet'])
            provenance.extend(source_rows)
    finally:
        book.close()
    if sha256(path) != observed_hash:
        raise ValueError('Original workbook changed during reading')
    return parsed, provenance


def write_csv(path, headers, rows):
    with Path(path).open('x', newline='', encoding='utf-8') as handle:
        writer = csv.writer(handle, lineterminator='\n')
        writer.writerow(headers)
        writer.writerows(rows)


def ingest(input_path, config_path, output_dir):
    config = json.loads(Path(config_path).read_text())
    parsed, provenance = parse_workbook(input_path, config)
    co2, temp = parsed['co2_ppm'], parsed['temp_anomaly_c']
    joined = keyed_join(co2, temp)
    if [r[0] for r in joined] != list(range(1959, 2022)):
        raise ValueError('Join coverage mismatch')
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=False)
    write_csv(output_dir/'co2-r01.csv', ['year', 'co2_ppm'], co2.items())
    write_csv(output_dir/'temperature-r01.csv', ['year', 'temp_anomaly_c'], temp.items())
    write_csv(output_dir/'joined-r01.csv', ['year', 'co2_ppm', 'temp_anomaly_c'], joined)
    checks = {
        'status': 'PASS', 'source_sha256': sha256(input_path), 'cutoff': 2021,
        'co2': {'rows': len(co2), 'year_range': [min(co2), max(co2)], 'min_ppm': str(min(co2.values())), 'max_ppm': str(max(co2.values()))},
        'temperature': {'rows': len(temp), 'year_range': [min(temp), max(temp)], 'min_anomaly_c': str(min(temp.values())), 'max_anomaly_c': str(max(temp.values())), 'baseline': '1951-1980'},
        'join': {'rows': len(joined), 'year_range': [joined[0][0], joined[-1][0]], 'co2_only_years': sorted(set(co2)-set(temp)), 'temperature_only_years': sorted(set(temp)-set(co2)), 'method': 'inner join by integer year'},
        'missing_values': 0, 'duplicate_years': 0, 'formula_cells': 0,
        'max_serialization_delta': max(r['serialization_delta'] for r in provenance),
        'all_127_values_preserved_at_supplied_precision': True,
        'original_workbook_unchanged': True,
        'checks_performed': ['expected source hash', 'named sheets and headers', 'no populated out-of-contract cells', 'integer unique complete year keys', 'finite numeric observations', 'hundredth precision within 1e-10', '63-row year join', 'original source hash after reading'],
        'scope': 'Pre-G2 ingestion only; no model fits or scientific acceptance.'
    }
    (output_dir/'ingestion-checks-r01.json').write_text(json.dumps(checks, indent=2)+'\n')
    (output_dir/'source-values-r01.json').write_text(json.dumps(provenance, indent=2)+'\n')
    print(json.dumps(checks, indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True)
    parser.add_argument('--config', required=True)
    parser.add_argument('--output-dir', required=True)
    args = parser.parse_args()
    ingest(args.input, args.config, args.output_dir)
