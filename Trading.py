# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 16:36:08 2022

@author: mmoec
"""
import ta as ta
import yfinance as yf
import pandas as pd
import datetime 
from datetime import datetime, timedelta
asset = input('Aktientitel eingeben: ')
asset.upper()
asset.strip()
s = str(input('Startdatum: '))
date = datetime.strptime(s, "%Y/%m/%d")
modified_date = date + timedelta(days=1)
ende =datetime.strftime(modified_date, "%Y/%m/%d")
yintraday = yf.download(asset,start=s,end=ende,interval=('1m'))
print(yf.Ticker(asset))
def intradaytrend(df, entry, exit):
    ret_120min = df.iloc[120].open/df.iloc[0].Open-1
    tickret = df.open.pct_change()
    if ret_120min > entry:
        buyprice = df.iloc[121].open
        buytime = df.iloc[121].name
        .append()
