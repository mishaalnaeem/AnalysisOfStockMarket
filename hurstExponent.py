import numpy as np

def HurstExponent(_timeSeries, _maxLags):
    
    taus = range(2, _maxLags) #tau = lag

    # Var(τ) ∝ τ^(2H)
    # var(τ)=(Var(x(t)-x(t-τ))) where x is log of adjusted closing price (s) or log(s) 
    varianceTau = [np.var(np.subtract(_timeSeries[tau:], _timeSeries[:-tau])) for tau in taus]

    # taking log on each side, and rearraging
    # [ log (Var(x(t)-x(t-τ))) / 2 log τ ] 2 ∝ H

    hurst = np.polyfit(np.log(taus), np.log(varianceTau), 1)

    return hurst[0] / 2