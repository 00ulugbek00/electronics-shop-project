from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        """
         Создает экземпляр класса Phone.
        """
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __repr__(self):
        return f"Phone{self.name, self.price, self.quantity, self.number_of_sim}"

    @property
    def number_of_sim(self) -> int:
        """
         Возвращает количество поддерживаемых сим-карт.
        """
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value) -> None:
        """
                Устанавливает количество физических SIM-карт, поддерживаемых телефоном.
                :raises: ValueError, если значение меньше или равно нулю.
        """
        if value <= 0:
            raise ValueError('ValueError: Количество физических SIM-карт должно быть целым числом больше нуля')
        self.__number_of_sim = value

    def __add__(self, other) -> int:
        """
        Переопределение оператора сложения (+) для Phone и Item.
        :TypeError: Не допустимое значение
        """
        if isinstance(other, (Item, Phone)):
            return self.quantity + other.quantity

        raise TypeError('TypeError: Не допустимое значение ')

    def __radd__(self, other):
        """
        Переопределение оператора обратного сложения (+) для Phone и Item
        """
        return self.__add__(other)
