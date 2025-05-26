import pytest
from unittest.mock import Mock, ANY
from skill_boost_testing.order_and_warehouse.order import Order
from skill_boost_testing.order_and_warehouse.warehouse import Warehouse
from skill_boost_testing.order_and_warehouse.mail_service import MailService


# Fake implementation of MailService for testing
class FakeMailService(MailService):
    def __init__(self):
        self.sent_messages = []

    def send(self, message: str) -> None:
        self.sent_messages.append(message)

    def number_sent(self) -> int:
        return len(self.sent_messages)


# Constants
TALISKER = "Talisker"
HIGHLAND_PARK = "Highland Park"


@pytest.fixture
def warehouse():
    """Set up a warehouse with some initial inventory."""
    wh = Warehouse()
    wh.add(TALISKER, 50)
    wh.add(HIGHLAND_PARK, 25)
    return wh


def test_order_sends_mail_if_unfilled_fake(warehouse):
    """Test that an order sends a mail if it cannot be filled (using a fake)."""
    # Setup
    order = Order(TALISKER, 51)
    mailer = FakeMailService()

    # Guard assertion to verify assumptions
    assert mailer.number_sent() == 0

    order.set_mailer(mailer)

    # Exercise
    order.fill(warehouse)

    # Verify
    assert mailer.number_sent() == 1


def test_order_sends_mail_if_unfilled_mock(warehouse):
    """Test that an order sends a mail if it cannot be filled (using mocks)."""
    # Setup
    mailer_mock = Mock(spec=MailService)
    order = Order(TALISKER, 51, mailer_mock)

    # Exercise
    order.fill(warehouse)

    # Verify - check that the send method was called with any string
    mailer_mock.send.assert_called_with(ANY)
