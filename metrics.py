import numpy as np

def performance_metrics(strategy_returns):

    sharpe = strategy_returns.mean() / strategy_returns.std()
    drawdown = (strategy_returns.cumsum() - strategy_returns.cumsum().cummax()).min()
    winrate = (strategy_returns > 0).mean()

    return sharpe, drawdown, winrate
