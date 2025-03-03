import numpy as np 
import pandas as pd 
import yfinance as yf 
# from tensorflow.keras.models import Sequential ,load_model
# from tensorflow.keras.optimizers import Adam 
# from tensorflow.keras import layers
from sklearn.linear_model import LinearRegression 
import json


model = LinearRegression()


def  write_json(data,filename): 
    with open(filename,"w") as f : 
        json.dump(data,f,indent=4)


def tick_trainer(name): 
    data = yf.download(name)
    print(data.head(1))
    data = data.drop(["Adj Close","Volume"],axis=1)
    df_lm_y = data["Close"] 
    df_lm_X = data.drop(["Close"],axis=1)
    model.fit(df_lm_X,df_lm_y)
    print(ticks.head())
    weigths = {
        'name' : ticks[ticks.Symbol == name]["name"].values[0],
        'ticker' : name ,
        'slopes' : model.coef_.tolist(), 
        'intercept' : model.intercept_
    }
    with open("C:\Project\STOCK_PREDICTOR\model_training\linear_model.json",'r') as h : 
        data = json.load(h)
        temp = data["weights"]
        temp.append(weigths)

    write_json(data,"C:\Project\STOCK_PREDICTOR\model_training\linear_model.json")

ticks = pd.read_csv(r"C:\Project\STOCK_PREDICTOR\model_training\nifty_tick.csv")
#ticks["Symbol"] = ticks["Symbol"].apply(lambda x : x + ".NS")
print(ticks.head())


for ticker in ticks.Symbol : 
    tick_trainer(ticker)