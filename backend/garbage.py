import yfinance as yf 
import datetime
import time 
import json 
import numpy as np 
from tensorflow.keras.models import load_model
import os 

def give_price(year,month,day,name): 
    data =  yf.download(tickers=name , period = "1d" , interval="1m" ,start = datetime.datetime(year, month, day, 9, 30, 0),end = datetime.datetime(year, month, day, 20, 30, 0)   )
    data = data.reset_index(drop=True)
    data = data["Open"]
    data = data.to_dict()   
    return data 

def give_price_failsafe(data,year,month,day,name):
    raw_data = give_price(year,month,day,name)
    if len(raw_data) == 0: 
        return give_price(year ,month , day-1, name)
    else : 
        return raw_data 

def get_date(index): 
    today = datetime.date.today().timetuple()
    #return datetime.datetime.strftime(today,"%y%m%d %H:%M:%S")
    return today[index]


def get_index(year,month,day,name): 
    dict = {"sensex":0,"niftybank":0,"niftyit":0}
    stock = yf.download(name,start=datetime.datetime(year,month,day))
    return stock["Close"].values.__float__()
#print(get_date(0))

def read_json(): 
    with open("stocks.json","r") as file : 
        data = json.load(file)
        return data 
    


# print(get_index(get_date(0),get_date(1),get_date(2),"^BSESN"))
# print(get_index(get_date(0),get_date(1),get_date(2),"^NSEBANK"))
# print(get_index(get_date(0),get_date(1),get_date(2),"^CNXIT"))
# ending = time.time()

def linear_pred(tick):
    inputs = yf.download(tick,period="1d")[["Open","High","Low"]]
    print(type(inputs))
    with open(r"C:\Project\STOCK_PREDICTOR\backend\models/linear_model.json" ,"r") as file : 
        data = json.load(file)
        weights = data["weights"]["ticker"==tick]
        slopes = weights["slopes"]
        intercept = weights["intercept"]
        x =  inputs["Open"].values* slopes[0] + inputs["High"].values*slopes[1] + inputs["Low"].values*slopes[2] + intercept 
        print("debug 1 is complete")
        return x[0]

def prediction_page(tick): 
   
    close =  yf.download(tick,period="4d")["Close"].values
    todays_price = give_price_failsafe({},get_date(0),get_date(1),get_date(2),tick)
    try : 
        inputs = np.array(close).reshape(1,3,1)
    except : 
        close = close[:-1]
        inputs = np.array(close).reshape(1,3,1)
    model = load_model(r"C:\Project\STOCK_PREDICTOR\backend\models/" +tick+".h5")
    prediction = model.predict(inputs)[0][0]
    linear_prediction  = linear_pred(tick) 
    print(type(prediction))
    models = {"lstm":str(prediction),"linear":str(linear_prediction),'graph_data' : todays_price}
    print("Debug 2 is complete")
    return models



def garbage(tick): 
    return give_price(get_date(0),get_date(1),get_date(2),tick)

