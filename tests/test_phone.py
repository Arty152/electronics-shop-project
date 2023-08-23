import pytest

from src.phone import Phone


@pytest.fixture
def fixture_phone():
    return Phone("iPhone 14", 120_000, 5, 2)


def test_phone_repr_str(fixture_phone):
    assert str(fixture_phone) == 'iPhone 14'
    assert repr(fixture_phone) == "Phone('iPhone 14', 120000, 5, 2)"


def test_phone_number_of_sim(fixture_phone):
    assert fixture_phone.number_of_sim == 2

    fixture_phone.number_of_sim = 1
    assert fixture_phone.number_of_sim == 1

    with pytest.raises(ValueError):
        fixture_phone.number_of_sim = 0
        fixture_phone.number_of_sim = 4.5


def test_init_phone():
    with pytest.raises(ValueError):
        Phone("iPhone 14", 120_000, 5, 0)
