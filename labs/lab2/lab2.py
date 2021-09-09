"""
Name: Oliver Aschenbrenner
lab2.py

Problem: develop programs that do input, produce output, and do arithmetic

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


import math


def sum_of_threes():
    upper_bound = eval(input("Enter the upper bound: "))
    accumulator = 0
    for x in range(0, upper_bound + 1, 3):
        accumulator = accumulator + x
    print("The sum of all multiples of 3 in the range is", accumulator)


# sum_of_threes()


def multiplication_table():
    for H in range(1, 11):
        for L in range(1, 11):
            print(H * L, end=" ")
        print()


# multiplication_table()


def triangle_area():
    a = eval(input("Side a of the triangle: "))
    b = eval(input("Side b of the triangle: "))
    c = eval(input("Sie c of the triangle: "))
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print("The area is", area)


# triangle_area()


def sum_squares():
    lower = eval(input("Enter the lower boundary of the range: "))
    upper = eval(input("Enter the upper boundary of the range: "))
    acc = 0
    for i in range(lower, upper + 1):
        acc = acc + (i ** 2)
    print("The sum of squares is", acc)


# sum_squares()


def power():
    base = eval(input("Enter the base: "))
    exponent = eval(input("Enter the exponent: "))
    acc = 1
    for j in range(exponent):
        acc = acc * base
    print("The answer is", acc)


# power()
