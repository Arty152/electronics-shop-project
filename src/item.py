import os
import csv

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
        self.name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

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
    def instantiate_from_csv(cls):
        """
        Класс-метод, инициализирующий экземпляры класса Item данными из файла src/items.csv
        :return: Список товаров
        """
        objects = []
        dir = os.path.dirname(os.path.abspath(__file__))
        csv_path = os.path.join(dir, 'items.csv')
        with open(csv_path) as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row['name']
                price = cls.string_to_number(row['price'])
                quantity = int(row['quantity'])
                object = cls(name, price, quantity)
                objects.append(object)
        return objects

    @staticmethod
    def string_to_number(num):
        """
        Статический метод, возвращающий число из числа-строки
        :param num: число, представленное в типе данных str
        :return: Преобразованное число
        """
        return int(float(num))
