"""
Name: Oliver Aschenbrenner
lab9.py
"""

import math
from graphics import *


def addTen(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] + 10


def squareEach(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2


def sumList(nums):
    acc = 0
    for i in range(len(nums)):
        acc = acc + nums[i]
    return acc


def toNumbers(strList):
    for i in range(len(strList)):
        strList[i] = float(strList[i])


def writeSumOfSquares():
    pass
    file = input("Enter name of file: ")
    infile = open(file, "r")
    outfile = open("output.txt", "w+")
    for line in infile:
        nums = line.split()
        toNumbers(nums)
        squareEach(nums)
        x = sumList(nums)
        outfile.write("Sum of squares = " + str(x) + '\n')


def starter():
    weight = eval(input("Enter weight: "))
    numWins = eval(input("Enter number of wins: "))
    if 150 <= weight <= 160 and numWins >= 5:
        print("is starter")
    elif weight > 199 or numWins > 20:
        print("is starter")
    else:
        print("not starter")


def leapYear(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print(year, "is a leap year")
        return True
    else:
        print(year, "is not a leap year")
        return False


def circleOverlap():
    win = GraphWin("CircleOverlap", 400, 400)
    p1 = win.getMouse()
    p2 = win.getMouse()
    radius = math.sqrt((p2.getX() - p1.getX()) ** 2 + (p2.getY() - p1.getY()) ** 2)
    circle = Circle(p1, radius)
    circle.draw(win)

    p3 = win.getMouse()
    p4 = win.getMouse()
    radius2 = math.sqrt((p4.getX() - p3.getX()) ** 2 + (p4.getY() - p3.getY()) ** 2)
    circle2 = Circle(p3, radius2)
    circle2.draw(win)

    distance = math.sqrt((p3.getX() - p1.getX()) ** 2 + (p3.getY() - p1.getY()) ** 2)
    if distance <= radius + radius2:
        overlap = Text(Point(200, 350), "The Circles Overlap")
        overlap.draw(win)
    else:
        notoverlap = Text(Point(200, 350), "The Circles Do Not Overlap")
        notoverlap.draw(win)
    win.getMouse()
    win.close()


def main():
    x = [5, 2, -3]
    addTen(x)
    print(x)

    y = [3, 5.7, 2]
    squareEach(y)
    print(y)

    a = sumList(y)
    print(a)

    z = ["3", "5.7", "2"]
    toNumbers(z)
    print(z)

    writeSumOfSquares()
    starter()
    leapYear(2000)
    leapYear(2011)
    circleOverlap()
    pass


main()
