#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""A tool to track changes in stock prices of various companies.

Changes accumulate around 1 to display changes in value starting from a certain date"""

from datetime import date
from typing import List

import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

parameters = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
PARAMS_INFO = f'Available parameters: {"   ".join(parameters)}\n' \
              'Which parameter do you want to display?\n'

STOCK_INFO = f'Which stock do you want to display?\n' \
             'Press <Enter> to stop\n'


def select_parameter() -> str:
    parameter = ''
    while parameter not in parameters:
        parameter = input(PARAMS_INFO).title()
    return parameter


def select_stocks() -> List[str]:
    tickers_list = []
    while True:
        stock_name = input(STOCK_INFO).upper()
        if not stock_name and tickers_list:
            break
        elif stock_name:
            tickers_list.append(stock_name)
    return tickers_list


def fetch_data(parameter: str, tickers_list: List[str], start_date: date) -> pd.DataFrame:
    data = pd.DataFrame(columns=tickers_list)
    for ticker in tickers_list:
        data[ticker] = yf.download(ticker, start_date, date.today())[parameter]
    # Remove nonexistent stocks
    return data.dropna(axis='columns')


def set_start_date() -> date:
    date_ = input('Start date (yyyy-mm-dd): ').split('-')
    if int(date_[0]) < 2000:
        print('Missing information.Try again')
        return set_start_date()
    else:
        try:
            return date(*map(lambda x: int(x), date_))
        except ValueError:
            print('Invalid date or format.Try again')
            return set_start_date()


def main() -> None:
    parameter = select_parameter()
    start_date = set_start_date()
    tickers_list = select_stocks()
    data = fetch_data(parameter, tickers_list, start_date)
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


if __name__ == '__main__':
    main()
