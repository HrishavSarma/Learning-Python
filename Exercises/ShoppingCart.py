# Python Shopping cart program

foods = []
prices = []
total = 0

while True:
    food = input("Enter the food: (q to quit)")

    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of {food}: $"))
        foods.append(food.capitalize())
        prices.append(price)

print("-----YOUR CART-----")

for food in foods:
    print(f"{food}", end = " ")

print()

for price in prices:
    print(f"${price}", end = " ")

for price in prices:
    total += price

print(f"\nYOUR TOTAL: ${total}")