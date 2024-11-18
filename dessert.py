from abc import ABC, abstractmethod


class DessertItem(ABC):
    def __init__(self, name: str = "", tax_percent: float = 7.25,):
        self.name = name
    @abstractmethod
    def calculate_cost():
        pass
    def calculate_tax():
        return self.name * self.tax_percent


class Candy(DessertItem):
    def __init__(self, name: str = "", candy_weight: float = 0.0, price_per_pound: float = 0.0):
        self.name = name
        self.candy_weight = candy_weight
        self.price_per_pound = price_per_pound
        super().__init__(name)

def calculate_cost():
    return corerct cost of item

class Cookie(DessertItem):
    def __init__(self, name: str =  "", cookie_quantity: int = 0, price_per_dozen: float = 0.0):
        self.name = name
        self.cookie_quantity = cookie_quantity
        self.price_per_dozen = price_per_dozen
        super().__init__(name)

    def calculate_cost():
    return corerct cost of item

class IceCream(DessertItem):
    def __init__(self, name: str = "", scoop_count: int = 0, price_per_scoop:  float = 0.0):
        self.name = name
        self.scoop_count = scoop_count
        self. price_per_scoop = price_per_scoop
        super().__init__(name)

    def calculate_cost():
    return corerct cost of item

class Sundae(IceCream):
    def __init__(self, name: str = "", scoop_count: int = 0, price_per_scoop: float = 0.0, topping_name: str = "", topping_price: float = 0.0):
        self.name = name
        self.scoop_count = scoop_count
        self.price_per_scoop = price_per_scoop
        self.topping_name = topping_name
        self.topping_price = topping_price
        super().__init__(name, scoop_count, price_per_scoop)

    def calculate_cost():
    return corerct cost of item

class Order():
    def main():
        Candy("Candy Corn", 1.5, .25)
        Candy("Gummy Bears", .25, .35)
        Cookie("Chocolate Chip", 6, 3.99)
        IceCream("Pistachio", 2, .79)
        Sundae("Vanilla", 3, .69, "Hot Fudge", 1.29)
        Cookie("Oatmeal Raisin", 2, 3.45)

    def order_cost():
        return cost of all items
    
    def order_tax():
        return tax of all items in the order
        