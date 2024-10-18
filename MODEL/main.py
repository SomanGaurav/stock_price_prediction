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
    name = request.get_json() 
    flag = 1
    name = name['params']['stockTick']
    print(name)
    if(name!=None and flag == 1): 
        linear_model = Linear_Regression(name)
        forecast_output = linear_model.make_prdictions()
        output = {"forecast" : forecast_output[0] , "modelScore" : forecast_output[1]}

    else : 
        output = name
    return output 

if __name__ == "__main__" : 
    app.run(debug=True , host='0.0.0.0') 