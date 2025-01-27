# Python Calculator

operator = input("Enter an operator: (+,-,x,/): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if operator == "+" :
    result = num1 + num2
    print(f"The result is: {round(result,2)}")
elif operator == "-" :
    result = num1 - num2
    print(f"The result is: {round(result,2)}")
elif operator == "x" :
    result = num1 * num2
    print(f"The result is: {round(result,2)}")
elif operator == "/" :
    result = num1 / num2
    print(f"The result is: {round(result,2)}")
else: 
    print(f"The {operator} is an invalid operator")
