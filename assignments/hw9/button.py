"""
Name: Oliver Aschenbrenner
button.py

Problem: create a button class and use it in a three door game

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import Point, Text


class Button:
    """
    here are the functions inside of the button class
    """
    def __init__(self, shape, label):
        """
        initializes the Button class
        """
        self.shape = shape
        self.text = Text(Point(self.shape.getP1().getX() + 40,
                               self.shape.getP1().getY() + 35), label)

    def get_label(self):
        """
        returns the label of the button
        """
        return self.text.getText()

    def draw(self, win):
        """
        draws the buttons and labels
        """
        self.shape.draw(win)
        self.text.draw(win)

    def undraw(self):
        """
        undraw the shape and label
        """
        self.shape.undraw()
        self.text.undraw()

    def is_clicked(self, point):
        """
        checks to see if the buttons have been clicked
        """
        if self.shape.getP1().getX() <= point.getX() <= self.shape.getP2().getX() \
                and self.shape.getP1().getY() <= point.getY() <= self.shape.getP2().getY():
            return True
        return False

    def color_button(self, color):
        """
        sets the color of the buttons
        """
        self.shape.setFill(color)

    def set_label(self, label):
        """
        updates the button labels
        """
        self.text.setText(label)
