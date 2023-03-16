import time
# import nest_asyncio
# from alpaca.data.live import StockDataStream
# from alpaca.data.historical import StockHistoricalDataClient
# from alpaca.trading.requests import MarketOrderRequest
# from alpaca.trading.enums import OrderSide, TimeInForce
# from alpaca.trading.client import TradingClient
# from alpaca.trading.requests import GetAssetsRequest
# from alpaca.trading.enums import AssetClass
# #trading_client
# from alpaca.trading.client import TradingClient
# #LimitOrderRequest
# from alpaca.trading.requests import LimitOrderRequest

# from alpaca.data.requests import StockLatestQuoteRequest


# nest_asyncio.apply()
import alpaca_trade_api as tradeapi
import pandas as pd


API_KEY = "PKUM529GXGRDHTQHPPI8"
SECRET_KEY = "hUV2Q6TgSVOrdl9D7r0nNoPMYlgN6Mr1HpOnX0Pl"

api_key = API_KEY
api_secret = SECRET_KEY
base_url = 'https://paper-api.alpaca.markets'  # Replace with 'https://api.alpaca.markets' for live trading

api = tradeapi.REST(api_key, api_secret, base_url, api_version='v2')

for i in range(0, 10):
    time.sleep(3)
    crypto_data = api.get_latest_crypto_trades(symbols=['BTC/USD'])

    print(crypto_data)

