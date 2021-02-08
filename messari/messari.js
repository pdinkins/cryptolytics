var XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;
const Http = new XMLHttpRequest();
const url = "https://data.messari.io/api/v1/assets?fields=id,slug,symbol,metrics/market_data/price_usd";

Http.open("GET", url);
Http.send();

Http.onreadystatechange = function() {
    if(this.readyState==4 && this.status==200){
        console.log(Http.responseText)
    }
}
