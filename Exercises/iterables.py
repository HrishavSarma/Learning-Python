# Iterables -> an object/collection that can return its element one at a time,
#              allowing it to be iterated in a loop

# numbers = [1,2,3,4,5]
# for num in numbers:
#     print(num)

# numbers = (1,2,3,4,5)
# for num in numbers:
#     print(num)

# fruits = {"apple", "orange", "Banana"} # sets not reversible
# for fruit in fruits:
#     print(fruit.capitalize())

# name = "Hrishav Sarma"
# for character in name:
#     print(character, end = " ")

my_dict = {'a':"Apple",'b':"Ball",'c':"Coconut",'d':"donkey"}

for key,value in my_dict.items():
    print(f"{key.capitalize()} = {value.capitalize()}")