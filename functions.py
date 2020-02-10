import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def head_n(df, i=1, n=5, s=0):
    '''
    Show up to n rows of df in intervals of i starting
    from index s. This is useful for dataframes such as 
    time series where we want to see values every i rows.
    
    Arguments:
    df(DataFrame) = DataFrame object to be operated on
    i(int) = interval to skip by
    n(int) = number of rows to display
    s(int) = starting row
    '''
    # doctest i n s
    # make class where df attribute of self?
    return df.iloc[s:n*i:i, :]

def explore_dataframe(df):
    '''
    Performs preliminary exploration tasks on data. Recommended
    to use when first reading data into DataFrame

    Arguments:
    df(DataFrame) = DataFrame object to be operated on
    '''
    print(df.shape)
    print(df.dtypes)
    pd.plotting.scatter_matrix(df)
    return df.describe()

def imputer(df, col, func=np.median):
    '''
    Function which imputes values using either mean, median,
    or custom function i.e. lambda x: 0
    WARNING: function replaces values of DataFrame column in place
    
    Arguments:
    df(DataFrame) = DataFrame object to be operated on
    col(str) = string referencing column in DataFrame to index
    func(Function) = Function to determine value that is imputed
    '''
    val = func(df[col])
    df[col] = df[col].fillna(val, inplace=True)