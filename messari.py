import requests

apiURL = "https://data.messari.io/api/v1/assets?fields=id,slug,symbol,metrics/market_data/price_usd"

response = requests.get(apiURL).json()
#print(type(response))

keys = response.keys()
keys_list = list()
for i in keys:
    keys_list.append(i)

data_response = response[keys_list[1]]
#print(response[keys_list[1]])
#print(data_response)
#print(type(data_response))

l2_keys = data_response[0].keys()
l2_keys_list = list()
for i in l2_keys:
    l2_keys_list.append(i)

def api_dump():
    for i in range (0,len(data_response)):
        for j in range(2,4):
            print(data_response[i][l2_keys_list[j]])

def bitcoin_price():
    return data_response[0][l2_keys_list[3]]['market_data']['price_usd']

def ethereum_price():
    return data_response[1][l2_keys_list[3]]['market_data']['price_usd']

def link_price():
    return data_response[9][l2_keys_list[3]]['market_data']['price_usd']


def test_price_oracles():
    print("btc", bitcoin_price())
    print("eth", ethereum_price())
    print("link", link_price())

if __name__ == "__main__":
    test_price_oracles()