from flask import Flask , request 
from flask_cors import CORS 
from models import Linear_Regression 

app = Flask(__name__) 
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type' 


@app.route("/test")
def home(): 
    return "Hello to my server" 


@app.route("/forecast" , methods = ["POST"])
def forecast_out(): 
    name = request.args.get('stockTick')
    linear_model = Linear_Regression(name)
    forecast_output = linear_model.make_prdictions()
    output = {"forecast" : forecast_output[0] , "modelScore" : forecast_output[1]}
    return output 

if __name__ == "__main__" : 
    app.run(debug=True) 