from flask import Flask 
from flask_cors import CORS 
import yfinance as yf 
from flask import request
from datetime import datetime 
from garbage import get_date ,give_price , get_index , read_json,prediction_page , give_price_failsafe
app = Flask(__name__)
CORS(app)

@app.route("/")
def index_nifty(): 
    sensex = get_index(get_date(0),get_date(1),get_date(2),"^BSESN")
    banknifty = get_index(get_date(0),get_date(1),get_date(2),"^NSEBANK")
    niftyit = get_index(get_date(0),get_date(1),get_date(2),"^CNXIT")
    nifty = give_price_failsafe({} , get_date(0),get_date(1),get_date(2),"^NSEI")
    return {"sensex":sensex,"banknifty":banknifty,"niftyit": niftyit , "nifty": nifty}

@app.route("/index",methods=["POST"])
def get_indice(): 
    tick = request.args.get("tick")
    print(tick)
    return prediction_page(tick)


@app.route("/stock_list")
def get_stock_name(): 
    return read_json() 
if __name__ == "__main__": 
    app.run(debug = True,threaded = True)



