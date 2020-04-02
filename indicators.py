import pandas as pd
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

stock = yf.download('AAPL', '2019-01-01')

# Adjusted closing price
daily_close = stock[['Adj Close']]

# Daily yield
daily_pct_change = daily_close.pct_change()
daily_pct_change.fillna(0, inplace=True)

# Daily log yield
# Allows you to better understand and explore changes over time
daily_log_returns = np.log(daily_close.pct_change()+1)


# Take stock values for the last business day of the month
monthly = stock.resample('BM').apply(lambda x: x[-1])

# Monthly yield
print(monthly.pct_change().tail())

# Recalculate the stock by quarters and take the average value for the quarter
quarter = stock.resample("4M").mean()

# Quarterly yield
print(quarter.pct_change().tail())

