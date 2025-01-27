# Logical Operators

# temp =  25
# is_raining = True

# if temp > 35 or temp < 0 or is_raining:
#     print("Event Cancelled")
# else:
#     print("Good weather")

temp = 27
is_sunny= True

if temp<26 and is_sunny :
    print("Event go!")
elif temp<25 and is_sunny :
    print("HUH?")
elif temp>37 and is_sunny :
    print("WHAT?")
elif temp<26 and not is_sunny:
    print("Itss colddd")
elif 28>temp>0 and is_sunny:
    print("it is warm")
else:
    print("Event cancelled")