"use strict"; 

const axios = require("axios") ; 

async function getIndices(params){
    // let data ; 
    // axios.post("http://172.17.0.3:5000/getIndices"  ,{
    //     params : {
    //         indexList : params 
    //     }
    // } ).then(response => {
    //     console.log(response.data)
    //     data = response.data ; 
    // }).catch(error => console.log(error)) ; 


    const response = await axios.post("http://172.17.0.3:5000/getIndices"  ,{
            params : {
                indexList : params 
            }
        } 
    )

    return response.data

}


async function printdata(){
    const data = getIndices("^NSEI_^BSESN_^NSEBANK_^CNXIT").then(response=>{
        console.log(response) 
    })
}

if(require.main === module){
    printdata(); 
}