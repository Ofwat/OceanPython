import pandas as pd
from util import validations
from dao import pr14SubmeasureDao

def upload_data_PR14_submeasues(cli_args):
    input_file_name = cli_args.input_file
    pd.set_option("display.precision", 18)
    df2 = pd.read_excel(input_file_name,
                        sheet_name='Sub-measures', usecols="A:BB,BK,BL,BG:BH,BM:BR", skiprows=[0, 1])
    df2.columns = ['unique_id', 'company_type', 'company', 'element_acronym', 'pc_ref', 'performance_commitment',
                   'odi_type', 'primary_category', 'pc_unit_description', 'starting_level_pr14_fd_2014_15',
                   'pcl_2015_16',
                   'pcl_2016_17', 'pcl_2017_18', 'pcl_2018_19', 'pcl_2019_20', 'sub_measure_id', 'sub_measure',
                   'sub_measure_category', 'sub_measure_weighting', 'pc_unit', 'decimal_places',
                   'submeasure_performace_level_reference_regulatory_output_during_2010_15',
                   'submeasure_performace_level_reference_expected_performance_by_2014_15',
                   'submeasure_performace_level_2015_16', 'submeasure_performace_level_2016_17',
                   'submeasure_performace_level_2017_18', 'submeasure_performace_level_2018_19',
                   'submeasure_performace_level_2019_20', 'submeasure_high_reference_regulatory_output_during_2010_15',
                   'submeasure_high_reference_expected_performance_by_2014_15', 'submeasure_high_2015_16',
                   'submeasure_high_2016_17', 'submeasure_high_2017_18', 'submeasure_high_2018_19',
                   'submeasure_high_2019_20', 'submeasure_low_reference_regulatory_output_during_2010_15',
                   'submeasure_low_reference_expected_performance_by_2014_15', 'submeasure_low_2015_16',
                   'submeasure_low_2016_17', 'submeasure_low_2017_18', 'submeasure_low_2018_19',
                   'submeasure_low_2019_20',
                   'failure_threshold_for_AMP6', 'actual_performance_level_pcs_submeasures_actual_2014_15',
                   'actual_performance_level_pcs_submeasures_actual_2015_16',
                   'actual_performance_level_pcs_submeasures_pcl_met_2015_16',
                   'actual_performance_level_pcs_submeasures_actual_2016_17',
                   'actual_performance_level_pcs_submeasures_pcl_met_2016_17',
                   'actual_performance_level_pcs_submeasures_actual_2017_18',
                   'actual_performance_level_pcs_submeasures_pcl_met_2017_18',
                   'actual_performance_level_pcs_submeasures_actual_2018_19',
                   'actual_performance_level_pcs_submeasures_pcl_met_2018_19',
                   'actual_performance_level_pcs_submeasures_actual_2019_20',
                   'actual_performance_level_pcs_submeasures_pcl_met_2019_20',
                   'actual_performance_level_pcs_submeasures_actual_estimate_2019_20',
                   'actual_performance_level_pcs_submeasures_pcl_met_estimate_2019_20',
                   'direction_of_improving_performance', 'comms_filter',
                   'actual_performance_compared_with_previous_actual_performance_2014_15_to_2015_16',
                   'actual_performance_compared_with_previous_actual_performance_2015_16_to_2016_17',
                   'actual_performance_compared_with_previous_actual_performance_2016_17_to_2017_18',
                   'actual_performance_compared_with_previous_actual_performance_2017_18_to_2018_19',
                   'actual_performance_compared_with_previous_actual_performance_2018_19_to_2019_20',
                   'actual_performance_compared_with_previous_actual_performance_2014_15_to_2016_17_amp_so_far']
    df2 = df2.astype({'unique_id': 'object', 'company_type': 'object', 'company': 'object', 'element_acronym': 'object',
                      'pc_ref': 'object', 'performance_commitment': 'object', 'odi_type': 'object',
                      'primary_category': 'object', 'pc_unit_description': 'object',
                      'starting_level_pr14_fd_2014_15': 'object', 'pcl_2015_16': 'object', 'pcl_2016_17': 'object',
                      'pcl_2017_18': 'object', 'pcl_2018_19': 'object', 'pcl_2019_20': 'object',
                      'sub_measure_id': 'object',
                      'sub_measure': 'object', 'sub_measure_category': 'object', 'sub_measure_weighting': 'object',
                      'pc_unit': 'object', 'decimal_places': 'object',
                      'submeasure_performace_level_reference_regulatory_output_during_2010_15': 'object',
                      'submeasure_performace_level_reference_expected_performance_by_2014_15': 'object',
                      'submeasure_performace_level_2015_16': 'object', 'submeasure_performace_level_2016_17': 'object',
                      'submeasure_performace_level_2017_18': 'object', 'submeasure_performace_level_2018_19': 'object',
                      'submeasure_performace_level_2019_20': 'object',
                      'submeasure_high_reference_regulatory_output_during_2010_15': 'object',
                      'submeasure_high_reference_expected_performance_by_2014_15': 'object',
                      'submeasure_high_2015_16': 'object', 'submeasure_high_2016_17': 'object',
                      'submeasure_high_2017_18': 'object', 'submeasure_high_2018_19': 'object',
                      'submeasure_high_2019_20': 'object',
                      'submeasure_low_reference_regulatory_output_during_2010_15': 'float64',
                      'submeasure_low_reference_expected_performance_by_2014_15': 'object',
                      'submeasure_low_2015_16': 'object', 'submeasure_low_2016_17': 'object',
                      'submeasure_low_2017_18': 'object', 'submeasure_low_2018_19': 'object',
                      'submeasure_low_2019_20': 'object', 'failure_threshold_for_AMP6': 'object',
                      'actual_performance_level_pcs_submeasures_actual_2014_15': 'object',
                      'actual_performance_level_pcs_submeasures_actual_2015_16': 'object',
                      'actual_performance_level_pcs_submeasures_pcl_met_2015_16': 'object',
                      'actual_performance_level_pcs_submeasures_actual_2016_17': 'object',
                      'actual_performance_level_pcs_submeasures_pcl_met_2016_17': 'object',
                      'actual_performance_level_pcs_submeasures_actual_2017_18': 'object',
                      'actual_performance_level_pcs_submeasures_pcl_met_2017_18': 'object',
                      'actual_performance_level_pcs_submeasures_actual_2018_19': 'object',
                      'actual_performance_level_pcs_submeasures_pcl_met_2018_19': 'object',
                      'actual_performance_level_pcs_submeasures_actual_2019_20': 'object',
                      'actual_performance_level_pcs_submeasures_pcl_met_2019_20': 'object',
                      'actual_performance_level_pcs_submeasures_actual_estimate_2019_20': 'object',
                      'actual_performance_level_pcs_submeasures_pcl_met_estimate_2019_20': 'object',
                      'direction_of_improving_performance': 'object', 'comms_filter': 'object',
                      'actual_performance_compared_with_previous_actual_performance_2014_15_to_2015_16': 'object',
                      'actual_performance_compared_with_previous_actual_performance_2015_16_to_2016_17': 'object',
                      'actual_performance_compared_with_previous_actual_performance_2016_17_to_2017_18': 'object',
                      'actual_performance_compared_with_previous_actual_performance_2017_18_to_2018_19': 'object',
                      'actual_performance_compared_with_previous_actual_performance_2018_19_to_2019_20': 'object',
                      'actual_performance_compared_with_previous_actual_performance_2014_15_to_2016_17_amp_so_far': 'object'})
    listofsubmeasurecolumns = []
    for column in df2:
        listofsubmeasurecolumns.append(column)
    for k in listofsubmeasurecolumns:
        df2[k] = validations.replace_spaces(df2, k)
        df2[k] = validations.replace_dashes_with_nan(df2, k)
        df2[k] = validations.replace_null_with_None(df2, k)
        if k in ['actual_performance_level_pcs_submeasures_pcl_met_2015_16',
                 'actual_performance_level_pcs_submeasures_pcl_met_2016_17',
                 'actual_performance_level_pcs_submeasures_pcl_met_2017_18',
                 'actual_performance_level_pcs_submeasures_pcl_met_2018_19',
                 'actual_performance_level_pcs_submeasures_pcl_met_2019_20',
                 'actual_performance_level_pcs_submeasures_pcl_met_estimate_2019_20']:
            df2[k] = validations.replace_yes_with_true(df2, k)
        if k == 'company':
            df2[k] = validations.change_company_to_UUW(df2)
    pr14SubmeasureDao.insert_pr14_submeasure_data_in_table(df2)