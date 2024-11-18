from dessert import (
    Candy,
    Cookie,
    IceCream,
    Sundae
)

class Order:
    
    def __init__(self):
        self.order = []

    def add(self, dessert_item):
        self.order.append(dessert_item)
        
    def __len__(self):
        return len(self.order)
    
    def __str__(self):
        order_string = ""
        for item in self.order:
            order_string += f"{item.name}\n"
        return order_string

    
def main():
    order = Order()
    order.add(Candy("Candy Corn", 1.5, .25))
    order.add(Candy("Gummy Bears", .25, .35))
    order.add(Cookie("Chocolate Chip", 6, 3.99))
    order.add(IceCream("Pistachio", 2, .79))
    order.add(Sundae("Vanilla", 3, .69, "Hot Fudge", 1.29))
    order.add(Cookie("Oatmeal Raisin", 2, 3.45))
    print(order)
    print("Total number of items in order: ", len(order))

if __name__ == "__main__":
    main()