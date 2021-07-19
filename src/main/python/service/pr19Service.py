import pandas as pd
from util import validations
from dao import pr19Dao


def upload_data_PR19_base(cli_args):
    input_file_name = cli_args.input_file
    pd.set_option("display.precision", 18)

    df1 = pd.read_excel(input_file_name,
                        sheet_name='App1', usecols="A,C:D,F:P,R:Z,AF,AQ:AU,BL:DE", skiprows=[0, 1, 2, 3, 4])
    df1.columns = ['company', 'unique_id', 'outcome', 'pc_ref', 'performance_commitment', 'pc_short_description',
                   'price_control_allocation_water_resources', 'price_control_allocation_water_network_plus',
                   'price_control_allocation_wastewater_network_plus', 'price_control_allocation_bioresources_sludge',
                   'price_control_allocation_residential_retail', 'price_control_allocation_business_retail',
                   'price_control_allocation_direct_procurement_for_customers',
                   'price_control_allocation_dummy_control',
                   'odi_type', 'odi_form', 'odi_timing', 'primary_category', 'pc_unit', 'pc_unit_description',
                   'decimal_places', 'direction_of_improving_performance',
                   'common_and_comparable_bespoke_performance_commitment', 'customers_relative_priority', 'pcl_2020_21',
                   'pcl_2021_22',
                   'pcl_2022_23',
                   'pcl_2023_24', 'pcl_2024_25', 'financial_odi_2020_21', 'financial_odi_2021_22',
                   'financial_odi_2022_23',
                   'financial_odi_2023_24', 'financial_odi_2024_25', 'enhanced_underp_payment_collar_2020_21',
                   'enhanced_underp_payment_collar_2021_22', 'enhanced_underp_payment_collar_2022_23',
                   'enhanced_underp_payment_collar_2023_24', 'enhanced_underp_payment_collar_2024_25',
                   'standard_underp_payment_collar_2020_21', 'standard_underp_payment_collar_2021_22',
                   'standard_underp_payment_collar_2022_23', 'standard_underp_payment_collar_2023_24',
                   'standard_underp_payment_collar_2024_25', 'underp_payment_deadband_2020_21',
                   'underp_payment_deadband_2021_22', 'underp_payment_deadband_2022_23',
                   'underp_payment_deadband_2023_24',
                   'underp_payment_deadband_2024_25', 'outp_payment_deadband_2020_21', 'outp_payment_deadband_2021_22',
                   'outp_payment_deadband_2022_23', 'outp_payment_deadband_2023_24', 'outp_payment_deadband_2024_25',
                   'standard_outp_payment_cap_2020_21', 'standard_outp_payment_cap_2021_22',
                   'standard_outp_payment_cap_2022_23', 'standard_outp_payment_cap_2023_24',
                   'standard_outp_payment_cap_2024_25', 'enhanced_outp_payment_cap_2020_21',
                   'enhanced_outp_payment_cap_2021_22', 'enhanced_outp_payment_cap_2022_23',
                   'enhanced_outp_payment_cap_2023_24', 'enhanced_outp_payment_cap_2024_25',
                   'underp_payment_incentive_standard_underp_payment1_tier2_where_tiers_apply_column',
                   'underp_payment_incentive_standard_underp_payment2_tier1_where_tiers_apply_column',
                   'underp_payment_incentive_standard_underp_payment3_tier3_where_tiers_apply_column',
                   'underp_payment_incentive_enhanced_underp_payment_column',
                   'outp_payment_incentive_standard_outp_payment1_tier2_where_tiers_apply_column',
                   'outp_payment_incentive_standard_outp_payment2_tier1_where_tiers_apply_column',
                   'outp_payment_incentive_standard_outp_payment3_tier3_where_tiers_apply_column',
                   'outp_payment_incentive_enhanced_outp_payment_column', 'standard_odi_cal', 'standard_odi_operand',
                   'standard_odi_operand_note']
    df1 = df1.astype({'company': 'object', 'unique_id': 'object', 'outcome': 'object', 'pc_ref': 'object',
                      'performance_commitment': 'object', 'pc_short_description': 'object',
                      'price_control_allocation_water_resources': 'float64',
                      'price_control_allocation_water_network_plus': 'float64',
                      'price_control_allocation_wastewater_network_plus': 'float64',
                      'price_control_allocation_bioresources_sludge': 'float64',
                      'price_control_allocation_residential_retail': 'float64',
                      'price_control_allocation_business_retail': 'float64',
                      'price_control_allocation_direct_procurement_for_customers': 'float64',
                      'price_control_allocation_dummy_control': 'float64',
                      'odi_type': 'object', 'odi_form': 'object', 'odi_timing': 'object', 'primary_category': 'object',
                      'pc_unit': 'object', 'pc_unit_description': 'object',
                      'decimal_places': 'object', 'direction_of_improving_performance': 'object',
                      'common_and_comparable_bespoke_performance_commitment': 'object',
                      'customers_relative_priority': 'object',
                      'pcl_2020_21': 'object', 'pcl_2021_22': 'object', 'pcl_2022_23': 'object',
                      'pcl_2023_24': 'object', 'pcl_2024_25': 'object', 'financial_odi_2020_21': 'object',
                      'financial_odi_2021_22': 'object', 'financial_odi_2022_23': 'object',
                      'financial_odi_2023_24': 'object', 'financial_odi_2024_25': 'object',
                      'enhanced_underp_payment_collar_2020_21': 'object',
                      'enhanced_underp_payment_collar_2021_22': 'object',
                      'enhanced_underp_payment_collar_2022_23': 'object',
                      'enhanced_underp_payment_collar_2023_24': 'object',
                      'enhanced_underp_payment_collar_2024_25': 'object',
                      'standard_underp_payment_collar_2020_21': 'object',
                      'standard_underp_payment_collar_2021_22': 'object',
                      'standard_underp_payment_collar_2022_23': 'object',
                      'standard_underp_payment_collar_2023_24': 'object',
                      'standard_underp_payment_collar_2024_25': 'object', 'underp_payment_deadband_2020_21': 'object',
                      'underp_payment_deadband_2021_22': 'object', 'underp_payment_deadband_2022_23': 'object',
                      'underp_payment_deadband_2023_24': 'object',
                      'underp_payment_deadband_2024_25': 'object', 'outp_payment_deadband_2020_21': 'object',
                      'outp_payment_deadband_2021_22': 'object',
                      'outp_payment_deadband_2022_23': 'object', 'outp_payment_deadband_2023_24': 'object',
                      'outp_payment_deadband_2024_25': 'object',
                      'standard_outp_payment_cap_2020_21': 'object', 'standard_outp_payment_cap_2021_22': 'object',
                      'standard_outp_payment_cap_2022_23': 'object', 'standard_outp_payment_cap_2023_24': 'object',
                      'standard_outp_payment_cap_2024_25': 'object', 'enhanced_outp_payment_cap_2020_21': 'object',
                      'enhanced_outp_payment_cap_2021_22': 'object', 'enhanced_outp_payment_cap_2022_23': 'object',
                      'enhanced_outp_payment_cap_2023_24': 'object', 'enhanced_outp_payment_cap_2024_25': 'object',
                      'underp_payment_incentive_standard_underp_payment1_tier2_where_tiers_apply_column': 'object',
                      'underp_payment_incentive_standard_underp_payment2_tier1_where_tiers_apply_column': 'object',
                      'underp_payment_incentive_standard_underp_payment3_tier3_where_tiers_apply_column': 'object',
                      'underp_payment_incentive_enhanced_underp_payment_column': 'object',
                      'outp_payment_incentive_standard_outp_payment1_tier2_where_tiers_apply_column': 'object',
                      'outp_payment_incentive_standard_outp_payment2_tier1_where_tiers_apply_column': 'object',
                      'outp_payment_incentive_standard_outp_payment3_tier3_where_tiers_apply_column': 'object',
                      'outp_payment_incentive_enhanced_outp_payment_column': 'object', 'standard_odi_cal': 'object',
                      'standard_odi_operand': 'object',
                      'standard_odi_operand_note': 'object'})
    listofPR19columns = []
    for column in df1:
        listofPR19columns.append(column)
    for j in listofPR19columns:
        df1[j] = validations.replace_spaces(df1, j)
        df1[j] = validations.replace_dashes_with_nan(df1, j)
        df1[j] = validations.replace_null_with_None(df1, j)
        if j in ['scheme_specific_factor', 'asset_health', 'nep', 'aim']:
            df1[j] = validations.replace_yes_with_true(df1, j)
        if j in ['underp_payment_incentive_standard_underp_payment1_tier2_where_tiers_apply_column',
                 'underp_payment_incentive_standard_underp_payment2_tier1_where_tiers_apply_column',
                 'underp_payment_incentive_standard_underp_payment3_tier3_where_tiers_apply_column',
                 'underp_payment_incentive_enhanced_underp_payment_column',
                 'outp_payment_incentive_standard_outp_payment1_tier2_where_tiers_apply_column',
                 'outp_payment_incentive_standard_outp_payment2_tier1_where_tiers_apply_column',
                 'outp_payment_incentive_standard_outp_payment3_tier3_where_tiers_apply_column',
                 'outp_payment_incentive_enhanced_outp_payment_column']:
            validations.is_numeric_and_only_numeric(df1, j)
    df1 = df1.rename(columns={
        'onlynumeric_underp_payment_incentive_standard_underp_payment1_tier2_where_tiers_apply_column': 'underp_payment_incentive_standard_underp_payment1_tier2_where_tiers_apply',
        'onlynumeric_underp_payment_incentive_standard_underp_payment2_tier1_where_tiers_apply_column': 'underp_payment_incentive_standard_underp_payment2_tier1_where_tiers_apply',
        'onlynumeric_underp_payment_incentive_standard_underp_payment3_tier3_where_tiers_apply_column': 'underp_payment_incentive_standard_underp_payment3_tier3_where_tiers_apply',
        'onlynumeric_underp_payment_incentive_enhanced_underp_payment_column': 'underp_payment_incentive_enhanced_underp_payment',
        'onlynumeric_outp_payment_incentive_standard_outp_payment1_tier2_where_tiers_apply_column': 'outp_payment_incentive_standard_outp_payment1_tier2_where_tiers_apply',
        'onlynumeric_outp_payment_incentive_standard_outp_payment2_tier1_where_tiers_apply_column': 'outp_payment_incentive_standard_outp_payment2_tier1_where_tiers_apply',
        'onlynumeric_outp_payment_incentive_standard_outp_payment3_tier3_where_tiers_apply_column': 'outp_payment_incentive_standard_outp_payment3_tier3_where_tiers_apply',
        'onlynumeric_outp_payment_incentive_enhanced_outp_payment_column': 'outp_payment_incentive_enhanced_outp_payment',
        'notes_underp_payment_incentive_standard_underp_payment1_tier2_where_tiers_apply_column': 'notes_underp_payment_incentive_standard_underp_payment1_tier2_where_tiers_apply',
        'notes_underp_payment_incentive_standard_underp_payment2_tier1_where_tiers_apply_column': 'notes_underp_payment_incentive_standard_underp_payment2_tier1_where_tiers_apply',
        'notes_underp_payment_incentive_standard_underp_payment3_tier3_where_tiers_apply_column': 'notes_underp_payment_incentive_standard_underp_payment3_tier3_where_tiers_apply',
        'notes_underp_payment_incentive_enhanced_underp_payment_column': 'notes_underp_payment_incentive_enhanced_underp_payment',
        'notes_outp_payment_incentive_standard_outp_payment1_tier2_where_tiers_apply_column': 'notes_outp_payment_incentive_standard_outp_payment1_tier2_where_tiers_apply',
        'notes_outp_payment_incentive_standard_outp_payment2_tier1_where_tiers_apply_column': 'notes_outp_payment_incentive_standard_outp_payment2_tier1_where_tiers_apply',
        'notes_outp_payment_incentive_standard_outp_payment3_tier3_where_tiers_apply_column': 'notes_outp_payment_incentive_standard_outp_payment3_tier3_where_tiers_apply',
        'notes_outp_payment_incentive_enhanced_outp_payment_column': 'notes_outp_payment_incentive_enhanced_outp_payment'})
    df1.drop(columns=['isnumeric_underp_payment_incentive_standard_underp_payment1_tier2_where_tiers_apply_column',
                      'isnumeric_underp_payment_incentive_standard_underp_payment2_tier1_where_tiers_apply_column',
                      'isnumeric_underp_payment_incentive_standard_underp_payment3_tier3_where_tiers_apply_column',
                      'isnumeric_underp_payment_incentive_enhanced_underp_payment_column',
                      'isnumeric_outp_payment_incentive_standard_outp_payment1_tier2_where_tiers_apply_column',
                      'isnumeric_outp_payment_incentive_standard_outp_payment2_tier1_where_tiers_apply_column',
                      'isnumeric_outp_payment_incentive_standard_outp_payment3_tier3_where_tiers_apply_column',
                      'isnumeric_outp_payment_incentive_enhanced_outp_payment_column'], axis=1, inplace=True)

    if not cli_args.test_run:
        pr19Dao.insert_pr19_data_in_table(df1)
