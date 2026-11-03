"""Author implementation tests, synthetic only; not independent acceptance."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'modeling'))
import climate_models_r02 as m
import numpy as np
import unittest
import tempfile
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'experiments'))
import analysis_r02 as experiment


def fixture():
    years=np.arange(1959,2022); x=(years-1959)/10
    co2=300+12*x+2*x*x
    temp=-0.1+3*np.log(co2/300)
    return {'year':years,'co2_ppm':co2,'temp_anomaly_c':temp}


class ModelChecks(unittest.TestCase):
    def test_quadratic_coefficients_and_direct_forecast(self):
        fit=m.fit_co2(fixture(),'Q',2001)
        np.testing.assert_allclose(list(fit['parameters'].values()),[300,12,2],atol=1e-10)
        self.assertAlmostEqual(float(m.predict_co2(fit,2050)),300+12*9.1+2*9.1**2,places=9)

    def test_exponential_coefficients(self):
        data=fixture();data['co2_ppm']=300*np.exp(0.02*m.xyears(data['year']))
        fit=m.fit_co2(data,'E',2001)
        np.testing.assert_allclose(list(fit['parameters'].values()),[0,0.02],atol=1e-12)
        self.assertAlmostEqual(float(m.predict_co2(fit,2010)),300*np.exp(0.102),places=9)

    def test_drift_uses_ten_elapsed_years_and_anchor(self):
        data=fixture();data['co2_ppm']=300+2*(data['year']-1959)
        fit=m.fit_co2(data,'D',2001)
        self.assertEqual(fit['n_train'],11)
        self.assertEqual(fit['parameters']['slope_ppm_per_year'],2)
        self.assertEqual(float(m.predict_co2(fit,2011)),404)

    def test_temperature_coefficient_recovery(self):
        data=fixture();fit=m.fit_temperature(data,'T1',2001)
        np.testing.assert_allclose(list(fit['parameters'].values()),[-.1,3],atol=1e-12)
        data['temp_anomaly_c']=.25+.12*m.xyears(data['year'])
        fit=m.fit_temperature(data,'T0',2001)
        np.testing.assert_allclose(list(fit['parameters'].values()),[.25,.12],atol=1e-12)

    def test_fixed_log_reference_scale_invariance(self):
        data=fixture();a=m.fit_temperature(data,'T1',2001,cref=300);b=m.fit_temperature(data,'T1',2001,cref=280)
        np.testing.assert_allclose(m.temperature_from_co2(a,[400,500]),m.temperature_from_co2(b,[400,500]),atol=1e-12)
        ea=m.fit_co2(data,'E',2001,cref=300);eb=m.fit_co2(data,'E',2001,cref=280)
        np.testing.assert_allclose(m.predict_co2(ea,[2010,2050]),m.predict_co2(eb,[2010,2050]),atol=1e-10)

    def test_ten_year_changes_and_equal_increase(self):
        years=np.arange(1959,2005);rows=m.ten_year_changes(years,300+2*(years-1959),range(1969,2005))
        self.assertEqual(len(rows),36)
        self.assertTrue(all(r['increase_ppm']==20 and r['average_growth_ppm_per_year']==2 for r in rows))

    def test_threshold_fractional_and_exact(self):
        for threshold in [305,306]:
            c=m.crossing(lambda t:300+2*(t-2000),threshold,2000,2020)
            self.assertEqual(c['first_year'],2003)
            self.assertLess(c['value_previous_year'],threshold)
        self.assertEqual(m.crossing(lambda t:.02*(t-2000),.05,2000,2020)['first_year'],2003)

    def test_threshold_no_crossing_and_already_above(self):
        self.assertEqual(m.crossing(lambda t:300,305,2000,2300)['status'],'NO_CROSSING_THROUGH_2300')
        above=m.crossing(lambda t:310,305,2000,2300)
        self.assertEqual(above['status'],'AT_OR_BEFORE_ORIGIN');self.assertIsNone(above['first_year'])

    def test_nonmonotone_first_passage(self):
        result=m.crossing(lambda t:10-(t-2004)**2,9,2000,2010)
        self.assertEqual(result['first_year'],2003)
        self.assertFalse(result['monotone_flag']);self.assertTrue(result['possible_recrossing'])

    def test_invalid_before_crossing(self):
        result=m.crossing(lambda t:float('nan'),1)
        self.assertEqual(result['status'],'INVALID_PATH')

    def test_nonpositive_log_rejected(self):
        fit=m.fit_temperature(fixture(),'T1',2001)
        for value in [0,-2,float('nan'),float('inf')]:
            with self.assertRaises(m.ModelFailure) as error:m.temperature_from_co2(fit,value)
            self.assertEqual(error.exception.status,'INVALID_UPSTREAM_PATH')

    def test_rank_deficiency_rejected(self):
        with self.assertRaises(m.ModelFailure) as error:m.least_squares(np.ones((5,2)),np.arange(5))
        self.assertEqual(error.exception.status,'RANK_DEFICIENT')

    def test_duplicate_missing_future_and_negative_co2_rejected(self):
        for kind in ['duplicate','missing','future','nonpositive']:
            data=fixture()
            if kind=='duplicate':data['year'][1]=data['year'][0]
            if kind=='missing':data={k:np.delete(v,3) for k,v in data.items()}
            if kind=='future':data['year'][-1]=2022
            if kind=='nonpositive':data['co2_ppm'][3]=0
            with self.subTest(kind=kind),self.assertRaises(m.ModelFailure):m.validate_data(data,np.arange(1959,2022))

    def test_year_misalignment_is_not_a_join(self):
        # Joining by position would assign the 1958 value to 1959; keyed truth differs.
        cy=np.array([1959,1960]);ty=np.array([1958,1959,1960]);tv=np.array([99,.03,-.03])
        keyed=np.array([dict(zip(ty,tv))[y] for y in cy])
        self.assertFalse(np.array_equal(tv[:2],keyed))
        np.testing.assert_array_equal(keyed,[.03,-.03])

    def test_future_mutation_cannot_change_fits_or_predictions(self):
        data=fixture();changed={k:v.copy() for k,v in data.items()};future=changed['year']>1991
        changed['co2_ppm'][future]*=2;changed['temp_anomaly_c'][future]-=20
        for kind in ['D','Q','E']:
            a=m.fit_co2(data,kind,1991);b=m.fit_co2(changed,kind,1991)
            self.assertEqual(a['parameters'],b['parameters'])
            np.testing.assert_array_equal(m.predict_co2(a,[1992,2001]),m.predict_co2(b,[1992,2001]))
            ta=m.fit_temperature(data,'T1',1991);tb=m.fit_temperature(changed,'T1',1991)
            np.testing.assert_array_equal(m.predict_temperature(ta,[1992,2001],a),m.predict_temperature(tb,[1992,2001],b))
        self.assertEqual(m.fit_temperature(data,'T0',1991)['parameters'],m.fit_temperature(changed,'T0',1991)['parameters'])

    def test_temperature_responds_to_forecast_producer(self):
        data=fixture();tf=m.fit_temperature(data,'T1',1991);a=m.fit_co2(data,'D',1991);b={**a,'parameters':{**a['parameters'],'slope_ppm_per_year':20}}
        self.assertNotEqual(float(m.predict_temperature(tf,2001,a)),float(m.predict_temperature(tf,2001,b)))

    def test_last30_keeps_1959_scale_and_drift_rule(self):
        data=fixture();fit=m.fit_co2(data,'E',2021,1992)
        self.assertEqual(fit['n_train'],30);self.assertEqual(fit['cref'],300)
        self.assertEqual(m.fit_co2(data,'D',2021,1992)['parameters'],m.fit_co2(data,'D',2021,1959)['parameters'])

    def test_selection_tie_and_failure(self):
        self.assertEqual(m.select_minimum({'Q':1,'E':1,'D':1},['D','E','Q']),'D')
        self.assertEqual(m.select_minimum({'T0':1,'T1-Q':1},['T0','T1-Q']),'T0')
        with self.assertRaises(m.ModelFailure):m.select_minimum({'D':None},['D'])

    def test_envelope_uses_all_shorter_horizon_errors(self):
        rows=[{'model_id':'Q','status':'OK','horizon':h,'error':float(11-h+i)} for i in range(5) for h in range(1,11)]
        radius=m.historical_envelope(rows,'Q')
        self.assertEqual(radius,{h:14 for h in range(1,11)})

    def test_exponential_overflow_not_success(self):
        fit=m.fit_co2(fixture(),'E',2001);fit['parameters']['b_log_ratio_per_decade']=1e5
        with self.assertRaises(m.ModelFailure):m.predict_co2(fit,2300)

    def test_constant_correlation_explicitly_undefined(self):
        self.assertEqual(m.correlation(np.ones(5),np.arange(5)),(None,'UNDEFINED_CORRELATION'))

    def test_upstream_overflow_status_is_translated(self):
        data=fixture();tf=m.fit_temperature(data,'T1',2001);cf=m.fit_co2(data,'E',2001);cf['parameters']['b_log_ratio_per_decade']=1e5
        with self.assertRaises(m.ModelFailure) as error:m.predict_temperature(tf,2300,cf)
        self.assertEqual(error.exception.status,'INVALID_UPSTREAM_PATH')

    def test_failed_fold_rows_and_metrics_preserve_nulls(self):
        obj=experiment.Analysis.__new__(experiment.Analysis);obj.data=fixture();obj.cref=300
        obj.fits=lambda *args:{mid:{'fit':None,'upstream':None,'status':'RANK_DEFICIENT','reason':'injected failure'} for mid in experiment.MODEL_IDS}
        rows,params,residuals,diag=obj.forecasts([2001],'synthetic_failure',fixture())
        self.assertEqual(len(rows),70);self.assertTrue(all(r['predicted'] is None and r['error'] is None and r['status']=='RANK_DEFICIENT' for r in rows))
        metrics=obj.metrics(rows);self.assertTrue(all(r['mae'] is None and r['status']=='INELIGIBLE_FAILED_ROWS' for r in metrics))
        self.assertIsNone(experiment.absolute_or_none(None));self.assertIsNone(experiment.difference_or_none(2,None));self.assertIsNone(experiment.offset_or_none(None,2))

    def test_final_table_tamper_blocks_production_consumption(self):
        with tempfile.TemporaryDirectory() as directory:
            path=Path(directory);receipt={}
            for name in ['final_forecasts','final_metrics']:
                (path/(name+'.csv')).write_text('model,value\nD,1\n');receipt[name+'_sha256']=experiment.sha(path/(name+'.csv'))
            experiment.verify_final_tables(path,receipt)
            (path/'final_forecasts.csv').write_text('model,value\nD,999\n')
            with self.assertRaisesRegex(ValueError,'Final evidence changed'):experiment.verify_final_tables(path,receipt)

    def test_crossing_then_later_invalid_preserves_event_and_warning(self):
        for invalid in [0,float('inf'),None]:
            fn=lambda year:invalid if year==2005 else 300+2*(year-2000)
            result=m.crossing(fn,305,2000,2010,positive_required=True)
            self.assertEqual(result['status'],'CROSSED');self.assertEqual(result['first_year'],2003)
            self.assertFalse(result['search_domain_valid']);self.assertEqual(result['valid_through_year'],2004);self.assertEqual(result['invalid_from_year'],2005);self.assertIsNotNone(result['invalid_reason'])

    def test_invalidity_before_or_at_hit_and_reentry_never_crosses(self):
        for invalid_year in [2000,2002,2003]:
            fn=lambda year:float('inf') if year==invalid_year else 300+2*(year-2000)
            result=m.crossing(fn,305,2000,2010,positive_required=True)
            self.assertEqual(result['status'],'INVALID_PATH');self.assertIsNone(result['first_year']);self.assertEqual(result['invalid_from_year'],invalid_year)
            self.assertIsNone(result['beyond_tested_horizon'])
        invalid_origin=m.crossing(lambda year:0,1,2000,2010,positive_required=True)
        self.assertIsNone(invalid_origin['valid_through_year']);self.assertIsNone(invalid_origin['monotone_flag'])

    def test_already_above_then_invalid_retains_status(self):
        result=m.crossing(lambda year:None if year==2002 else 310,305,2000,2010,positive_required=True)
        self.assertEqual(result['status'],'AT_OR_BEFORE_ORIGIN');self.assertIsNone(result['first_year']);self.assertEqual(result['valid_through_year'],2001);self.assertFalse(result['search_domain_valid'])

    def test_negative_anomaly_valid_and_monotone_definition(self):
        result=m.crossing(lambda year:-.1+.02*(year-2000),0,2000,2010)
        self.assertEqual(result['first_year'],2005);self.assertTrue(result['search_domain_valid']);self.assertTrue(result['monotone_flag'])
        declining=m.crossing(lambda year:310-(year-2000),500,2000,2010,positive_required=True)
        self.assertFalse(declining['monotone_flag']);self.assertEqual(declining['monotonicity_end_year'],2010)


if __name__=='__main__':unittest.main(verbosity=2)
