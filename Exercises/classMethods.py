# Class methods -> allows operations related to the class itself
#                    takes (cls) as the first parameter, which represents the class itself.
#                  Best for class-level data or require access to the class itself

class Student:
    
    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa
    
    def get_info(self):
        return f"{self.name} -> {self.gpa}"
    
    @classmethod
    def get_count(cls):
        return f"Number of students: {cls.count}"
    
    @classmethod
    def average_gpa(cls):
        if cls.count == 0:
            return 0
        else: 
            return f"Average gpa = {cls.total_gpa / cls.count:.2f}"
    
student1 = Student("Patrick", 2.0)
student2 = Student("Spongebob", 3.2)
student3 = Student("Cindy", 4.0)

print(Student.get_count())
print(student1.get_info())
print(student2.get_info())
print(student3.get_info())
print(Student.average_gpa())