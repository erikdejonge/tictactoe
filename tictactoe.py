#!/usr/bin/env python3
# coding=utf-8
"""
tic tac toe
dave koning
2015
"""
import random
import readline


def textoutput(s=None):
    """
    @type s: str, None
    @return: None
    """
    if s is None:
        print()
    else:
        print("\033[0;34m" + str(s) + "\033[0m")


def choose_random_move_from_list(board, moves_list):
    """
    @type board: list
    @type moves_list: list
    @return: None
    """

    # returns a valid move from the passed list on the passed board.
    # returns None if there is no valid move.
    possible_moves = []

    for i in moves_list:
        if is_space_free(board, i):
            possible_moves.append(i)

    if len(possible_moves) != 0:
        return random.choice(possible_moves)
    else:
        return None


def draw_board(board):
    """
    @type board: list
    @return: None
    """
    num = []

    for i in range(10):
        num.append("\033[37m" + str(i) + "\033[0m")

    # this function textoutputs out the board that it was passed.
    # "board" is a list of 10 strings representing the board (ignore index 0)
    boardstring = num[7] + '  |' + num[8] + '  |' + num[9] + '\n'
    boardstring += ' ' + board[7] + ' | ' + board[8] + ' | ' + board[9] + '\n'
    boardstring += '   |   |\n'
    boardstring += '___________\n'
    boardstring += num[4] + '  |' + num[5] + '  |' + num[6] + '\n'
    boardstring += ' ' + board[4] + ' | ' + board[5] + ' | ' + board[6] + '\n'
    boardstring += '   |   |\n'
    boardstring += '___________\n'
    boardstring += num[1] + '  |' + num[2] + '  |' + num[3] + '\n'
    boardstring += ' ' + board[1] + ' | ' + board[2] + ' | ' + board[3] + '\n'
    boardstring += '   |   |\n'
    boardstring = boardstring.replace("X", "\033[0;35mX\033[0m")
    boardstring = boardstring.replace("O", "\033[0;91mO\033[0m")
    boardstring = boardstring.replace("_", "\033[0;38m-\033[0m")
    boardstring = boardstring.replace("|", "\033[0;38m|\033[0m")
    print(boardstring)


def get_board_copy(board):
    """
    @type board: list
    @return: None
    """

    # make a duplicate of the board list and return it the duplicate.
    dupe_board = []

    for i in board:
        dupe_board.append(i)

    return dupe_board


def get_computer_move(board, computer_letter):
    """
    @type board: list
    @type computer_letter: str
    @return: None
    """

    # given a board and the computer's letter, determine where to move and return that move.
    if computer_letter == 'X':
        player_letter = 'O'
    else:
        player_letter = 'X'

    # here is our algorithm for our tic tac toe ai:
    # first, check if we can win in the next move
    for i in range(1, 10):
        copy = get_board_copy(board)

        if is_space_free(copy, i):
            make_move(copy, computer_letter, i)

            if is_winner(copy, computer_letter):
                return i

    # check if the player could win on his next move, and block them.
    for i in range(10):
        if i > 0:
            copy = get_board_copy(board)

            if is_space_free(copy, i):
                make_move(copy, player_letter, i)

                if is_winner(copy, player_letter):
                    return i

    # try to take one of the corners, if they are free.
    move = choose_random_move_from_list(board, [1, 3, 7, 9])

    if move is not None:
        return move

    # try to take the center, if it is free.

    if is_space_free(board, 5):
        return 5

    # move on one of the sides.
    return choose_random_move_from_list(board, [2, 4, 6, 8])


def get_player_move(board):
    """
    @type board: list
    @return: None
    """

    # let the player type in his move.
    move = ' '

    while move not in '1 2 3 4 5 6 7 8 9'.split() or not is_space_free(board, int(move)):
        textoutput('Wat is uw volgende zet? (1-9, s=stoppen)')
        try:
            move = input()
        except KeyboardInterrupt:
            exit(1)

        if move.strip().lower() == "s" or move.strip().lower() == "stoppen":
            exit(1)

    return int(move)


def input_player_letter():
    """
    input_player_letter
    """

    # lets the player type which letter they want to be.
    # returns a list with the player's letter as the first item, and the computer's letter as the second.
    letter = ''

    while not (letter == 'X' or letter == 'O'):
        print('\033[0;34mWilt u X \033[34mof\033[0m O \033[0;34mzijn:\033[0m'.replace("X", "\033[0;35mX\033[0m").replace("O", "\033[0;91mO\033[0m"))
        try:
            letter = input().upper()
        except KeyboardInterrupt:
            exit(1)

    # the first element in the tuple is the player's letter, the second is the computer's letter.
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def is_board_full(board):
    """
    @type board: list
    @return: None
    """

    # return True if every space on the board has been taken. otherwise return false.
    for i in range(10):
        if i > 0:
            if is_space_free(board, i):
                return False

    return True


def is_space_free(board, move):
    """
    @type board: list
    @type move: int
    @return: None
    """

    # return true if the passed move is free on the passed board.
    return board[move] == ' '


def is_winner(bo, le):
    """
    @type bo: list
    @type le: str
    @return: None
    """

    # given a board and a player's letter, this function returns True if that player has won.
    # we use bo instead of board and le instead of letter so we don't have to type as much.
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or  # across the top
            (bo[4] == le and bo[5] == le and bo[6] == le) or  # across the middle
            (bo[1] == le and bo[2] == le and bo[3] == le) or  # across the bottom
            (bo[7] == le and bo[4] == le and bo[1] == le) or  # down the left side
            (bo[8] == le and bo[5] == le and bo[2] == le) or  # down the middle
            (bo[9] == le and bo[6] == le and bo[3] == le) or  # down the right side
            (bo[7] == le and bo[5] == le and bo[3] == le) or  # diagonal
            (bo[9] == le and bo[5] == le and bo[1] == le))  # diagonal


def main():
    """
    main
    """

    textoutput("\033[95m== Boter Kaas en Eieren! ==\033[0m")
    textoutput()

    while True:

        # reset the board
        the_board = [' '] * 10

        # draw_board(the_board)
        player_letter, computer_letter = input_player_letter()
        turn = who_goes_first()

        if turn == "player":
            turnvis = "U"
        else:
            turnvis = "De computer"

        textoutput(turnvis + ' mag beginnen.')
        game_is_playing = True

        while game_is_playing:
            if turn == 'player':
                # player's turn.
                draw_board(the_board)
                move = get_player_move(the_board)
                make_move(the_board, player_letter, move)

                if is_winner(the_board, player_letter):
                    draw_board(the_board)
                    textoutput(b'U heeft gewonnen! \xf0\x9f\x98\x8e'.decode())
                    game_is_playing = False
                else:
                    if is_board_full(the_board):
                        draw_board(the_board)
                        textoutput(b'Gelijkspel! \xf0\x9f\x98\x90'.decode())
                        break
                    else:
                        turn = 'computer'
            else:
                # computer's turn.
                move = get_computer_move(the_board, computer_letter)
                make_move(the_board, computer_letter, move)

                if is_winner(the_board, computer_letter):
                    draw_board(the_board)
                    textoutput(b'U heeft verloren \xf0\x9f\x98\xa2'.decode())
                    game_is_playing = False
                else:
                    if is_board_full(the_board):
                        draw_board(the_board)
                        textoutput(b'Gelijkspel! \xf0\x9f\x98\x90'.decode())
                        break
                    else:
                        turn = 'player'

        if not play_again():
            textoutput(b"Tot ziens. \xf0\x9f\x98\x80".decode())
            break


def make_move(board, letter, move):
    """
    @type board: list
    @type letter: str
    @type move: int
    @return: None
    """
    board[move] = letter


def play_again():
    """
    play_again
    """

    # this function returns True if the player wants to play again, otherwise it returns false.
    print()
    textoutput('Nog een keer? (ja of nee)')
    return input().lower().startswith('j')


def who_goes_first():
    """
    who_goes_first
    """

    # randomly choose the player who goes first.
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

readline.parse_and_bind("tab: complete")


if __name__ == "__main__":
    main()
