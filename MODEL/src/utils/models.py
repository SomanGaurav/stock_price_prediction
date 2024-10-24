from src.utils.data_collector import DATACOLLECTOR 
#from data_collector import DATACOLLECTOR 
from sklearn.linear_model import LinearRegression 

'''when running this file change the import to remove src.utils as they are in same directory 
but for main.py we have to specify the path for the dependency graph '''




class Linear_Regression : 
    def __init__(self , stock_tick ) -> None:
        self.stock_tick = stock_tick 
        self.dc = DATACOLLECTOR()
        self.lr = LinearRegression()
        self.start = "2012-01-01" 

    def model_train(self): 
        X_train , X_test , y_train , y_test = self.dc.linear_reg_data(self.stock_tick , self.start)
        self.lr.fit(X_train , y_train)
        self.lr_score = self.lr.score(X_test , y_test) 
        return self.lr_score


    def make_prdictions(self): 
        self.model_score = self.model_train()
        inputs = self.dc.pred_data()
        lr_pred = self.lr.predict(inputs) 
        return (lr_pred.tolist() , self.model_score) 
 



if __name__ == "__main__" : 
    linearmodel = Linear_Regression("ADANIENT.NS") 
    print(linearmodel.make_prdictions())