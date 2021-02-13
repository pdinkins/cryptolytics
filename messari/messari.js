var XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;
const Http = new XMLHttpRequest();
const fetch = require("node-fetch");
const url = "https://data.messari.io/api/v1/assets?fields=id,slug,symbol,metrics/market_data/price_usd";


// fetch method
// fetch(url)
//.then(data => {return data.json()})
//.then(response => {console.log(response)})

function simpleRawRequests(url) {
    Http.open("GET", url);
    Http.send();
    Http.onreadystatechange = (e) => {var responseData = Http.responseText}
    return responseData
};

function rawRequest(url) {
    Http.open("GET", url);
    Http.send();
    Http.onreadystatechange = function() {
        if(this.readyState==4 && this.status==200){
            console.log(Http.responseText)}
        }
    };

function fetchRequest(url) {
    const fetch = require("node-fetch");
    fetch(url)
    .then(data => {return data.json()})
    .then(response => {var responseData = Http.response})
    return responseData
};

rawRequest(url);