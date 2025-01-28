# *args     -> allows you to pass multiple non-key arguments. turns the list of arguments into a tuple
# *kwargs   -> allows you to pass multiple keyword arguments. turns the list of arguments into dictionary
#            * is the unpacking operator
#                      1. Positional 2. default, 3.keyword, 4. ARBITRARY

# def add(*nums):
#     print(type(nums))

# add()

# def add(*nums):
#     total = 0
#     for num in nums:
#         total += num
#     return total

# print(add(1,2,3,4,5))

# def display_name(*names):
#     for name in names:
#         print(name, end = "")

# display_name("Dr. ","Spongebob ", "Herold ", "Squarepants ","III")

# def display_address(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# display_address(street="1234 fake st.",
#                 apt = "100",
#                 city="Guwahati",
#                 state="Assam",
#                 zip="123456")

def shipping_address(*args, **kwargs):
    for arg in args:
        print(arg, end = " ")
    print()
    if 'apt' in kwargs:
        print(kwargs.get('street'),kwargs.get('apt'))
    elif 'pobox' in kwargs:
        print(kwargs.get('street'),kwargs.get('pobox'))
    else:
        print(kwargs.get('street'))
    
    print(kwargs.get('city'), kwargs.get('state'), kwargs.get('zip'))

shipping_address("Mr.", "Hrishav", "Sarma", 
                 street="123 fake st.",
                 pobox = "no. 1001",
                 city="Guwahati",
                 state="Assam",
                 zip="123456")