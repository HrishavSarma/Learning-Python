#Variable is a container for value(strings, integers, floats, boolean)
#           A variable behaves as if it was the value it

#Strings

first_name = "Hrishav"
food = "Marshmallows"
email = "123@fake.com"

print(first_name)
#How to use variable along with some text
#F-String-> f means format
#The variable inside the {} is known as the placeholder


print(f"Hello {first_name}")
print(f"Your favorite food is {food}")
print(f"Your email is {email}")

#Integer

age = 25
quantity = 3
num_of_students = 70

print(f"You are {age} years old")
print(f"You are buying {quantity} items")
print(f"Your class has {num_of_students} students")

#Float

price = 10.99
cgpa = 8.41
distance = 5.5

print(f"The price is ${price}")
print(f"Your CGPA in 5th sem was {cgpa}")
print(f"Your ran {distance}Kms")

#Boolean
#Binary

for_sale = False
is_online = True
if is_online:
    print(f"You are online")
else:
    print(f"You are not online")