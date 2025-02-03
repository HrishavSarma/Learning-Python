# super() -> Function used in a child class to call methods from the parent class(superclass).
#            Allows us to extend the functionality of the inherited methods

class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled
    def describe(self):
        print(f"It is {self.color} and is {"filled" if self.is_filled else "not filled"}")
        
    
class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

    def describe(self): # this method will override the parent method
        print(f"It is a cirlce. The radius is {self.radius}")
        super().describe() # we can also call the methods from the parent class

class Triangle(Shape):
    def __init__(self, color, is_filled, height, width):
        super().__init__(color, is_filled)
        self.height = height
        self.width = width

    def describe(self): # this method will override the parent method
        super().describe()
        print(f"It is a triangle. The height and width is {self.height}cm and {self.width}cm")


circle = Circle(color = "Blue", is_filled = True, radius= 7)
triangle = Triangle(color = "red", is_filled = "False", height = 6, width = 5) 
# print(circle.is_filled)
# print(circle.color)
# print(f"{circle.radius}cm")
                
circle.describe()
triangle.describe()