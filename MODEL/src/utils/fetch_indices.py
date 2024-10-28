import numpy as np 
import pandas as pd
import yfinance as yf
import json

__package__ = None 
class IndexCollector : 
    def __init__(self , indices : list):
        self.indices = indices 
        self.length = len(indices) 
        self.data = {}

    def fetch_data(self): 
        self.valid_tickers = [] 
        for tick in self.indices : 
            try : 
                stock = yf.Ticker(tick) 
                stock_name = stock.info.get('longName') 
                historical_data : pd.DataFrame = yf.download(tick , period="5y")["Close"].reset_index()
                historical_data['Date'] = historical_data['Date'].dt.strftime('%Y-%m-%d')
                self.data[tick] ={"name" : stock_name , "data" :  historical_data.to_dict(orient='list')}

            except(KeyError , IndexError): 
                self.data[tick] = "NAN"
                continue 
        
        return self.data


    def get_hist_data(self): 
        temp_data : pd.DataFrame = self.historical_data 
        json_result = temp_data.to_json(orient='records')
        return json_result 

    def trial(self): 
        tick = self.indices[0]
        try : 
            stock = yf.Ticker(tick) 
            stock_name = stock.info.get('longName') 
            historical_data = yf.download(tick , period="5y")["Close"]
            historical_data = historical_data.reset_index()
            historical_data['Date'] = historical_data['Date'].dt.strftime('%Y-%m-%dT%H:%M:%S')
            print(historical_data.head(5))
            return historical_data.to_numpy()
        except(KeyError , IndexError): 
            return 0 
            
        


if __name__ == "__main__": 
#"^NSEI" , "^BSESN" , "^NSEBANK" , "^CNXIT"
    IC = IndexCollector(["^NSEI" , "^BSESN" , "^NSEBANK" , "^CNXIT" ])
    print(IC.fetch_data())
