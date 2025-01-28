#Python Rock Paper Scissors game
import random

options = ("Rock", "Paper", "Scissors")


is_running = True

while is_running:
    player = None
    computer = random.choice(options).lower()
    player = input("Enter your input(Rock, Paper, Scissors): ").lower()
    
    print(player.capitalize())
    print(computer.capitalize())
    
    
    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissors":
        print("You Win!")
    elif player == "scissors" and computer == "paper":
        print("You Win!")
    elif player == "paper" and computer == "rock":
        print("You Win!")
    else:
        print("You Lose!")
    if input("Play again?(q to quit): ").lower() == "q":
        break

print("Thanks for playing!")