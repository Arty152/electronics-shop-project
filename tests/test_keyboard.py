import pytest
from src.keyboard import Keyboard, KeyboardMixin



@pytest.fixture
def fixture_keyboard():
    return Keyboard('Dark Project KD87A', 9600, 5)


def test_keyboard_repr_str(fixture_keyboard):
    assert str(fixture_keyboard) == 'Dark Project KD87A'
    assert repr(fixture_keyboard) == "Keyboard('Dark Project KD87A', 9600, 5)"


def test_change_lang(fixture_keyboard):
    with pytest.raises(AttributeError):
        fixture_keyboard.language = 'CH'
    fixture_keyboard.language = 'RU'
    assert fixture_keyboard.language == 'RU'


def test_mixin():
    kb = KeyboardMixin()
    kb.change_lang()
    assert kb._language == 'RU'
    kb.change_lang()
    assert kb._language == 'EN'
    assert kb._language == 'EN'


if __name__ == '__main__':
    pytest.main([__file__])
