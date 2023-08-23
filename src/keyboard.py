from src.item import Item


class KeyboardMixin:

    def __init__(self):
        self._language = 'EN'

    def change_lang(self):
        if self._language == 'EN':
            self._language = 'RU'
        else:
            self._language = 'EN'
        return self


class Keyboard(Item, KeyboardMixin):

    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
        self._language = 'EN'

    def __str__(self):
        return super().__str__()

    def __repr__(self, ):
        return super().__repr__()

    @property
    def language(self):
        return self._language

    @language.setter
    def language(self, value):
        if value not in ['EN', 'RU']:
            raise AttributeError("property 'language' of 'Keyboard' object has no setter")

