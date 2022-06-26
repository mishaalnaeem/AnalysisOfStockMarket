# AnalysisOfStockMarket

This approach uses Hurst Exponent to to identify the patterns of price action over time. 

The library used for getting data is yfinances. It contains data for stock market over ten years.


### Trading Strategy
Strategy of trading is based on whether the stock in general is mean-reverting, trending, or random over time. 

### Hurst Exponent
Long-term memory of a time series. 
Goal is to measure the amount by which a given time series deviates from a random walk. 

#### stockMarketAnalysis.py
Example of S&P 500

#### Driver
Pass Ticker, Start Date, End Date, and Maximum number of Lags to see the plot of said ticker and Hurst Exponent

Driver also tells what sort of behaviour it implies