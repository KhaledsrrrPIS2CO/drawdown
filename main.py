# (second trial)Step 1: Get the data

import yfinance as yf
import numpy as np

# Then I get data and compute the simple returns.

data = yf.download("SPY", start="2020-01-01", end="2022-07-31")
returns = data["Adj Close"].pct_change()


# Step 2: Create the drawdown function

def drawdown(returns):
    """Determines the drawdown

    Parameters
    ----------
    returns : pd.Series
        Daily returns of an asset, noncumulative

    Returns
    -------
    drawdown : pd.Series

    """

    # replace the first nan value with 0.0
    returns.fillna(0.0, inplace=True)

    # create cumulative returns
    cumulative = (returns + 1).cumprod()

    # np.maximum.accumulate takes the running max value
    # of the input series. in this case, it will maintain
    # the running maximum value. this is the running
    # maximum return
    running_max = np.maximum.accumulate(cumulative)

    # compute the change between the cumulative return
    # and the running maximum return
    return (cumulative - running_max) / running_max


# And the plot.

drawdown(returns).plot(kind="area", color="salmon", alpha=0.5)


# Step 3: Create a max drawdown function

def max_drawdown(returns):
    """ Determines the maximum drawdown

    Parameters
    ----------
    returns : pd.Series
        Daily returns of an asset, noncumulative

    Returns
    -------
    max_drawdown : float

    """

    return np.min(drawdown(returns))


# Here’s the plot.
returns.rolling(30).apply(max_drawdown).plot(kind="area", color="salmon", alpha=0.5)
