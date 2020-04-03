import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas.plotting import scatter_matrix


from stock_price_informant import *

DAILY, MONTHLY, QUARTER = 'daily', 'monthly', 'quarter'
modes = [DAILY, MONTHLY, QUARTER]


def profitability(mode: str = DAILY, log: bool = False) -> pd.DataFrame:
    """
    :param mode: Displays what data to collect
    :param log: Allows you to better understand and explore changes over time
    :return: Profitability on the collected data
    """
    stock = yf.download('AAPL', '2019-01-01')

    if mode not in modes:
        raise ValueError('unknown mode')

    daily_close = stock[['Adj Close']]
    daily = daily_close.pct_change()
    daily.fillna(0, inplace=True)

    data_modes = {
        DAILY: lambda: daily,
        MONTHLY: lambda: stock.resample('BM').apply(lambda x: x[-1]),
        QUARTER: lambda: stock.resample("4M").mean()
    }

    return np.log(data_modes[mode]() + 1) if log else data_modes[mode]()


def cumulative_profitability(prof: pd.DataFrame) -> pd.DataFrame:
    return (1 + prof).cumprod()


ticker = ['AFLT.ME', 'DSKY.ME', 'IRAO.ME', 'PIKK.ME', 'PLZL.ME', 'SBER.ME', 'ENRU.ME']
stock = yf.download(ticker, '2018-01-01')
# Daily yield
daily_pct_change = stock['Adj Close'].pct_change()
# Distribution
daily_pct_change.hist(bins=50, sharex=True, figsize=(20, 8))
plt.show()


# Dispersion matrix
scatter_matrix(daily_pct_change, diagonal='kde', alpha=0.1, figsize=(20, 20))

plt.show()
