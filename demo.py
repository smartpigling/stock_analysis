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
    date = date.strftime("%Y-%m-%d")
    df = ts.get_tick_data(tick, date=date)
    if len(df.index) > 3 :
        df['date'] = date
        trading_data.append(df)
df_trading_data = pd.concat(trading_data)
df_trading_data.to_excel(r'D:\Workspace\CodeWorkspace\mydata.xlsx', sheet_name='mytest')
print('Run Over!')
#%%
for res in ((lambda x: (x,x+1)) for x in range(10)):
    print(res)
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
