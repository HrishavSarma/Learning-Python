# Condition expression -> One-line shortcut for if-else statements 
#                         Ternary operator
#                         assigns or prints one of two values
#                         x if condition else y

num = 6
a = 7
b = 8
age = 25
temp = 25
user_role = "guest"

# print("Positive" if num>0 else "Negative")
# print("Even" if num%2==0 else "Odd")
# max_num = a if a>b else b
# min_num = a if a<b else b

# print(max_num)

# status = "Adult" if age>=18 else "Child"

# print(status)

# print("Hot" if temp>25 else "Cold")

print("Full Access" if user_role=="Admin" else "Limited Access")