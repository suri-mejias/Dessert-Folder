from abc import ABC, abstractmethod
class Dessert(ABC):
    def __init__(self, name, quantity, price_per_unit, tax_percent=7.0):
        self.name = name
        self.quantity = quantity
        self.price_per_unit = price_per_unit
        self.tax_percent = tax_percent 

    def calculate_tax(self):
<<<<<<< HEAD
        return self.calculate_cost() * (self.tax_percent / 100)
=======
        return self.calculate_cost() * 0.07
    
    @abstractmethod
    def calculate_cost(self):
        return self.quantity * self.price_per_unit
 
>>>>>>> 8a017092600d4dc8d0b09e5133e48ef030535055

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
    

