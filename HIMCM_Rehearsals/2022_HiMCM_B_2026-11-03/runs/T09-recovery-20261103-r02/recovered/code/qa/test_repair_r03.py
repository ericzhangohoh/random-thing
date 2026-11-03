"""Executed A03 regression probes using synthetic data, before historical fits."""
import contextlib,csv,io,json,sys,tempfile,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'experiments'))
import analysis_r02 as before
import analysis_r03 as after
import numpy as np


def object_fixture(module,directory):
    obj=module.Analysis.__new__(module.Analysis)
    obj.out=Path(directory);obj.out.mkdir(parents=True,exist_ok=True)
    years=np.arange(1959,2022);co2=300+2*(years-1959)
    obj.data={'year':years,'co2_ppm':co2,'temp_anomaly_c':-.1+3*np.log(co2/300)};obj.cref=300.
    obj.config={'run_id':'T05-synthetic-repair','development_origins':[1981,1986,1991,1996,2001]}
    obj.identity={'synthetic_identity':'same-frozen-fixture'};obj.trace={'run_id':obj.config['run_id'],'data_sha256':'synthetic','spec_sha256':'unchanged-r02'}
    with contextlib.redirect_stdout(io.StringIO()):obj.development()
    return obj


def read_json(path):return json.loads(Path(path).read_text())
def replace_json(path,value):Path(path).write_text(json.dumps(value,allow_nan=False)+'\n')
def table(path):
    with Path(path).open() as f:return list(csv.DictReader(f))


class RepairChecks(unittest.TestCase):
    def test_f01_ids_only_before_accepts_after_rejects_before_writes(self):
        for module,reject in [(before,False),(after,True)]:
            with self.subTest(version=module.__name__),tempfile.TemporaryDirectory() as directory:
                obj=object_fixture(module,directory);path=obj.out/'selection_frozen.json';receipt=read_json(path)
                self.assertEqual((receipt['selected_co2_id'],receipt['selected_temperature_id']),('D','T1-D'))
                hashes={name:module.sha(obj.out/name) for name in ['development_forecasts.csv','development_metrics.csv']}
                receipt.update(selected_co2_id='Q',selected_temperature_id='T1-Q');replace_json(path,receipt)
                if reject:
                    with self.assertRaisesRegex(ValueError,'Frozen selection semantic mismatch'):obj.final()
                    self.assertFalse(list(obj.out.glob('final_*')))
                else:
                    with contextlib.redirect_stdout(io.StringIO()):obj.final()
                    result=read_json(obj.out/'final_assessment_receipt.json')
                    self.assertEqual(result['status'],'COMPLETED');self.assertFalse(result['selection_changed'])
                self.assertEqual(hashes,{name:module.sha(obj.out/name) for name in hashes})

    def test_f01_independent_receipt_field_tampers_rejected(self):
        mutations={
            'co2_id':lambda r:r.update(selected_co2_id='E'),
            'temperature_id':lambda r:r.update(selected_temperature_id='T1-Q'),
            'sequential_pair':lambda r:r.update(temperature_selection_candidates=['T0','T1-Q']),
            'eligible_ids':lambda r:r.update(eligible_ids=['D','T0']),
            'score':lambda r:r['development_mae'].update(D=999.),
            'candidate_set':lambda r:r.update(co2_candidates=['D','Q']),
            'temperature_set':lambda r:r.update(temperature_comparators=['T0','T1-D']),
            'tie_order':lambda r:r['selection_rule'].update(co2_tie_order=['Q','E','D']),
            'temperature_tie':lambda r:r['selection_rule'].update(temperature_tie_order=['T1-D','T0']),
            'tie_tolerance':lambda r:r['selection_rule'].update(absolute_tie_tolerance=.1),
            'score_rule':lambda r:r['selection_rule'].update(score='final_mae'),
            'horizons':lambda r:r.update(horizons=[1]),
            'origins':lambda r:r.update(development_origins=[2001]),
            'final_exposure':lambda r:r.update(final_targets_used_for_selection=True),
        }
        for name,mutate in mutations.items():
            with self.subTest(field=name),tempfile.TemporaryDirectory() as directory:
                obj=object_fixture(after,directory);path=obj.out/'selection_frozen.json';receipt=read_json(path);mutate(receipt);replace_json(path,receipt)
                with self.assertRaisesRegex(ValueError,'Frozen selection semantic mismatch'):obj.final()
                self.assertFalse(list(obj.out.glob('final_*')))

    def test_f01_changed_metrics_with_rehashed_receipt_still_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            obj=object_fixture(after,directory);path=obj.out/'development_metrics.csv';rows=table(path)
            row=next(r for r in rows if r['model_id']=='D' and r['grouping']=='overall');row['mae']='999'
            with path.open('w',newline='') as f:
                w=csv.DictWriter(f,fieldnames=rows[0].keys(),lineterminator='\n');w.writeheader();w.writerows(rows)
            frozen=obj.out/'selection_frozen.json';receipt=read_json(frozen);receipt['development_metrics_sha256']=after.sha(path);receipt['development_mae']['D']=999.;replace_json(frozen,receipt)
            with self.assertRaisesRegex(ValueError,'Development metrics disagree with forecasts'):obj.final()
            self.assertFalse(list(obj.out.glob('final_*')))

    def test_f01_production_also_rejects_semantic_tamper_before_writes(self):
        with tempfile.TemporaryDirectory() as directory:
            obj=object_fixture(after,directory)
            with contextlib.redirect_stdout(io.StringIO()):obj.final()
            path=obj.out/'selection_frozen.json';receipt=read_json(path);receipt['eligible_ids']=[];replace_json(path,receipt)
            with self.assertRaisesRegex(ValueError,'Frozen selection semantic mismatch'):obj.production()
            self.assertFalse(list(obj.out.glob('production_*')))

    def test_f01_unmodified_control_completes_all_stages(self):
        with tempfile.TemporaryDirectory() as directory:
            obj=object_fixture(after,directory);frozen_hash=after.sha(obj.out/'selection_frozen.json')
            with contextlib.redirect_stdout(io.StringIO()):obj.final();obj.production()
            self.assertEqual(after.sha(obj.out/'selection_frozen.json'),frozen_hash)
            self.assertEqual(read_json(obj.out/'production_receipt.json')['status'],'COMPLETED')
            self.assertTrue(all(r['nonpositive_co2_count']=='0' for r in table(obj.out/'path_diagnostics.csv') if r['target']=='co2'))

    def run_path_fixture(self,module,failure):
        with tempfile.TemporaryDirectory() as directory:
            obj=object_fixture(module,directory)
            with contextlib.redirect_stdout(io.StringIO()):obj.final()
            original=obj.predict
            def injected(mid,pack,year):
                if mid=='D' and year in [2023,2024]:
                    if failure=='negative':return -1.
                    if failure=='zero':return 0.
                    raise module.m.ModelFailure(failure,'injected separate failure cause')
                return original(mid,pack,year)
            obj.predict=injected
            with contextlib.redirect_stdout(io.StringIO()):obj.production()
            self.assertEqual(read_json(obj.out/'production_receipt.json')['status'],'COMPLETED')
            return table(obj.out/'path_diagnostics.csv'),table(obj.out/'threshold_search_paths.csv')

    def test_f02_negative_before_zero_after_one_per_affected_window(self):
        for module,count in [(before,0),(after,1)]:
            with self.subTest(version=module.__name__):
                diagnostics,paths=self.run_path_fixture(module,'negative')
                for window in ['full','last30']:
                    diag=next(r for r in diagnostics if r['model_id']=='D' and r['fit_window']==window)
                    self.assertEqual(int(diag['nonpositive_co2_count']),count);self.assertEqual(int(diag['invalid_count']),278)
                    affected=[r for r in paths if r['model_id']=='D' and r['fit_window']==window]
                    self.assertEqual(next(r['status'] for r in affected if r['year']=='2023'),'NONPOSITIVE_CO2')
                    self.assertEqual(next(r['value'] for r in affected if r['year']=='2023'),'')
                    self.assertTrue(all(r['status']=='INVALID_PATH' for r in affected if int(r['year'])>=2024))

    def test_f02_zero_is_nonpositive_but_overflow_and_missing_are_not(self):
        for failure,expected in [('zero',1),('NONFINITE_PREDICTION',0),('MISSING_PREDICTION',0)]:
            with self.subTest(failure=failure):
                diagnostics,paths=self.run_path_fixture(after,failure)
                for row in diagnostics:
                    if row['model_id']=='D':self.assertEqual(int(row['nonpositive_co2_count']),expected);self.assertEqual(int(row['invalid_count']),278)


if __name__=='__main__':unittest.main(verbosity=2)
