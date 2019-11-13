import numpy as np
import pandas as pd

# load csv to data DataFrame
def create_dataframe(url):
    df = pd.read_csv(url)
    return df


# check data frame for columns in columns, at least 10 entries
def test_create_datadrame(df,columns):
    # set output to True, then look for conditions to turn False.
    a = True
    # check whether data frame contains only the columns listed in input 'columns'
    # first, sort column list alaphabetically in case columns is not in same order as the columns in df
    if df.columns.tolist().sort() != columns.sort():
        a = False
    # check number of entries in data frame
    elif len(df) <= 10:
        a = False
    return a

def test_dataframe_types(df):

    # loop through columns
    for column in df.columns.tolist():
        # find type of first entry
        datatype = type(df[column][0])
        # loop through rows to check if the types match that of the first rows
        for i in range(len(df[column])):
            if datatype == type(df[column][i]):
                continue
            else:
                raise TypeError('data types in %s do not match' %column)
