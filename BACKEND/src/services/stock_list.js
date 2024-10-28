

const fs = require('fs'); 


function sorted_symbol_data(data){
    const keys = Object.keys(data); 
    keys.sort(); 
    const sorted_array = {} ; 
    keys.forEach(key => {
        sorted_array[key] = data[key]; 
    })

    return sorted_array ; 
}

if (require.main === module){
    const data = require("./trialdata.json")
    const jsonstring = JSON.stringify(sorted_symbol_data(data) , null , 4); 

    fs.writeFile('data.json' , jsonstring , (err)=> {
        if(err){
            console.error("Error while writing the file "); 
        }

        else {
            console.log("File write successful to data.json ")
        }
    }) ; 
}


