#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tushare as ts
import datetime

tick = '600581'

start_day = datetime.datetime.now() + datetime.timedelta(days=-3)
dates = pd.date_range(start_day.strftime("%Y-%m-%d"), periods=3)


trading_data = []
for date in dates:
    _df_trading_data = ts.get_tick_data(tick, date=date.strftime("%Y-%m-%d"))
    if len(_df_trading_data.index) > 3 :
        trading_data.append(_df_trading_data)
df_trading_data = pd.concat(trading_data)

#%%
df = ts.get_tick_data(tick, date='2016-11-27')
len(df.index)

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
