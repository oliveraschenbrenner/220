"""
Name: Oliver Aschenbrenner
weighted_average.py

Problem: create a program that gives each students avg and the class avg in a new file

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def weighted_average(in_file_name, out_file_name):
    in_file = open(in_file_name, 'r')
    out_file = open(out_file_name, 'w+')
    avg = 0
    times = 0
    colon = 0
    for line in in_file:
        acc = 0
        accumulator = 0
        word = line.split()
        name_line = line.split(":")
        name = name_line[0]
        for i in range(len(word)):
            if word[i].find(':') > -1:
                colon = i
                word[i] = word[i].replace(":", "")
        for i in range(colon + 1, len(word), 2):
            acc = acc + int(word[i])
        if acc > 100:
            out_file.write(name + "'s average: Error: The weights are more than 100." + '\n')
        elif acc < 100:
            out_file.write(name + "'s average: Error: The weights are less than 100." + '\n')
        else:
            for i in range(colon + 1, len(word), 2):
                accumulator = accumulator + (int(word[i]) * int(word[i + 1]))
            students_avg = accumulator / 100
            times += 1
            avg = (avg + students_avg)
            out_file.write(name + "'s average: {:.1f}".format(students_avg) + '\n')
    if times == 0:
        avg = 0
    else:
        avg = avg / times
    out_file.write("Class average: {:.1f}".format(avg))


def main():
    weighted_average('grades.txt', 'avg.txt')


if __name__ == '__main__':
    main()
