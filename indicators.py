import pandas as pd
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

ibm = yf.download('IBM', '2016-01-01')
# Скорректированая цена закрытия`
daily_close = ibm['Adj Close']
print(daily_close)
# Дневная доходность
# daily_pct_change = daily_close.pct_change()
#
# # Заменить NA значения на 0
# daily_pct_change.fillna(0, inplace=True)
#
# print(daily_pct_change.head())
#
# # Дневная лог доходность
# daily_log_returns = np.log(daily_close.pct_change()+1)
#
# print(daily_log_returns.head())