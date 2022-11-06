import yfinance as yf
import pandas as pd
import numpy as np
import ta
import matplotlib.pyplot as plt
df = yf.download('SQ', start='2019-01-01')
df['ma_20'] = df.Close.rolling(20).mean()
df['vola'] = df.Close.rolling(20).std()
df['upper_bb'] = df.ma_20 + (2 * df.vola)
df['lower_bb'] = df.ma_20 - (2 * df.vola)
df[['Close','ma_20', 'upper_bb', 'lower_bb']].plot()
df['rsi'] = ta.momentum.rsi(df.Close, window=6)

conditions = [(df.rsi < 30) & (df.Close < df.lower_bb),
            ((df.rsi > 70) & (df.Close > df.upper_bb))]
choices = ['Buy', 'Sell']
df['signal'] = np.select(conditions,choices)
df.dropna(inplace=True)
df.signal = df.signal.shift()
position = False
for index, row in df.iterrows():
buydates,selldates = [],[]
buyprice, sellprice = [][]

