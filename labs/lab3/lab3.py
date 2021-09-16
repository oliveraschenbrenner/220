"""
Name: Oliver Aschenbrenner
lab3.py

Problem:

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def average():
    assignments = eval(input("Enter the number of grades: "))
    acc = 0
    for i in range(1, assignments+1):
        grades = eval(input("Enter your grade on HW " + str(i) + ": "))
        acc = acc + grades
    print(acc / assignments)


average()


def tip_jar():
    total = 0
    for i in range(1, 6):
        tips = eval(input("Enter the value of the tip: "))
        total = total + tips
    print("The total amount is", total, "dollars.")


tip_jar()


def newton():
    x = eval(input("Enter the x value: "))
    refine = eval(input("How many times do you want to refine? "))
    approx = x / 2
    for i in range(refine):
        approx = (approx + (x / approx)) / 2
    print(approx)


newton()


def sequence():
    number = eval(input("Enter the number of terms in the series: "))
    for i in range(1, number+1):
        y = 1 + ((i//2)*2)
        print(y, end=" ")


sequence()


def pi():
    acc = 1
    n = eval(input("Enter the number of terms in the series: "))
    for x in range(n):
        num = 2 + ((x // 2) * 2)
        denom = 1 + (((x + 1) // 2) * 2)
        fract = (num / denom)
        acc = acc * fract
    print(acc*2)


pi()
