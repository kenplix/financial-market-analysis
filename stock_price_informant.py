import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

parameters = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
parameter = ''
while parameter not in parameters:
    print(f'Available parameters: {"   ".join(parameters)}\n'
           'Which parameter do you want to display?')
    parameter = input().title()

# Identify publicly traded shares of a particular stock on a particular stock market
tickers_list = ['AAPL', 'WMT', 'IBM', 'MU', 'BA', 'AXP']

D = yf.download('AAPL', '2019-04-01', '2020-04-01')
print(D.keys())

data = pd.DataFrame(columns=tickers_list)
# Fetch the data
for ticker in tickers_list:
    data[ticker] = yf.download(ticker, '2019-04-01', '2020-04-01')[parameter]

# Plot all the close prices
aligned_percentage = data.pct_change() + 1
cumulative_product = aligned_percentage.cumprod()

cumulative_product.plot(figsize=(10, 7))
plt.legend()
plt.title(parameter, fontsize=16)
plt.ylabel('Price', fontsize=14)
plt.xlabel('Year', fontsize=14)
plt.grid(which="major", color='k', linestyle='-.', linewidth=0.5)
plt.show()

