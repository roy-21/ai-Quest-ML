'''
Nested Dictionary Sorting:
Given a nested dictionary containing product details (product name, price, and quantity),
write a Python program to sort the products based on their prices in ascending order.
'''

#Sample nested dictionary
products = {
    "P101": {"name": "Laptop", "price": 75000, "quantity": 10},
    "P102": {"name": "Mobile", "price": 25000, "quantity": 50},
    "P103": {"name": "Tablet", "price": 18000, "quantity": 30},
    "P104": {"name": "Headphones", "price": 3000, "quantity": 100}
}

#Sort products by price
sorted_products = dict(sorted(products.items(), key=lambda item: item[1]["price"]))

#Print sorted products
print("Products sorted by price (ascending):")
for pid, details in sorted_products.items():
    print(f"ID: {pid}, Name: {details['name']}, Price: {details['price']}, Quantity: {details['quantity']}")