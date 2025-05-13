import logging
from binance.client import Client
from binance.enums import *
import sys

# Setup Logging
logging.basicConfig(filename='bot.log', level=logging.INFO,
                    format='%(asctime)s %(levelname)s:%(message)s')

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.client = Client(api_key, api_secret)
        if testnet:
            self.client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi'

    def place_order(self, symbol, side, order_type, quantity, price=None):
        try:
            if order_type == 'MARKET':
                order = self.client.futures_create_order(
                    symbol=symbol, side=side, type=order_type, quantity=quantity)
            elif order_type == 'LIMIT':
                order = self.client.futures_create_order(
                    symbol=symbol, side=side, type=order_type,
                    quantity=quantity, price=price, timeInForce=TIME_IN_FORCE_GTC)
            logging.info(f"Order response: {order}")
            return order
        except Exception as e:
            logging.error(f"Error placing order: {str(e)}")
            return None

# CLI Input Handling
if __name__ == "__main__":
    api_key = input("Enter API Key: ")
    api_secret = input("Enter API Secret: ")

    bot = BasicBot(api_key, api_secret)

    symbol = input("Symbol (e.g. BTCUSDT): ").upper()
    side = input("Side (BUY/SELL): ").upper()
    order_type = input("Order Type (MARKET/LIMIT): ").upper()
    quantity = float(input("Quantity: "))
    price = None
    if order_type == 'LIMIT':
        price = input("Price: ")

    result = bot.place_order(symbol, side, order_type, quantity, price)
    if result:
        print("Order Placed:", result)
    else:
        print("Order Failed")
# Add another condition in place_order
elif order_type == 'STOP_MARKET':
    order = self.client.futures_create_order(
        symbol=symbol, side=side, type='STOP_MARKET',
        stopPrice=stop_price, quantity=quantity, timeInForce=TIME_IN_FORCE_GTC)
