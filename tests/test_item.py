import pytest
from src.item import Item
from src.phone import Phone


@pytest.fixture
def fixture_item():
    return Item("Тестовый товар", 10.0, 5)


@pytest.fixture
def fixture_phone():
    return Phone("iPhone 14", 120_000, 5, 2)


def test_calculate_total_price(fixture_item):
    assert fixture_item.calculate_total_price() == 50.0


def test_apply_discount(fixture_item):
    fixture_item.pay_rate = 0.8
    fixture_item.apply_discount()
    assert fixture_item.price == 8.0


def test_instantiate_from_csv():
    items = Item.instantiate_from_csv()
    assert len(items) == 5


def test_string_to_number(fixture_item):
    assert fixture_item.string_to_number('10') == 10
    assert fixture_item.string_to_number('5.5') == 5


def test_name_setter(fixture_item):
    fixture_item.name = "Супермегасмартфон"
    assert fixture_item.name == "Супермегас"
    fixture_item.name = "Фен"
    assert fixture_item.name == "Фен"


def test_repr(fixture_item):
    assert repr(fixture_item) == "Item('Тестовый товар', 10.0, 5)"


def test_str(fixture_item):
    assert str(fixture_item) == "Тестовый товар"


def test_add(fixture_phone, fixture_item):
    assert fixture_phone + fixture_item == 10
    other = "Object of another class"
    with pytest.raises(TypeError):
        fixture_phone + other
