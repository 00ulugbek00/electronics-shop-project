class Item:
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price, quantity: int) -> None:
        '''
         Создание экземпляров Item
        '''
        self.name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    @property
    def name(self) -> str:
        """
        Получает название товара
        """
        return self.__name

    @name.setter
    def name(self, value) -> None:
        """
        Устанавливает название товара.
        Если длина названия превышает 10 символов, обрезает его до первых 10 символов.
        :param value: Новое название товара.
        """
        self.__name = value if len(value) <= 10 else value[:10]

    def calculate_total_price(self) -> float:
        '''
        Возвращение общей стоимости
        '''
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    def private_name(self):
        print(self.name)

    @staticmethod
    def string_to_number(value: str) -> int:
        """
        Преобразует числовую строку в число.

        :param value: Числовая строка.
        :return: Преобразованное число.
        """
        return int(float(value))

    @classmethod
    def instantiate_from_csv(cls) -> None:
        """
        Инициализирует экземпляры класса Item данными из CSV-файла.

        Файл должен содержать строки с данными в формате: "name,price,quantity".
        :raises: FileNotFoundError, если файл items.csv не найден.
        :raises: InstantiateCSVError, если файл item.csv поврежден.
     """



