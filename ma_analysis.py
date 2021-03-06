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
from utils.common import num_group

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

def add_ma(df, ma_list=[5,10]):
    """
        计算移动平均线
    Parameters
    ------
        df:DataFrame
                  DataFrame
        ma_list:list, 默认 [5,10]
                  需计算移动平均线列表
    return
    -------
        DataFrame      
    """
    for ma in ma_list:
        df['ma_%s' % ma] = df['close'].rolling(window=ma).mean()
    return df

def add_ema(df, ema_list=[5,10]):
    """
        指数平滑移动平均线EMA
    Parameters
    ------
        df:DataFrame
                  DataFrame
        ema_list:list, 默认 [5,10]
                  需计算指数平滑移动平均线列表
    return
    -------
        DataFrame      
    """
    for ema in ema_list:
        df['ema_%s' % ema] = df['close'].ewm(span=ema).mean()
    return df

def ma_analysis(stock_code, years=5, ma_list=[5,10]):
    """
        对移动平均线分析
    Parameters
    ------
        stock_code:string
                  股票代码
        years:int, 默认 5
                  需分析的年限
        ma_list:list, 默认 [5,10]
                  需分析的移动平均线                  
    return
    -------
        DataFrame      
    """    
    df = add_ma(fetch_market_data(stock_code, years), ma_list)
    df.sort_values(by='date', ascending=True, inplace=True)
    df_ma = df[df['ma_%s' % ma_list[0]] > df['ma_%s' % ma_list[1]]] 
    maCons=[_ids for _ids in num_group(df_ma.index)] # 将均线持续上穿天数分组
    results = []
    for _maCons in maCons:
        _df_ma = df_ma.loc[_maCons]
        ind_buy_price = round(_df_ma.iloc[0]['open'], 2)
        ind_sale_price = round(_df_ma.iloc[-1]['close'], 2)
        pl_percent = round((ind_sale_price - ind_buy_price) / ind_buy_price, 4)*100
        results.append({
            u'指标买入价格' : ind_buy_price,
            u'指标卖出价格' : ind_sale_price,
            u'盈亏比例' : pl_percent, 
            u'锁定天数' : len(_maCons)
        })

    return pd.DataFrame(results)

df_res = ma_analysis('603198')
df_res.to_excel(r'F:\Workspace\CodeWorkspace\mares.xlsx')
print 'done!!!'
