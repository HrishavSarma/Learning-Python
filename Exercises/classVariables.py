# Class variables -> These variables are shared among all instances of a class
#                    Instance variables are defined inside of the constructor
#                    Class variables are defined outside of the constructor
#                    data from variables are shared among all objects from the class
#                    instance variables have their own data

class Student:

    class_year = 2026 #these are class variables
    class_strength = 0

    def __init__(self, name, roll):
        self.name = name #self -> for student1 this is basically student1.name
        self.roll = roll
        Student.class_strength += 1 #for each time it constructs an object it increments

    def describe(self):
        print(f"{Student.class_year} {Student.class_strength} {self.name} {self.roll}")

student1 = Student("Paul", 23) 
student2 = Student("Bob", 24)
student3 = Student("Peter", 21)

print(student1.name) #instance variables
student2.describe()

print(f"My graduating class of {Student.class_year} has {Student.class_strength} students")