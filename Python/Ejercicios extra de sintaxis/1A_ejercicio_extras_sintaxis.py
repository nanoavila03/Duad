#Cree un pseudocódigo que le pida un precio de producto al usuario, calcule su descuento y muestre el precio final tomando en cuenta que:


product_price = 0
discount = 0
final_price = 0

product_price = float(input("Enter the product price: "))

if (product_price > 100):
    discount = product_price * 0.02
else:
    discount = product_price * 0.10

final_price = product_price - discount

print("The final price of the product is:", final_price)