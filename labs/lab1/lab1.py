"""
Name: Oliver Aschenbrenner
lab1.py

Problem: This function calculates the area of a rectangle
"""


def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)


def calc_volume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    height = eval(input("Enter the height: "))
    volume = length * width * height
    print("Volume =", volume)


def shooting_percentage():
    shots_made = eval(input("Enter the number of shots made: "))
    total_shots = eval(input("Enter the total number of shots: "))
    percentage = (shots_made / total_shots) * 100
    print("You made", percentage, "% of shots")


def coffee():
    coffee_bought = eval(input("Enter number of pounds of coffee purchased: "))
    coffee_cost = coffee_bought * 10.50
    fixed_cost = 1.50
    shipping_cost = .86 * coffee_bought
    total_cost = coffee_cost + fixed_cost + shipping_cost
    print("Your total is $", total_cost)


def kilometers_to_miles():
    kilometers = eval(input("Enter kilometers traveled: "))
    miles = kilometers * .621
    print("You traveled", miles, "miles.")


# calc_rec_area()
# calc_volume()
# shooting_percentage()
# coffee()
# kilometers_to_miles()
