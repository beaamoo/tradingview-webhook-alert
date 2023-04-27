import requests, json
from chalice import Chalice

app = Chalice(app_name='tradingview-webhook-alert')

API_KEY = 'PKOOLJAMYKF4WNY6MYD2'
SECRET_KEY = 'emMXDK7zhuMxam0HhQpoKoWT6s4Y1ntsKCmqxMzy'
BASE_URL = "https://paper-api.alpaca.markets"
ORDERS_URL = "{}/v2/orders".format(BASE_URL)
HEADERS = {'APCA-API-KEY-ID': API_KEY, 'APCA-API-SECRET-KEY': SECRET_KEY}

@app.route('/')
def index():
    return{'hello': 'world'}

@app.route('/trade', methods=['POST'])
def trade():
    request = app.current_request
    webhook_message = request.json_body
    
    action = webhook_message['action']
    position_size = webhook_message['position_size']#total value of a particular trade
    
    data = {
        'symbol': webhook_message['ticker'],
        "qty": webhook_message['contracts'],
        "side": action,
        "type": "limit",
        "time_in_force": "gtc",
        "limit_price": webhook_message['close'],
        "order_class": "simple", #simple for crypto, bracket has three parts: a buy/sell order, a profit target order, and a stop loss order
        "take_profit": {
            "limit_price": webhook_message['close'] * 1.05
        },
        "stop_loss": {
            "stop_price": webhook_message['close'] * 0.90,
        }
    }
    r = requests.post(ORDERS_URL, json=data, headers=HEADERS)
    
    response = json.loads(r.content)

    return {
        'message': 'I traded the stock!',
        'webhook_message': webhook_message,
        'id': response['id'],
        'client_order_id': response['client_order_id']
    }