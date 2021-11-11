"""
Name: Oliver Aschenbrenner
hangman.py
"""

import random


def word_choices(file):
    infile = open(file, "r")
    acc = []
    for line in infile:
        acc = acc + [line.strip()]
    return acc


def secret_word():
    word = random.choice(word_choices("wordfile.txt")).lower()
    return word


def guessed_word(secret, guess, blank):
    for i in range(len(secret)):
        if guess == secret[i]:
            blank[i] = guess
    return blank


def guessed(blank):
    acc = 0
    for i in blank:
        if i == "_":
            acc = acc + 1
    if acc == 0:
        return True
    return False


def tries(secret, guess):
    acc = 0
    for i in range(len(secret)):
        if secret[i] == guess:
            acc = acc + 1
    return acc


def playgame():
    secret = secret_word()
    attempts = 7
    print("You have", attempts, "attempts left.")
    blank = []
    for i in range(len(secret)):
        blank = blank + ["_"]
    print(blank)
    while not guessed(blank) and attempts != 0:
        print("You have", attempts, "attempts left.")
        guess = input("Guess a letter: ")
        update = guessed_word(secret, guess, blank)
        print(" ".join(update))
        if tries(secret, guess) == 0:
            attempts = attempts - 1
    if attempts == 0:
        print("You lost")
    else:
        print("You won!")


def main():
    #print(word_choices("wordfile.txt"))
    playgame()


main()
