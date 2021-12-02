"""
Name: Oliver Aschenbrenner
lab13.py
"""

from random import randint


def is_in_binary(search_val, values):
    mid = len(values) // 2
    while values[mid] != search_val and len(values) != 1:
        if values[mid] < search_val:
            values = values[mid:]
        else:
            values = values[:mid]
        mid = len(values) // 2
    if values[mid] == search_val:
        return True
    return False


def selection_sort(values):
    for i in range(len(values)):
        lowest = values[i]
        pos = i
        for j in range(i, len(values)):
            if values[j] < lowest:
                lowest = values[j]
                pos = j
        values[i], values[pos] = values[pos], values[i]


def rect_sort(rectangles):
    d = {}
    areas = []
    for rect in rectangles:
        d[calc_area(rect)] = rect
        areas.append(calc_area(rect))
    selection_sort(areas)
    for i in range(len(areas)):
        rectangles[i] = d[areas[i]]
    print(areas)


def calc_area(rect):
    return randint(1, 100)


def trade_alert(filename):
    infile = open(filename, "r")
    data = infile.read().split()
    for num in range(len(data)):
        if int(data[int(num)]) > 830:
            print("Alert!", str(num + 1), "seconds.")
        if 500 < int(data[int(num)]) < 831:
            print("Warning!", str(num + 1), "seconds.")


def main():
    print(is_in_binary(3, [1, 2, 5, 6, 8, 9]))
    x = [5, 2, 1, 3]
    selection_sort(x)
    print(x)
    trade_alert("trades.txt")


main()
