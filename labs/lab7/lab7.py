"""
Name: Oliver Aschenbrenner
Partner: Eric Beaver
lab7.py
"""

from math import pi


def cash_conversion():
    money = eval(input('Enter an integer: '))
    print("$" + '{:.2f}'.format(money))


def encode():
    s = input('Enter a message to be encoded: ')
    key = eval(input("Enter key: "))
    acc = ""
    for i in s:
        j = ord(i)
        j = j + key
        i = chr(j)
        acc = acc + i
    print(acc)


def sphere_area(radius):
    surface_area = 4 * pi * (radius ** 2)
    return surface_area


def sphere_volume(radius):
    volume = (4 / 3) * pi * (radius ** 3)
    return volume


def sum_n(n):
    total = 0
    for i in range(n + 1):
        total = total + i
    return total


def sum_n_cubes(n):
    total = 0
    for i in range(n + 1):
        total = total + (i ** 3)
    return total


def encode_better():
    message = input("Enter message to be encoded: ")
    key = input("Enter key to be used: ")
    acc = ""
    for i in range(len(message)):
        c = message[i]
        keyword = key[i % len(key)]
        c_value = ord(c)
        keyword_value = ord(keyword) - 97
        j = c_value + keyword_value
        k = chr(j)
        acc = acc + k
    print(acc)


def main():
    cash_conversion()
    encode()
    print(sphere_area(3))
    print(sphere_volume(3))
    print(sum_n(5))
    print(sum_n_cubes(3))
    encode_better()
    pass


main()
