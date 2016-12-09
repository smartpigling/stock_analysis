# -*- coding: utf-8 -*-
"""
@author: TangXiaochuang
@contact: QQ:173387911 email:173387911@qq.com
@desc: basics analysis
"""

#%%
import pandas as pd
import tushare as ts


def bas_analysis():
    df = ts.get_stock_basics()
    return df


df = bas_analysis()
df
#%%
# df.sort_values(by=['industry','pe'], ascending=True).groupby('industry').head(3)
df.sort_values(by=['pb','pe'])