# Exercise 3 -> Hypotenuse of a right triangle
import math

height = float(input("Enter the height of the right triangle: "))
base = float(input("Enter the size of the base of the right triangle: "))

hypo = math.sqrt(math.pow(height,2)+math.pow(base,2))

print(f"The hypotenuse of the triangle with height {height} cm and base {base} cm is : {round(hypo,2)} cm²")