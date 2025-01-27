#Python concession stand program

menu = {"BURGER": 5.99,
        "PIZZA": 8.99,
        "TACO": 2.99,
        "PASTA": 7.49,
        "SUSHI": 12.99,
        "SALAD": 4.99,
        "ICE CREAM": 3.49,
        "COFFEE": 2.99}

cart = []
total = 0

print("------- MENU -------")
for key, value in menu.items():
    print(f"{key:10} : ${value:.2f}")
print("--------------------")

while True:
    item = input("Select the items(Q to quit): ").upper()
    if item == "Q":
        break
    elif menu.get(item) is None:
        print("Item is not on the menu\nPlease select again:")
        continue
    elif menu.get(item) is not None:
        cart.append(item)
        print("Added")
print("------- CART -------")
print(f"{"Items":10} : Price")

for food in cart:
    total += menu.get(food)
    print(f"{food:10} : ${menu.get(food):.2f}")


print("--------------------")
print(f"{"TOTAL":>10} : ${total}")
