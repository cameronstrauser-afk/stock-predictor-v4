import streamlit as st
import pandas as pd
import plotly.graph_objects as go

from data import *
from features import *
from models import *
from optimizer import *
from risk import *
from backtester import *
from metrics import *
from execution import *
from regime import *

st.set_page_config(layout="wide")
st.title("🏦 Autonomous AI Hedge Fund")

tickers = st.text_input("Enter tickers (comma separated)", "AAPL,MSFT,GOOGL")
tickers = [t.strip() for t in tickers.split(",")]

if st.button("Deploy AI Fund"):

    raw_data = get_data(tickers)
    processed = {}

    for t in tickers:
        df = add_features(raw_data[t])
        processed[t] = df

    returns = pd.DataFrame({t: processed[t]["Return"] for t in tickers})
    weights = optimize(returns)

    st.subheader("AI Portfolio Allocation")
    for t,w in zip(tickers,weights):
        st.write(t, round(w*100,2), "%")

    main_df = processed[tickers[0]]
    regime = detect_regime(main_df)

    equity, strat_returns = backtest(main_df)
    sharpe, dd, win = performance_metrics(strat_returns)

    fig = go.Figure()
    fig.add_trace(go.Scatter(y=equity, name="AI Equity Curve"))
    st.plotly_chart(fig)

    st.write("Market Regime:", regime)
    st.write("Sharpe Ratio:", sharpe)
    st.write("Max Drawdown:", dd)
    st.write("Win Rate:", win)

    trades = generate_trade_log(main_df)
    st.write("Trade Log:", trades[:10])
