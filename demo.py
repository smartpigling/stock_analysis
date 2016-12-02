#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tushare as ts
import datetime
from utils.decorator import coroutine

stock_code = '600581'

start_day = datetime.datetime.now() + datetime.timedelta(days=-3)
dates = pd.date_range(start_day.strftime("%Y-%m-%d"), periods=3)

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
def get_stock_his_trading():
    df = None
    while True:
        try:
            stock_code, date = yield df
            df = ts.get_tick_data(stock_code, date=date.strftime("%Y-%m-%d"))
            if len(df.index) > 3:
                df['date'] = date           
        except RuntimeError as e:
            print('Get Trading Data Error:%s!' % e)
            continue
        
trading_data = []
gtd = get_stock_his_trading()
for date in dates:
    trading_data.append(gtd.send((stock_code, date)))
gtd.close()
pd.concat(trading_data)
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
