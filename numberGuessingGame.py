# Python Number Guessing Game
import random

low = 1
high = 100

answer = random.randint(low, high)
guesses = 0

is_running = True

while is_running:
    guess = input("Enter a number : ")

    if guess.isdigit():
        guess = int(guess)
        
        if guess > high or guess < low:
            print("Number is out of range")
            print("Please enter a valid number")
            
        elif guess < answer:
            print("Too Low!\nTry again")
            guesses += 1
        elif guess > answer:
            print("Too High!\nTry again")
            guesses += 1
        else:
            print(f"CORRECT! The answer was {answer}")
            print(f"Number of guesses: {guesses}")
            guesses += 1
    else:
        print("Invalid Input")
        print("Please enter a valid number")