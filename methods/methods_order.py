import requests
from data import Constants
import json

class OrderMethods:
    def create_order(color):
        data = Constants.DATA_FOR_CREATE_ORDER
        data["color"] = color
        json_data = json.dumps(data)
        response = requests.post(f'{Constants.BASE_URL}{Constants.ORDER_URL}', json_data)
        return response.json()

    def list_of_orders():
        response = requests.get(f'{Constants.BASE_URL}{Constants.ORDER_URL}?courierId={Constants.ID}')
        return response.status_code, response.json()
