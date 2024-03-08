class Product:
    def __init__(self, name, price, amount):
        self.__name = name
        self.__price = price
        self.__amount = amount

    def sale(self):
        if self.__amount == 0:
            print('Нет в наличии')
        else:
            self.__amount -= 1

    def refund(self):
        self.__amount += 1

    def get_info(self):
        return f'Товар: {self.__name}, цена: {self.__price}, количество: {self.__amount}'


name = input()
pr = int(input())
am = int(input())
method = input()
x1 = Product(name, pr, am)
if method == 'sale':
    x1.sale()
else:
    x1.refund()
print(x1.get_info())