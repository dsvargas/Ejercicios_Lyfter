class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}: ${self.price:.2f} (Quantity: {self.quantity})"
    
class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def show_inventory(self):
        if not self.products:
            return "Inventory is empty."
        return "\n".join(str(product) for product in self.products)
    
    def calculate_total_value_of_inventory(self):
        return sum(product.price * product.quantity for product in self.products)
    
product1 = Product("Mouse", 5000, 3)
product2 = Product("Teclado", 8000, 2)
inventory = Inventory()
inventory.add_product(product1)
inventory.add_product(product2)
print(inventory.show_inventory())
print(f"Total inventory value: ${inventory.calculate_total_value_of_inventory():.2f}")