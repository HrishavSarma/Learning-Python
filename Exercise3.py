#Exercise 3 -> Calc Circumference & area of circle
import math

radius = float(input("Enter the radius of the cirlce: "))
circum = 2*math.pi*radius
area = math.pi*math.pow(radius,2)

print(f"The circumference of the circle is {round(circum,2)} cm")
print(f"The area of the circle is {round(area,2)} cm²")