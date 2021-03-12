from alpha_vantage.foreignexchange import ForeignExchange
from pprint import pprint
import sys
import time


# TODO: api keys 
apikey = src/api1.key
__debug = True
currencylayerAPI_key = src/api.key
currencylayerAPI_baseurl = "http://apilayer.net/api/"

def cc_indo():
    cc = ForeignExchange(key=apikey)
    # There is no metadata in this call
    while __debug:
        data, moredata = cc.get_currency_exchange_rate(from_currency='BTC',to_currency='USD')
        print(data["5. Exchange Rate"], end="\r")
        time.sleep(2)

if __name__ == "__main__":
    if __debug:
        cc_indo()
    else:
        sys.exit()
