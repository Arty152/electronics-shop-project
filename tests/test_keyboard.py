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
        setattr(fixture_keyboard, 'language', 'CH')
    assert fixture_keyboard.language == 'EN'


def test_mixin():
    kb = KeyboardMixin()
    kb.change_lang()
    assert kb.language == 'RU'
    kb.change_lang()
    assert kb.language == 'EN'
    assert kb.language == 'EN'


if __name__ == '__main__':
    pytest.main([__file__])
