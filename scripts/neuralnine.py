# example code is from this video
# https://www.youtube.com/watch?v=HqGlkACB3rg

import pandas_datareader as web
import matplotlib.pyplot as plt
import mplfinance as mpf
import seaborn as sns
import datetime as dt

currency = "USD"
metric = "Close"

MacroView = False
Heatmap = False

start = dt.datetime(2020, 1, 1)
end = dt.datetime.now()

crypto = ['BTC', 'ETH', 'LTC', 'LINK']
colnames = []

first = True

for ticker in crypto:
    data = web.DataReader(f'{ticker}-{currency}', "yahoo", start, end)
    if first:
        combined = data[[metric]].copy()
        colnames.append(ticker)
        combined.columns = colnames
        first = False
    else:
        combined = combined.join(data[metric])
        colnames.append(ticker)
        combined.columns = colnames

if MacroView:
    plt.yscale('log')
    for ticker in crypto:
        plt.plot(combined[ticker], label=ticker)
    plt.legend(loc="upper left")
    plt.show()

if Heatmap:
    combined = combined.pct_change().corr(method="pearson")
    sns.heatmap(combined, annot=True, cmap="coolwarm")
    plt.show()
