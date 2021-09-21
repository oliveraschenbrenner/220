"""
Name: Oliver Aschenbrenner
mean.py

Problem: create a program that can calculate rms, harmonic mean, and geometric mean.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

import math

# 1) the program will take inputted numbers and calculate the rms,
# harmonic mean, and geometric mean.

# 2) the user should be allowed to enter any amount of numbers and
# the program will output the rms, harmonic mean,
# and geometric mean for all of the numbers inputted.

# 3) define the main function


def main():
    # user specifies the number of values that will be entered
    num = eval(input("Specify the number of values: "))
    # create accumulators for each of the three means
    acc = 0
    accumulator = 0
    total = 1
    # create a for loop that has a range of the entered value
    for i in range(1, num + 1):
        # user can input all their values here
        inputs = eval(input("enter value " + str(i) + ": "))
        # set the acc =  to itself plus the inputs squared
        acc = acc + (inputs ** 2)
        # set the accumulator = to itself + (one over the inputs)
        accumulator = accumulator + (1 / inputs)
        # set the third accumulator = to total times the inputs
        total = total * inputs
    # do the math for each calculation outside of the for loop
    # take the sqrt of the acc divided by the total number of inputs (num)
    rms_average = math.sqrt(acc / num)
    # print the rms
    print(round(rms_average, 3))
    # divide the number of inputs by the second accumulator
    harmonic_mean = num / accumulator
    # print the harmonic mean
    print(round(harmonic_mean, 3))
    # raise the 3rd accumulator to the power of (1 divided by the num of inputs)
    geometric_mean = total ** (1 / num)
    # print the geometric mean
    print(round(geometric_mean, 3))


# call the main function
if __name__ == '__main__':
    main()
