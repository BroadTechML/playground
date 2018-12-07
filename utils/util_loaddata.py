# -*- coding: utf-8 -*-
# Date: 2018/12/6 0006
# Author: Stone

import pandas as pd
import os


def read_csv_userfeat_days(lst_days, dir_userfeat_days, lst_columns, len_filename=8, frac=None):
    lst_days = lst_days
    df_days = pd.DataFrame()
    for day in lst_days:
        print('load day:', day)
        path_day = dir_userfeat_days + day + '/'
        lst_day_files = os.listdir(path_day)
        for day_file in lst_day_files:
            if len(day_file) != len_filename:
                continue
            df_prestat = pd.read_csv(path_day + day_file, names=lst_columns)
            if frac:
                df_prestat = df_prestat.sample(frac=frac)
            df_days = df_days.append(df_prestat)
    return df_days
