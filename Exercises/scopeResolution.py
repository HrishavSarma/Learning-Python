# Variable Scope -> where variable is visible and accessible
# Scope Resolution -> (LEGB) Local -> Enclosed -> Global -> Built-in

# #local
# def func1():
#     x = 1
#     print(x)
# def func2():
#     x = 2
#     print(x)
# func1()
# func2()

# #enclosed
# def func1():
#     x = 2 #this is enclosed version of x
#     def func2():
#         # x = 1 #this x would be used as this is the local
#         print(x)
#     func2()
# func1()

# #Global

# def func1():
#     #x = 1 # This would get used as this is local version
#     print(x)
# def func2():
#     #x = 3 # This would get used as this is local version
#     print(x)
# x=2
# func1()
# func2()

# # Built-in
# from math import e
# def func1():
#     print(e)
# #e = 3 # this would get used because this is global
# func1()