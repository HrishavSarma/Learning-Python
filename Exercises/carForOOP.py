#class file for OOP

class Car:
    def __init__(self, series, model, name, color, for_sale): #This is a constructor, works similarly to a function 
        self.series = series #these are instance variables
        self.model = model
        self.name = name
        self.color = color
        self.for_sale = for_sale
    def drive(self):
        print(f"You drive a {self.series} {self.color} {self.model} {self.name}")
    
    def stop(self):
        print("You stop the car")

    def describe(self):
        print(f"{self.color} {self.series} {self.model} {self.name}")