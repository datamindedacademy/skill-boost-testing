import pytest
from unittest.mock import Mock, ANY
from skill_boost_testing.order_and_warehouse.order import Order
from skill_boost_testing.order_and_warehouse.warehouse import Warehouse

TALISKER = "Talisker"

"""
The difference lies in the objects that are created. The SUT (System Under Test) is the same - an order. 
The collaborator, however, is no longer a warehouse object, but a mock warehouse.
The second part of the setup creates expectations about the mock object. The expectations indicate which methods 
should be called on the mock when the SUT is exercised.
Once all expectations are set, we execute the test method on the SUT.
After execution, verification happens, which has two aspects. I perform assertions against the SUT - just like before.
However, I also verify the mocks - checking if they were executed according to their expectations.

The main difference here is how we check if the order did the right thing in the interaction with the warehouse.
With state verification, we do this by checking against the state of the warehouse.
Mocks, however, use behavior verification, where we instead check if the order made the method calls on the warehouse object.
We do this check by telling the mock what to expect during setup and asking the mock to verify itself during verification.
If the order class method doesn't change the state of the order, there may not be any assertions at all, and we only check 
if warehouse methods were called using verify!
"""


def test_filling_removes_inventory_if_in_stock():
    # setup - data
    order = Order(TALISKER, 50)
    warehouse_mock = Mock(spec=Warehouse)

    # setup - expectations
    warehouse_mock.has_inventory.return_value = True
    warehouse_mock.remove.return_value = True

    # exercise
    order.fill(warehouse_mock)

    # verify
    warehouse_mock.has_inventory.assert_called_with(TALISKER)
    warehouse_mock.remove.assert_called_with(TALISKER, 50)
    assert order.is_filled is True


def test_filling_does_not_remove_if_not_enough_in_stock():
    # setup
    order = Order(TALISKER, 51)
    warehouse = Mock(spec=Warehouse)

    # setup expectations
    warehouse.has_inventory.return_value = False

    # exercise
    order.fill(warehouse)

    # verify
    warehouse.has_inventory.assert_called_with(TALISKER)
    assert order.is_filled is False
