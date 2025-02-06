# Python file detection

import os # provides a way for python programs to interact with the operating system


#two ways to access path:
#Relative -> "folder/text.txt"
#Absolute -> "c:/user/Me/Desktop/text.txt"

#RELATIVE
file_path = "C:/Users/Troy/Desktop/test"

if os.path.exists(file_path):
    print(f"{file_path} exists")

    if os.path.isfile(file_path):
        print("It is a file")
    elif os.path.isdir(file_path):
        print("It is a directory")
else:
    print(f"{file_path} does not exist")