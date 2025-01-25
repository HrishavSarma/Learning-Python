# Python Weight Converter

weight = float(input("Enter the weight: "))
unit = input("Kilograms or Pounds? (K or L): ")

if unit == "K":
    result = weight * 2.205
    print(f"{weight} kg is converted to {round(result,2)} lbs")
elif unit == "L":
    result = weight / 2.205
    print(f"{weight} lbs is converted to {round(result,2)} kg")
else :
    print(f"{unit} is an invalid unit")