
const fs = require("fs"); 


const url = "https://query1.finance.yahoo.com/v8/finance/chart/ADANIENT.NS" ; 

async function fetchData(url){
    let response = await fetch(url) ; 
    let data = await response.json(); 
    return data ; 
}


fetchData(url).then((data)=> {
    let data1 = JSON.stringify(data)
    fs.writeFile('data.json' , data1 , (err)=> {
        if(err)console.log(err);
        else console.log("Data written")
    })
});  