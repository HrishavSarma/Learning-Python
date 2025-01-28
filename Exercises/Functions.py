# Function -> A block of reusable code
#            place () after the function name to invoke it

# def happy_birthday(name, age):
#     print(f"Happy Birthday to you {name}!")
#     print(f"to you {age} old to you!")
#     print("TO YOU TO YOU!")

# happy_birthday("hrishav", 20)

# def invoice(name, amount, date):
#     print(f"Hello {name}")
#     print(f"You are due ${amount:.2f} on due : {date}")

# invoice("Hrishav", 50.12, "01/01")

#Return -> statement used to end a function
#          and send a result back to the caller

# def add(x,y):
#     z = x+y
#     return z

# print(add(1,2))

def create_name(first,last):
    first=first.capitalize()
    last=last.capitalize()
    return first + " " + last

fullname = create_name("Hrishav", "Sarma")

print(fullname)