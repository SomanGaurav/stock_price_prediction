import json
import pandas as pd 
def read_json(): 
    name = []
    tick = []
    with open("model_training/stocks.json","r") as file : 
        data = json.load(file)
        for i in range(0,50): 
            name.append(data[i]["name"])
            tick.append(data[i]["tick"])

        stocks = pd.DataFrame({'name': name,'tick':tick }, columns=['name','tick'])

        stocks.to_csv('nifty_tick.csv')

print(read_json())