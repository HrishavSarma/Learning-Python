try:
    with open(file_path, "w") as file:
        # file.write(employees) # shows typeError
        json.dump(d_employees, file, indent= 4)
        print(f"json file '{file_path}' was created")
except FileExistsError:
    print(f"'{file_path}' already exists")