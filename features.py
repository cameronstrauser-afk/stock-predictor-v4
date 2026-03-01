import numpy as np

def add_features(df):
    df["Return"] = df["Close"].pct_change()
    df["Volatility"] = df["Return"].rolling(20).std()
    df["MA50"] = df["Close"].rolling(50).mean()
    df["MA200"] = df["Close"].rolling(200).mean()
    df["Momentum"] = df["Close"] - df["Close"].shift(10)
    df["Drawdown"] = df["Close"] / df["Close"].cummax() - 1
    df["Direction"] = (df["Return"] > 0).astype(int)
    df.dropna(inplace=True)
    return df
