import pandas as pd
import os.path, datetime
import math
from actuals.pcRecord import PCRecord
from actuals.pcCommonData import PCCommonData
from dao import actualsDao
import numpy as np


comment = 'Initial APR load'
excel_user = 'Fred'

submission_status_actual = 'Actual'
submission_status_past_performance = 'Past performance'


def get_bespoke_text(pc_sheet):
    if ("3A" == pc_sheet):
        return 'Bespoke PCs - Water and Retail (Financial)'
    elif ("3B" == pc_sheet):
        return 'Bespoke PCs - Wastewater (Financial)'
    elif ("3E" == pc_sheet):
        return 'Bespoke PCs '
    return None

def select_all_pcs(data_area_of_all_pcs):
    all_pcs = data_area_of_all_pcs[data_area_of_all_pcs.iloc[:,1].notnull()]
    return all_pcs

def select_bespoke_pcs(pc_sheet, data_area_of_all_pcs):
    bespoke_text = get_bespoke_text(pc_sheet)
    row_index_with_bespoke = np.where(
        (True == (bespoke_text == data_area_of_all_pcs.iloc[:,0])) & (data_area_of_all_pcs.iloc[:,1].isnull()))
    if (0 == len(row_index_with_bespoke[0])):
        print("Sheet: ", pc_sheet, " Bespoke text '", bespoke_text, "' not found")
        return pd.DataFrame()

    index_of_bespoke_row = row_index_with_bespoke[0][0]
    data_area_of_bespoke_pcs_only = data_area_of_all_pcs.iloc[index_of_bespoke_row:, 0:10]
    bespoke_pcs_only = data_area_of_bespoke_pcs_only[data_area_of_bespoke_pcs_only.iloc[:,1].notnull()]
    return bespoke_pcs_only

def read_pc_sheet(excel_sheet, pc_sheet, outcome_performance_type, pc_records, common_data):
    spreadsheet = pd.read_excel(excel_sheet, sheet_name=pc_sheet, header=None)
    spreadsheet_updated = datetime.datetime.utcfromtimestamp(os.path.getmtime(excel_sheet))
    data_area_of_all_pcs = spreadsheet.iloc[5:, 1:10]
    # pc_data = select_all_pcs(data_area_of_all_pcs)
    pc_data = select_bespoke_pcs(pc_sheet, data_area_of_all_pcs)
    print(pc_data)
    for i in range(len(pc_data)):
        if ("3A" == pc_sheet or "3B" == pc_sheet):
            pc_record = PCRecord(spreadsheet_updated, outcome_performance_type, pc_data.iloc[i, 0], pc_data.iloc[i, 1], pc_data.iloc[i, 2], pc_data.iloc[i, 3], pc_data.iloc[i, 4], pc_data.iloc[i, 5], pc_data.iloc[i, 6], pc_data.iloc[i, 7], pc_data.iloc[i, 8], common_data.company_acronym, common_data.company_name, common_data.year, submission_status_actual, common_data.excel_user, common_data.excel_file, common_data.comment)
        elif ("3E" == pc_sheet):
            pc_record = PCRecord(spreadsheet_updated, outcome_performance_type, pc_data.iloc[i, 0], pc_data.iloc[i, 1], pc_data.iloc[i, 2], pc_data.iloc[i, 3], None, pc_data.iloc[i, 5], pc_data.iloc[i, 6], None, None, common_data.company_acronym, common_data.company_name, common_data.year, submission_status_actual, common_data.excel_user, common_data.excel_file, common_data.comment)
        pc_records[pc_record.unique_reference + pc_record.year] = pc_record
        if ("2020-21" == common_data.year and not isCellEmpty(pc_data.iloc[i, 4])):
            if ("3A" == pc_sheet or "3B" == pc_sheet):
                pc_record = PCRecord(spreadsheet_updated, outcome_performance_type, pc_data.iloc[i, 0], pc_data.iloc[i, 1], pc_data.iloc[i, 2], pc_data.iloc[i, 3], None, pc_data.iloc[i, 4], '-', None, None, common_data.company_acronym, common_data.company_name, "2019-20", submission_status_past_performance, common_data.excel_user, common_data.excel_file, common_data.comment)
            elif ("3E" == pc_sheet):
                pc_record = PCRecord(spreadsheet_updated, outcome_performance_type, pc_data.iloc[i, 0], pc_data.iloc[i, 1], pc_data.iloc[i, 2], pc_data.iloc[i, 3], None, pc_data.iloc[i, 4], '-', None, None, common_data.company_acronym, common_data.company_name, "2019-20", submission_status_past_performance, common_data.excel_user, common_data.excel_file, common_data.comment)
            pc_records[pc_record.unique_reference + pc_record.year] = pc_record

def isCellEmpty(cell):
        # This test does not work
        # if (isinstance(cell, (int, float)) and not cell):
        #     print("type: ", type(cell), " empty with not cell")

        # This is all ok
        if (None == cell):
            # print("Null cell")
            return True
        if (isinstance(cell, (int, float)) and math.isnan(cell)):
            # print("type: ", type(cell), " empty")
            return True
        if (isinstance(cell, str) and not cell):
            # print("type: ", type(cell), " str")
            return True
        if (isinstance(cell, datetime.datetime) and not cell):
            # print("type: ", type(cell), " empty")
            return True
        return False

def read_validation_summary_sheet(excel_sheet, common_data, companies):
    ss_validation_summary = pd.read_excel(excel_sheet, sheet_name='Validation summary', header=None)
    common_data.year = ss_validation_summary.iloc[1, 1]
    common_data.company_name = ss_validation_summary.iloc[2, 1]
    common_data.company_acronym = companies[common_data.company_name]
 
def read_validation_sheet(excel_sheet):
    ss_validation = pd.read_excel(excel_sheet, sheet_name='Validation', header=None)
    data_area = ss_validation.iloc[5:, 1:3]
    data_area = data_area[data_area.iloc[:,1].notnull()]
    companies = {} 
    for i in range(len(data_area)):
        companies[data_area.iloc[i, 0]] = data_area.iloc[i, 1]
    return companies
    
def print_all_records(pc_records):
    for key in pc_records:
        print(key)
        pc_records.get(key).print_content()
        print('')

def print_common_data(common_data):
    print("common_data")
    print(common_data.year)
    print(common_data.company_acronym)
    print(common_data.company_name)
    print(common_data.excel_user)
    print(common_data.excel_file)
    print(common_data.comment)

def record_batch_data(excel_sheet, common_data):
    common_data.excel_user = excel_user
    common_data.excel_file = excel_sheet
    common_data.comment = comment

def read_sheets(excel_sheet):
    # Read sheets
    common_data = PCCommonData()
    record_batch_data(excel_sheet, common_data)
    companies = read_validation_sheet(excel_sheet)
    read_validation_summary_sheet(excel_sheet, common_data, companies)
    print_common_data(common_data)

    pc_records = {}
    read_pc_sheet(excel_sheet, "3A", "Water performance commitments (financial)", pc_records, common_data)
    read_pc_sheet(excel_sheet, "3B", "Wastewater performance commitments (financial)", pc_records, common_data)
    read_pc_sheet(excel_sheet, "3E", "Non financial performance commitments", pc_records, common_data)
    print_all_records(pc_records)
    # print("Number of PCs = ", len(pc_records))
    return pc_records


def write_to_database(pc_records):
    records_for_db = []
    for value in pc_records.values():
        records_for_db.append(value.data_for_db())
        # print(value.data_for_db())
        # print('')
    actualsDao.insert_to_actuals_table(records_for_db)

    

def process_actuals(cli_args):
    pc_records = read_sheets(cli_args.input_file)
    if (not cli_args.test_run):
        write_to_database(pc_records)



# code to use data frame validation.
# Note: validations actually corrects the data rather than validating it.
# I don't think this is needed at present as:
# 1. As yet there is no use case to correct any of the data.
# 2. Using existing validation routines means re-writing data access to use dataframes. 
# This is left here as we may need it in the future if we need to correct data.
# Validation of data is a separate story, which isn't specified yet.
# df= pd.DataFrame(records_for_db)
# df.columns= ['updated_at', 'excel_file', 'excel_user', 'comment', 'amp', 'year', 'submission_status', 
#              'unique_reference', 'company_acronym', 'company_name','pcl_actual_cry', 'pcl_met', 
#              'outperformance_or_underperformance_payment',  'forecast_of_total_2020_25_outperformance_or_underperformance_payment']  # call them whatever you like

# list_of_cols = []
# for column in df:
#     list_of_cols.append(column)
# for i in list_of_cols:
#     # full set of fields as a template
#     # if i in ['updated_at', 'excel_file', 'excel_user', 'comment', 'amp', 'year', 'submission_status', 
#     #          'unique_reference', 'company_acronym', 'company_name','pcl_actual_cry', 'pcl_met', 
#     #          'outperformance_or_underperformance_payment',  'forecast_of_total_2020_25_outperformance_or_underperformance_payment']:

#     # not required
#     # df[i] = validations.replace_null_with_None(df, i)
#     if i in ['pcl_met']:
#        df[i] = validations.replace_dashes_with_nan(df, i)

# df.to_csv('fred.csv')



