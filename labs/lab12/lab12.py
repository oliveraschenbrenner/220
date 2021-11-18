"""
Name: Oliver Aschenbrenner
lab12.py
"""

from random import randint


def find_and_remove_list(lst, value):
    try:
        i = lst.index(value)
        lst[i] = "Oliver"
    except:
        pass


def read_data(filename):
    file = open(filename, "r")
    data = file.read()
    data = data.split()
    i = 0
    while i < len(data):
        data[i] = int(data[i])
        i += 1
    return data


def is_in_linear(search_val, values):
    i = 0
    while i < len(values):
        if values[i] == search_val:
            return True
        i += 1
    return False


def good_input():
    x = eval(input("Enter a number from 1 to 10: "))
    while x < 1 or x > 10:
        x = eval(input("Enter a number from 1 to 10: "))
    return x


def num_digits():
    num = eval(input("Enter a positive integer: "))
    while num > 0:
        digits = 0
        while num > 0:
            num = num // 10
            digits += 1
        print("The number of digits is", digits)
        num = eval(input("Enter a positive integer: "))


def hi_lo_game():
    num = randint(1, 100)
    guesses = 0
    guess = eval(input("Enter a guess: "))
    while guess != num and guesses != 7:
        guesses += 1
        if guess > num:
            print("The guess was too high")
        elif guess < num:
            print("The guess was too low")
        if guess != num and guesses != 7:
            guess = eval(input("Enter a guess: "))
    if guess == num:
        print("You won! Number of guesses =", guesses)
    else:
        print("You lost!")


def main():
    lst = [1, 2, 3, 4, 5, 6, 9]
    find_and_remove_list(lst, 3)
    read_data("numbers.txt")
    is_in_linear(10, read_data("numbers.txt"))
    good_input()
    num_digits()
    hi_lo_game()


main()
