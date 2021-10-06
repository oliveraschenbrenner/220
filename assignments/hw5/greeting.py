"""
Name: Oliver Aschenbrenner
greeting.py

Problem: create a heart using graphics and have an arrow pass through it

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import GraphWin, Rectangle, Point, Circle, Polygon, Text, Line, time


def main():
    win = GraphWin("Assignment 5", 500, 500)
    background = Rectangle(Point(0, 0), Point(500, 500))
    background.setFill("pink")
    background.draw(win)
    arrow = Line(Point(50, 450), Point(150, 350))
    arrow.setWidth(3)
    arrow.setFill("black")
    arrow.draw(win)
    arrow_point = Polygon(Point(155, 355), Point(145, 345), Point(157, 342))
    arrow_point.setFill("black")
    arrow_point.draw(win)
    circle1 = Circle(Point(200, 200), 55)
    circle2 = Circle(Point(300, 200), 55)
    circle1.setFill("red")
    circle1.setOutline("red")
    circle2.setFill("red")
    circle2.setOutline("red")
    triangle = Polygon(Point(148.5, 220), Point(250, 375), Point(351.5, 220))
    triangle.setFill("red")
    triangle.setOutline("red")
    circle1.draw(win)
    circle2.draw(win)
    triangle.draw(win)
    text = Text(Point(250, 75), "Happy Valentine's Day!")
    text.setSize(30)
    text.setOutline("white")
    text.draw(win)
    text2 = Text(Point(252, 75), "Happy Valentine's Day!")
    text2.setSize(30)
    text2.setOutline("purple")
    text2.draw(win)
    for _ in range(50):
        arrow_point.move(10, -10)
        arrow.move(10, -10)
        time.sleep(.1)
    text_final = Text(Point(250, 490), "Click anywhere to close")
    text_final.draw(win)

    win.getMouse()
    win.close()


if __name__ == '__main__':
    main()
