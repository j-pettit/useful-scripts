''' Check a stock price on a day or across a range of days'''

import argparse
import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf

parser = argparse.ArgumentParser(description='check a stock price')
parser.add_argument('ticker', help='the stock ticker to check')
parser.add_argument('start', help='the start date to check the price on, format YYYY-MM-DD')
parser.add_argument('end', nargs='?', help='the end date to check the price on, format YYYY-MM-DD')
parser.add_argument('-g', '--graph', action='store_true', help='plot the price data')
args = parser.parse_args()

# get the ticker info
ticker = yf.download(args.ticker, start=args.start, end=args.end, progress=False)

# plot the data
if args.graph:
    ticker['Adj Close'].plot()
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title(f'{args.ticker.upper()} Price Data')
    plt.show()

# output the price
start_val = ticker['Adj Close'][0]
end_val = ticker['Adj Close'][-1]
print(f' Start: {start_val}')
print(f' End  : {end_val}')
