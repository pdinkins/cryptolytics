import requests

apiURL = "https://data.messari.io/api/v1/assets?fields=id,slug,symbol,metrics/market_data/price_usd"
apiURL_BTC = "https://data.messari.io/api/v1/assets/bitcoin/metrics"
metrics_endpoint = "https://data.messari.io/api/v1/assets/metrics"

response = requests.get(apiURL).json()
response2 = requests.get(apiURL_BTC).json()

print(response2)

def btc_priceUSD():
    return response['data'][0]['metrics']['market_data']['price_usd']

def eth_priceUSD():
    return response['data'][1]['metrics']['market_data']['price_usd']

def usdt_priceUSD():
    return response['data'][2]['metrics']['market_data']['price_usd']

def ada_priceUSD():
    return response['data'][3]['metrics']['market_data']['price_usd']

def dot_priceUSD():
    return response['data'][4]['metrics']['market_data']['price_usd']

def xrp_priceUSD():
    return response['data'][5]['metrics']['market_data']['price_usd']

def bnb_priceUSD():
    return response['data'][6]['metrics']['market_data']['price_usd']

def ltc_priceUSD():
    return response['data'][7]['metrics']['market_data']['price_usd']

def doge_priceUSD():
    return response['data'][8]['metrics']['market_data']['price_usd']

def link_priceUSD():
    return response['data'][9]['metrics']['market_data']['price_usd']

def bch_priceUSD():
    return response['data'][10]['metrics']['market_data']['price_usd']

def xlm_priceUSD():
    return response['data'][11]['metrics']['market_data']['price_usd']

def usdc_priceUSD():
    return response['data'][12]['metrics']['market_data']['price_usd']

def aave_priceUSD():
    return response['data'][13]['metrics']['market_data']['price_usd']

def uni_priceUSD():
    return response['data'][14]['metrics']['market_data']['price_usd']

def wbtc_priceUSD():
    return response['data'][15]['metrics']['market_data']['price_usd']

def tern_priceUSD():
    return response['data'][16]['metrics']['market_data']['price_usd']

def bsv_priceUSD():
    return response['data'][17]['metrics']['market_data']['price_usd']

def eos_priceUSD():
    return response['data'][18]['metrics']['market_data']['price_usd']

def egld_priceUSD():
    return response['data'][19]['metrics']['market_data']['price_usd']

def test_price_functions():
    print("btc", btc_priceUSD())
    print("eth", eth_priceUSD())
    print("usdt", usdt_priceUSD())
    print("ada", ada_priceUSD())
    print("dot", dot_priceUSD())
    print("xrp", xrp_priceUSD())
    print("bnb", bnb_priceUSD())
    print("ltc", ltc_priceUSD())
    print("doge", doge_priceUSD())
    print("link", link_priceUSD())
    print("bch", bch_priceUSD())
    print("xlm", xlm_priceUSD())
    print("usdc", usdc_priceUSD())
    print("aave", aave_priceUSD())
    print("uni", uni_priceUSD())
    print("wbtc", wbtc_priceUSD())
    print("tern", tern_priceUSD())
    print("bsv", bsv_priceUSD())
    print("eos", eos_priceUSD())
    print("egld", egld_priceUSD())


if __name__ == "__main__":
    test_price_functions()