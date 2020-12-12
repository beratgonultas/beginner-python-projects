import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = len(word)


    while len(word_letters) > 0 and lives > 0:
        print(f"You have {lives} lives.")
        lives -= 1
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("Current word is: ", " ".join(word_list))

        user_letter = input("Guess a letter: ").upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                lives += 1
        elif user_letter in used_letters:
            print("You've already used this letter.")
        else:
            print("You typed a wrong character. Try again.")
        print("You have used letters", " ".join(used_letters))

    if lives > 0:
        print(f"You won. The word is {word}")
    else:
        print(f"The man is dead. The word was {word}")

hangman()
