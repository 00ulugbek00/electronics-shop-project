from src.item import Item
import pytest


@pytest.mark.parametrize(
    ['price', 'quantity', 'total_price'], (
        (10_000, 20, 200_000),
        (1_000, 5, 5_000),
        (1_000, 0, 0),
    )
)
def test_calculate_total_price(price, quantity, total_price):
    item = Item('test_item', price, quantity)
    assert item.calculate_total_price() == total_price