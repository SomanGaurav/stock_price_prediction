# Stock Price Prediction 
Stock Price Prediction is a web based appication that makes use of Models like Long Short Term Memory and Linear Regression to assist **Intraday Traders** for choosing a correct stock and predicting the price at which the stock closes . 
This Application Makes use of Basic Html , CSS and Javascript to serve the frontend on the browser . We make use of Flask library in Python to provide the RESTFUL API to allow authenticated users to avail the model services . 

### How does this Application helps Intraday traders . 
- The *LSTM* model make a next day prediction using previous month data to whether tommorrow the stock price will increase or decrease .
- The *Linear Regressor* makes prediction using current day data , i.e. Open , High , Low Prices to predict at what price will the stock close .

### Model Training and Setup 

To train the model locally one must first install and Setup Python and install dependencies such as :- 
* Flask
* Tensorflow and keras
* yfinance
* etc .
Once the dependencies are installed run the linear_trainer.py and lstm_trainer.py files from the model_training directory. 
   
**How are the models Saved** 
- The Linear Regression saves the model for a particular stock in form of it's weights and bias in a json file associated with stock symbol .
- The LSTM model is save inside the model folder as a form of tensorflow saved model . 

### How to use the model . 
- The First step would be setup and to complete the model training for both linear regressor and LSTM .
- Start the Flask server and note the port it's running on .
- From the browser access that port thorugh localhost to expose the frontend code .
- Select the Stock that you want to further analyse .
- The specific stock page provide predictions from both the LSTM and the Linear model .
