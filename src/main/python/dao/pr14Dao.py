from util import dbUtils


def insert_pr14_data_in_table(df):
    conn = dbUtils.sql_server_connection()
    schemanameused = dbUtils.schema_present()
    queryfortablecheck = dbUtils.table_present(schemanameused, 'PR14FinalCSVcreatedbyPython')
    cursor = conn.cursor()

    if queryfortablecheck is True:
        cursor.execute("DROP TABLE " + schemanameused + ".PR14FinalCSVcreatedbyPython")
        print("Dropped the existing PR14FinalCSVcreatedbyPython table")
        print("Creating new PR14FinalCSVcreatedbyPython table")
    else:
        print("Creating PR14FinalCSVcreatedbyPython table")
    cursor.execute(
        'CREATE TABLE ' + schemanameused + '''.PR14FinalCSVcreatedbyPython(unique_id nvarchar(max),
            company_type nvarchar(max),
            company nvarchar(max),
            element_name nvarchar(max),
            element_acronym nvarchar(max),
            outcome nvarchar(max),
            pc_ref nvarchar(max),
            annex nvarchar(max),
            performance_commitment nvarchar(max),
            odi_type nvarchar(max),
            odi_form nvarchar(max),
            in_period_odi nvarchar(max),
            vanilla_odi nvarchar(max),
            primary_category nvarchar(max),
            pc_unit nvarchar(max),
            pc_unit_description nvarchar(max),
            decimal_places nvarchar(max),
            direction_of_improving_performance nvarchar(max),
            starting_level_pr14_fd_2014_15 nvarchar(max),
            pcl_2015_16 nvarchar(max),
            pcl_2016_17 nvarchar(max),
            pcl_2017_18 nvarchar(max),
            pcl_2018_19 nvarchar(max),
            pcl_2019_20 nvarchar(max),
            PR14_comparative_drinking_water_compliance nvarchar(max),
            PR14_comparative_water_quality_contacts nvarchar(max),
            PR14_comparative_supply_interruptions_3_hours nvarchar(max),
            PR14_comparative_pollution_incidents_cat_3 nvarchar(max),
            PR14_comparative_internal_sewer_flooding nvarchar(max),
            scheme_specific_factor nvarchar(max),
            asset_health nvarchar(max),
            nep nvarchar(max),
            aim nvarchar(max),
            no_of_sub_measures int,
            financial_odi_2015_16 nvarchar(max),
            financial_odi_2016_17 nvarchar(max),
            financial_odi_2017_18 nvarchar(max),
            financial_odi_2018_19 nvarchar(max),
            financial_odi_2019_20 nvarchar(max),
            notes_underp_payment_collar_2015_16 nvarchar(max),
            underp_payment_collar_2015_16 float,
            notes_underp_payment_collar_2016_17 nvarchar(max),
            underp_payment_collar_2016_17 float,
            notes_underp_payment_collar_2017_18 nvarchar(max),
            underp_payment_collar_2017_18 float,
            notes_underp_payment_collar_2018_19 nvarchar(max),
            underp_payment_collar_2018_19 float,
            notes_underp_payment_collar_2019_20 nvarchar(max),
            underp_payment_collar_2019_20 float,
            underp_payment_deadband_2015_16 nvarchar(max),
            underp_payment_deadband_2016_17 nvarchar(max),
            underp_payment_deadband_2017_18 nvarchar(max),
            underp_payment_deadband_2018_19 nvarchar(max),
            underp_payment_deadband_2019_20 nvarchar(max),
            outp_payment_deadband_2015_16 nvarchar(max),
            outp_payment_deadband_2016_17 nvarchar(max),
            outp_payment_deadband_2017_18 nvarchar(max),
            outp_payment_deadband_2018_19 nvarchar(max),
            outp_payment_deadband_2019_20 nvarchar(max),
            outp_payment_cap_2015_16 nvarchar(max),
            outp_payment_cap_2016_17 nvarchar(max),
            outp_payment_cap_2017_18 nvarchar(max),
            outp_payment_cap_2018_19 nvarchar(max),
            outp_payment_cap_2019_20 nvarchar(max),
            notes_underp_payment1_incentive_rate_gbpm nvarchar(max),
            underp_payment1_incentive_rate_gbpm float,
            notes_underp_payment2_incentive_rate_gbpm nvarchar(max),
            underp_payment2_incentive_rate_gbpm float,
            notes_underp_payment3_incentive_rate_gbpm nvarchar(max),
            underp_payment3_incentive_rate_gbpm float,
            notes_underp_payment4_incentive_rate_gbpm nvarchar(max),
            underp_payment4_incentive_rate_gbpm float,
            notes_outp_payment1_incentive_rate_gbpm nvarchar(max),
            outp_payment1_incentive_rate_gbpm float,
            notes_outp_payment2_incentive_rate_gbpm nvarchar(max),
            outp_payment2_incentive_rate_gbpm float,
            standard_odi_operand float,
            standard_odi_operand_note nvarchar(max),
            performance_level_actual_2014_15 nvarchar(max),
            performance_level_actual_2015_16 nvarchar(max),
            pcl_met_2015_16 nvarchar(max),
            outp_payment_or_underp_payment_in_period_odis_2015_16 nvarchar(max),
            outp_payment_or_underp_payment_in_period_odis_gbpm_2015_16 nvarchar(max),
            notional_outp_payment_or_underp_payment_accrued_at_31_march_2016_2015_16 nvarchar(max),
            notional_outp_payment_or_underp_payment_accrued_at_31_march_2016_gbpm_2015_16 nvarchar(max),
            total_amp6_outp_payment_or_underp_payment_31_march_2020_forecast_2015_16 nvarchar(max),
            total_amp6_outp_payment_or_underp_payment_31_march_2020_forecast_gbpm_2015_16 nvarchar(max),
            performance_level_actual_2016_17 nvarchar(max),
            pcl_met_2016_17 nvarchar(max),
            outp_payment_or_underp_payment_in_period_odis_2016_17 nvarchar(max),
            outp_payment_or_underp_payment_in_period_odis_gbpm_2016_17 nvarchar(max),
            notional_outp_payment_or_underp_payment_accrued_at_31_march_2017_2016_17 nvarchar(max),
            notional_outp_payment_or_underp_payment_accrued_at_31_march_2017_gbpm_2016_17 nvarchar(max),
            total_amp6_outp_payment_or_underp_payment_31_march_2020_forecast_2016_17 nvarchar(max),
            total_amp6_outp_payment_or_underp_payment_31_march_2020_forecast_gbpm_2016_17 nvarchar(max),
            performance_level_actual_2017_18 nvarchar(max),
            pcl_met_2017_18 nvarchar(max),
            outp_payment_or_underp_payment_in_period_odis_2017_18 nvarchar(max),
            outp_payment_or_underp_payment_in_period_odis_gbpm_2017_18 nvarchar(max),
            notional_outp_payment_or_underp_payment_accrued_at_31_march_2018_2017_18 nvarchar(max),
            notional_outp_payment_or_underp_payment_accrued_at_31_march_2018_gbpm_2017_18 nvarchar(max),
            total_amp6_outp_payment_or_underp_payment_31_march_2020_forecast_2017_18 nvarchar(max),
            total_amp6_outp_payment_or_underp_payment_31_march_2020_forecast_gbpm_2017_18 nvarchar(max),
            performance_level_actual_2018_19 nvarchar(max),
            pcl_met_2018_19 nvarchar(max),
            outp_payment_or_underp_payment_in_period_odis_2018_19 nvarchar(max),
            outp_payment_or_underp_payment_in_period_odis_gbpm_2018_19 nvarchar(max),
            notional_outp_payment_or_underp_payment_accrued_at_31_march_2019_2018_19 nvarchar(max),
            notional_outp_payment_or_underp_payment_accrued_at_31_march_2019_gbpm_2018_19 nvarchar(max),
            total_amp6_outp_payment_or_underp_payment_31_march_2020_forecast_2018_19 nvarchar(max),
            total_amp6_outp_payment_or_underp_payment_31_march_2020_forecast_gbpm_2018_19 nvarchar(max),
            performance_level_actual_2019_20 nvarchar(max),
            pcl_met_2019_20 nvarchar(max),
            outp_payment_or_underp_payment_in_period_odis_2019_20 nvarchar(max),
            outp_payment_or_underp_payment_in_period_odis_gbpm_2019_20 nvarchar(max),
            notional_outp_payment_or_underp_payment_accrued_at_31_march_2020_2019_20 nvarchar(max),
            notional_outp_payment_or_underp_payment_accrued_at_31_march_2020_gbpm_2019_20 nvarchar(max),
            performance_level_actual_estimates_2019_20 nvarchar(max),
            pcl_met_estimates_2019_20 nvarchar(max),
            outp_payment_or_underp_payment_in_period_odis_estimates_2019_20 nvarchar(max),
            outp_payment_or_underp_payment_in_period_odis_gbpm_estimates_2019_20 nvarchar(max),
            notional_outp_payment_or_underp_payment_accrued_at_31_march_2020_estimates_2019_20 nvarchar(max),
            notional_outp_payment_or_underp_payment_accrued_at_31_march_2020_gbpm_estimates_2019_20 nvarchar(max),
            price_control_allocation_water_resources float,
            price_control_allocation_water_network_plus float,
            price_control_allocation_wastewater_network_plus float,
            price_control_allocation_bioresources_sludge float,
            price_control_allocation_residential_retail float,
            price_control_allocation_business_retail float,
            price_control_allocation_direct_procurement_for_customers float,
            price_control_allocation_dummy_control float)''')

    for row in df.itertuples():
        cursor.execute('''
        INSERT INTO ''' + schemanameused + '''.PR14FinalCSVcreatedbyPython (
            unique_id,
            company_type,
            company,
            element_name,
            element_acronym,
            outcome,
            pc_ref,
            annex,
            performance_commitment,
            odi_type,
            odi_form,
            in_period_odi,
            vanilla_odi,
            primary_category,
            pc_unit,
            pc_unit_description,
            decimal_places,
            direction_of_improving_performance,
            starting_level_pr14_fd_2014_15,
            pcl_2015_16,
            pcl_2016_17,
            pcl_2017_18,
            pcl_2018_19,
            pcl_2019_20,
            PR14_comparative_drinking_water_compliance,
            PR14_comparative_water_quality_contacts,
            PR14_comparative_supply_interruptions_3_hours,
            PR14_comparative_pollution_incidents_cat_3,
            PR14_comparative_internal_sewer_flooding,
            scheme_specific_factor,
            asset_health,
            nep,
            aim,
            no_of_sub_measures,
            financial_odi_2015_16,
            financial_odi_2016_17,
            financial_odi_2017_18,
            financial_odi_2018_19,
            financial_odi_2019_20,
            notes_underp_payment_collar_2015_16,
            underp_payment_collar_2015_16,
            notes_underp_payment_collar_2016_17,
            underp_payment_collar_2016_17,
            notes_underp_payment_collar_2017_18,
            underp_payment_collar_2017_18,
            notes_underp_payment_collar_2018_19,
            underp_payment_collar_2018_19,
            notes_underp_payment_collar_2019_20,
            underp_payment_collar_2019_20,
            underp_payment_deadband_2015_16,
            underp_payment_deadband_2016_17,
            underp_payment_deadband_2017_18,
            underp_payment_deadband_2018_19,
            underp_payment_deadband_2019_20,
            outp_payment_deadband_2015_16,
            outp_payment_deadband_2016_17,
            outp_payment_deadband_2017_18,
            outp_payment_deadband_2018_19,
            outp_payment_deadband_2019_20,
            outp_payment_cap_2015_16,
            outp_payment_cap_2016_17,
            outp_payment_cap_2017_18,
            outp_payment_cap_2018_19,
            outp_payment_cap_2019_20,
            notes_underp_payment1_incentive_rate_gbpm,
            underp_payment1_incentive_rate_gbpm ,
            notes_underp_payment2_incentive_rate_gbpm,
            underp_payment2_incentive_rate_gbpm ,
            notes_underp_payment3_incentive_rate_gbpm,
            underp_payment3_incentive_rate_gbpm ,
            notes_underp_payment4_incentive_rate_gbpm,
            underp_payment4_incentive_rate_gbpm ,
            notes_outp_payment1_incentive_rate_gbpm,
            outp_payment1_incentive_rate_gbpm ,
            notes_outp_payment2_incentive_rate_gbpm,
            outp_payment2_incentive_rate_gbpm ,
            standard_odi_operand ,
            standard_odi_operand_note,
            performance_level_actual_2014_15,
            performance_level_actual_2015_16,
            pcl_met_2015_16,
            outp_payment_or_underp_payment_in_period_odis_2015_16,
            outp_payment_or_underp_payment_in_period_odis_gbpm_2015_16,
            notional_outp_payment_or_underp_payment_accrued_at_31_march_2016_2015_16,
            notional_outp_payment_or_underp_payment_accrued_at_31_march_2016_gbpm_2015_16,
            total_amp6_outp_payment_or_underp_payment_31_march_2020_forecast_2015_16,
            total_amp6_outp_payment_or_underp_payment_31_march_2020_forecast_gbpm_2015_16,
            performance_level_actual_2016_17,
            pcl_met_2016_17,
            outp_payment_or_underp_payment_in_period_odis_2016_17,
            outp_payment_or_underp_payment_in_period_odis_gbpm_2016_17,
            notional_outp_payment_or_underp_payment_accrued_at_31_march_2017_2016_17,
            notional_outp_payment_or_underp_payment_accrued_at_31_march_2017_gbpm_2016_17,
            total_amp6_outp_payment_or_underp_payment_31_march_2020_forecast_2016_17,
            total_amp6_outp_payment_or_underp_payment_31_march_2020_forecast_gbpm_2016_17,
            performance_level_actual_2017_18,
            pcl_met_2017_18,
            outp_payment_or_underp_payment_in_period_odis_2017_18,
            outp_payment_or_underp_payment_in_period_odis_gbpm_2017_18,
            notional_outp_payment_or_underp_payment_accrued_at_31_march_2018_2017_18,
            notional_outp_payment_or_underp_payment_accrued_at_31_march_2018_gbpm_2017_18,
            total_amp6_outp_payment_or_underp_payment_31_march_2020_forecast_2017_18,
            total_amp6_outp_payment_or_underp_payment_31_march_2020_forecast_gbpm_2017_18,
            performance_level_actual_2018_19,
            pcl_met_2018_19,
            outp_payment_or_underp_payment_in_period_odis_2018_19,
            outp_payment_or_underp_payment_in_period_odis_gbpm_2018_19,
            notional_outp_payment_or_underp_payment_accrued_at_31_march_2019_2018_19,
            notional_outp_payment_or_underp_payment_accrued_at_31_march_2019_gbpm_2018_19,
            total_amp6_outp_payment_or_underp_payment_31_march_2020_forecast_2018_19,
            total_amp6_outp_payment_or_underp_payment_31_march_2020_forecast_gbpm_2018_19,
            performance_level_actual_2019_20,
            pcl_met_2019_20,
            outp_payment_or_underp_payment_in_period_odis_2019_20,
            outp_payment_or_underp_payment_in_period_odis_gbpm_2019_20,
            notional_outp_payment_or_underp_payment_accrued_at_31_march_2020_2019_20,
            notional_outp_payment_or_underp_payment_accrued_at_31_march_2020_gbpm_2019_20,
            performance_level_actual_estimates_2019_20,
            pcl_met_estimates_2019_20,
            outp_payment_or_underp_payment_in_period_odis_estimates_2019_20,
            outp_payment_or_underp_payment_in_period_odis_gbpm_estimates_2019_20,
            notional_outp_payment_or_underp_payment_accrued_at_31_march_2020_estimates_2019_20,
            notional_outp_payment_or_underp_payment_accrued_at_31_march_2020_gbpm_estimates_2019_20,
            price_control_allocation_water_resources ,
            price_control_allocation_water_network_plus ,
            price_control_allocation_wastewater_network_plus ,
            price_control_allocation_bioresources_sludge ,
            price_control_allocation_residential_retail ,
            price_control_allocation_business_retail ,
            price_control_allocation_direct_procurement_for_customers,
            price_control_allocation_dummy_control)
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
        ''',
            row.unique_id,
            row.company_type,
            row.company,
            row.element_name,
            row.element_acronym,
            row.outcome,
            row.pc_ref,
            row.annex,
            row.performance_commitment,
            row.odi_type,
            row.odi_form,
            row.in_period_odi,
            row.vanilla_odi,
            row.primary_category,
            row.pc_unit,
            row.pc_unit_description,
            row.decimal_places,
            row.direction_of_improving_performance,
            row.starting_level_pr14_fd_2014_15,
            row.pcl_2015_16,
            row.pcl_2016_17,
            row.pcl_2017_18,
            row.pcl_2018_19,
            row.pcl_2019_20,
            row.PR14_comparative_drinking_water_compliance,
            row.PR14_comparative_water_quality_contacts,
            row.PR14_comparative_supply_interruptions_3_hours,
            row.PR14_comparative_pollution_incidents_cat_3,
            row.PR14_comparative_internal_sewer_flooding,
            row.scheme_specific_factor,
            row.asset_health,
            row.nep,
            row.aim,
            row.no_of_sub_measures,
            row.financial_odi_2015_16,
            row.financial_odi_2016_17,
            row.financial_odi_2017_18,
            row.financial_odi_2018_19,
            row.financial_odi_2019_20,
            row.notes_underp_payment_collar_2015_16,
            row.underp_payment_collar_2015_16,
            row.notes_underp_payment_collar_2016_17,
            row.underp_payment_collar_2016_17,
            row.notes_underp_payment_collar_2017_18,
            row.underp_payment_collar_2017_18,
            row.notes_underp_payment_collar_2018_19,
            row.underp_payment_collar_2018_19,
            row.notes_underp_payment_collar_2019_20,
            row.underp_payment_collar_2019_20,
            row.underp_payment_deadband_2015_16,
            row.underp_payment_deadband_2016_17,
            row.underp_payment_deadband_2017_18,
            row.underp_payment_deadband_2018_19,
            row.underp_payment_deadband_2019_20,
            row.outp_payment_deadband_2015_16,
            row.outp_payment_deadband_2016_17,
            row.outp_payment_deadband_2017_18,
            row.outp_payment_deadband_2018_19,
            row.outp_payment_deadband_2019_20,
            row.outp_payment_cap_2015_16,
            row.outp_payment_cap_2016_17,
            row.outp_payment_cap_2017_18,
            row.outp_payment_cap_2018_19,
            row.outp_payment_cap_2019_20,
            row.notes_underp_payment1_incentive_rate_gbpm,
            row.underp_payment1_incentive_rate_gbpm,
            row.notes_underp_payment2_incentive_rate_gbpm,
            row.underp_payment2_incentive_rate_gbpm,
            row.notes_underp_payment3_incentive_rate_gbpm,
            row.underp_payment3_incentive_rate_gbpm,
            row.notes_underp_payment4_incentive_rate_gbpm,
            row.underp_payment4_incentive_rate_gbpm,
            row.notes_outp_payment1_incentive_rate_gbpm,
            row.outp_payment1_incentive_rate_gbpm,
            row.notes_outp_payment2_incentive_rate_gbpm,
            row.outp_payment2_incentive_rate_gbpm,
            row.standard_odi_operand,
            row.standard_odi_operand_note,
            row.performance_level_actual_2014_15,
            row.performance_level_actual_2015_16,
            row.pcl_met_2015_16,
            row.outp_payment_or_underp_payment_in_period_odis_2015_16,
            row.outp_payment_or_underp_payment_in_period_odis_gbpm_2015_16,
            row.notional_outp_payment_or_underp_payment_accrued_at_31_march_2016_2015_16,
            row.notional_outp_payment_or_underp_payment_accrued_at_31_march_2016_gbpm_2015_16,
            row.total_amp6_outp_payment_or_underp_payment_31_march_2020_forecast_2015_16,
            row.total_amp6_outp_payment_or_underp_payment_31_march_2020_forecast_gbpm_2015_16,
            row.performance_level_actual_2016_17,
            row.pcl_met_2016_17,
            row.outp_payment_or_underp_payment_in_period_odis_2016_17,
            row.outp_payment_or_underp_payment_in_period_odis_gbpm_2016_17,
            row.notional_outp_payment_or_underp_payment_accrued_at_31_march_2017_2016_17,
            row.notional_outp_payment_or_underp_payment_accrued_at_31_march_2017_gbpm_2016_17,
            row.total_amp6_outp_payment_or_underp_payment_31_march_2020_forecast_2016_17,
            row.total_amp6_outp_payment_or_underp_payment_31_march_2020_forecast_gbpm_2016_17,
            row.performance_level_actual_2017_18,
            row.pcl_met_2017_18,
            row.outp_payment_or_underp_payment_in_period_odis_2017_18,
            row.outp_payment_or_underp_payment_in_period_odis_gbpm_2017_18,
            row.notional_outp_payment_or_underp_payment_accrued_at_31_march_2018_2017_18,
            row.notional_outp_payment_or_underp_payment_accrued_at_31_march_2018_gbpm_2017_18,
            row.total_amp6_outp_payment_or_underp_payment_31_march_2020_forecast_2017_18,
            row.total_amp6_outp_payment_or_underp_payment_31_march_2020_forecast_gbpm_2017_18,
            row.performance_level_actual_2018_19,
            row.pcl_met_2018_19,
            row.outp_payment_or_underp_payment_in_period_odis_2018_19,
            row.outp_payment_or_underp_payment_in_period_odis_gbpm_2018_19,
            row.notional_outp_payment_or_underp_payment_accrued_at_31_march_2019_2018_19,
            row.notional_outp_payment_or_underp_payment_accrued_at_31_march_2019_gbpm_2018_19,
            row.total_amp6_outp_payment_or_underp_payment_31_march_2020_forecast_2018_19,
            row.total_amp6_outp_payment_or_underp_payment_31_march_2020_forecast_gbpm_2018_19,
            row.performance_level_actual_2019_20,
            row.pcl_met_2019_20,
            row.outp_payment_or_underp_payment_in_period_odis_2019_20,
            row.outp_payment_or_underp_payment_in_period_odis_gbpm_2019_20,
            row.notional_outp_payment_or_underp_payment_accrued_at_31_march_2020_2019_20,
            row.notional_outp_payment_or_underp_payment_accrued_at_31_march_2020_gbpm_2019_20,
            row.performance_level_actual_estimates_2019_20,
            row.pcl_met_estimates_2019_20,
            row.outp_payment_or_underp_payment_in_period_odis_estimates_2019_20,
            row.outp_payment_or_underp_payment_in_period_odis_gbpm_estimates_2019_20,
            row.notional_outp_payment_or_underp_payment_accrued_at_31_march_2020_estimates_2019_20,
            row.notional_outp_payment_or_underp_payment_accrued_at_31_march_2020_gbpm_estimates_2019_20,
            row.price_control_allocation_water_resources,
            row.price_control_allocation_water_network_plus,
            row.price_control_allocation_wastewater_network_plus,
            row.price_control_allocation_bioresources_sludge,
            row.price_control_allocation_residential_retail,
            row.price_control_allocation_business_retail,
            row.price_control_allocation_direct_procurement_for_customers,
            row.price_control_allocation_dummy_control)

    conn.commit()
    conn.close()
