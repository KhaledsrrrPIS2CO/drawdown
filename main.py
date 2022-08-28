# import the librarieswe need
import yfinance as yf
import numpy as np

# get data and compute the simple returns
data = yf.download("SPY", start="2020-01-01", end="2022-07-31")
returns = data["Adj Close"].pct_change()

# now we create the drawdown function
