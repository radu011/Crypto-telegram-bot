from ssl import ALERT_DESCRIPTION_HANDSHAKE_FAILURE
from binance import Client


def getCryptoPrice(crypto):
    api_key = ""            # insert Binance API key here
    api_secret = ""         # insert Binance API secret here

    client = Client(api_key, api_secret, testnet=True)

    ex = crypto + "USDT"

    info = client.get_symbol_info(ex)

    data = info[name] + ": " + info[price]

    return data