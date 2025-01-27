#Python quiz Game

questions = (("What is the capital of France?"),
             ("Which planet is known as the Red Planet?"),
             ("Which is the smallest prime number?"),
             ("What is the chemical symbol for water?"),
             ("How many continents are there on Earth?"))

options = (("a. Berlin", "b. Madrid", "c. Paris", "d. Rome"),
           ("a. Jupiter", "b. Mars", "c. Venus", "d. Saturn"),
           ("a. 1", "b. 4", "c. 2", "d. 3"),
           ("a. CO₂", "b. HCl", "c. H₂O", "d. O₂"),
           ("a. 5", "b. 7", "c. 6", "d. 8"))
alpha = ("a", "b", "c", "d")
answers = ("c", "b", "c", "c", "b")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("----------------------------------------")
    print(question)
    for option in options:
        print(option)

    guess = input("Enter your guess(a,b,c,d): ").lower()
    while True:
        if guess in ("a", "b", "c", "d"):
            break
        else:
            print("Invalid input. Try Again")
            guess = input("Enter your guess(a,b,c,d): ").lower()
            
    guesses.append(guess)

    for guess in guesses[question_num]:
        if guess == answers[question_num]:
            print("CORRECT!")
            score += 1
        else:
            print(f"{guess} is wrong. {options[question_num][ord(answers[question_num])-97]} is the correct answer")
    

    question_num += 1
score = score/len(questions)*100
print("----------------------")
print("--------RESULTS-------")
print(f"Your score: {score}%")
print("----------------------")
print("----------------------")