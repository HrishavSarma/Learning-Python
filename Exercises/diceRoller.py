# Python Dice Roller
import random

print("● ┌ ─ ┐ │ └ ┘")

dice_art = {
    1:("┌───────┐",
       "│       │",
       "│   ●   │",
       "│       │",
       "└───────┘"),
    2:("┌───────┐",
       "│ ●     │",
       "│       │",
       "│     ● │",
       "└───────┘"),
    3:("┌───────┐",
       "│ ●     │",
       "│   ●   │",
       "│     ● │",
       "└───────┘"),
    4:("┌───────┐",
       "│ ●   ● │",
       "│       │",
       "│ ●   ● │",
       "└───────┘"),
    5:("┌───────┐",
       "│ ●   ● │",
       "│   ●   │",
       "│ ●   ● │",
       "└───────┘"),
    6:("┌───────┐",
       "│ ●   ● │",
       "│ ●   ● │",
       "│ ●   ● │",
       "└───────┘")    
}

dice = []
num_of_dice = int(input("Enter the number of dice: "))
total = 0

for num in range(num_of_dice):
    dice.append(random.randint(1,6))

print(dice)

# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)

for line in range(5):
    for die in dice:
        print("|",end="")
        print(dice_art.get(die)[line], end = "")
    print("|")

for die in dice:
    total += die

print(dice)
print(total)