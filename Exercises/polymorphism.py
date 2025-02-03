# Polymorphism -> Greek word that means to "have many faces or forms"
#                 Poly -> many
#                 morph -> form

#                 Two ways to polymorphism
#                 1 Inheritance -> An object could be treated of the same type as a parent class
#                 2 "Duck Typing" -> Object must have necessary attributes/methods

#                 1 Inheritance: 

from abc import ABC, abstractclassmethod

class Shape(ABC):

    @abstractclassmethod
    def area(self):
        pass

class Circle(Shape): # a Circle is a circle and also a shape but not a square or triangle
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Triangle(Shape):
    def __init__(self, height, base):
        super().__init__()
        self.height = height
        self.base = base
    def area(self):
        return self.base * self.height * 0.5
    
class Sqaure(Shape):
    def __init__(self, side):
        super().__init__()
        self.side = side
    
    def area(self):
        return self.side ** 2

class Pizza(Circle): # a pizza is a pizza and it is also a circle and it is also a shape but not a triangle or a square
    def __init__(self, topping, radius):
        self.topping = topping
        super().__init__(radius)



shapes = [Circle(5), Triangle(6,7), Sqaure(6), Pizza("Pepperoni", 15)]

for shape in shapes:
    print(f"{shape.area()}cm²")