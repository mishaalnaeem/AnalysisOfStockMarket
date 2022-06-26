# AnalysisOfStockMarket

This approach uses Hurst Exponent to to identify the patterns of price action over time. 

The library used for getting data is yfinances. It contains data for stock market over ten years.


### Trading Strategy
Strategy of trading is based on whether the stock in general is mean-reverting, trending, or random over time. 

### Hurst Exponent
Long-term memory of a time series. 
Goal is to measure the amount by which a given time series deviates from a random walk. 

#### stockMarketAnalysis.py
Contains the GetAndPlotData function and
Example of S&P 500

### hurstExponent.py
Contains the HurstExponent function

Running for example

#### Driver
Pass Ticker, Start Date, End Date, and Maximum number of Lags to see the plot of said ticker and Hurst Exponent

Driver also tells what sort of behaviour it implies

How to Run:

python driver.py -t <ticker> -s <start date in format YYYY-MM-DD> -e <end date in format YYYY-MM-DD> -l <maxlag>

Example:

python driver.py -t GOOGL -s 2012-06-25 -e 2022-06-25 -l 20