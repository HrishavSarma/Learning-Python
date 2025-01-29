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