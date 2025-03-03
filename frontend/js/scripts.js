// SIDEBAR TOGGLE

var sidebarOpen = false;
var sidebar = document.getElementById("sidebar");

function openSidebar() {
  if(!sidebarOpen) {
    sidebar.classList.add("sidebar-responsive");
    sidebarOpen = true;
  }
}
console.log(window.location)
$("#Dashboard").click(function(){
  window.location.assign("http://127.0.0.1:5500/frontend/index.html");
  return false ; 
})


$("#Stocks").click(function(){
  window.location.assign("http://127.0.0.1:5500/frontend/stocks.html"); 
  return false 
})




function sendRequest(){
  $.get("http://127.0.0.1:5000/" ,(data)=>{ 
    let stocknames = [] ; 
    let objDAT  = data["nifty"] ; 
    let nifty = Object.values(data["nifty"]); 
    let sensex = data["sensex"]; 
    let banknifty = data["banknifty"]; 
    let niftyit = data["niftyit"]; 
    document.getElementById("nifty").innerHTML = nifty.slice(-1)[0] ; 
    document.getElementById("sensex").innerHTML = sensex ; 
    document.getElementById("banknifty").innerHTML = banknifty ; 
    document.getElementById("niftyit").innerHTML = niftyit ; 

    localStorage.setItem("nifty",nifty.slice(-1)[0])
    localStorage.setItem("sensex",sensex)
    localStorage.setItem("banknifty",banknifty)
    localStorage.setItem("niftyit",niftyit)
    // document.getElementById("sensex").innerHTML = sensex
    var nifty_chart = {
      series : [{
          name : "Nifty " , 
          data : nifty 
      }] ,chart :{
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
        categories : Object.keys(objDAT)
      }
  }
    var nifty_chart = new ApexCharts(document.querySelector("#chartDiv"),nifty_chart)
    nifty_chart.render()
  })

  
}
function closeSidebar() {
  if(sidebarOpen) {
    sidebar.classList.remove("sidebar-responsive");
    sidebarOpen = false;
  }
}

window.onload = () => {
  sendRequest()
}


// ---------- CHARTS ----------

// BAR CHART








// AREA CHART

var areaChart = new ApexCharts(document.querySelector("#area-chart"), areaChartOptions);
areaChart.render();