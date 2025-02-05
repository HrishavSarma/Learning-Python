# Exception -> An event that interrupts the flow of a program
#              (ZeroDivisionError, TypeError, ValueError)
#              1. try, 2. except, 3. finally

# 1/0 # zerodivisionerror
# 1 + "1" # typeerror
# int("pizza") # ValueError

try:
    number = int(input("Enter a number: "))
    print(1/number)
    # print(1+number)
except ZeroDivisionError:
    print("You cant divide by zero")
except ValueError:
    print("Enter numbers")
except TypeError:
    print("number cannot be modified with a text")
except Exception:
    print("Something went wrong!")
finally:
    print("Cleaning")