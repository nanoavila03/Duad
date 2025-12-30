#Dada una lista de productos vendidos, donde cada uno tiene categoría y precio, cree un diccionario que acumule el total por categoría.

products = [
    {"name": "Gaming Monitor", "category": "Electronics", "price": 350},
    {"name": "Mechanical Keyboard", "category": "Electronics", "price": 120},
    {"name": "Office Chair", "category": "Furniture", "price": 280},
    {"name": "Standing Desk", "category": "Furniture", "price": 450},
    {"name": "Wireless Mouse", "category": "Electronics", "price": 45},
    {"name": "Bookshelf", "category": "Furniture", "price": 150},
    {"name": "Laptop Stand", "category": "Electronics", "price": 35},
    {"name": "Desk Lamp", "category": "Lighting", "price": 60},
    {"name": "Filing Cabinet", "category": "Furniture", "price": 200},
    {"name": "Webcam", "category": "Electronics", "price": 85},
]

category_totals = {}

for product in products:
    category = product["category"]
    price = product["price"]
    
    if category not in category_totals:
        category_totals[category] = 0
    category_totals[category] += price
print(category_totals)
