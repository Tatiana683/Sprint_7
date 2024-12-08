class Constants:
    BASE_URL = 'https://qa-scooter.praktikum-services.ru/api/v1/'
    COURIERS_URL = 'courier'
    LOGIN_URL = 'courier/login'
    ORDER_URL = 'orders'

    LOGIN = "test_user_123"
    PASSWORD = "141091"
    FIRST_NAME = "Gosling"
    ID = 431995

    DATA_FOR_CREATE_ORDER = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2024-12-12",
        "comment": "Saske, come back to Konoha"
    }

    DATA_FOR_CHECK = {'orders': [], 'pageInfo': {'page': 0, 'total': 0, 'limit': 30}, 'availableStations': []}

