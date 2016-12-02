#-*- coding:utf-8 -*-
#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tushare as ts
import datetime
from utils.decorator import coroutine



# def get_stock_his_trading(stock_code, dates):
#     for date in dates:
#         df = ts.get_tick_data(stock_code, date=date.strftime("%Y-%m-%d"))
#         if len(df.index) > 3:
#             df['date'] = date
#             yield df
#         continue

# trading_data = []
# for df in get_stock_his_trading(stock_code, dates):
#     trading_data.append(df)
# pd.concat(trading_data)

@coroutine
def get_stock_trading_data(stock_code):
    """
        获取交易数据
    Parameters
    ------
        stock_code:string
                  股票代码 e.g. 000001
    return
    -------
        DataFrame    
    """
    df = None
    while True:
        try:
            date = yield df
            df = ts.get_tick_data(stock_code, date=date.strftime("%Y-%m-%d"))
            if len(df.index) > 3:
                df['date'] = date           
        except RuntimeError as e:
            print('Get Trading Data Error:%s!' % e)
            continue

def get_several_days_trading(stock_code, days=1):
    """
        交易数据分析
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
    trading_data = []
    start_day = datetime.datetime.now() + datetime.timedelta(days=-days)
    dates = pd.date_range(start_day.strftime("%Y-%m-%d"), periods=days)
    gstd = get_stock_trading_data(stock_code)
    for date in dates:
        trading_data.append(gstd.send(date))
    gstd.close()
    return pd.concat(trading_data)

dfs = get_several_days_trading('600581', 5)
dfs
#%%
buy_vol_sum = df_trading_data[df_trading_data['type'] == '买盘']['volume'].sum()
'buy volume:%s' % buy_vol_sum
#%%
sell_vol_sum = df_trading_data[df_trading_data['type'] == '卖盘']['volume'].sum()
'sell volume:%s' % sell_vol_sum
#%%
mid_vol_sum = df_trading_data[df_trading_data['type'] == '中性盘']['volume'].sum()
'mid volume:%s' % mid_vol_sum
#%%
trading_vol_sum = df_trading_data['volume'].sum()
'total volume:%s' % trading_vol_sum
