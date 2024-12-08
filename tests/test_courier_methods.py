from data import Constants
from methods.methods_courier import CourierMethods
from helpers import RandomCred
import pytest

class TestCreateCourier:

    def test_create_courier(self):
        login = RandomCred.generate_login()
        password = RandomCred.generate_password()
        first_name = RandomCred.generate_name()
        courier_data = CourierMethods.create_courier(login, password, first_name)
        assert courier_data == (201, {'ok': True})

    def test_create_similar_courier(self):
        login = Constants.LOGIN
        password = Constants.PASSWORD
        first_name = Constants.FIRST_NAME
        courier_data = CourierMethods.create_courier(login, password, first_name)
        assert courier_data == (409, {"code": 409, "message": "Этот логин уже используется. Попробуйте другой."})

    @pytest.mark.parametrize(
        'login, password, first_name',
        [
            ("", RandomCred.generate_password, RandomCred.generate_name),
            (RandomCred.generate_login, "", RandomCred.generate_name)
        ]
    )
    def test_create_courier_ncomplete_data(self, login, password, first_name):
        courier_data = CourierMethods.create_courier(login, password, first_name)
        assert courier_data == (400, {"code": 400, "message": "Недостаточно данных для создания учетной записи"})

class TestLoginCourier:
    def test_login_courier(self):
        login = Constants.LOGIN
        password = Constants.PASSWORD
        courier_data = CourierMethods.login_courier(login, password)
        assert courier_data['id'] == Constants.ID

    @pytest.mark.parametrize(
        'login, password',
        [
            (Constants.LOGIN, "123"),
            ("test_user_8", Constants.PASSWORD)
        ]
    )
    def test_login_courier_with_error(self, login, password):
        courier_data = CourierMethods.login_courier(login, password)
        assert courier_data == ({"code": 404, "message": "Учетная запись не найдена"})

    @pytest.mark.parametrize(
        'login, password',
        [
            (Constants.LOGIN, ""),
            ("", Constants.PASSWORD)
        ]
    )
    def test_login_courier_incomplete_data(self, login, password):
        courier_data = CourierMethods.login_courier(login, password)
        assert courier_data == ({"code": 400, "message": "Недостаточно данных для входа"})
