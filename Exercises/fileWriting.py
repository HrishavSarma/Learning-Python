# Python writing files (.txt, .json, .csv)

import json
import csv

txt_data = "I like marshmallows!"
txt_append = "This was appended" # we can add \n here or there

employees = ["Eugene", "spongebob", "squidward"]
d_employees = {
    "name": "Spongebob",
    "age": 30,
    "job": "cook"
}
csv_employees =[["name", "age", "job"],
                ["Paul", 20, "manager"],
                ["Saul", 37, "lawyer"],
                ["Armin", 28, "unemployed"]]


file_path1 = "stuffs/output.txt"
file_path2 = "stuffs/output.json"
file_path3 = "stuffs/output.csv"


# #WRITE
# with open(file_path1, "w") as file: # with is a statement that wraps the code block to execute. If we open a file with statement also closes it
#     # open(file, mode )
#     # "as file" basically means file = File()
#     file.write(txt_data)
#     print(f"text file {file1_path} was created")

# # X
# try:    
#     with open(file_path1, "x") as file: # with is a statement that wraps the code block to execute. If we open a file with statement also closes it
#         # open(file, mode )
#         # "as file" basically means file = File()
#         file.write(txt_data)
#         print(f"text file {file1_path} was created")

# except FileExistsError:
#     print(f"File '{file1_path}' already exists")

# #APPEND
# with open(file_path1, "a") as file: # with is a statement that wraps the code block to execute. If we open a file with statement also closes it
#         # open(file, mode )
#         # "as file" basically means file = File()
#         file.write("\n" + txt_append)
#         print(f"text file {file1_path} was modified")

#.txt
try:
    with open(file_path1, "w") as file:
        # file.write(employees) # shows typeError
        for employee in employees:
            file.write(employee + " ")
        print(f"txt file '{file_path1}' was created")
except FileExistsError:
    print(f"'{file_path1}' already exists")

# #.json is made of key value pairs
# try:
#     with open(file_path2, "w") as file:
#         # file.write(employees) # shows typeError
#         json.dump(d_employees, file, indent= 4)
#         print(f"json file '{file_path2}' was created")
# except FileExistsError:
#     print(f"'{file_path2}' already exists")

# #csv comma seperated values
# try:
#     with open(file_path3, "w", newline="") as file:
#         # file.write(employees) # shows typeError
#         writer = csv.writer(file)
#         for row in csv_employees:
#             writer.writerow(row)
#         print(f"csv file '{file3_path}' was created")
# except FileExistsError:
#     print(f"'{file3_path}' already exists")
# except PermissionError:
#     print(f"'{file3_path}' is open. Close to continue")