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



# hint for thinking about board, hover over a board and turn head 90* left

# TODO implement - 
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

if __name__ == "__main__":
    b1 = new_board()

    b1[0][2] = 'X'
    b1[3][5] = 'X'
    b1[0][1] = 'X'
    b1[0][3] = 'X'
    b1[0][4] = 'X'
    b1[0][5] = 'X'
    b1[0][0] = 'X'
    b1[5][0] = 'X'
    b1[5][1] = 'X'
    b1[5][2] = 'X'
    b1[5][3] = 'X'
    b1[5][4] = 'X'
    b1[5][5] = 'X'
    b1[6][5] = 'X'
    
    render(b1)
    move_1 = get_move(b1)
    b1 = make_move(b1, move_1, 'O')
    render(b1)
    move_2 = get_move(b1)
    b1 = make_move(b1, move_2, 'O')
    render(b1)