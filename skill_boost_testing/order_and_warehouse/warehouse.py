from typing import Dict


class Warehouse:
    def __init__(self):
        self.items: Dict[str, int] = {}

    def add(self, product: str, quantity: int) -> None:
        self.items[product] = quantity

    def get_inventory(self, product: str) -> int:
        return self.items.get(product, 0)

    def remove(self, product: str, quantity: int) -> bool:
        inventory = self.items.get(product, 0)
        if quantity <= inventory:
            self.items[product] = inventory - quantity
            return True
        return False

    def has_inventory(self, product: str) -> bool:
        inventory = self.items.get(product, 0)
        return inventory > 0
