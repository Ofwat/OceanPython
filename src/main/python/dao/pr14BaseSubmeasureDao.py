from util import dbUtils

def insert_pr14_submeasure_data_in_table(df2):
    conn = dbUtils.sql_server_connection()
    schemanameused = dbUtils.create_schema()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM information_schema.tables where table_schema ='" + schemanameused + "' and table_name = 'PR14SubmeasureFinalCSVcreatedbyPython'")
    queryfortablecheck = cursor.fetchone()
    if queryfortablecheck is not None:
        print("Table PR14SubmeasureFinalCSVcreatedbyPython is existing")
        cursor.execute("DROP TABLE " + schemanameused + ".PR14SubmeasureFinalCSVcreatedbyPython")
        print("Dropped the existing PR14SubmeasureFinalCSVcreatedbyPython table")
        print("Creating new PR14SubmeasureFinalCSVcreatedbyPython table")
    else:
        print("Creating PR14SubmeasureFinalCSVcreatedbyPython table")
    cursor.execute(
        'CREATE TABLE ' + schemanameused + '.PR14SubmeasureFinalCSVcreatedbyPython(unique_id nvarchar(max),company_type nvarchar(max),company nvarchar(max),element_acronym nvarchar(max),pc_ref nvarchar(max),performance_commitment nvarchar(max),odi_type nvarchar(max),primary_category nvarchar(max),pc_unit_description nvarchar(max),starting_level_pr14_fd_2014_15 nvarchar(max),pcl_2015_16 nvarchar(max),pcl_2016_17 nvarchar(max),pcl_2017_18 nvarchar(max),pcl_2018_19 nvarchar(max),pcl_2019_20 nvarchar(max),sub_measure_id nvarchar(max),sub_measure nvarchar(max),sub_measure_category nvarchar(max),sub_measure_weighting nvarchar(max),pc_unit nvarchar(max),decimal_places nvarchar(max),submeasure_performace_level_reference_regulatory_output_during_2010_15 nvarchar(max),submeasure_performace_level_reference_expected_performance_by_2014_15 nvarchar(max),submeasure_performace_level_2015_16 nvarchar(max),submeasure_performace_level_2016_17 nvarchar(max),submeasure_performace_level_2017_18 nvarchar(max),submeasure_performace_level_2018_19 nvarchar(max),submeasure_performace_level_2019_20 nvarchar(max),submeasure_high_reference_regulatory_output_during_2010_15 nvarchar(max),submeasure_high_reference_expected_performance_by_2014_15 nvarchar(max),submeasure_high_2015_16 nvarchar(max),submeasure_high_2016_17 nvarchar(max),submeasure_high_2017_18 nvarchar(max),submeasure_high_2018_19 nvarchar(max),submeasure_high_2019_20 nvarchar(max),submeasure_low_reference_regulatory_output_during_2010_15 float,submeasure_low_reference_expected_performance_by_2014_15 float,submeasure_low_2015_16 nvarchar(max),submeasure_low_2016_17 nvarchar(max),submeasure_low_2017_18 nvarchar(max),submeasure_low_2018_19 nvarchar(max),submeasure_low_2019_20 nvarchar(max),failure_threshold_for_AMP6 nvarchar(max),actual_performance_level_pcs_submeasures_actual_2014_15 nvarchar(max),actual_performance_level_pcs_submeasures_actual_2015_16 nvarchar(max),actual_performance_level_pcs_submeasures_pcl_met_2015_16 nvarchar(max),actual_performance_level_pcs_submeasures_actual_2016_17 nvarchar(max),actual_performance_level_pcs_submeasures_pcl_met_2016_17 nvarchar(max),actual_performance_level_pcs_submeasures_actual_2017_18 nvarchar(max),actual_performance_level_pcs_submeasures_pcl_met_2017_18 nvarchar(max),actual_performance_level_pcs_submeasures_actual_2018_19 nvarchar(max),actual_performance_level_pcs_submeasures_pcl_met_2018_19 nvarchar(max),actual_performance_level_pcs_submeasures_actual_2019_20 nvarchar(max),actual_performance_level_pcs_submeasures_pcl_met_2019_20 nvarchar(max),actual_performance_level_pcs_submeasures_actual_estimate_2019_20 nvarchar(max),actual_performance_level_pcs_submeasures_pcl_met_estimate_2019_20 nvarchar(max),direction_of_improving_performance nvarchar(max),comms_filter nvarchar(max),actual_performance_compared_with_previous_actual_performance_2014_15_to_2015_16 nvarchar(max),actual_performance_compared_with_previous_actual_performance_2015_16_to_2016_17 nvarchar(max),actual_performance_compared_with_previous_actual_performance_2016_17_to_2017_18 nvarchar(max),actual_performance_compared_with_previous_actual_performance_2017_18_to_2018_19 nvarchar(max),actual_performance_compared_with_previous_actual_performance_2018_19_to_2019_20 nvarchar(max),actual_performance_compared_with_previous_actual_performance_2014_15_to_2016_17_amp_so_far nvarchar(max))')
    for row in df2.itertuples():
        cursor.execute('''
            INSERT INTO ''' + schemanameused + '''.PR14SubmeasureFinalCSVcreatedbyPython (unique_id,company_type,company,element_acronym,pc_ref,performance_commitment,odi_type,primary_category,pc_unit_description,starting_level_pr14_fd_2014_15,pcl_2015_16,pcl_2016_17,pcl_2017_18,pcl_2018_19,pcl_2019_20,sub_measure_id,sub_measure,sub_measure_category,sub_measure_weighting,pc_unit,decimal_places,submeasure_performace_level_reference_regulatory_output_during_2010_15,submeasure_performace_level_reference_expected_performance_by_2014_15,submeasure_performace_level_2015_16,submeasure_performace_level_2016_17,submeasure_performace_level_2017_18,submeasure_performace_level_2018_19,submeasure_performace_level_2019_20,submeasure_high_reference_regulatory_output_during_2010_15,submeasure_high_reference_expected_performance_by_2014_15,submeasure_high_2015_16,submeasure_high_2016_17,submeasure_high_2017_18,submeasure_high_2018_19,submeasure_high_2019_20,submeasure_low_reference_regulatory_output_during_2010_15,submeasure_low_reference_expected_performance_by_2014_15,submeasure_low_2015_16,submeasure_low_2016_17,submeasure_low_2017_18,submeasure_low_2018_19,submeasure_low_2019_20,failure_threshold_for_AMP6,actual_performance_level_pcs_submeasures_actual_2014_15,actual_performance_level_pcs_submeasures_actual_2015_16,actual_performance_level_pcs_submeasures_pcl_met_2015_16,actual_performance_level_pcs_submeasures_actual_2016_17,actual_performance_level_pcs_submeasures_pcl_met_2016_17,actual_performance_level_pcs_submeasures_actual_2017_18,actual_performance_level_pcs_submeasures_pcl_met_2017_18,actual_performance_level_pcs_submeasures_actual_2018_19,actual_performance_level_pcs_submeasures_pcl_met_2018_19,actual_performance_level_pcs_submeasures_actual_2019_20,actual_performance_level_pcs_submeasures_pcl_met_2019_20,actual_performance_level_pcs_submeasures_actual_estimate_2019_20,actual_performance_level_pcs_submeasures_pcl_met_estimate_2019_20,direction_of_improving_performance,comms_filter,actual_performance_compared_with_previous_actual_performance_2014_15_to_2015_16,actual_performance_compared_with_previous_actual_performance_2015_16_to_2016_17,actual_performance_compared_with_previous_actual_performance_2016_17_to_2017_18,actual_performance_compared_with_previous_actual_performance_2017_18_to_2018_19,actual_performance_compared_with_previous_actual_performance_2018_19_to_2019_20,actual_performance_compared_with_previous_actual_performance_2014_15_to_2016_17_amp_so_far)
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
            ''',
                       row.unique_id,
                       row.company_type,
                       row.company,
                       row.element_acronym,
                       row.pc_ref,
                       row.performance_commitment,
                       row.odi_type,
                       row.primary_category,
                       row.pc_unit_description,
                       row.starting_level_pr14_fd_2014_15,
                       row.pcl_2015_16,
                       row.pcl_2016_17,
                       row.pcl_2017_18,
                       row.pcl_2018_19,
                       row.pcl_2019_20,
                       row.sub_measure_id,
                       row.sub_measure,
                       row.sub_measure_category,
                       row.sub_measure_weighting,
                       row.pc_unit,
                       row.decimal_places,
                       row.submeasure_performace_level_reference_regulatory_output_during_2010_15,
                       row.submeasure_performace_level_reference_expected_performance_by_2014_15,
                       row.submeasure_performace_level_2015_16,
                       row.submeasure_performace_level_2016_17,
                       row.submeasure_performace_level_2017_18,
                       row.submeasure_performace_level_2018_19,
                       row.submeasure_performace_level_2019_20,
                       row.submeasure_high_reference_regulatory_output_during_2010_15,
                       row.submeasure_high_reference_expected_performance_by_2014_15,
                       row.submeasure_high_2015_16,
                       row.submeasure_high_2016_17,
                       row.submeasure_high_2017_18,
                       row.submeasure_high_2018_19,
                       row.submeasure_high_2019_20,
                       row.submeasure_low_reference_regulatory_output_during_2010_15,
                       row.submeasure_low_reference_expected_performance_by_2014_15,
                       row.submeasure_low_2015_16,
                       row.submeasure_low_2016_17,
                       row.submeasure_low_2017_18,
                       row.submeasure_low_2018_19,
                       row.submeasure_low_2019_20,
                       row.failure_threshold_for_AMP6,
                       row.actual_performance_level_pcs_submeasures_actual_2014_15,
                       row.actual_performance_level_pcs_submeasures_actual_2015_16,
                       row.actual_performance_level_pcs_submeasures_pcl_met_2015_16,
                       row.actual_performance_level_pcs_submeasures_actual_2016_17,
                       row.actual_performance_level_pcs_submeasures_pcl_met_2016_17,
                       row.actual_performance_level_pcs_submeasures_actual_2017_18,
                       row.actual_performance_level_pcs_submeasures_pcl_met_2017_18,
                       row.actual_performance_level_pcs_submeasures_actual_2018_19,
                       row.actual_performance_level_pcs_submeasures_pcl_met_2018_19,
                       row.actual_performance_level_pcs_submeasures_actual_2019_20,
                       row.actual_performance_level_pcs_submeasures_pcl_met_2019_20,
                       row.actual_performance_level_pcs_submeasures_actual_estimate_2019_20,
                       row.actual_performance_level_pcs_submeasures_pcl_met_estimate_2019_20,
                       row.direction_of_improving_performance,
                       row.comms_filter,
                       row.actual_performance_compared_with_previous_actual_performance_2014_15_to_2015_16,
                       row.actual_performance_compared_with_previous_actual_performance_2015_16_to_2016_17,
                       row.actual_performance_compared_with_previous_actual_performance_2016_17_to_2017_18,
                       row.actual_performance_compared_with_previous_actual_performance_2017_18_to_2018_19,
                       row.actual_performance_compared_with_previous_actual_performance_2018_19_to_2019_20,
                       row.actual_performance_compared_with_previous_actual_performance_2014_15_to_2016_17_amp_so_far
                       )

    conn.commit()
    conn.close()