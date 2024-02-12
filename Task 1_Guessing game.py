import random

randnum = random.randint(1, 100)
guessnum = None

while randnum != guessnum:
    guess = input("Guess the Number: ")
    try:
        guessnum = int(guess)
    except ValueError:
        print("Enter only integer values")
        continue

    if guessnum > randnum:
        print("Your guess is high")
    elif guessnum < randnum:
        print("Your guess is low")
    else:
        print("Your Guess is Correct!")
        break
