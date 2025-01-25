# Exercise 5 -> User input validation
# 1. characters <= 12
# 2. no " "
# 3. no digits

name = input("Enter your first name: ")
print("Invalid input. Must not have more than 12 characters or contain any spaces or number" if len(name.replace(" ", ""))>12 or name.find(" ")>0 or not name.isalpha() else f"{name.capitalize()}")