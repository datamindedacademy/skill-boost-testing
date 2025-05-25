import pytest

from skill_boost_testing.order_and_warehouse.order import Order
from skill_boost_testing.order_and_warehouse.warehouse import Warehouse


class TestOrder:
    TALISKER = "Talisker"
    HIGHLAND_PARK = "Highland Park"

    @pytest.fixture
    def warehouse(self):
        warehouse = Warehouse()
        warehouse.add(self.TALISKER, 50)
        warehouse.add(self.HIGHLAND_PARK, 25)
        return warehouse

    def test_order_is_filled_if_enough_in_warehouse(self, warehouse):
        order = Order(self.TALISKER, 50)
        order.fill(warehouse)

        assert order.is_filled
        assert warehouse.get_inventory(self.TALISKER) == 0

    def test_order_does_not_remove_if_not_enough(self, warehouse):
        order = Order(self.TALISKER, 51)
        order.fill(warehouse)

        assert not order.is_filled
        assert warehouse.get_inventory(self.TALISKER) == 50
