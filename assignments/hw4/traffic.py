"""
Name: Oliver Aschenbrenner
traffic.py

Problem: Use accumulators and nested loops to calculate and output the num of vehicles
that traveled down the road each day as well
as the total and average number of vehicles for all of the roads

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def main():
    num_of_roads = eval(input("How many roads were surveyed? "))
    acc = 0
    accumulator = 0
    for i in range(1, num_of_roads + 1):
        num_of_days = eval(input("How many days was road " + str(i) + " surveyed? "))
        for j in range(1, num_of_days + 1):
            num_of_cars = eval(input("How many cars traveled on day " + str(j) + "? "))
            acc = acc + num_of_cars
            accumulator = accumulator + num_of_cars
        print("Road", str(i), "average vehicles per day: ", round(acc / num_of_days, 2))
        for _ in range(j):
            acc = 0
    print("Total number of vehicles traveled on all roads: ", accumulator)
    print("Average number of vehicles per road: ", round(accumulator / num_of_roads, 2))


if __name__ == '__main__':
    main()
