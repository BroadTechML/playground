import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

def plot_miss_count(df, figsize=(10,20)):
    miss_val_count = df.isnull().sum()
    miss_val_pct = 100 * miss_val_count / df.shape[0]
    miss_val_pct = pd.DataFrame(miss_val_pct)
    miss_val_pct = miss_val_pct.rename(columns={0:'percnet'})
    return miss_val_pct.sort_values(by='percent').plot(kind='barh', figsize=figsize)