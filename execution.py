def generate_trade_log(df):

    trades = []
    position = 0

    for i in range(1,len(df)):
        if df["Signal"].iloc[i] and position==0:
            trades.append(("BUY", df.index[i], df["Close"].iloc[i]))
            position=1
        elif not df["Signal"].iloc[i] and position==1:
            trades.append(("SELL", df.index[i], df["Close"].iloc[i]))
            position=0

    return trades
