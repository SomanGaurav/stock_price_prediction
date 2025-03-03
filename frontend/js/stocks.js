$("#Dashboard").click(function(){
    window.location.assign("http://127.0.0.1:5500/frontend/index.html");
    return false ; 
  })
  
  
  $("#Stocks").click(function(){
    window.location.assign("http://127.0.0.1:5500/frontend/stocks.html"); 
    return false 
  })
  
  

function generateList(arg){
  let items = "" ; 
  for(let i = 0 ; i < arg.length ; i++){
    items += `<span class="container"><h4>${arg[i]}</h3></span>`
  }
  return items ; 
}
function getRequest(){
    $.get("http://127.0.0.1:5000/stock_list",data =>{
        let stocks = data["stocks"]
        let stocknames = [] ; 
        let stockticks = []; 
        let stockobj = {}; 
        stocks.forEach(Element => {
          stocknames.push(Element["name"])
          stockticks.push(Element["tick"])
          stockobj[Element["name"]] = Element["tick"]
        })
        document.querySelector(".stock-container").innerHTML = `
          ${generateList(stocknames)}
        `
        $(".container").click(function(e){
          let clicked_div = $(this).text()
          let clicked_tick = stockobj[clicked_div]
          localStorage.setItem("stock_name",clicked_div)
          localStorage.setItem("stock_tick",clicked_tick)
          window.location.assign("http://127.0.0.1:5500/frontend/prediction.html")
        })

    })
}

window.onload = ()=>{

  getRequest()
}