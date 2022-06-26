from getopt import getopt
from hurstExponent import *
from stockMarketAnalysis import *
import sys, getopt

def main(argv):

    ticker, startDate, endDate = " ", " ", " "
    maxLag = 0
    try:
        opts, args = getopt.getopt(argv, "t:s:e:l:", ["ticker=", "startdate=", "enddate=","maxlag="])
    except getopt.GetoptError:
        print('driver.py -t <ticker> -s <start date in format YYYY-MM-DD> -e <end date in format YYYY-MM-DD> -l <maxlag>')

    for opt, arg in opts:
        if opt == '-t':
            ticker = arg
        elif opt == '-s':
            startDate = arg
        elif opt == '-e':
            endDate = arg
        elif opt == '-l':
            maxLag = int(arg)

    data = GetAndPlotData(ticker, startDate, endDate)

    hurstexp = HurstExponent(data["Adj Close"].values, maxLag)
    print("Hurst exponent with lag ", maxLag, ": ", hurstexp)

    if (hurstexp < 0.5):
        print("Mean Reverting: High value will be followed by Low value next and vice versa")
    elif (hurstexp == 0.5):
        print("Geometric Random Walk: No clear deduction possible from given params")
    else:
        print("Trending: High value will be followed by High value and Low value by low")

if __name__ == "__main__":
   main(sys.argv[1:])