# Python temperature conversion

unit = input("Enter the unit (C or F): ")
temp = float(input("Enter the temperature: "))

if unit == "C" :
    result = (temp*9)/5 + 32
    print(f"{temp}°C Celsius is {round(result,1)}°F Fahrenheit")
elif unit == "F" :
    result = (temp*5)/9 - 32
    print(f"{temp}°F Fahrenheit is {round(result,1)}­°C Celsius")
else :
    print(f"{unit} is an invalid unit")