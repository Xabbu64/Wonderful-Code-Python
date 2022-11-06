
import pandas as pd
import yfinance as yf
import numpy as np
from sqlalchemy import create_engine
tradeslist = []
#df = yf.download('TSLA', import tastart= '2017-01-01')
engine = create_engine('sqlite:///RaynerDB.db')
symbols = pd.read_html('https://en.wikipedia.org/wiki/Russell_1000_Index')[2]
#symbols = pd.read_html('https://en.wikipedia.org/wiki/DAX')[3]
symbols = symbols.Ticker.to_list()
for symbol in symbols:
    df = yf.download(symbol, start='2015-01-01')
    df.to_sql(symbol, engine)
def applyindicators(df):
    df['SMA200'] = df.Close.rolling(200).mean()
    df['SMA20'] = df.Close.rolling(20).mean()
    df['standdev'] = df.Close.rolling(20).std()
    df['Upper'] = df.SMA20 + 2.5 * df.standdev
    df['Lower'] = df.SMA20 - 2.5 * df.standdev
    df['rsi'] = ta.momentum.rsi(df.Close, 2)
#print(df.tail(250)[['Close', 'SMA20', 'Upper', 'Lower']].plot())

def conditions(df):
    df['Buy'] = np.where((df.Close > df.SMA200) & (df.Close < df.Lower) & (0.97 * df.Close >= df.Low.shift(-1)), 1, 0)
    df['Sell'] = np.where((df.rsi > 50), 1, 0)
    df['Buyprice'] = 0.97 * df.Close
    df['Sellprice'] = df.Open.shift(-1)

def matchtrades(df):
    buysell = df[(df.Buy == 1) | (df.Sell == 1)]
    matched = buysell[(buysell.Buy.diff() == 1) | (buysell.Sell.diff() == 1)]
    return matched

for symbol in symbols:
    df = pd.read_sql(symbol, engine, index_col='Date')
    applyindicators(df)
    conditions(df)
    trades = matchtrades(df)
    tradeslist.append(trades)

tradesdf = pd.concat(tradeslist)    

tradesdf['profit'] = ((tradesdf.Sellprice.shift(-1)) - (tradesdf.Buyprice) / tradesdf.Buyprice)

frame = pd.DataFrame({'profit': tradesdf[::2].profit.values, 'Buydates':tradesdf[::2].index, 'Selldates':tradesdf[1::2].index})


sorted_df = frame.sort_values(by='Buydates')
sorted_df = sorted_df.set_index('Buydates', drop=False)
print(tradeslist)
    
