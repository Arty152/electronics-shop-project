import pytest
from src.keyboard import Keyboard, KeyboardMixin


@pytest.fixture
def fixture_phone():
    return Keyboard('Dark Project KD87A', 9600, 5)


def test_keyboard_repr_str(fixture_phone):
    assert str(fixture_phone) == 'Dark Project KD87A'
    assert repr(fixture_phone) == "Keyboard('Dark Project KD87A', 9600, 5)"


def test_change_lang(fixture_phone):
    fixture_phone.change_lang()
    assert fixture_phone.language == 'RU'
    fixture_phone.change_lang()
    assert fixture_phone.language == 'EN'
    with pytest.raises(AttributeError):
        fixture_phone.language = 'CH'


def test_mixin():
    test_kb = KeyboardMixin()
    assert test_kb._language == 'EN'
