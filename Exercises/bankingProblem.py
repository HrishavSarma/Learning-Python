# Python Banking Problem

def show_balance(balance):
    print(f"{"********************".replace("*","-")}")
    print(f"Your balance : ${balance:.2f}")
    print(f"{"********************".replace("*","-")}")

def deposit():
    print("********************")
    amount = float(input("Enter amount to be deposited : $"))
    print("********************")
    if amount < 0:
        print(f"{"********************".replace("*","!")}")
        print(f"Amount cannot be less than zero. Please try again")
        print(f"{"********************".replace("*","!")}")
        return 0
    else:
        return amount


def withdraw(balance):
    print("********************")
    amount = float(input("Enter amount to be withdrawn: $"))
    print("********************")
    if amount > balance:
        print(f"{"********************".replace("*","!")}")
        print(f"Insufficient Balance")
        print(f"{"********************".replace("*","!")}")
        return 0
    elif amount < 0:
        print(f"{"********************".replace("*","!")}")
        print(f"Amount cannot be less than zero. Please try again")
        print(f"{"********************".replace("*","!")}")
        return 0
    else:
        return amount



def main():
    balance = 0
    is_running = True
    while is_running:
        print("********************")
        print("   TROY BANK INC.   ")
        print("********************")
        print("1. Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("********************")
        choice = input("Enter your choice : ")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else :
            print(f"{"********************".replace("*","!")}")
            print("INVALID CHOICE. PLEASE TRY AGAIN")
            print(f"{"********************".replace("*","!")}")
if __name__ == '__main__':
    main()