# Nested Loops -> A loop within a loop(outer, inner)
#                 outer loop:
#                   inner loop:

row = 7
column = 35

for i in range(row):
    print("| ",end="")
    if i == 0:
        for y in range(column):
            print("¯",end="")
    elif i == row-1:
        for y in range(column):
            print("_",end="")
    else: 
        for y in range(column):
            print("*",end="")
    print(" |")