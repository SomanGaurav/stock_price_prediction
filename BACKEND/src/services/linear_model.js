const axios = require("axios"); 

async function Linear_model() {
    axios.post("http://172.17.0.3:5000/forecast" , {
        params:{
            stockTick : "ADANIENT.NS"
        }
    }).then(response => {
        return response.data 
    })
    .catch(error => console.error(error));
}


console.log(await Linear_model())

