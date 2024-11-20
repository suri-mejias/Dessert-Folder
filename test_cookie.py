from dessert import Cookie


def test_cookie():
    cookie1 = Cookie("Chocolate Chip", 12, 5.6)
    cookie2 = Cookie("Sugar Cookie", 6, 5.9)
    cookie3 = Cookie('Snickerdoodle', 3, 6.3)

    assert cookie1.name == "Chocolate Chip"
    assert cookie1.quantity == 12
    assert cookie1.price_per_unit == 5.6

    assert cookie2.name == "Sugar Cookie"
    assert cookie2.quantity == 6
    assert cookie2.price_per_unit == 5.9

    assert cookie3.name == "Snickerdoodle"
    assert cookie3.quantity == 3
    assert cookie3.price_per_unit == 6.3