from tradingview_ta import TA_Handler, Interval
output = TA_Handler(symbol='TSLA',screener='America', exchange='NASDAQ',interval=Interval.INTERVAL_1_MINUTE)
output.get_analysis().summary
print(output)