
import json 
import sys 
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from utils.fetch_indices import IndexCollector 

class Indices(IndexCollector): 
    def __init__(self, input_dictionary): 
        self.input_arr : list = self.clean_index(input_dictionary)
        self.collected_data = {} 
        super().__init__(self.input_arr) 


    def create_json(self): 
        self.collected_data = self.fetch_data()
        with open('src/routes/data.json' , 'w') as file : 
            json.dump(self.collected_data , file , indent= 4)

        
        
    def clean_index(self , input_string): 
    # indices = input_string.split("_") 
        indices = input_string['params']['indexList']
        indices = indices.split("_")
        return indices 
    
    # super().__init__(indices)


if __name__ == "__main__": 
    input_dict = {'params' : {'indexList' : "^NSEI_^BSESN_^NSEBANK_^CNXIT"} }
    indices = Indices(input_dict)
    print(indices.create_json())


