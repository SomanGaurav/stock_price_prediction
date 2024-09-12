
import yfinance as yf
import pandas as pd
import numpy as np 
from sklearn.model_selection import train_test_split

class DATACOLLECTOR : 
    def __init__(self) -> None:
        stock_data = pd.DataFrame() 
        self.forecast_out = 30 
        self.stock_data = stock_data 


    def download(self , stock_tick , start): 
        self.stock_data = yf.download(stock_tick , start=start) 


    def linear_reg_data(self ,stock_tick , start): 
        self.download(stock_tick , start)
        self.stock_data['Prediction'] = self.stock_data[['Adj Close']].shift(-self.forecast_out)
        self.X = np.array(self.stock_data.drop(['Prediction'] , axis=1))
        self.X = self.X[:-self.forecast_out]
        self.y = np.array(self.stock_data['Prediction'])
        self.y = self.y[:-self.forecast_out]
        self.x_forecast = np.array(self.stock_data.drop(['Prediction'] , axis = 1))[-self.forecast_out : ]
        X_train , X_test , y_train , y_test = train_test_split(self.X , self.y , test_size = 0.2)
        return X_train , X_test , y_train , y_test 
    

    def pred_data(self): 
        return self.x_forecast 


if __name__ == "__main__" : 
    dc = DATACOLLECTOR()
    dc.linear_reg_data("ADANIENT.NS")