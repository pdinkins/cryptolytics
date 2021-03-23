import requests
import pprint

apiURL = "https://data.messari.io/api/v1/assets?fields=id,slug,symbol,metrics/market_data/price_usd"
apiURL_BTC = "https://data.messari.io/api/v1/assets/bitcoin/metrics"
metrics_endpoint = "https://data.messari.io/api/v1/assets/metrics"

response = requests.get(apiURL).json()
response2 = requests.get(apiURL_BTC).json()


def btc_priceUSD():
    for i in range(0,19):
        if response['data'][i]['slug'] == 'bitcoin':
            return response['data'][i]['slug'], response['data'][i]['metrics']['market_data']['price_usd']

def eth_priceUSD():
    for i in range(0,19):
        if response['data'][i]['slug'] == 'ethereum':
            return response['data'][i]['slug'], response['data'][i]['metrics']['market_data']['price_usd']

def usdt_priceUSD():
    for i in range(0,19):
        if response['data'][i]['slug'] == 'tether':
            return response['data'][i]['slug'], response['data'][i]['metrics']['market_data']['price_usd']

def ada_priceUSD():
    for i in range(0,19):
        if response['data'][i]['slug'] == 'cardano':
            return response['data'][i]['slug'], response['data'][i]['metrics']['market_data']['price_usd']

def dot_priceUSD():
    for i in range(0,19):
        if response['data'][i]['slug'] == 'polkadot':
            return response['data'][i]['slug'], response['data'][i]['metrics']['market_data']['price_usd']

def xrp_priceUSD():
    for i in range(0,19):
        if response['data'][i]['slug'] == 'xrp':
            return response['data'][i]['slug'], response['data'][i]['metrics']['market_data']['price_usd']

def bnb_priceUSD():
    for i in range(0,19):
        if response['data'][i]['slug'] == 'binance-coin':
            return response['data'][i]['slug'], response['data'][i]['metrics']['market_data']['price_usd']

def ltc_priceUSD():
    for i in range(0,19):
        if response['data'][i]['slug'] == 'litecoin':
            return response['data'][i]['slug'], response['data'][i]['metrics']['market_data']['price_usd']

def doge_priceUSD():
    for i in range(0,19):
        if response['data'][i]['slug'] == 'dogecoin':
            return response['data'][i]['slug'], response['data'][i]['metrics']['market_data']['price_usd']

def link_priceUSD():
    for i in range(0,19):
        if response['data'][i]['slug'] == 'chainlink':
            return response['data'][i]['slug'], response['data'][i]['metrics']['market_data']['price_usd']

def bch_priceUSD():
    for i in range(0,19):
        if response['data'][i]['slug'] == 'bitcoin-cash':
            return response['data'][i]['slug'], response['data'][i]['metrics']['market_data']['price_usd']

def usdc_priceUSD():
    for i in range(0,19):
        if response['data'][i]['slug'] == 'usd-coin':
            return response['data'][i]['slug'], response['data'][i]['metrics']['market_data']['price_usd']

def uni_priceUSD():
    for i in range(0,19):
        if response['data'][i]['slug'] == 'uniswap':
            return response['data'][i]['slug'], response['data'][i]['metrics']['market_data']['price_usd']

def theta_priceUSD():
    for i in range(0,19):
        if response['data'][i]['slug'] == 'theta-token':
            return response['data'][i]['slug'], response['data'][i]['metrics']['market_data']['price_usd']

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
    print("usdc", usdc_priceUSD())
    print("uni", uni_priceUSD())
    print("theta", theta_priceUSD())


if __name__ == "__main__":
    #pprint.pprint(response)
    #test_price_functions()
    name, price = btc_priceUSD()
    print(price)