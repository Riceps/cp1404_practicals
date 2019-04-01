"""A shop requires a calculator"""

number_of_items = int(input("Number of items: "))
total_price = 0

while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of Items: "))

for i in range(number_of_items):
    item_price = float(input("Price of item: "))
    while item_price < 0:
        print("Invalid price of item!")
        item_price = float(input("Price of item: "))
    total_price = total_price + item_price

if total_price > 100:
    total_price = total_price * 0.9
print("Total price: {}".format(total_price))
