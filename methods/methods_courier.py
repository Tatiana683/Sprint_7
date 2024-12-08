import requests
from data import Constants

class CourierMethods:
    def create_courier(login, password, first_name):
        data = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        response = requests.post(f'{Constants.BASE_URL}{Constants.COURIERS_URL}', data = data)
        return response.status_code, response.json()

    def login_courier(login, password):
        data = {
            "login": login,
            "password": password
        }
        response = requests.post(f'{Constants.BASE_URL}{Constants.LOGIN_URL}', data = data)
        return response.json()
