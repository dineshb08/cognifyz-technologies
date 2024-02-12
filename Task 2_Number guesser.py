import random

randnum = random.randint(1, 500)
guessnum = None

while randnum != guessnum:
    guess = input("Guess the Number [range of the number is 1-500]: ")
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
