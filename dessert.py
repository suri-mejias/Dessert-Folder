from abc import ABC, abstractmethod
<<<<<<< HEAD
=======

>>>>>>> 913efd367ed4ed04ea9190cb818c1cbb05c028a3
class Dessert(ABC):
    def __init__(self, name, quantity, price_per_unit):
        self.name = name
        self.quantity = quantity
        self.price_per_unit = price_per_unit

<<<<<<< HEAD
    def calculate_tax(self):
        return self.calculate_cost() * 0.07
    
    @abstractmethod
    def calculate_cost(self):
        return self.quantity * self.price_per_unit
 
=======
    @abstractmethod
    def calculate_cost(self):
        pass

    def calculate_tax(self):
        return self.calculate_cost() * 0.07
>>>>>>> 913efd367ed4ed04ea9190cb818c1cbb05c028a3

class Candy(Dessert):
    def __init__(self, name, quantity, price_per_unit):
        super().__init__(name, quantity, price_per_unit)

    def calculate_cost(self):
        return self.quantity * self.price_per_unit

class Cookie(Dessert):
    def __init__(self, name, quantity, price_per_unit):
        super().__init__(name, quantity, price_per_unit)

    def calculate_cost(self):
        return (self.quantity / 12) * self.price_per_unit  # Assume price per dozen

class IceCream(Dessert):
    def __init__(self, name, quantity, price_per_unit):
        super().__init__(name, quantity, price_per_unit)

    def calculate_cost(self):
        return self.quantity * self.price_per_unit

class Sundae(IceCream):
    def __init__(self, name, quantity, price_per_unit, topping_name, topping_price):
        super().__init__(name, quantity, price_per_unit)
        self.topping_name = topping_name
        self.topping_price = topping_price

    def calculate_cost(self):
<<<<<<< HEAD
        return super().calculate_cost() + self.topping_price 
    

=======
        return super().calculate_cost() + self.topping_price
>>>>>>> 913efd367ed4ed04ea9190cb818c1cbb05c028a3
