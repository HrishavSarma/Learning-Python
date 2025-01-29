# Membership Operators -> used to test whether a variable or value is in a sequence
#                         (string,list,tuple,set or dictionary)
#                         1. in
#                         2. not in

# word = "Banana"

# letter = input("Guess a letter in secret word: ").capitalize()

# if letter in word.upper():
#     print(f"{letter} is there")
# else:
#     print(f"{letter} is not there")

# students = {"spongebob", "patrick", "sandy"}

# student = input("Enter the name of a student: ").lower()

# if student in students:
#     print(f"{student.capitalize()} is a student")
# else:
#     print(f"{student.capitalize()} was not found")

# grades = {"bob": "A",
#           "mark": "B",
#           "paul": "C",
#           "larry": "D"}

# student = input("Enter the name of a student: ").lower()

# if student in grades:
#     print(f"{student.capitalize()}'s grade is {grades[student]}")
# else:
#     print(f"{student.capitalize()} not found")

email = "fake@gmail.com"

if "@" in email and "." in email:
    print(f"{email}: valid email")
else:
    print(f"{email} is invalid")