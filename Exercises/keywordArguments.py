# Default Arguments -> arguments preceeded by an identifier
#                      helps with readability
#                      order of arguments doesn't matter
#                      1. Positional 2. default, 3.KEYWORD, 4. arbitrary

# def hello(greet,title,name,last):
#     print(f"{greet.capitalize()} {title.capitalize()}. {name.capitalize()} {last.capitalize()} ")

# hello("hello", title="Mrs", last="john", name="james") #keyword arguments should follow positional arguments

# for x in range(1,11):
#     print(x, end = " ") #here end is a keyword argument for the print function

# print("1","2","3","4","5",sep = "-")

def get_phone(country, area, zip, personal):
    return f"{country}-{area}-{zip}-{personal}"

phone_no=get_phone(country="+91",area=12,zip=3456,personal=7890)
print(phone_no)