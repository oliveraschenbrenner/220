"""
Name: Oliver Aschenbrenner
lab10.py
"""


def build_board():
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return list1


def display_board(board):
    print("{0} | {1} | {2}".format(board[0], board[1], board[2]))
    print("---------")
    print("{0} | {1} | {2}".format(board[3], board[4], board[5]))
    print("---------")
    print("{0} | {1} | {2}".format(board[6], board[7], board[8]))


def fill_spot(board, pos, char):
    if (char == 'o' or char == 'x') and is_legal(board, pos):
        board[pos - 1] = char
    else:
        return


def is_legal(board, pos):
    if pos > 9 or type(board[pos - 1]) != int:
        return False
    else:
        return True


def game_won(board, char):
    if board[0] == char and board[1] == char and board[2] == char:
        return True
    if board[0] == char and board[3] == char and board[6] == char:
        return True
    if board[3] == char and board[4] == char and board[5] == char:
        return True
    if board[6] == char and board[7] == char and board[8] == char:
        return True
    if board[1] == char and board[4] == char and board[7] == char:
        return True
    if board[2] == char and board[5] == char and board[8] == char:
        return True
    if board[0] == char and board[4] == char and board[8] == char:
        return True
    if board[6] == char and board[4] == char and board[2] == char:
        return True
    else:
        return False


def game_over(board):
    acc = 0
    for i in board:
        if type(i) == int:
            acc += 1
    if (game_won(board, 'x') or game_won(board, 'o')) or acc == 0:
        return True
    return False


def play_game():
    p1char = input("Player 1 pick o or x: ")
    p1 = 1
    p2char = input("Player 2 pick the other character: ")
    p2 = 2
    board1 = build_board()
    i = 1
    display_board(board1)
    while not game_over(board1):
        if i == 1:
            pos = input("Player " + str(p1) + ", enter the position ")
            if is_legal(board1, int(pos)):
                fill_spot(board1, int(pos), p1char)
            display_board(board1)
            if game_won(board1, p1char):
                print('Player 1 wins')
        if i == 2:
            pos = input("Player " + str(p2) + ", enter the position ")
            if is_legal(board1, int(pos)):
                fill_spot(board1, int(pos), p2char)
            display_board(board1)
            if game_won(board1, p2char):
                print('Player 2 wins')
        i += 1
        if i > 2:
            i = 1
    if not game_won(board1, p1char) and not game_won(board1, p2char):
        print("It's a tie")


def main():
    play_game()


main()
