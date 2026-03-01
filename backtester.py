def backtest(df):

    df["Signal"] = df["MA50"] > df["MA200"]
    df["Strategy"] = df["Signal"].shift(1) * df["Return"]

    equity = (1 + df["Strategy"]).cumprod()

    return equity, df["Strategy"]
