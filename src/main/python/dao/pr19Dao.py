from util import dbUtils

def insert_pr19_data_in_table(df1):
    conn = dbUtils.sql_server_connection()
    schemanameused = dbUtils.create_schema()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM information_schema.tables where table_schema ='" + schemanameused + "' and table_name = 'PR19FinalCSVcreatedbyPython'")
    queryfortablecheck = cursor.fetchone()
    if queryfortablecheck is not None:
        print("Table PR19FinalCSVcreatedbyPython is existing")
        cursor.execute("DROP TABLE " + schemanameused + ".PR19FinalCSVcreatedbyPython")
        print("Dropped the existing PR19FinalCSVcreatedbyPython table")
        print("Creating new PR19FinalCSVcreatedbyPython table")
    else:
        print("Creating PR19FinalCSVcreatedbyPython table")
    cursor.execute(
        'CREATE TABLE ' + schemanameused + '.PR19FinalCSVcreatedbyPython (company nvarchar(max),unique_id nvarchar(max),outcome nvarchar(max),pc_ref nvarchar(max),performance_commitment nvarchar(max),pc_short_description nvarchar(max),price_control_allocation_water_resources float,price_control_allocation_water_network_plus float,price_control_allocation_wastewater_network_plus float,price_control_allocation_bioresources_sludge float,price_control_allocation_residential_retail float,price_control_allocation_business_retail float,price_control_allocation_direct_procurement_for_customers float,price_control_allocation_dummy_control float,odi_type nvarchar(max),odi_form nvarchar(max),odi_timing nvarchar(max),primary_category nvarchar(max),pc_unit nvarchar(max),pc_unit_description nvarchar(max),decimal_places nvarchar(max),direction_of_improving_performance nvarchar(max),common_and_comparable_bespoke_performance_commitment nvarchar(max),customers_relative_priority nvarchar(max),pcl_2020_21 nvarchar(max),pcl_2021_22 nvarchar(max),pcl_2022_23 nvarchar(max),pcl_2023_24 nvarchar(max),pcl_2024_25 nvarchar(max),financial_odi_2020_21 nvarchar(max),financial_odi_2021_22 nvarchar(max),financial_odi_2022_23 nvarchar(max),financial_odi_2023_24 nvarchar(max),financial_odi_2024_25 nvarchar(max),enhanced_underp_payment_collar_2020_21 nvarchar(max),enhanced_underp_payment_collar_2021_22 nvarchar(max),enhanced_underp_payment_collar_2022_23 nvarchar(max),enhanced_underp_payment_collar_2023_24 nvarchar(max),enhanced_underp_payment_collar_2024_25 nvarchar(max),standard_underp_payment_collar_2020_21 nvarchar(max),standard_underp_payment_collar_2021_22 nvarchar(max),standard_underp_payment_collar_2022_23 nvarchar(max),standard_underp_payment_collar_2023_24 nvarchar(max),standard_underp_payment_collar_2024_25 nvarchar(max),underp_payment_deadband_2020_21 nvarchar(max),underp_payment_deadband_2021_22 nvarchar(max),underp_payment_deadband_2022_23 nvarchar(max),underp_payment_deadband_2023_24 nvarchar(max),underp_payment_deadband_2024_25 nvarchar(max),outp_payment_deadband_2020_21 nvarchar(max),outp_payment_deadband_2021_22 nvarchar(max),outp_payment_deadband_2022_23 nvarchar(max),outp_payment_deadband_2023_24 nvarchar(max),outp_payment_deadband_2024_25 nvarchar(max),standard_outp_payment_cap_2020_21 nvarchar(max),standard_outp_payment_cap_2021_22 nvarchar(max),standard_outp_payment_cap_2022_23 nvarchar(max),standard_outp_payment_cap_2023_24 nvarchar(max),standard_outp_payment_cap_2024_25 nvarchar(max),enhanced_outp_payment_cap_2020_21 nvarchar(max),enhanced_outp_payment_cap_2021_22 nvarchar(max),enhanced_outp_payment_cap_2022_23 nvarchar(max),enhanced_outp_payment_cap_2023_24 nvarchar(max),enhanced_outp_payment_cap_2024_25 nvarchar(max),notes_underp_payment_incentive_standard_underp_payment1_tier2_where_tiers_apply nvarchar(max),underp_payment_incentive_standard_underp_payment1_tier2_where_tiers_apply float,notes_underp_payment_incentive_standard_underp_payment2_tier1_where_tiers_apply nvarchar(max),underp_payment_incentive_standard_underp_payment2_tier1_where_tiers_apply float,notes_underp_payment_incentive_standard_underp_payment3_tier3_where_tiers_apply nvarchar(max),underp_payment_incentive_standard_underp_payment3_tier3_where_tiers_apply float,notes_underp_payment_incentive_enhanced_underp_payment nvarchar(max),underp_payment_incentive_enhanced_underp_payment float,notes_outp_payment_incentive_standard_outp_payment1_tier2_where_tiers_apply nvarchar(max),outp_payment_incentive_standard_outp_payment1_tier2_where_tiers_apply float,notes_outp_payment_incentive_standard_outp_payment2_tier1_where_tiers_apply nvarchar(max),outp_payment_incentive_standard_outp_payment2_tier1_where_tiers_apply float,notes_outp_payment_incentive_standard_outp_payment3_tier3_where_tiers_apply nvarchar(max),outp_payment_incentive_standard_outp_payment3_tier3_where_tiers_apply float,notes_outp_payment_incentive_enhanced_outp_payment nvarchar(max),outp_payment_incentive_enhanced_outp_payment float,standard_odi_cal nvarchar(max),standard_odi_operand float,standard_odi_operand_note nvarchar(max))')
    for row in df1.itertuples():
        cursor.execute('''
        INSERT INTO ''' + schemanameused + '''.PR19FinalCSVcreatedbyPython (company ,unique_id ,outcome ,pc_ref ,performance_commitment ,pc_short_description ,price_control_allocation_water_resources ,price_control_allocation_water_network_plus ,price_control_allocation_wastewater_network_plus ,price_control_allocation_bioresources_sludge ,price_control_allocation_residential_retail ,price_control_allocation_business_retail ,price_control_allocation_direct_procurement_for_customers ,price_control_allocation_dummy_control ,odi_type ,odi_form ,odi_timing ,primary_category ,pc_unit ,pc_unit_description ,decimal_places ,direction_of_improving_performance ,common_and_comparable_bespoke_performance_commitment ,customers_relative_priority ,pcl_2020_21 ,pcl_2021_22 ,pcl_2022_23 ,pcl_2023_24 ,pcl_2024_25 ,financial_odi_2020_21 ,financial_odi_2021_22 ,financial_odi_2022_23 ,financial_odi_2023_24 ,financial_odi_2024_25 ,enhanced_underp_payment_collar_2020_21 ,enhanced_underp_payment_collar_2021_22 ,enhanced_underp_payment_collar_2022_23 ,enhanced_underp_payment_collar_2023_24 ,enhanced_underp_payment_collar_2024_25 ,standard_underp_payment_collar_2020_21 ,standard_underp_payment_collar_2021_22 ,standard_underp_payment_collar_2022_23 ,standard_underp_payment_collar_2023_24 ,standard_underp_payment_collar_2024_25 ,underp_payment_deadband_2020_21 ,underp_payment_deadband_2021_22 ,underp_payment_deadband_2022_23 ,underp_payment_deadband_2023_24 ,underp_payment_deadband_2024_25 ,outp_payment_deadband_2020_21 ,outp_payment_deadband_2021_22 ,outp_payment_deadband_2022_23 ,outp_payment_deadband_2023_24 ,outp_payment_deadband_2024_25 ,standard_outp_payment_cap_2020_21 ,standard_outp_payment_cap_2021_22 ,standard_outp_payment_cap_2022_23 ,standard_outp_payment_cap_2023_24 ,standard_outp_payment_cap_2024_25 ,enhanced_outp_payment_cap_2020_21 ,enhanced_outp_payment_cap_2021_22 ,enhanced_outp_payment_cap_2022_23 ,enhanced_outp_payment_cap_2023_24 ,enhanced_outp_payment_cap_2024_25 ,notes_underp_payment_incentive_standard_underp_payment1_tier2_where_tiers_apply ,underp_payment_incentive_standard_underp_payment1_tier2_where_tiers_apply ,notes_underp_payment_incentive_standard_underp_payment2_tier1_where_tiers_apply ,underp_payment_incentive_standard_underp_payment2_tier1_where_tiers_apply ,notes_underp_payment_incentive_standard_underp_payment3_tier3_where_tiers_apply ,underp_payment_incentive_standard_underp_payment3_tier3_where_tiers_apply ,notes_underp_payment_incentive_enhanced_underp_payment ,underp_payment_incentive_enhanced_underp_payment ,notes_outp_payment_incentive_standard_outp_payment1_tier2_where_tiers_apply ,outp_payment_incentive_standard_outp_payment1_tier2_where_tiers_apply ,notes_outp_payment_incentive_standard_outp_payment2_tier1_where_tiers_apply ,outp_payment_incentive_standard_outp_payment2_tier1_where_tiers_apply ,notes_outp_payment_incentive_standard_outp_payment3_tier3_where_tiers_apply ,outp_payment_incentive_standard_outp_payment3_tier3_where_tiers_apply ,notes_outp_payment_incentive_enhanced_outp_payment ,outp_payment_incentive_enhanced_outp_payment ,standard_odi_cal ,standard_odi_operand ,standard_odi_operand_note)
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
        ''',
                       row.company,
                       row.unique_id,
                       row.outcome,
                       row.pc_ref,
                       row.performance_commitment,
                       row.pc_short_description,
                       row.price_control_allocation_water_resources,
                       row.price_control_allocation_water_network_plus,
                       row.price_control_allocation_wastewater_network_plus,
                       row.price_control_allocation_bioresources_sludge,
                       row.price_control_allocation_residential_retail,
                       row.price_control_allocation_business_retail,
                       row.price_control_allocation_direct_procurement_for_customers,
                       row.price_control_allocation_dummy_control,
                       row.odi_type,
                       row.odi_form,
                       row.odi_timing,
                       row.primary_category,
                       row.pc_unit,
                       row.pc_unit_description,
                       row.decimal_places,
                       row.direction_of_improving_performance,
                       row.common_and_comparable_bespoke_performance_commitment,
                       row.customers_relative_priority,
                       row.pcl_2020_21,
                       row.pcl_2021_22,
                       row.pcl_2022_23,
                       row.pcl_2023_24,
                       row.pcl_2024_25,
                       row.financial_odi_2020_21,
                       row.financial_odi_2021_22,
                       row.financial_odi_2022_23,
                       row.financial_odi_2023_24,
                       row.financial_odi_2024_25,
                       row.enhanced_underp_payment_collar_2020_21,
                       row.enhanced_underp_payment_collar_2021_22,
                       row.enhanced_underp_payment_collar_2022_23,
                       row.enhanced_underp_payment_collar_2023_24,
                       row.enhanced_underp_payment_collar_2024_25,
                       row.standard_underp_payment_collar_2020_21,
                       row.standard_underp_payment_collar_2021_22,
                       row.standard_underp_payment_collar_2022_23,
                       row.standard_underp_payment_collar_2023_24,
                       row.standard_underp_payment_collar_2024_25,
                       row.underp_payment_deadband_2020_21,
                       row.underp_payment_deadband_2021_22,
                       row.underp_payment_deadband_2022_23,
                       row.underp_payment_deadband_2023_24,
                       row.underp_payment_deadband_2024_25,
                       row.outp_payment_deadband_2020_21,
                       row.outp_payment_deadband_2021_22,
                       row.outp_payment_deadband_2022_23,
                       row.outp_payment_deadband_2023_24,
                       row.outp_payment_deadband_2024_25,
                       row.standard_outp_payment_cap_2020_21,
                       row.standard_outp_payment_cap_2021_22,
                       row.standard_outp_payment_cap_2022_23,
                       row.standard_outp_payment_cap_2023_24,
                       row.standard_outp_payment_cap_2024_25,
                       row.enhanced_outp_payment_cap_2020_21,
                       row.enhanced_outp_payment_cap_2021_22,
                       row.enhanced_outp_payment_cap_2022_23,
                       row.enhanced_outp_payment_cap_2023_24,
                       row.enhanced_outp_payment_cap_2024_25,
                       row.notes_underp_payment_incentive_standard_underp_payment1_tier2_where_tiers_apply,
                       row.underp_payment_incentive_standard_underp_payment1_tier2_where_tiers_apply,
                       row.notes_underp_payment_incentive_standard_underp_payment2_tier1_where_tiers_apply,
                       row.underp_payment_incentive_standard_underp_payment2_tier1_where_tiers_apply,
                       row.notes_underp_payment_incentive_standard_underp_payment3_tier3_where_tiers_apply,
                       row.underp_payment_incentive_standard_underp_payment3_tier3_where_tiers_apply,
                       row.notes_underp_payment_incentive_enhanced_underp_payment,
                       row.underp_payment_incentive_enhanced_underp_payment,
                       row.notes_outp_payment_incentive_standard_outp_payment1_tier2_where_tiers_apply,
                       row.outp_payment_incentive_standard_outp_payment1_tier2_where_tiers_apply,
                       row.notes_outp_payment_incentive_standard_outp_payment2_tier1_where_tiers_apply,
                       row.outp_payment_incentive_standard_outp_payment2_tier1_where_tiers_apply,
                       row.notes_outp_payment_incentive_standard_outp_payment3_tier3_where_tiers_apply,
                       row.outp_payment_incentive_standard_outp_payment3_tier3_where_tiers_apply,
                       row.notes_outp_payment_incentive_enhanced_outp_payment,
                       row.outp_payment_incentive_enhanced_outp_payment,
                       row.standard_odi_cal,
                       row.standard_odi_operand,
                       row.standard_odi_operand_note
                       )

    conn.commit()
    conn.close()