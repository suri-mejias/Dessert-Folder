class Dessert:
    def __init__(self, name, quantity, price_per_unit):
        self.name = name
        self.quantity = quantity
        self.price_per_unit = price_per_unit

    def calculate_cost(self):
        return self.quantity * self.price_per_unit

    def calculate_tax(self):
        return self.calculate_cost() * 0.07  

class Candy(Dessert):
    def __init__(self, name, quantity, price_per_unit):
        super().__init__(name, quantity, price_per_unit)

class Cookie(Dessert):
    def __init__(self, name, quantity, price_per_unit):
        super().__init__(name, quantity, price_per_unit)

class IceCream(Dessert):
    def __init__(self, name, quantity, price_per_unit):
        super().__init__(name, quantity, price_per_unit)

class Sundae(IceCream):
    def __init__(self, name, quantity, price_per_unit, topping_name, topping_price):
        super().__init__(name, quantity, price_per_unit)
        self.topping_name = topping_name
        self.topping_price = topping_price

    def calculate_cost(self):
        return super().calculate_cost() + self.topping_price 

    def calculate_tax(self):
        return self.calculate_cost() * 0.07