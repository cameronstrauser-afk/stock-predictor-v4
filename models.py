import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LogisticRegression
from xgboost import XGBRegressor
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

def train_models(df):

    features = ["MA50","MA200","Volatility","Momentum"]
    X = df[features]
    y_price = df["Close"]
    y_dir = df["Direction"]

    xgb = XGBRegressor().fit(X, y_price)
    rf = RandomForestRegressor().fit(X, y_price)
    clf = LogisticRegression().fit(X, y_dir)

    scaler = MinMaxScaler()
    scaled = scaler.fit_transform(df["Close"].values.reshape(-1,1))

    X_lstm, y_lstm = [], []
    for i in range(60,len(scaled)):
        X_lstm.append(scaled[i-60:i])
        y_lstm.append(scaled[i])
    X_lstm, y_lstm = np.array(X_lstm), np.array(y_lstm)

    lstm = Sequential([
        LSTM(64, input_shape=(60,1)),
        Dense(1)
    ])
    lstm.compile(optimizer="adam", loss="mse")
    lstm.fit(X_lstm, y_lstm, epochs=5, verbose=0)

    return xgb, rf, clf, lstm, scaler
