from sys import argv
from hurstExponent import *
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

def GetAndPlotData(_ticker, _startDate, _endDate, _progress=False):

    data = yf.download(_ticker, _startDate, _endDate, _progress)

    data["Adj Close"].plot(title=_ticker)
    plt.show()

    return data

#Example
if(len(argv) == 1):
    dataSP500 = GetAndPlotData("^GSPC", "2012-6-25", "2022-6-25")
    lag = 20
    hurstexp = HurstExponent(dataSP500["Adj Close"].values, lag)

    print("Hurst exponent with lag ", lag, ": ", hurstexp)