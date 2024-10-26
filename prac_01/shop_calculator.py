"""
CP1404/CP5632 - Practical - Florian N Eisen
Program for small scale retail totalling prices of goods
"""

number_items = int(input("Enter the number of items: "))
total_price = 0

for number_items in range(0, number_items, 1):
    price_item = float(input("Enter the price: $"))
    total_price = total_price + price_item
print(f"The total price is ${total_price:.2f}")
