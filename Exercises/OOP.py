# Object -> A "bundle" of related Attributes(variables) and methods(functions)
#          Ex. phone, book, cup
#          Attribute of a cup can be : liquid = "coffee" or temp = 93.3
#          methods are functions within an object
#          methods for a cup can be def fill_cup(): or def empty_cup():

# Class -> (blueprint) used to design the structure and layout of an object


# class Car:
#     def __init__(self, series, model, name, color, for_sale):
#         self.series = series
#         self.model = model
#         self.name = name
#         self.color = color
#         self.for_sale = for_sale
# I added this class to another file

from carForOOP import Car

car1 = Car("F80", "BMW", "M4", "blue", True) #This is an object(instance) of the class Car
car2 = Car("2024", "Toyota", "Tacoma", "grey", False)
car3 = Car("2016", "Hyundai", "Creta", "red", False)

car1.describe()
car1.drive()