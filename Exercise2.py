#Exercise 2 : Shopping Cart Problem

item = input("What item would you like to buy?: ")
price = float(input("What is the price of the item?: "))
quantity = int(input("How much would you like to buy?: "))

total = price * quantity
print(f"Your Shopping Cart has: {quantity} {item} ${price}")
print(f"Your total is ${total}")