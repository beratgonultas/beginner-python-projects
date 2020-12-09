import random

def guess(x):
    number = random.randint(1, x)
    guess = 0
    while guess != number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < number:
            print("It was too low. Guess again: ")
        elif guess > number:
            print("It was too high. Guess again: ")
        elif guess == number:
            print("You got it! Congratulations..")
guess(10)
