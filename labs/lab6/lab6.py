"""
Name: Oliver Aschenbrenner
lab6.py
"""


def name_reverse():
    """
    Read a name in first-last order and display it in last-comma-first order.
    """
    name = input("Enter a name in first name - last name order: ")
    name = name.split()
    print(name[1] + ", " + name[0])


def company_name():
    company = input("Enter a three-part internet domain name: ")
    company = company.split('.')
    print(company[1])


def initials():
    num = eval(input("How many names will be input? "))
    for i in range(1, num + 1):
        first = input("Enter the first name of student " + str(i) + ": ")
        last = input("Enter " + first + "'s last name: ")
        print(first + "'s initials are " + first[0] + last[0])


def names():
    list_of_names = input("Enter people's names, separated by commas: ")
    list_of_names = list_of_names.split(",")
    print("The initials are", end=" ")
    for name in list_of_names:
        parts = name.split()
        print(parts[0][0] + parts[1][0], end=" ")


def thirds():
    sentence = eval(input("How many sentences will be input? "))
    for _ in range(1, sentence + 1):
        s = input("Enter sentence " + str(_) + ": ")
        print(s[2::3])


def word_average():
    sentence = input("Enter a sentence: ")
    acc = 0
    sentence = sentence.split()
    for word in sentence:
        acc = acc + len(word)
    print(acc / len(sentence))


def pig_latin():
    x = input("Enter a sentence: ")
    x = x.lower()
    x = x.split()
    for word in x:
        print(word[1:] + word[0] + "ay", end=" ")


def main():
    # name_reverse()
    # company_name()
    # initials()
    # names()
    # thirds()
    # word_average()
    # pig_latin()


main()
