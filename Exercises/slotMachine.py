# Python Slot machine
import random
def spin_row():
    symbols = ["🍏", "🔔", "🍉", "🍾", "⭐"]
    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print(" | ".join(row))

def show_payout(row , betted):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍏":
            return betted * 2
        elif row[0] == "🔔":
            return betted * 3
        elif row[0] == "🍉":
            return betted * 4
        elif row[0] == "🍾":
            return betted * 10
        elif row[0] == "⭐":
            return betted * 20
    return 0
def main():
    balance = 100
    betted = 0
    print("Welcome to Python Gamble")

    while balance >0:
        print(f"Your available balance : ${balance}")
        betted = input("Place your bets \n$")
        
        if not betted.isdigit():
            print("INVALID INPUT. PLEASE TRY AGAIN")
            continue

        betted = int(betted)

        if betted > balance:
            print(f"Insufficient Balance")
            continue
        if betted < 0:
            print("INVALID INPUT. PLEASE TRY AGAIN")
            continue

        balance -= betted
        row = spin_row()
        print("Spinning...\n")
        print_row(row)

        payout = show_payout(row,betted)

        if payout > 0:
            print(f"YOU WON! ${payout}")

        else:
            print(f"Lmao you lost your ${betted}")
        
        balance += payout

        play_again = input("Do you want to play again? (Enter: yes/N: no): ").upper()
        if play_again == "N":
            break

    print(f"GAME OVER! Final balance ${balance}")

if __name__=='__main__':
    main()