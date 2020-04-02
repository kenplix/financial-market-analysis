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

# Diagram
daily_pct_change.hist(bins=50)

plt.show()

# General statistics
print(daily_pct_change.describe())

#~~~~~~

# Cumulative daily yield
cum_daily_return = (1 + daily_pct_change).cumprod()
print(cum_daily_return.tail())

# Построение кумулятивной дневной доходности
cum_daily_return.plot(figsize=(12,8))
plt.show()


# Monthly  cumulative yield
cum_monthly_return = cum_daily_return.resample("M").mean()
print(cum_monthly_return.tail())


ticker = ['AFLT.ME','DSKY.ME','IRAO.ME','PIKK.ME', 'PLZL.ME','SBER.ME','ENRU.ME']
stock = yf.download(ticker,'2018-01-01')
# Daily yield
daily_pct_change = stock['Adj Close'].pct_change()
# Distribution
daily_pct_change.hist(bins=50, sharex=True, figsize=(20,8))
plt.show()


from pandas.plotting import scatter_matrix
# Dispersion matrix
scatter_matrix(daily_pct_change, diagonal='kde', alpha=0.1,figsize=(20,20))

plt.show()