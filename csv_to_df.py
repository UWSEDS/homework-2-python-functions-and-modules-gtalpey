import numpy as np
import pandas as pd

# load csv to data DataFrame
def create_dataframe(url):
    df = pd.read_csv(url)
    return df


# check data frame for columns in columns, at least 10 entries and that all datatypes are the same
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
    # take 'set' of dypes in df. If length is 1, all data types are the same.
    elif len(set(df.dtypes)) != 1:
        a = False
    return a
