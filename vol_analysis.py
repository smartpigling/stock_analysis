# -*- coding: utf-8 -*-
"""
@author: TangXiaochuang
@contact: QQ:173387911 email:173387911@qq.com
@desc: volume analysis
"""
#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tushare as ts
import datetime
from utils.decorator import coroutine

@coroutine
def get_day_trade_data(stock_code):
    """
        获取交易数据-协程
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

def fetch_trade_data(stock_code, days=5):
    """
        获取多日该股票交易数据
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
    gstd = get_day_trade_data(stock_code)
    for date in dates:
        chunks.append(gstd.send(date))
    gstd.close()
    return pd.concat(chunks, ignore_index=True)

result = fetch_trade_data('600582', 5)
result
