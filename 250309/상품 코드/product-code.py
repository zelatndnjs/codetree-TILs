class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

a,b = input().split()
b = int(b)
product1 = Product("codetree",50)
product2 = Product(a,b)
print(f"product {product1.price} is {product1.name}")
print(f"product {product2.price} is {product2.name}")
