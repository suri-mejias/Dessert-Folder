from dessert import IceCream

def test_icecream():
<<<<<<< HEAD
    icecream1 = IceCream("Starwberry", 2, 2.50)
    icecream2 = IceCream("Chocolate", 3, 1.75)
    icecream3 = IceCream("Vanilla", 1, 3.50)
    
    assert icecream1.name() == 2.50
    assert icecream1.quantity() == 2
    assert icecream1.price_per_unit() == "Starwberry"

    assert icecream2.name() == 1.75
    assert icecream2.quantity() == 3
    assert icecream2.price_per_unit() == "Chocolate"

    assert icecream3.name() == 3.50
    assert icecream3.quantity() == 1
    assert icecream3.price_per_unit() == "vanilla"
=======
    icecream1 = IceCream("Strawberry", 2, 2.50)
    icecream2 = IceCream("Chocolate", 3, 1.75)
    icecream3 = IceCream("Vanilla", 1, 3.50)
    
    assert icecream1.name == "Strawberry"
    assert icecream1.quantity == 2
    assert icecream1.price_per_unit == 2.50

    assert icecream2.name == "Chocolate"
    assert icecream2.quantity == 3
    assert icecream2.price_per_unit == 1.75

    assert icecream3.name == "Vanilla"
    assert icecream3.quantity == 1
    assert icecream3.price_per_unit == 3.50

if __name__ == "__main__":
    test_icecream()
>>>>>>> 913efd367ed4ed04ea9190cb818c1cbb05c028a3
