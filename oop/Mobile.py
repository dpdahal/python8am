class Mobile:

    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    x = 10

    def get_brand(self):
        return f"Brand Name : {self.brand}"

    def get_price(self):
        return f"Price Rs: {self.price}"

    def __private(self):
        return "Hello"

    def get_private(self):
        return self.__private()

    def _proct(self):
        return "hi"


class Mi(Mobile):
    def __init__(self, brand, price, company):
        super().__init__(brand, price)
        self.cmp = company

    def get_company(self):
        return f"Company name: {self.cmp}"

    def get_proct(self):
        return self.__private()


obj = Mi("Abc", 1000, 'test')

print(obj.get_price())
print(obj.get_brand())
print(obj.get_company())

# print(obj.__private())

print(obj.get_proct())
