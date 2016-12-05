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
# df = df.loc[:,['date','ma_5','ma_10','ma_30']]
# df.set_index('date', inplace=True)
df.to_excel(r'F:\Workspace\CodeWorkspace\ma.xlsx')
# df.plot()
# plt.savefig(r'F:\Workspace\CodeWorkspace\ma.png')

#%%
dfma = pd.read_excel(r'F:\Workspace\CodeWorkspace\ma.xlsx')
dfma
#%%

dfma=dfma[dfma['ma_5'] > dfma['ma_10']]

x=df.index.intersection(dfma.index)
x
#intersection


# records = []
# for i, item in enumerate(dfma.index):
#     try:
#         if dfma.index[i+1] - item != 1:
#             print  '%s - %s' % (dfma.index[i+1] , item)
#             records.append(item)
#     except IndexError:
#         pass
# records