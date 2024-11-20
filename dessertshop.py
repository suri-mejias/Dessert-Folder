from dessert import Candy, Cookie, IceCream, Sundae
import receipt

class Order:
    def __init__(self):
        self.items = []

    def add(self, dessert_item):
        self.items.append(dessert_item)

    def get_data(self):
        data = []
        for item in self.items:
            cost = item.calculate_cost()
            tax = item.calculate_tax()
            data.append([item.name, f"${cost:.2f}", f"${tax:.2f}"])

        order_cost = self.order_cost()
        order_tax = self.order_tax()
        data.append(["Order Subtotals", f"${order_cost:.2f}", f"${order_tax:.2f}"])
        data.append(["Order Total", f"${order_cost + order_tax:.2f}", ""])
        data.append([f"Total items in the order", len(self.items), ""])

        return data

    def order_cost(self):
        return sum(item.calculate_cost() for item in self.items)

    def order_tax(self):
        return sum(item.calculate_tax() for item in self.items)

def main():
    order = Order()
    order.add(Candy("Candy Corn", 1.5, 0.25))
    order.add(Candy("Gummy Bears", 0.25, 0.35))
    order.add(Cookie("Chocolate Chip", 6, 3.99))
    order.add(IceCream("Pistachio", 2, 0.79))
    order.add(Sundae("Vanilla", 3, 0.69, "Hot Fudge", 1.29))
    order.add(Cookie("Oatmeal Raisin", 2, 3.45))

    data = order.get_data()

    pdf_path = "receipt.pdf"

    receipt.make_receipt(data, pdf_path)
    print(f"Receipt PDF has been saved to: {pdf_path}")

if __name__ == "__main__":
    main()