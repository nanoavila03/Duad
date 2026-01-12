# Cree una clase Product con:
# Nombre, precio y cantidad
# Cree una clase Inventory que:
# Guarde productos en una lista
# Tenga métodos para:
# Agregar un producto
# Mostrar todos los productos
# Calcular el valor total del inventario

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
class Inventory:
    def __init__(self):
        self.products = []
    
    def add_product(self, product):
        self.products.append(product)
    
    def show_products(self):
        for product in self.products:
            print(f'Product: {product.name}, Price: {product.price}, Quantity: {product.quantity}')
    
    def total_value(self):
        return sum(product.price * product.quantity for product in self.products)

inventory = Inventory()
inventory.add_product(Product("Macbook Pro", 1600, 5))
inventory.add_product(Product("Macbook Air", 1100, 3))
inventory.add_product(Product("Macbook", 900, 2))
inventory.show_products()
print(f"Total value: {inventory.total_value()}")
