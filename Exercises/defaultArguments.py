# Default Arguments -> a default value for certain parameters
#                      default is used when that argument is omitted
#                      functions more flexible, reduces no. of arguments
#                      1. Positional 2. DEFAULT, 3.keyword, 4. arbitrary

# def net_price(amount, discount=0, tax=0.05):
#     return amount * (1 - discount) * (1 + tax)

# print(net_price(500))
# print(net_price(500, 0.05))
# print(net_price(500,0.01,0))

import time

def count(end, start=0): #default arg should follow non default arg
    for x in range(start, end+1):
        print(x)
        time.sleep(0.3)
    print("DONE!")

count(10,5)