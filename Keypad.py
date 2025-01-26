#Python Keypad with 2D lists

row1 = ["1", "2", "3"]
row2 = ["4", "5", "6"]
row3 = ["7","8", "9"]
row4 = ["*", "0", "#"]

keypad =[row1, row2, row3, row4]

# for row in keypad:
#     for key in row:
#         print(key, end = " ")
#     print()

for row in keypad:
    

    for i in range(3):
            print(" ", end = "")
            print("___", end = "")
    print()

    for key in row:
        print("|",end = " ")
        print(key,end = " ")
    print("|", end = "")

    print()
    for i in range(3): 
        print(" ", end = "")
        print("¯¯¯", end = "")
    print()
