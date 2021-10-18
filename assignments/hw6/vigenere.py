"""
Name: Oliver Aschenbrenner
vigenere.py

Problem: create a vigenere cipher and display it in a graphics window

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import Text, Point, Entry, Rectangle, GraphWin


def code(message, keyword):
    cipher = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    message = message.upper()
    message = message.replace(" ", "")
    keyword = keyword.upper()
    acc = 0
    string_accumulator = ""
    for i in range(len(message)):
        message1 = cipher.find(message[i])
        key1 = cipher.find(keyword[acc])
        if message1 + key1 > 25:
            total = message1 + key1 - 26
        else:
            total = message1 + key1
        string_accumulator = string_accumulator + cipher[total]
        acc = acc + 1
        if acc > len(keyword) - 1:
            acc = 0

    return string_accumulator


def main():
    win = GraphWin("Vigenere", 400, 300)

    # make the text and entry boxes
    message_text = Text(Point(70, 50), "Message to Code")
    message_text.draw(win)
    keyword_text = Text(Point(70, 100), "Enter Keyword")
    keyword_text.draw(win)
    message_box = Entry(Point(200, 50), 20)
    message_box.draw(win)
    keyword_box = Entry(Point(200, 100), 20)
    keyword_box.draw(win)

    # make the button
    button = Rectangle(Point(160, 150), Point(240, 190))
    button.draw(win)
    encode = Text(Point(200, 170), "Encode")
    encode.draw(win)

    # after clicking encode
    win.getMouse()
    button.undraw()
    encode.undraw()
    result = Text(Point(200, 200), "Resulting Message")
    result.draw(win)
    message_result = Text(Point(200, 220), code(message_box.getText(), keyword_box.getText()))
    message_result.draw(win)
    close = Text(Point(200, 280), "Click Anywhere to Close Window")
    close.draw(win)

    win.getMouse()
    win.close()


if __name__ == '__code__':
    code("message", "keyword")


if __name__ == '__main__':
    main()
