import pytest

from data import Constants
from methods.methods_order import OrderMethods


class TestCreateCourier:

    @pytest.mark.parametrize(
        'color',
        [
            ([]),
            (["BLACK"]),
            (["GREY"]),
            (["BLACK", "GREY"])
        ]
    )
    def test_create_order_with_different_colors_of_scooter(self, color):
        order_data = OrderMethods.create_order(color)
        assert order_data['track'] is not None

    def test_uploading_list_of_orders(self):
        order_data = OrderMethods.list_of_orders()
        assert order_data == (200, Constants.DATA_FOR_CHECK)
