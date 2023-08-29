import os
import csv


FILE_PATH = os.path.join(os.path.dirname(__file__), 'items.csv')

class InstantiateCSVError(Exception):
    """Исключение для ошибок при чтении CSV файла."""

    def __init__(self, message):
        super().__init__(message)


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.__name}"

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        raise TypeError(f'other не является классом Item')

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @property
    def name(self):
        """
        Возвращает наименование товара
        """
        return self.__name

    @name.setter
    def name(self, name_data):
        if len(name_data) > 10:
            self.__name = name_data[:10]
        else:
            self.__name = name_data

    @classmethod
    def instantiate_from_csv(cls, csv_path = FILE_PATH):
        """
        Класс-метод, инициализирующий экземпляры класса Item данными из файла src/items.csv
        :return: Список товаров
        """
        objects = []
        try:
            with open(csv_path, encoding='utf-8') as file:
                reader = csv.DictReader(file)
                if len(reader.fieldnames) == 3:
                    for row in reader:
                        name = row['name']
                        price = cls.string_to_number(row['price'])
                        quantity = int(row['quantity'])
                        objects.append(cls(name, price, quantity))
                    return objects
                else:
                    raise InstantiateCSVError('Файл items.csv поврежден.')
        except FileNotFoundError:
            raise FileNotFoundError('Отсутствует файл items.csv') from None


    @staticmethod
    def string_to_number(num):
        """
        Статический метод, возвращающий число из числа-строки
        :param num: число, представленное в типе данных str
        :return: Преобразованное число
        """
        return int(float(num))
