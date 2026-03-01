def position_size(capital, volatility):
    risk_per_trade = 0.02 * capital
    size = risk_per_trade / volatility
    return size
