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
