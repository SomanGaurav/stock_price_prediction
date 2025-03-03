import pandas as pd 
import yfinance as yf 
from tensorflow.keras.models import Sequential , load_model
from tensorflow.keras.optimizers import Adam 
from tensorflow.keras import layers , backend




ticks = pd.read_csv("model_training/nifty_tick.csv")
# ticks["Symbol"] = ticks["Symbol"].apply(lambda x : x + ".NS")


def tick_trainer(name): 
    backend.clear_session()
    model = Sequential([layers.Input((3,1)),layers.LSTM(128)])
    model.add(layers.Dense(64,activation="relu"))
    model.add(layers.Dense(32,activation="relu"))
    model.add(layers.Dense(1))
    model.compile(loss="mse" ,optimizer = Adam(learning_rate=0.001) ,metrics=["mean_absolute_error"])

    data = yf.download(name)
    data = data[["Close"]]
    data["TARGET_3"] = data["Close"].shift(3)
    data["TARGET_2"] = data["Close"].shift(2)
    data["TARGET_1"] = data["Close"].shift(1)
    data = data.dropna()
    X = data[["TARGET_3","TARGET_2","TARGET_1"]].values
    y = data[["Close"]].values
    X = X.reshape(X.shape[0],X.shape[1],1)
    model.fit(X,y,epochs=50)
    file = "model/" +  name + ".h5"
    model.save(file)

for tickers in ticks.Symbol : 
    tick_trainer(tickers)