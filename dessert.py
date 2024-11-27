from abc import ABC, abstractmethod

class Dessert(ABC):
    def __init__(self, name, quantity, price_per_unit, tax_percent=7.0):
        self.name = name
        self.quantity = quantity
        self.price_per_unit = price_per_unit
        self.tax_percent = tax_percent 

    @abstractmethod
    def calculate_cost(self):
        pass

    def calculate_tax(self):
        return self.calculate_cost() * (self.tax_percent / 100)

class Candy(Dessert):
    def __init__(self, name, quantity, price_per_unit, tax_percent=7.0):
        super().__init__(name, quantity, price_per_unit, tax_percent)

    def calculate_cost(self):
        return self.quantity * self.price_per_unit

class Cookie(Dessert):
    def __init__(self, name, quantity, price_per_unit, tax_percent=7.0):
        super().__init__(name, quantity, price_per_unit, tax_percent)

    def calculate_cost(self):
        return (self.quantity / 12) * self.price_per_unit

class IceCream(Dessert):
    def __init__(self, name, quantity, price_per_unit, tax_percent=7.0):
        super().__init__(name, quantity, price_per_unit, tax_percent)

    def calculate_cost(self):
        return self.quantity * self.price_per_unit

class Sundae(IceCream):
    def __init__(self, name, quantity, price_per_unit, topping_name, topping_price, tax_percent=7.0):
        super().__init__(name, quantity, price_per_unit, tax_percent)
        self.topping_name = topping_name
        self.topping_price = topping_price

    def calculate_cost(self):
        return super().calculate_cost() + self.topping_price
