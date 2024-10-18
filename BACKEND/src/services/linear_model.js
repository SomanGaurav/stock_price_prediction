


const axios = require("axios"); 


axios.post("http://172.17.0.3:5000/forecast" , {
    params:{
        stockTick : "ADANIENT.NS"
    }
}).then(response => {console.log(response.data)})
.catch(error => console.error(error));
