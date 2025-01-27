# Dictionary = a collection of {key:value} pairs
#              ordered and changeable. No duplicates

capitals = {"France": "Paris",
            "Japan" : "Tokyo",
            "India" : "New Delhi",
            "Australia" : "Canberra",
            "Canada" : "Ottawa"}

#print(capitals.get("India"))
#print(capitals.get("America"))
# if capitals.get("India"):
#     print("Capital exist")
# else:
#     print("Nope")

# capitals.update({"France" : "Europe"})
# capitals.update({"Russia" : "Ukraine"})
# capitals.pop("Japan")
# capitals.popitem()
# capitals.clear()

# keys = capitals.keys()
# print(keys)
# for key in keys:
#     print(key)

# values = capitals.values()
# print(values)
# for value in values:
#     print(value)

items = capitals.items() # Returns 2D lists of tuples
print(items)
for key, value in items:
    print(f"{key} : {value}")
    