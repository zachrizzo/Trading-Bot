import time
import pandas as pd
from requests import HTTPError

import alpaca_trade_api as tradeapi
from alpaca_trade_api.common import URL
from alpaca_trade_api.stream import Stream


from bot import Bot


API_KEY = "PKUM529GXGRDHTQHPPI8"
SECRET_KEY = "hUV2Q6TgSVOrdl9D7r0nNoPMYlgN6Mr1HpOnX0Pl"
BASE_URL = 'https://paper-api.alpaca.markets'  # Replace with 'https://api.alpaca.markets' for live trading

api = tradeapi.REST(API_KEY, SECRET_KEY, BASE_URL, api_version='v2')

window = {}
account = api.get_account()
balance = account.cash


#### REFACTOR THESE
## Buy
# order = api.submit_order(
#     symbol='BTCUSD',
#     qty=0.0001,
#     side='buy',
#     type='market',
#     time_in_force='gtc'
# )

## Sell
# api.close_position('BTCUSD')



# Get the current balance of a cryptocurrency
try:
    balance = api.get_position('BTCUSD')
    print(balance)
except HTTPError as e:
    print("No position found")
except Exception as other:
    print(other)


async def quote_callback(q):
    print(q)

# bot = Bot(api, ["BTC/USD"], 10, 32, 1, 0.995, 0.01, 0.001, 0.9, 100000)
# bot.run()


"""
# Initiate Class Instance
stream = Stream(API_KEY,
                SECRET_KEY,
                base_url=URL(BASE_URL)
                )  # <- replace to 'sip' if you have PRO subscription

# subscribing to event
stream.subscribe_crypto_quotes(quote_callback, 'BTC/USD')


print("Running stream:")
stream.run()
"""