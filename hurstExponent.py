import numpy as np

def hurstExponent(_timeSeries, _maxLags):
    
    taus = range(2, _maxLags) #tau = lag

    # Var(τ) ∝ τ^(2H)
    # var(τ)=(Var(x(t)-x(t-τ))) where x is log of adjusted closing price (s) or log(s) 
    varianceTau = [np.var(np.subtract(_timeSeries[tau:], _timeSeries[:-tau])) for tau in taus]

    # taking log on each side, and rearraging
    # [ log (Var(x(t)-x(t-τ))) / 2 log τ ] 2 ∝ H

    hurst = np.polyfit(np.log(taus), np.log(varianceTau), 1)

    return hurst[0] / 2

def get_hurst_exponent(time_series, max_lag=20):
    """Returns the Hurst Exponent of the time series"""
    
    lags = range(2, max_lag)

    # variances of the lagged differences
    tau = [np.std(np.subtract(time_series[lag:], time_series[:-lag])) for lag in lags]

    # calculate the slope of the log plot -> the Hurst Exponent
    reg = np.polyfit(np.log(lags), np.log(tau), 1)

    return reg[0]