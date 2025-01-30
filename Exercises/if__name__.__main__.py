# if __name == __main__: (this script can be imported or run standalone)
# Functions and classes in this module can be reused without the main block of code executing
# Good practice (code is modular,
#                helps in readability,
#                leaves no global variables,
#                avoid unintended execution)

#                Ex. library = import library from functionality
#                    When running library directly, display a help page

def main():
    #Main block of program
    print("main")

if __name__ == '__main__':
    main()