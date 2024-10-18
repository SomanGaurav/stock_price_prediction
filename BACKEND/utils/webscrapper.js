


async function getData(){
    const url = "https://www.nseindia.com/market-data/live-equity-market" ; 

    const response = await fetch(url); 
    const html = await response.text(); 
    
    console.log(html[145138]); 
}

getData()