# example code is from this video
# https://www.youtube.com/watch?v=7Xsf_G2xEeQ

import pandas_datareader as web
import matplotlib.pyplot as plt
import mplfinance as mpf
import datetime as dt

crypto = "BTC"
currency = "USD"

start = dt.datetime(2020, 1, 1)
end = dt.datetime.now()

def getBTCdata():
    data = web.DataReader(f"{crypto}-{currency}", "yahoo", start, end)
    return data

def plotBTCpriceclose():
    data = getBTCdata()
    plt.plot(data["Close"])
    plt.show()

def platBTCcancdlechart():
    data = getBTCdata()
    mpf.plot(data, type="candle", volume="True", style="yahoo")


