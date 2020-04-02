import yfinance as yf
import matplotlib.pyplot as plt

# Get the data for the stock AAPL
data = yf.download('AAPL','2019-04-01','2020-04-01')

# Plot the close price of the AAPL
print(data)
data['Adj Close'].plot()
plt.show()