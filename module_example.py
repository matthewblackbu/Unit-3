import pandas as pd
import numpy as np

df = pd.DataFrame([[3,6,23],[25,9,34],[2,7,27],[3,7,29],[2,6,25]])

def null_count(df):
    """Returns # of null values"""
    return df.isnull().sum().sum()

def rm_outlier(df):
    """Removes outliers"""
    remove_index = []
    for i in range(len(df.columns)):
        df = df.sort_values(by=i,ascending = False)
        IQR_1_5 = [df[i].quantile(.75)*1.5,df[i].quantile(0.25) * 1.5]
        print(IQR_1_5)
        for j in range(len(df)):
            if (df.loc[j][i] > IQR_1_5[0] or df.loc[j][i] > IQR_1_5[1]):
                remove_index.append(j)
    df.drop(remove_index,inplace=True)
    return df



