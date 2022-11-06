import yfinance as yf
import matplotlib.pyplot as plt
df = yf.download('TSLA', start ='2018-01-01')
print(df)
def MACD(df):
    df['EMA12'] = df.Close.ewm(span=12).mean()
    df['EMA26'] = df.Close.ewm(span=26).mean()
    df['MACD'] = df.EMA12 - df.EMA26
    df['signal'] = df.MACD.ewm(span=9).mean()
    print('done')
MACD(df)
plt.figure(figsize = (16,8))
plt.plot(df.signal, label = 'Signal', color = 'red')
plt.plot(df.MACD, label = 'MACD', color = 'blue')
Buy, Sell = [],[]
for i in range(2,len(df)):
    if  df.MACD.iloc[i] > df.signal.iloc[i] and df.MACD.iloc[i-1] < df.signal.iloc[i-1]:
        Buy.append(i)
    elif df.MACD.iloc[i] < df.signal.iloc[i] and df.MACD.iloc[i-1] > df.signal.iloc[i-1]:
        Sell.append(i)
df.iloc[Buy].index
df.iloc[Sell].index
plt.figure(figsize = (12,4))
plt.scatter(df.iloc[Buy].index, df.iloc[Buy].Close, marker = '^', color = 'green')
plt.scatter(df.iloc[Sell].index, df.iloc[Sell].Close, marker = '^', color = 'red')
plt.plot(df.Close, label = 'TSLA close', color = 'k')
plt.legend()
plt.show()
Realbuy = [i+1 for i in Buy]
Realsell = [i+1 for i in Sell] 
Buyprices = df.Open.iloc[Realbuy]
Sellprices = df.Open.iloc[Realsell]
if Sellprices.index[0] < Buyprices.index[0]:
    Sellprices = Sellprices.drop(Sellprices.index[0])
elif Buyprices.index[-1] > Sellprices.index[-1]:
    Buyprices = Buyprices.drop(Buyprices.index[-1]) 
plt.figure(figsize = (16,4))
plt.scatter(df.iloc[Buy].index, df.iloc[Buy].Close, marker = '^', color = 'green')
plt.scatter(df.iloc[Sell].index, df.iloc[Sell].Close, marker = '^', color = 'red')
plt.plot(df.Close, label = 'TSLA close', color = 'k')
plt.legend()
plt.show()
profits =[]
for i in range(len(Buyprices)):
    profits.append(Sellprices[i] - Buyprices[i])
sum(profits)
sum(Buyprices)
profitrel = (sum(profits) / sum(Buyprices)) *100
print(profitrel)