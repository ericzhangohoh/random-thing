"""Behavior checks with known values and counterexamples to positional joining."""
import importlib.util
from pathlib import Path
import sys
import unittest
from decimal import Decimal

module_path = Path(__file__).resolve().parents[1]/'data'/'ingest_r01.py'
spec = importlib.util.spec_from_file_location('ingest', module_path)
ingest = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ingest)


class IngestionChecks(unittest.TestCase):
    def test_permuted_join_and_extra_temperature_year(self):
        co2, _ = ingest.normalize_rows([(2, 1960, 316.91), (3, 1959, 315.98)], [1959,1960], 'co2')
        temp, _ = ingest.normalize_rows([(2, 1958, 0.06), (3,1960,-0.03), (4,1959,0.03)], [1958,1959,1960], 'temperature')
        self.assertEqual(ingest.keyed_join(co2,temp), [(1959,Decimal('315.98'),Decimal('0.03')),(1960,Decimal('316.91'),Decimal('-0.03'))])

    def test_negative_and_zero_are_valid(self):
        values, _ = ingest.normalize_rows([(2,1959,-0.20),(3,1960,0)], [1959,1960], 'temperature')
        self.assertEqual(values, {1959:Decimal('-0.20'),1960:Decimal('0.00')})

    def test_binary_serialization_tail_is_not_extra_precision(self):
        values, _ = ingest.normalize_rows([(2,1960,316.91000000000003)], [1960], 'co2')
        self.assertEqual(values[1960], Decimal('316.91'))

    def test_rejects_duplicate_year(self):
        with self.assertRaisesRegex(ValueError, 'duplicate'):
            ingest.normalize_rows([(2,1959,315.98),(3,1959,316.91)], [1959,1960], 'co2')

    def test_rejects_missing_or_future_year(self):
        for rows in [[(2,1959,315.98)], [(2,1959,315.98),(3,2022,420)]]:
            with self.assertRaisesRegex(ValueError, 'coverage'):
                ingest.normalize_rows(rows, [1959,1960], 'co2')

    def test_rejects_invalid_value(self):
        for value in [None, '315.98', float('nan'), float('inf'), True]:
            with self.subTest(value=value), self.assertRaisesRegex(ValueError, 'value'):
                ingest.normalize_rows([(2,1959,value)], [1959], 'co2')

    def test_rejects_fractional_or_boolean_year(self):
        for year in [1959.5,True,None]:
            with self.subTest(year=year), self.assertRaisesRegex(ValueError, 'integer year'):
                ingest.normalize_rows([(2,year,315.98)], [1959], 'co2')

    def test_rejects_unsupported_precision(self):
        with self.assertRaisesRegex(ValueError,'precision'):
            ingest.normalize_rows([(2,1959,315.981)], [1959], 'co2')

    def test_empty_expected_sample_has_no_spurious_rows(self):
        values, provenance = ingest.normalize_rows([], [], 'empty')
        self.assertEqual(values,{})
        self.assertEqual(provenance,[])
        self.assertEqual(ingest.keyed_join(values,{1959:Decimal('0.03')}),[])


if __name__ == '__main__':
    unittest.main(verbosity=2)
