# Pattern ->
# 444444444
# 433333334
# 432222234
# 432111234
# 432101234
# 432111234
# 432222234
# 433333334
# 444444444

# num = int(input("Enter a number: "))
num = 4

lines = num * 2 + 1

for row in range(lines):
    if row == 0 or row == lines-1: # for 4s
        for line in range(lines-1):
            print(abs(num-row), end = "")

    if row == 1 or row == lines-2: # for 3s
        print(num,end="")
        for nums in range(lines-2):
            print(abs(num-row),end='')   

    if row == 2 or row == lines-3: # for 2s
        print(num,end="")
        print(num-1,end="")
        for nums in range(lines-4):
            print(abs(num-row),end='')
        print(num-1,end="")

    if row == 3 or row == lines-4: # for 1s
        print(num,end="")
        print(num-1,end="")
        print(num-2,end="")
        for nums in range(lines-6):
            print(abs(num-row),end='')
        print(num-2,end="")
        print(num-1,end="")

    if row == 4 or row == lines-5: # for 0s
        print(num,end="")
        print(num-1,end="")
        print(num-2,end="")
        print(num-3,end="")
        for nums in range(lines-8):
            print(abs(num-row),end='')
        print(num-3,end="")
        print(num-2,end="")
        print(num-1,end="")

    print(num,end="\n")