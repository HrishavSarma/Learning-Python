import random

low = 1
high = 100
options = ("Rock", "Paper", "Scissors")
choices = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
# number = random.randint(1,6)
# number = random.randint(low, high)
# option = random.choice(options)
random.shuffle(choices)

print(choices)