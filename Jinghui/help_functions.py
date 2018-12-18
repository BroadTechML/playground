import numpy as np
import pandas as pd

import matplotlib.pyplot as plt



# 缺失值统计
def plot_miss_count(df, figsize=(10, 12), title="missing counts"):
    '''
    df : DataFrame
    figsize : tuple(x, y)
    title : str
    '''
    miss_val_count = df.isnull().sum()
    miss_val_pct = 100 * miss_val_count / df.shape[0]
    miss_val_pct = pd.DataFrame(miss_val_pct)
    miss_val_pct = miss_val_pct.rename(columns={0:'percent'})
    return miss_val_pct, miss_val_pct.sort_values(by='percent').plot(kind='barh', figsize=figsize, title=title)

# Release your precious memory

def reduce_mem_usage(df):
    numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64'] 
    for col in df.columns:
        col_type = df[col].dtypes
        if col_type in numerics:
            c_min = df[col].min()
            c_max = df[col].max()
            if str(col_type)[:3] == 'int':
                if c_min > np.iinfo(np.int8).min and c_max < np.iinfo(np.int8).max:
                    df[col] = df[col].astype(np.int8)
                elif c_min > np.iinfo(np.int16).min and c_max < np.iinfo(np.int16).max:
                    df[col] = df[col].astype(np.int16)
                elif c_min > np.iinfo(np.int32).min and c_max < np.iinfo(np.int32).max:
                    df[col] = df[col].astype(np.int32)
                elif c_min > np.iinfo(np.int64).min and c_max < np.iinfo(np.int64).max:
                    df[col] = df[col].astype(np.int64)  
            else:
                if c_min > np.finfo(np.float16).min and c_max < np.finfo(np.float16).max:
                    df[col] = df[col].astype(np.float16)
                elif c_min > np.finfo(np.float32).min and c_max < np.finfo(np.float32).max:
                    df[col] = df[col].astype(np.float32)
                else:
                    df[col] = df[col].astype(np.float64)    
    return df
