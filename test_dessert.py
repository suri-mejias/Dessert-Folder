from dessert import (
    DessertItem,
    Candy,
    Cookie,
    IceCream,
    Sundae
)

def test_dessert_item():
    dessert = DessertItem(" Brownie ")
    assert isinstance(dessert, DessertItem)
    assert dessert.name == "Brownie"
    assert hasattr(dessert, "Brownie")
def test_candy():
    testcandy = Candy("Skittles", 2.8, 1.2)
    assert testcandy.name == "Skittles"
    assert testcandy.candy_weight == 2.8
    assert testcandy.price_per_pound == 1.2

def test_cookie():
    testcookie = Cookie("Chocolate Chip", 3, 8)
    assert testcookie.name == "Chocolate Chip"
    assert testcookie.cookie_quantity == 3
    assert testcookie.price_per_dozen == 8

def test_ice_cream():
    testicecream = IceCream("Cookies and cream", 4, 1.3)
    assert testicecream.name == "Cookies and Cream"
    assert testicecream.scoop_count == 4
    assert testicecream.price_per_scoop == 1.3

def test_sundae():
    testsundae = Sundae("Vanilla Sundae", 3, 1.5, "Chocolate Chips", 0.5)
    assert testsundae.name == "Vanilla Sundae"
    assert testsundae.price_per_scoop == 1.5
    assert testsundae.topping_price == 1.5
    assert testsundae.topping_name == "Chocolate Chips"
    assert testsundae.topping_price == 0.5


def test_candy_calculate_cost():
    candy = Candy("Candy Corn", 0.5, 0.76)
    assert candy.calculate_cost() == 0.38

def test_candy_calculate_tax():
    candy = Candy("Candy Corn", 0.5, 0.76)
    assert round(candy.calculate_tax(), 2) == 0.03
