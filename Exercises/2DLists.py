# 2D Lists -> These are lists of lists
#             2dlists = [list1, list2, list3]

fruits = ["apple", "banana", "coconut"]
vegetables = ["cabage", "spinach", "broccoli"]
meat = ["chicken", "fish", "goat"]

#can be also
# groceries = [["apple", "banana", "coconut"], 
#              ["cabage", "spinach", "broccoli"], 
#              ["chicken", "fish", "goat"]]

groceries = [fruits, vegetables, meat]

#print(groceries[0])
for collection in groceries:
    if collection == ["apple", "banana", "coconut"]:
        print("Fruits:")
    elif collection == ["cabage", "spinach", "broccoli"]:
        print("Vegetables:")
    else:
        print("Meat:")
    for food in collection:
        print(food,end = " ")
    print()
