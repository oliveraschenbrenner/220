"""
Name: Oliver Aschenbrenner
lab5.py

Problem: use python graphics
"""

from graphics import *
import math


def target():
    win_width = 500
    win_height = 500
    win = GraphWin("Archery Target", win_width, win_height)

    # Add code here to get the dimensions and draw the target
    z = 500
    circle1 = Circle(Point(z/2, z/2), 250)
    circle1.setFill("white")
    circle1.draw(win)
    circle2 = Circle(Point(z/2, z/2), 200)
    circle2.setFill("black")
    circle2.draw(win)
    circle3 = Circle(Point(z/2, z/2), 150)
    circle3.setFill("blue")
    circle3.draw(win)
    circle4 = Circle(Point(z/2, z/2), 100)
    circle4.setFill("red")
    circle4.draw(win)
    circle5 = Circle(Point(z/2, z/2), 50)
    circle5.setFill("yellow")
    circle5.draw(win)
    instruction_text = Text(Point(z/2, 480), "Click to close the screen")
    instruction_text.draw(win)
    # Wait for another click to exit

    win.getMouse()
    win.close()


def triangle():

    win_width = 500
    win_height = 500
    win = GraphWin("Draw a Triangle", win_width, win_height)

    p1 = win.getMouse()
    p2 = win.getMouse()
    p3 = win.getMouse()
    triangle_shape = Polygon(p1, p2, p3)
    triangle_shape.draw(win)
    dx1 = p2.getX() - p1.getX()
    dy1 = p2.getY() - p1.getY()
    length1 = math.sqrt((dx1 ** 2) + (dy1 ** 2))
    a = length1
    dx2 = p3.getX() - p2.getX()
    dy2 = p3.getY() - p2.getY()
    length2 = math.sqrt((dx2 ** 2) + (dy2 ** 2))
    b = length2
    dx3 = p3.getX() - p1.getX()
    dy3 = p3.getY() - p1.getY()
    length3 = math.sqrt((dx3 ** 2) + (dy3 ** 2))
    c = length3
    perimeter = round(a + b + c, 3)
    perimeter_text = Text(Point(100, 50), "The perimeter is " + str(perimeter))
    perimeter_text.draw(win)
    s = (a + b + c) / 2
    area = math.sqrt((s * (s - a) * (s - b) * (s - c)))
    area_round = round(area, 3)
    area_text = Text(Point(100, 100), "The area is " + str(area_round))
    area_text.draw(win)
    # Add code here to accept the mouse clicks, draw the triangle.
    # and display its area in the graphics window.

    # Wait for another click to exit
    win.getMouse()
    win.close()


def color_shape():
    # Create code to allow a user to color a shape by entering rgb amounts
    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")

    # display rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)

# code here
    red_box = Entry(Point(win_width / 2, win_height / 2 + 40), 5)
    red_box.draw(win)
    green_box = Entry(Point(win_width / 2, win_height / 2 + 70), 5)
    green_box.draw(win)
    blue_box = Entry(Point(win_width / 2, win_height / 2 + 100), 5)
    blue_box.draw(win)

    for _ in range(5):
        win.getMouse()
        red = int(red_box.getText())
        green = int(green_box.getText())
        blue = int(blue_box.getText())
        color = color_rgb(red, green, blue)
        shape.setFill(color)

    # Wait for another click to exit
    win.getMouse()
    win.close()


def process_string():
    string = input("enter a string: ")
    print(string[0])
    print(string[-1])
    print(string[2:6])
    print(string[0] + string[-1])
    print(string[0:3] * 10)
    for c in string:
        print(c)
    print(len(string))


def process_list():
    pt = Point(5, 10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]
    x = values[1] + values[3]
    print(str(x))
    x = values[0] + values[2]
    print(x)
    x = values[1] * 5
    print(x)
    x = values[2:5]
    print(x)
    x = [values[2], values[3], values[0]]
    print(x)
    x = [values[2], values[0], float(values[5])]
    print(x)
    x = values[0] + values[2] + float(values[5])
    print(x)
    x = len(values)
    print(x)


def another_series():
    num_of_terms = eval(input("Enter the number of terms: "))
    acc = 0
    for i in range(num_of_terms):
        y = 2 + 2 * (i % 3)
        print(y, end=" ")
        acc = acc + y
    print("\nsum = ", acc)


def main():
    target()
    # triangle()
    # color_shape()
    # process_string()
    # process_list()
    # another_series()
    # pass


main()
