from itertools import takewhile, repeat

import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

parameters = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
PARAMS_INFO = f'Available parameters: {"   ".join(parameters)}\n' \
               'Which parameter do you want to display?\n'

STOCK_INFO = f'Which stock do you want to display?\n' \
              'Press <Enter> to stop\n'

parameter = ''
while parameter not in parameters:
    parameter = input(PARAMS_INFO).title()

tickers_list = []
while True:
    stock_name = input(STOCK_INFO).upper()
    if not stock_name and tickers_list:
        break
    elif stock_name:
        tickers_list.append(stock_name)


data = pd.DataFrame(columns=tickers_list)
# Fetch the data
for ticker in tickers_list:
    data[ticker] = yf.download(ticker, '2019-04-01', '2020-04-01')[parameter]

# Remove nonexistent stocks
data = data.dropna(axis='columns')
aligned_percentage = data.pct_change() + 1
cumulative_product = aligned_percentage.cumprod()

# Plot all the prices
cumulative_product.plot(figsize=(10, 7))
plt.legend()
plt.title(parameter, fontsize=16)
plt.ylabel('Price', fontsize=14)
plt.xlabel('Year', fontsize=14)
plt.grid(which="major", color='k', linestyle='-.', linewidth=0.5)
plt.show()

