class Item:
    '''
    Класс для предоставления товара в магазине
    '''
    pay_rate = 1.0
    all = []

    def __init__(self, product_name: str, price, quantity: int):
        '''
         Создание экземпляров Item
        '''
        self.product_name = product_name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def calculate_total_price(self):
        '''
        Возвращение общей стоимости
        '''
        return self.price * self.quantity

    def apply_discount(self):
        '''
        Принимает скидку
        '''
        self.price *= self.pay_rate
