const { response } = require("express");
const https = require("https"); 


function getData(){
    fetch("https://www.nseindia.com/market-data/live-equity-market")
    .then(async (response) => {
            let data = await response.text()
            return data ; 
    })
}

const data = getData()
console.log(data); 


