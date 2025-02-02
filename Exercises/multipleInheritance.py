# Multiple Inheritance -> Inherit from more than one parent class
#                         C(A, B)
#
#

class Animal:
    def __init__(self, name):
        self.name = name
    def eat(self):
        print(f"The {self.name} is eating")

    def sleep(self):
        print(f"The {self.name} is sleeping")

class Prey(Animal):
        
    def flee(self):
        print(f"The {self.name} is fleeing")

class Predator(Animal):

    def hunt(self):
        print(f"The {self.name} is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit('rabbit')
hawk = Hawk('hawk')
fish = Fish('fish')

fish.hunt()
fish.flee()
rabbit.flee()
hawk.hunt()
hawk.eat()
