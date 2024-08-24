import data_collector 
from sklearn.linear_model import LinearRegression 

class Linear_Regression : 
    def __init__(self , stock_tick , start) -> None:
        self.stock_tick = stock_tick 
        self.dc = data_collector.DATACOLLECTOR()
        self.lr = LinearRegression()
        self.start = start 

    def model_train(self): 
        X_train , X_test , y_train , y_test = self.dc.linear_reg_data(self.stock_tick , self.start)
        self.lr.fit(X_train , y_train)



if __name__ == "__main__" : 
    linearmodel = Linear_Regression("ADANIENT.NS" , start = "2012-01-01") 
    linearmodel.model_train()