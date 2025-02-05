# @property -> Decorator used to define a method as a property (it can be accessed like an attribute)
#              Benefits: Adds additional logic when read, write, or delete attributes
#              Gives you getter, setter and deleter method

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height 
        # _ means protected

    @property
    def width(self):
        return f"{self._width:.1f}cm"
    
    @property
    def height(self):
        return f"{self._height:.1f}cm"
    
    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be greater than zero")
    
    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("heigth must be greater than zero")

    @width.deleter
    def width(self):
        del self._width
        print("Width was deleted")
    
    @height.deleter
    def height(self):
        del self._height
        print("Height was deleted")
    
rectangle = Rectangle(3,4)

rectangle.height = 6
rectangle.width = 4

del rectangle.height
del rectangle.width

# print(rectangle.height)
# print(rectangle.width)