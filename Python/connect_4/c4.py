# Colored terminal output needs a workaround for windows

#from termcolor import colored, cprint

BOARD_HEIGHT = 6 
BOARD_WIDTH = 7
PRINTED_GRID_WIDTH = 15

# neither of these working on windows
# TODO get colour working on windows
#RED = colored('O', 'red', attrs=['bold'])
#YELLOW = colored('O', 'yellow', attrs=['bold'])
#RED = u'\33[31m'
#YELLOW = u'\33[33m'
#BLOCK = u'\u2588'

RED = 'R'
YELLOW = 'Y'

# Creates a board data structure for the game
# [col][row], all None
def new_board():
    return [[None for x in range(BOARD_HEIGHT)] for x in range(BOARD_WIDTH)]

# board[y][x] to print properly, as columns contain rows, not other way around
def render(board):
    horizontal_line = str()
    for i in range(PRINTED_GRID_WIDTH):
        if i % 2 == 0:
            horizontal_line += '+'
        else:
            horizontal_line += '-'
    print(" 0 1 2 3 4 5 6 ")
    lines = list()
    for x in range(BOARD_HEIGHT):
        line = str()
        line_to_output = '|'
        print(horizontal_line)
        for y in range(BOARD_WIDTH):
            if board[y][x] is None:
                line_to_output += ' '
                line_to_output += '|'
            else:
                line_to_output += board[y][x]
                line_to_output += '|'
        #print(line_to_output)
        print(line_to_output)
    print(horizontal_line)

# get column, go though x elements in column until not None, then place x-1
# move is (x, y)
def make_move(board, move, player_symbol):
    new_board_state = new_board()
    for i in range(BOARD_HEIGHT):
        for j in range(BOARD_WIDTH):
            new_board_state[j][i] = board[j][i]

    x = move[0]
    y = move[1]

    if new_board_state[x][y] is None:
        new_board_state[x][y] = player_symbol
    else:
        raise Exception("Co-ordinate already used")

    return new_board_state

# returns a move (x, y)
# get a column from user, then return the row the token will drop to
def get_move(board):
    valid_columns = get_valid_columns(board)
    col_selection = None
    x_move = None
    y_move = None

    print("Available moves: ",', '.join(str(x) for x in valid_columns))

    while col_selection not in valid_columns:
        col_selection = int(input("Enter your selection: "))
    
    x_move = col_selection
    y_move = get_drop_row_index(board[x_move])

    return(x_move, y_move)

# returns the index of the 'bottom' empty row
# eg [None, None, None, None, 'O', 'O'] returns 3
# will never be given a full column, get_move() only gets non-full columns
def get_drop_row_index(column):
    for i in range(BOARD_HEIGHT):
        if column[i] is not None:
            return i-1
    return BOARD_HEIGHT-1

def check_if_column_full(col):
    for x in range(BOARD_HEIGHT):
        if col[x] == None:
            return False
    return True

# return a list of non full columns
def get_valid_columns(board):
    valid_columns = list()
    for i in range(BOARD_WIDTH):
        if not check_if_column_full(board[i]):
            valid_columns.append(i)
    return valid_columns

def check_if_board_full(board):
    for x in range(BOARD_HEIGHT):
        for y in range(BOARD_WIDTH):
            if board[y][x] is None:
                return False
    return True

# TODO implement
# return the winning player
# return None if no winner
def get_winner(board):
    # get all possible line co-cords
    # if a line contains 4 in a row, return a cell contents
    return None
"""
# tictactoe.py
def get_winner(board):
    # TODO implement properly, cheated
    # list of all lines, if a line has 3 of same type, return player
    all_line_coords = get_all_coords()

    for line in all_line_coords:
        line_values = [board[x][y] for (x, y) in line]
        if len(set(line_values)) == 1 and line_values[0] is not None:
            return line_values[0]

    return None

"""

def play_game(player1, player2):
    players = [
        (RED, player1),
        (YELLOW, player2)
    ]

    board = new_board()
    turn_number = 0

    while not check_if_board_full(board):
        current_player_symbol, current_player = players[turn_number % 2]
        print("Current player: ", current_player)
        render(board)

        move = get_move(board)
        board = make_move(board, move, current_player_symbol)
        render(board)

        if get_winner(board):
            # TODO un-comment following line once get_winner() implemented
            # return current_player
            return 'Won'

        turn_number += 1

    return 'Draw'

if __name__ == "__main__":
    player1 = 'R'
    player2 = 'Y'
    b1 = new_board()

    winner = play_game(player1, player2)
    print(winner)