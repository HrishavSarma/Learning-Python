# Static methods -> A method that belongs to a class rather than any object from that class (instance)
#                   Usually used for general utility functions

# Instance methods -> Best for operations on instances of the class (objects)
# Static methods -> Best for utility functions that do not need access to class data

class Employee:
    
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} = {self.position}"
    
    @staticmethod
    def is_valid_position(position):
        valid_positions = ["manager", "cook", "cashier", "janitor"]
        return position in valid_positions
    
employee1= Employee("Eugene", "janitor")
employee2= Employee("Patrick", "cashier")
employee3= Employee("Spongebob", "cook")

print(Employee.is_valid_position("rocket science")) #no object/instance needed to call the method

print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())