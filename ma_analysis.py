# -*- coding: utf-8 -*-
"""
@author: TangXiaochuang
@contact: QQ:173387911 email:173387911@qq.com
@desc: Moving Average analysis
"""

#%%
import pandas as pd
import matplotlib.pyplot as plt
import tushare as ts
import datetime
from utils.index_utils import nn_index_group

def fetch_market_data(stock_code, years=1):
    """
        获取一个时间段股票行情数据
    Parameters
    ------
        stock_code:string
                  股票代码 e.g. 000001
        days:int, 默认 1
                  获取当前几天的交易数据
    return
    -------
        DataFrame            
    """
    _end = datetime.datetime.now().strftime('%Y-%m-%d')
    _start = (datetime.datetime.now() + 
        datetime.timedelta(days=-years * 365)).strftime('%Y-%m-%d')
    return ts.get_k_data(stock_code, start=_start, end=_end)


def add_ma(df, ma_list=[5,10,30]):
    """
        计算移动平均线
    Parameters
    ------
        df:DataFrame
                  DataFrame
        ma_list:list, 默认 [5,10,30]
                  需计算移动平均线列表
    return
    -------
        DataFrame      
    """
    for ma in ma_list:
        df['ma_%s' % ma] = df['close'].rolling(window=ma).mean()
    return df

def add_ema(df, ema_list=[5,10,30]):
    """
        指数平滑移动平均线EMA
    Parameters
    ------
        df:DataFrame
                  DataFrame
        ema_list:list, 默认 [5,10,30]
                  需计算指数平滑移动平均线列表
    return
    -------
        DataFrame      
    """
    for ema in ema_list:
        df['ema_%s' % ema] = df['close'].ewm(span=ema).mean()
    return df

df = add_ma(fetch_market_data('600582', years=3))
df.sort_values(by='date', ascending=True, inplace=True)
df_ma = df[df['ma_5'] > df['ma_10']]
idgs=[_ids for _ids in nn_index_group(df_ma.index)]
for ids in idgs:
    _df=df.loc[ids]
    _df.to_excel(r'D:\Workspace\CodeWorkspace\%s.xlsx' % ids)

# df.set_index('date', inplace=True)
# df.to_excel(r'D:\Workspace\CodeWorkspace\ma.xlsx')
# df.plot()
# plt.savefig(r'F:\Workspace\CodeWorkspace\ma.png')

#%%
dfma = pd.read_excel(r'D:\Workspace\CodeWorkspace\ma.xlsx')
dfma
#%%

dfma=dfma[dfma['ma_5'] > dfma['ma_10']]
#%%


index_group=[g for g in ntl_seq_group(dfma.index)]
dfma.loc[index_group[0]]

#%%

