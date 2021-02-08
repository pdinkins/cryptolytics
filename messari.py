import requests

apiURL = "https://data.messari.io/api/v1/assets?fields=id,slug,symbol,metrics/market_data/price_usd"
apiURL_BTC = "https://data.messari.io/api/v1/assets/bitcoin/metrics"

response = requests.get(apiURL).json()

def bitcoin_price():
    return response['data'][0]['metrics']['market_data']['price_usd']

def ethereum_price():
    return response['data'][1]['metrics']['market_data']['price_usd']

def link_price():
    return response['data'][9]['metrics']['market_data']['price_usd']


def test_price_oracles():
    print("btc", bitcoin_price())
    print("eth", ethereum_price())
    print("link", link_price())

if __name__ == "__main__":
    test_price_oracles()