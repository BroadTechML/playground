import pandas as pd
from functools import reduce
from joblib import Parallel, delayed
import warnings
warnings.filterwarnings("ignore")


def ph(n_jobs, func, obj):
    return Parallel(n_jobs=n_jobs, max_nbytes=None)(delayed(func)(chunk) for chunk in obj)

class BigCSVDataFrame(object):
    def __init__(self, csv_file, chunksize=20000):
        self.file = csv_file
        self.chunksize = chunksize
        self.columns = self.get_columns()

    def shape(self, n_jobs=2):
        data = pd.read_csv(self.file, chunksize=self.chunksize)
        chunk_shape = lambda d: d.shape
        chunk_shapes = ph(n_jobs, chunk_shape, data)
        sample_num = sum([i[0] for i in chunk_shapes])
        col_num = chunk_shapes[0][1]
        return sample_num, col_num
    
    def get_columns(self, n_jobs=2):
        data = pd.read_csv(self.file, chunksize=self.chunksize)
        columns = data.get_chunk().columns
        return columns

    def max(self, n_jobs=2):
        data = pd.read_csv(self.file, chunksize=self.chunksize)
        max_cal = lambda d: d.max().reset_index()
        all_max = pd.concat(ph(n_jobs, max_cal, data))
        return all_max.groupby(['index']).max().reset_index()
    def min(self, n_jobs=2):
        data = pd.read_csv(self.file, chunksize=self.chunksize)
        min_cal = lambda d: d.min().reset_index()
        all_min = pd.concat(ph(n_jobs, min_cal, data))
        return all_min.groupby(['index']).min().reset_index()
    
    def groupby_count(self, cols, n_jobs=4):
        data = pd.read_csv(self.file, chunksize=self.chunksize)
        group_count = lambda d: d.groupby(cols).count().reset_index().copy(deep=True)
        all_count = pd.DataFrame()
        for d in data:
            g = group_count(d)
            all_count = pd.concat([all_count, g]).groupby(cols).sum().reset_index().copy(deep=True)
        return all_count



if __name__ == "__main__":
     b = BigCSVDataFrame(r"E:\projects\TelecomFraud\data\calllog_acess_20080280800.csv")
     print(b.groupby_count(['phone']))
    #  print(b.min())
