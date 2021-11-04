"""
Name: Oliver Aschenbrenner
bumper.py

Problem: create a program that represents bumper cars

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from random import randint

from time import sleep

import math

from graphics import color_rgb, GraphWin, Circle, Point


def get_random(move_amount):
    return randint(-move_amount, move_amount)


def did_collide(ball1, ball2):
    ball1center = ball1.getCenter()
    ball2center = ball2.getCenter()
    ball1x = ball1center.getX()
    ball1y = ball1center.getY()
    ball2x = ball2center.getX()
    ball2y = ball2center.getY()
    ball1radius = ball1.getRadius()
    ball2radius = ball2.getRadius()
    distance = math.sqrt(((ball2x - ball1x) ** 2) + ((ball2y - ball1y) ** 2))
    radius = ball1radius + ball2radius
    return distance <= radius


def hit_vertical(ball, win):
    ball_center = ball.getCenter()
    ballx = ball_center.getX()
    radius = ball.getRadius()
    width = win.getWidth()
    return ballx <= radius or ballx >= width - radius


def hit_horizontal(ball, win):
    ball_center = ball.getCenter()
    bally = ball_center.getY()
    radius = ball.getRadius()
    height = win.getHeight()
    return bally <= radius or bally >= height - radius


def get_random_color(circle):
    color = color_rgb(randint(0, 255), randint(0, 255), randint(0, 255))
    circle.setFill(color)


def main():
    win = GraphWin("bumper.py", 500, 500)
    # draw cars
    radius = 25
    car1 = Circle(Point(50, 50), radius)
    car2 = Circle(Point(450, 450), radius)
    get_random_color(car1)
    get_random_color(car2)
    car1.draw(win)
    car2.draw(win)
    # set random movement
    v1x = get_random(15)
    v1y = get_random(15)
    v2x = get_random(15)
    v2y = get_random(15)
    velocity = [[v1x, v1y], [v2x, v2y]]
    # check for collisions and move the car
    for _ in range(5000):
        sleep(.04)
        if did_collide(car1, car2):
            velocity[0][0] = -velocity[0][0]
            velocity[1][1] = -velocity[1][1]
            velocity[0][1] = -velocity[0][1]
            velocity[1][0] = -velocity[1][0]
        if hit_vertical(car1, win):
            velocity[0][0] = -velocity[0][0]
        if hit_vertical(car2, win):
            velocity[1][0] = -velocity[1][0]
        if hit_horizontal(car1, win):
            velocity[0][1] = -velocity[0][1]
        if hit_horizontal(car2, win):
            velocity[1][1] = -velocity[1][1]

        car1.move(velocity[0][0], velocity[0][1])
        car2.move(velocity[1][0], velocity[1][1])
    # close window
    win.getMouse()
    win.close()


if __name__ == '__main__':
    main()
