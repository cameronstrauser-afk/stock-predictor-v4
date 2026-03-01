import yfinance as yf
import pandas as pd

def get_data(tickers, period="3y"):
    data = {}
    for t in tickers:
        df = yf.download(t, period=period)
        df.dropna(inplace=True)
        data[t] = df
    return data
