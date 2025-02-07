# Python reading files(.txt, .json, .csv)

import json
import csv

txt_file_path = "stuffs/output.txt"
json_file_path = "stuffs/output.json"
csv_file_path = "stuffs/output.csv"

# # .txt
# try:
#         with open(txt_file_path, "r") as file:
#             content = file.read()
#             print(content)
# except FileNotFoundError:
#         print(f"'{file_path}' was not found")

# except PermissionError:
#        print("No permission to read file")

# # .json
# try:
#         with open(json_file_path, "r") as file:
#             content = json.load(file)
#             print(content["name"])
# except FileNotFoundError:
#         print(f"'{json_file_path}' was not found")

# except PermissionError:
#        print("No permission to read file")

# .csv
try:
        with open(csv_file_path, "r") as file:
            content = csv.reader(file)
            for line in content:
                print(line)
except FileNotFoundError:
        print(f"'{csv_file_path}' was not found")

except PermissionError:
       print("No permission to read file")