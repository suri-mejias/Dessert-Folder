from dessert import Sundae

def test_sundae():
    sundae1 = Sundae("Strawberry", 2, 2.50, "Sprinkles", 1.00)
    sundae2 = Sundae("Chocolate", 3, 1.75, "Cherries", 1.50)
    sundae3 = Sundae("Vanilla", 1, 3.50, "Whipped Cream", 0.75)
    
    assert sundae1.name() == "Strawberry"
    assert sundae1.price_per_unit() == 2.50 
    assert sundae1.topping_name() == "Sprinkles" 

    assert sundae2.name() == "Chocolate"
    assert sundae2.price_per_unit() == 1.75
    assert sundae2.topping_name() == "Cherries"

    assert sundae3.name() == "Vanilla"
    assert sundae3.price_per_unit() == 3.50
    assert sundae3.topping_name() == "Whipped Cream"