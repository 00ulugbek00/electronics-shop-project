import pytest

from src.item import Item


@pytest.fixture(autouse=True)
def clear_items():
    Item.all = []


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


@pytest.mark.parametrize(
    ['discount', 'price_with_discount'], (
            (0, 10_000),
            (0.15, 8_500),
            (0.27, 7_300),
    )
)
def test_apply_discount(discount, price_with_discount):
    item = Item('test_item', 10_000, 20)
    Item.pay_rate = 1 - discount

    item.apply_discount()

    assert item.price == price_with_discount


def test_all_items():
    item1 = Item('test_1', 10_000, 20)
    item2 = Item('test_2', 20_000, 5)

    assert Item.all == [item1, item2]


def test_instantiate_from_csv():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5

    assert Item.string_to_number('5.5') == 5


def test_item1_from_csv_name():
    Item.instantiate_from_csv()
    item1 = Item.all[0]
    assert item1.name == 'Смартфон'
