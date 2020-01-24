# Colored terminal output needs a workaround for windows

#from termcolor import colored, cprint

BOARD_HEIGHT = 6 
BOARD_WIDTH = 7
PRINTED_GRID_WIDTH = 15

# neither of these working on windows
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



# hint for thinking about board, hover over a board and turn head 90* left

# TODO implement - 
# get column, go though x elements in column until not None, then place x-1
# move is (x, y)
def make_move(board, move, player_symbol):
    pass

# returns a move (x, y)
# get a column from user, then return the row the token will drop to
# TODO implement
def get_move(board):
    pass

def check_if_column_full(board, col):
    for x in range(BOARD_HEIGHT):
        if col[x] == None:
            return False
    return True


def check_if_board_full(board):
    for x in range(BOARD_HEIGHT):
        for y in range(BOARD_WIDTH):
            if board[y][x] is None:
                return False
    return True

if __name__ == "__main__":
    b1 = new_board()
    b1[0][2] = 'X'
    b1[3][5] = 'X'
    render(b1)