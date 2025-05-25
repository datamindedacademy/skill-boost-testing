from skill_boost_testing.order_and_warehouse.warehouse import Warehouse


class Order:
    def __init__(self, product: str, quantity: int):
        self.product = product
        self.quantity = quantity
        self.is_filled = False

    def fill(self, warehouse: Warehouse) -> None:
        # If the product exists and there's enough capacity, our order is successful and we exit this function
        if warehouse.has_inventory(self.product):
            if warehouse.remove(self.product, self.quantity):
                self.is_filled = True
                return
