# Decorator -> A function that extends the behavior of another function
#              without modifying the base function
#              we pass base function as a argument to the decorator

#               @add_sprikles
#               get_add_icecream("vanilla")

def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("I got sprinkles! 🎊")
        func(*args, **kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("I got fudge! 🍫")
        func(*args, **kwargs)
    return wrapper

@add_fudge
@add_sprinkles
def get_icecream(flavor):
    print(f"I got {flavor} ice cream! 🍨")

get_icecream("vanilla")