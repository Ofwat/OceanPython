# import datetime

import numpy as np


# import pandas as pd


def replace_spaces(dataframe, iteratorvariable):
    return dataframe[iteratorvariable].replace(r'^\s*$', np.nan, regex=True)


def replace_dashes_with_nan(dataframe, iteratorvariable):
    return dataframe[iteratorvariable].replace('-', np.nan)


def replace_null_with_None(dataframe, iteratorvariable):
    return np.where(dataframe[iteratorvariable].isnull(), None, dataframe[iteratorvariable])


def replace_yes_with_true(dataframe, iteratorvariable):
    return np.where(dataframe[iteratorvariable].str.lower() == 'yes', 'TRUE', None)


def is_numeric_and_only_numeric(dataframe, iteratorvariable):
    dataframe['isnumeric_' + iteratorvariable] = (dataframe[iteratorvariable].apply(
        lambda x: isinstance(x, (int, np.int64)))) | (dataframe[iteratorvariable].apply(
            lambda x: isinstance(x, (float, np.float64))))
    dataframe['isnumeric_' + iteratorvariable].astype('bool')
    dataframe['onlynumeric_' + iteratorvariable] = ''
    dataframe['onlynumeric_' + iteratorvariable] = np.where(dataframe['isnumeric_' + iteratorvariable] == True,
                                                            dataframe[iteratorvariable], None)
    na_mask = dataframe['onlynumeric_' + iteratorvariable].notnull()
    dataframe.loc[na_mask, 'onlynumeric_' + iteratorvariable] = dataframe.loc[
        na_mask, 'onlynumeric_' + iteratorvariable].astype('float64').round(18)
    dataframe['notes_' + iteratorvariable] = ''
    dataframe['notes_' + iteratorvariable] = np.where(dataframe['isnumeric_' + iteratorvariable] == False,
                                                      dataframe[iteratorvariable], None)
    na_mask = dataframe['notes_' + iteratorvariable].notnull()


def change_company_to_UUW(dataframe):
    dataframe['company'] = np.where((dataframe.company == 'UU'), 'UUW', dataframe.company)
    return dataframe['company']

# Commenting the method which rounds the time value in the columns eg. 19:17:415 = 19:17 /16:58.876 = 16:59
# is noted till milliseconds
# def convert_time(dataframe, iteratorvariable):
#     new_list_of_tuple1 = []
#     for index in dataframe[iteratorvariable].items():
#         new_list_of_tuple = []
#         list_of_tuple = list(index)
#         first_element_of_list = list_of_tuple[1]
#         if isinstance(first_element_of_list, type(datetime.time(1, 19, 17, 468000))):
#             if first_element_of_list.microsecond > 500000:
#                 first_element_of_list = first_element_of_list.replace(microsecond=0)
#                 first_element_of_list = first_element_of_list.replace(second=first_element_of_list.second + 1)
#             else:
#                 first_element_of_list = first_element_of_list.replace(microsecond=0)
#                 first_element_of_list = first_element_of_list.replace(second=first_element_of_list.second)
#         new_list_of_tuple.append(first_element_of_list)
#         new_list_of_tuple1 += new_list_of_tuple
#     new_index = pd.Series(new_list_of_tuple1)
#     return new_index
#
# Commenting the method which makes each value in the columns as string so each value with decimal and each time value
# is noted till milliseconds eg. 19.2344444444 = 19.2344444444 and 19:17:415 = 19:17:415
# Logic which is yet to implement is as we make everything str it will even make all None to 'None' and not NULL.
# def making_all_columns_to_read_as_string(dataframe, iteratorvariable):
#     new_list_of_tuple1 = []
#     for index in dataframe[iteratorvariable].items():
#         new_list_of_tuple = []
#         list_of_tuple = list(index)
#         first_element_of_list = list_of_tuple[1]
#         if type(first_element_of_list) == int or type(first_element_of_list) == float:
#             first_element_of_list = round(first_element_of_list, 18)
#         elif isinstance(first_element_of_list, type(None)):
#             first_element_of_list = None
#         new_list_of_tuple.append(str(first_element_of_list))
#         new_list_of_tuple1 += new_list_of_tuple
#     new_index = pd.Series(new_list_of_tuple1)
#     return new_index
