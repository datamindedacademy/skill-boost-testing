from typing import Optional
from skill_boost_testing.order_and_warehouse.warehouse import Warehouse
from skill_boost_testing.order_and_warehouse.mail_service import MailService


class Order:
    def __init__(self, product: str, quantity: int, mail_service: Optional[MailService] = None):
        self.product = product
        self.quantity = quantity
        self.is_filled = False
        self.mail_service: Optional[MailService] = mail_service

    def fill(self, warehouse: Warehouse) -> None:
        # If the product exists and there's enough capacity, our order is successful and we exit this function
        if warehouse.has_inventory(self.product):
            if warehouse.remove(self.product, self.quantity):
                self.is_filled = True
                return

        self._send_email()

    def set_mailer(self, mail_service: MailService) -> None:
        self.mail_service = mail_service

    def _send_email(self) -> None:
        if self.mail_service is not None:
            self.mail_service.send(f"The product {self.product} is currently not available :(")
