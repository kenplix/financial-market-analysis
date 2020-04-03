import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas.plotting import scatter_matrix

from stock_price_informant import *

DAILY, MONTHLY, QUARTER = 'daily', 'monthly', 'quarter'
modes = [DAILY, MONTHLY, QUARTER]


def profitability(stocks: pd.DataFrame, mode: str = DAILY, log: bool = False) -> pd.DataFrame:
    """
    :param mode: Displays what data to collect
    :param log: Allows you to better understand and explore changes over time
    :return: Profitability on the collected data
    """

    if mode not in modes:
        raise ValueError('unknown mode')

    daily = stocks.pct_change()
    daily.fillna(0, inplace=True)

    data_modes = {
        DAILY: lambda: daily,
        MONTHLY: lambda: stocks.resample('BM').apply(lambda x: x[-1]),
        QUARTER: lambda: stocks.resample("4M").mean()
    }

    return np.log(data_modes[mode]() + 1) if log else data_modes[mode]()


def cumulative_profitability(prof: pd.DataFrame) -> pd.DataFrame:
    return (1 + prof).cumprod()

def draw_distribution(prof: pd.DataFrame) -> None:
    prof.hist(bins=50, sharex=True, figsize=(20, 8))
    plt.show()

def draw_scatter_matrix(prof: pd.DataFrame) -> None:
    scatter_matrix(prof, diagonal='kde', alpha=0.1, figsize=(20, 20))
    plt.show()

def draw_cumulative(prof: pd.DataFrame) -> None:
    cumulative_profitability(prof).plot(figsize=(10, 7))
    plt.legend()
    plt.ylabel('Price', fontsize=14)
    plt.xlabel('Year', fontsize=14)
    plt.grid(which="major", color='k', linestyle='-.', linewidth=0.5)
    plt.show()

def main():
    parameter = select_parameter()
    start_date = set_start_date()
    tickers_list = select_stocks()
    data = fetch_data(parameter, tickers_list, start_date)
    prof = profitability(stocks=data, mode=DAILY)

    draw_distribution(prof)
    draw_scatter_matrix(prof)
    draw_cumulative(prof)

if __name__ == '__main__':
    main()