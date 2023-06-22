from src.item import Item
import pytest

def test_item_name(item1, item2):
    item1.name = 'Смартфон'
    item2.name = 'Смартфон'
    assert item1.name == 'Смартфон'


def test_item1_price(item1):
    assert item1.price == 1000.0


def test_item1_quantity(item1):
    assert item1.quantity == 5


def test_item1_total_price(item1):
    assert item1.calculate_total_price() == 5000.0


def test_item1_discount(item1):
    item1.pay_rate = 0.9
    item1.apply_discount()
    assert item1.price == 900.0


def test_item1_from_csv_name():
    Item.instantiate_from_csv()
    item1 = Item.all[0]
    assert item1.name == 'Смартфон'


def test_item1(item2):
    assert item2 == "Item('Смартфон', 10000, 20)"


def test_item1_str(item2):
    assert str(item2) == 'Смартфон'
