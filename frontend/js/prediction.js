

const stock_name = localStorage.getItem("stock_name")
const stock_tick = localStorage.getItem("stock_tick")

$("#Dashboard").click(function(){
    window.location.assign("http://127.0.0.1:5500/frontend/index.html");
    return false ; 
  })
  
  
  $("#Stocks").click(function(){
    window.location.assign("http://127.0.0.1:5500/frontend/stocks.html"); 
    return false 
  })
  document.getElementById("stockname").innerHTML = `<h2>${stock_name}</h2>`
  document.getElementById("nifty").innerHTML = localStorage.getItem("nifty") ; 
  document.getElementById("sensex").innerHTML = localStorage.getItem("sensex") ; 
  document.getElementById("banknifty").innerHTML = localStorage.getItem("banknifty") ; 
  document.getElementById("niftyit").innerHTML = localStorage.getItem("niftyit") ; 

$.post(`http://127.0.0.1:5000/index?tick=${stock_tick}`, data =>{
    const graph = Object.values(data["graph_data"])
    let lstm = []; 
    let linear = [];
    for(var i = 0 ; i < graph.length ; i++){
        lstm.push(data["lstm"]);
        linear.push(data["linear"]); 
    }
    var lstm_chart = {
        series : [{
            name : stock_name , 
            data : graph 
        } ,{
            name : 'LSTM' , 
            data : lstm
        } , {
            name : 'LINEAR', 
            data : linear 
        }
    ] ,chart :{
            height : 350 , 
            type : "area"
        },dataLabels: {
          enabled: false
          }, stroke :{
            curve : "smooth", 
        },xaxis: {
          type: "category" , 
          labels : {
            show : false 
          } ,
          categories : Object.keys(data["graph_data"])
        }
    }
      var lstm_charts = new ApexCharts(document.querySelector("#chartlstm"),lstm_chart)
      lstm_charts.render()

    document.getElementById("sname").innerHTML = stock_name ;
    document.getElementById("stick").innerHTML = stock_tick ;
    document.getElementById("open").innerHTML = graph[0] ;
    document.getElementById("high").innerHTML = Math.max.apply(Math,graph) ;
    document.getElementById("low").innerHTML = Math.min.apply(Math,graph) ;
    document.getElementById("lstmpred").innerHTML = data["lstm"] ;
    document.getElementById("linearpred").innerHTML = data["linear"];

})



