import pandas as pd
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

ibm = yf.download('AAPL', '2020-01-01')

# Adjusted closing price
daily_close = ibm[['Adj Close']]
print(daily_close)

# Daily yield
daily_pct_change = daily_close.pct_change()
daily_pct_change.fillna(0, inplace=True)
print(daily_pct_change)

# Daily log yield
daily_log_returns = np.log(daily_close.pct_change()+1)
print(daily_log_returns)