from dessert import Candy

def test_candy():
    candy1 = Candy("M&Ms", 1.3, 8.5)
    candy2 = Candy("Palitos", 4, 5.9)
    candy3 = Candy('Skittles', 1, 6.3)

    assert candy1.name == "M&Ms"
    assert candy1.quantity == 1.3
    assert candy1.price_per_unit == 8.5

    assert candy2.name == "Palitos"
    assert candy2.quantity == 4
    assert candy2.price_per_unit == 5.9

    assert candy3.name == "Skittles"
    assert candy3.quantity == 1
    assert candy3.price_per_unit == 6.3