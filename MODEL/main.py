from flask import Flask , request 
from flask_cors import CORS 
from flask import jsonify
import sys 
import os 


from src.utils.models import Linear_Regression 
from src.routes.index_data import Indices 
#when running from this file there is no need for sys.path as this is not part of the package directory . 


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


@app.route("/getIndices" , methods = ["POST"]) 
def indices_out(): 
    indices = request.get_json() 
    # clean_index(indices)
    return jsonify({"Hello" : "NODE"} )
if __name__ == "__main__" : 
    input_dict = {'params' : {'indexList' : "^NSEI_^BSESN_^NSEBANK_^CNXIT"} }
    IC = Indices(input_dict)
    app.run(debug=True , host='0.0.0.0') 