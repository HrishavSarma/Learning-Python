# While loop -> executes code while some condition is true

#name = input("Enter your name: ")
#
# while name == "":
#     print(f"You did not enter your name")
#     name = input("Enter your name: ")

# print(f"Hello {name}")

# age = int(input("Enter your age: "))

# while age<0:
#     print("Your age can not be negative")
#     age = int(input("Enter your age: "))

# print(f"You are {age} years old")

# name = input("Enter food you like : (q to quit)")

# while not name == "q":
#     print(f"You like {name}")
#     name = input("Enter another food you like : (q to quit)")

# print("Bye")

num = int(input("Enter a number between 1 and 10"))

while num>10 or num<1:
    print(f"{num} is not a valid number")
    num = int(input("Enter a number between 1 and 10"))

print(f"Your number {num}")