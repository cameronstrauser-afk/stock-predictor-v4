def detect_regime(df):
    if df["MA50"].iloc[-1] > df["MA200"].iloc[-1]:
        return "Bull"
    elif df["MA50"].iloc[-1] < df["MA200"].iloc[-1]:
        return "Bear"
    else:
        return "Sideways"
