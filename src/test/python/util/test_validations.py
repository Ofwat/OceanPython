import unittest

import numpy as np
import pandas as pd
from pandas._testing import assert_frame_equal

from src.main.python.util import validations


class TestValidatation(unittest.TestCase):

    def test_replace_spaces(self):
        expected_value = {'column1': [2.1, ' ', 'A sentence']}
        expected_df = pd.DataFrame(data=expected_value)

        expected_value_from_method = validations.replace_spaces(expected_df, 'column1')
        expected_df_from_method = expected_value_from_method.to_frame()

        actual_value = {'column1': [2.1, np.nan, 'A sentence']}
        actual_df = pd.DataFrame(data=actual_value)

        assert_frame_equal(expected_df_from_method, actual_df)

    def test_replace_dashes_with_nan(self):
        expected_value = {'column1': [2.1, '-', 'A sentence']}
        expected_df = pd.DataFrame(data=expected_value)

        expected_value_from_method = validations.replace_dashes_with_nan(expected_df, 'column1')
        expected_df_from_method = expected_value_from_method.to_frame()

        actual_value = {'column1': [2.1, np.nan, 'A sentence']}
        actual_df = pd.DataFrame(data=actual_value)

        assert_frame_equal(expected_df_from_method, actual_df)

    def test_replace_null_with_None(self):
        expected_value = {'column1': [2.1, np.nan, 'A sentence']}
        expected_df = pd.DataFrame(data=expected_value)

        expected_value_from_method = validations.replace_null_with_None(expected_df, 'column1')
        expected_df_from_method = pd.DataFrame(data=expected_value_from_method, columns=["column1"])

        actual_value = {'column1': [2.1, None, 'A sentence']}
        actual_df = pd.DataFrame(data=actual_value)

        assert_frame_equal(expected_df_from_method, actual_df)

    def test_replace_yes_with_true(self):
        expected_value = {'column1': [2.1, 'Yes', 'A sentence']}
        expected_df = pd.DataFrame(data=expected_value)

        expected_value_from_method = validations.replace_yes_with_true(expected_df, 'column1')
        expected_df_from_method = pd.DataFrame(data=expected_value_from_method, columns=["column1"])

        actual_value = {'column1': [None, 'TRUE', None]}
        actual_df = pd.DataFrame(data=actual_value)

        assert_frame_equal(expected_df_from_method, actual_df)

    def test_is_numeric_and_only_numeric(self):
        expected_value = {'column1': [2.13456345634564563456, 0.0000542, 24]}
        expected_df = pd.DataFrame(data=expected_value)

        validations.is_numeric_and_only_numeric(expected_df, 'column1')

        actual_value = {'column1': [2.1345634563456457, 5.42e-05, 24],
                        'isnumeric_column1': [True, True, True],
                        'onlynumeric_column1': [2.1345634563456457, 5.42e-05, 24],
                        'notes_column1': [None, None, None]}
        actual_df = pd.DataFrame.from_dict(data=actual_value)

        assert_frame_equal(expected_df, actual_df)

    def test_is_numeric_and_only_numeric_with_text_value(self):
        expected_value = {'column1': [2.13456345634564563456, 0.0000542, 24, 'A sentence']}
        expected_df = pd.DataFrame(data=expected_value)

        validations.is_numeric_and_only_numeric(expected_df, 'column1')
        actual_value = {'column1': [2.1345634563456457, 5.42e-05, 24, 'A sentence'],
                        'isnumeric_column1': [True, True, True, False],
                        'onlynumeric_column1': [2.1345634563456457, 5.42e-05, 24, None],
                        'notes_column1': [None, None, None, 'A sentence']}
        actual_df = pd.DataFrame.from_dict(data=actual_value).astype(
            {'column1': object, 'isnumeric_column1': bool, 'onlynumeric_column1': object, 'notes_column1': object})
        assert_frame_equal(expected_df, actual_df)

    def test_change_company_to_UUW(self):
        expected_company_value = {'company': ['UU', 'AFW']}
        expected_company_df = pd.DataFrame(data=expected_company_value)

        validations.change_company_to_UUW(expected_company_df)

        actual_company_value = {'company': ['UUW', 'AFW']}
        actual_company_df = pd.DataFrame(data=actual_company_value)

        assert_frame_equal(expected_company_df, actual_company_df)
