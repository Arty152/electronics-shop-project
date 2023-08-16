"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def fixture():
    return Item("Тестовый товар", 10.0, 5)


def test_calculate_total_price(fixture):
    assert fixture.calculate_total_price() == 50.0


def test_apply_discount(fixture):
    fixture.pay_rate = 0.8
    fixture.apply_discount()
    assert fixture.price == 8.0


def test_instantiate_from_csv():
    items = Item.instantiate_from_csv()
    assert len(items) == 5


def test_string_to_number(fixture):
    assert fixture.string_to_number('10') == 10
    assert fixture.string_to_number('5.5') == 5


def test_name_setter(fixture):
    fixture.name = "Супермегасмартфон"
    assert fixture.name == "Супермегас"
    fixture.name = "Фен"
    assert fixture.name == "Фен"


def test_repr(fixture):
    expected = "Item('Тестовый товар', 10.0, 5)"
    assert repr(fixture) == expected


def test_str(fixture):
    expected = "Тестовый товар"
    assert str(fixture) == expected
