"""
Name: Oliver Aschenbrenner
three_door_game.py

Problem: create a button class and use it in a three door game

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from random import randint

from graphics import Rectangle, Text, Point, GraphWin

from button import Button


def main():
    win = GraphWin("Three Door Game", 500, 500)
    win.setBackground("gray")
    door1 = Button(Rectangle(Point(110, 370), Point(190, 430)), "Door 1")
    door2 = Button(Rectangle(Point(210, 370), Point(290, 430)), "Door 2")
    door3 = Button(Rectangle(Point(310, 370), Point(390, 430)), "Door 3")
    text = Text(Point(250, 200), "One of These is a Secret Door")
    text.setSize(30)

    # draw the buttons and text
    door1.draw(win)
    door2.draw(win)
    door3.draw(win)
    text.draw(win)

    # create random int for the secret door
    num = randint(1, 3)

    # all possible combinations
    # multiple clicks might be needed
    if num == 1 and door1.is_clicked(win.getMouse()):
        door1.color_button("green")
        door1.set_label("Secret Door")

    if num == 1 and door2.is_clicked(win.getMouse()):
        door2.color_button("red")
        door1.color_button("green")
        door2.set_label("You Lost")
        door1.set_label("Secret Door")

    if num == 1 and door3.is_clicked(win.getMouse()):
        door1.color_button("green")
        door3.color_button("red")
        door3.set_label("You Lost")
        door1.set_label("Secret Door")

    if num == 2 and door2.is_clicked(win.getMouse()):
        door2.color_button("green")
        door2.set_label("Secret Door")

    if num == 2 and door1.is_clicked(win.getMouse()):
        door1.color_button("red")
        door2.color_button("green")
        door1.set_label("You Lost")
        door2.set_label("Secret Door")

    if num == 2 and door3.is_clicked(win.getMouse()):
        door2.color_button("green")
        door3.color_button("red")
        door3.set_label("You Lost")
        door2.set_label("Secret Door")

    if num == 3 and door3.is_clicked(win.getMouse()):
        door3.color_button("green")
        door3.set_label("Secret Door")

    if num == 3 and door1.is_clicked(win.getMouse()):
        door1.color_button("red")
        door3.color_button("green")
        door1.set_label("You Lost")
        door3.set_label("Secret Door")

    if num == 3 and door2.is_clicked(win.getMouse()):
        door3.color_button("green")
        door2.color_button("red")
        door2.set_label("You Lost")
        door3.set_label("Secret Door")

    win.getMouse()
    win.close()


if __name__ == '__main__':
    main()
