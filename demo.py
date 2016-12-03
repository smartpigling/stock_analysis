#-*- coding:utf-8 -*-
#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tushare as ts
import datetime
from utils.decorator import coroutine


@coroutine
def get_stock_trade_data(stock_code):
    """
        协程-获取交易数据
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
            print('Get trade Data Error:%s!' % e)
            continue

def fetch_trade_data(stock_code, days=1):
    """
        获取一个时间段股票交易数据
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
    chunks = []
    start_day = datetime.datetime.now() + datetime.timedelta(days=-days)
    dates = pd.date_range(start_day.strftime("%Y-%m-%d"), periods=days)
    gstd = get_stock_trade_data(stock_code)
    for date in dates:
        chunks.append(gstd.send(date))
    gstd.close()
    return pd.concat(chunks, ignore_index=True)

result = fetch_trade_data('600582', 5)
result
#%%
buy_vol_sum = df_trade_data[df_trade_data['type'] == '买盘']['volume'].sum()
'buy volume:%s' % buy_vol_sum
#%%
sell_vol_sum = df_trade_data[df_trade_data['type'] == '卖盘']['volume'].sum()
'sell volume:%s' % sell_vol_sum
#%%
mid_vol_sum = df_trade_data[df_trade_data['type'] == '中性盘']['volume'].sum()
'mid volume:%s' % mid_vol_sum
#%%
trade_vol_sum = df_trade_data['volume'].sum()
'total volume:%s' % trade_vol_sum
