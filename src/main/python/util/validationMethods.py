import numpy as np


def replacespaces(dataframe):
    dataframe = dataframe.replace(r'^\s*$', np.nan, regex=True)
    return dataframe

def replacedashes(dataframe, iteratorvariable):
    return dataframe[iteratorvariable].replace('-', np.nan)

def replacenullvalues(dataframe, iteratorvariable):
    return np.where(dataframe[iteratorvariable].isnull(), None, dataframe[iteratorvariable])

def replaceyeswithtrues(dataframe, iteratorvariable):
    # dataframe[iteratorvariable] = dataframe[iteratorvariable].replace('yes', 'Yes')
    return np.where(dataframe[iteratorvariable].str.lower() == 'yes', 'TRUE', None)

def isnumericandonlynumeric(dataframe, iteratorvariable):
    dataframe['isnumeric_' + iteratorvariable] = (dataframe[iteratorvariable].apply(
        lambda x: isinstance(x, (int, np.int64)))) | (
                                                     dataframe[iteratorvariable].apply(
                                                         lambda x: isinstance(x, (float, np.float64))))
    dataframe['isnumeric_' + iteratorvariable].astype('bool')
    dataframe['onlynumeric_' + iteratorvariable] = ''
    dataframe['onlynumeric_' + iteratorvariable] = np.where(dataframe['isnumeric_' + iteratorvariable] == True,
                                                            dataframe[iteratorvariable], None)
    na_mask = dataframe['onlynumeric_' + iteratorvariable].notnull()
    dataframe.loc[na_mask, 'onlynumeric_' + iteratorvariable] = dataframe.loc[
        na_mask, 'onlynumeric_' + iteratorvariable].astype(float).round(18)


