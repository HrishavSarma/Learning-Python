# List Comprehension = A consise way to create lists in Python
#                      Compact and easier to read than traditional loops
#                      [expression for value in iterable if condition]

# doubles = []

# for x in range (1,11):
#     x*=2
#     doubles.append(x)
# print(doubles)

# doubles = [x * 2 for x in range(1,11)]
# triples = [y * 3 for y in range(1,11)]
# sqaures = [z * z for z in range(1,11)]
# print(sqaures)

# fruits = ["apple", "banana", "coconut"]

# # fruits_first=[fruit[0] for fruit in fruits]
# fruits_cap=[fruit.capitalize() for fruit in fruits]

# print(fruits_cap)

# numbers = [1,2,-6,-7,4,5,6,-7]

# positive_nums = [num for num in numbers if num >= 0]
# negative_nums = [num for num in numbers if num < 0]
# even_nums = [num for num in numbers if num % 2 == 0]
# odd_nums = [num for num in numbers if num % 2 == 1]

# print(numbers)
# print(positive_nums)
# print(negative_nums)
# print(even_nums)
# print(odd_nums)

grades = [21,65,98,45,67,65,87,78]

passing_grades = [grade for grade in grades if grade > 60]

print(passing_grades)