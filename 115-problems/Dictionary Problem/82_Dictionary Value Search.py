'''
Dictionary Value Search: Given a dictionary of items and their prices, 
write a Python program to search for an item based on its price and print the item’s name.
'''

#Sample dictionary input
n = int(input("Enter number of items: "))
items_dict = {}

for _ in range(n):
    item = input("Enter item name: ")
    price = float(input("Enter item price: "))
    items_dict[item] = price

#Price to search
target_price = float(input("Enter the price to search for: "))

#Search for items with the given price
found = False
for item, price in items_dict.items():
    if price == target_price:
        print(f"Item with price {target_price} is: {item}")
        found = True

if not found:
    print(f"No item found with price {target_price}")