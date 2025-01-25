#Typecasting -> The process of coverting a variable from one data type to another
#               str(), int(), float(), bool()

name = "Hrishav Sarma"
age = 25
cgpa = 8.41
is_student = True

#we can get the datatype of a variable or a value
#we use the type function

print(f"Type of age now: {type(age)}")

#typecasting

name = bool(name)

print(name)