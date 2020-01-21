BOARD_HEIGHT = 3
BOARD_WIDTH = 3
PRINTED_GRID_WIDTH = 14

# Creates a board data structure for the game
# [][], all None
def new_board():
    return [[None for x in range(BOARD_HEIGHT)] for x in range(BOARD_WIDTH)]

# render the board as a 2d grid, rather than printing 
# [[X, X, None], [O, None, None], O, None, None]] eg
def render(board):
    lines = list()
    for i in range(BOARD_HEIGHT):
        line = list()
        for j in range(BOARD_WIDTH):
            line.append(board[j][i])
        lines.append(line)

    horizontal_line = str()
    for i in range(PRINTED_GRID_WIDTH):
        horizontal_line += '-'
    
    line_no = 0
    print(' | 0 | 1 | 2 |')
    for line in lines:
        line_to_output = '|'
        print(horizontal_line)
        for cell in line:
            if cell is None:
                line_to_output += ' '
                line_to_output += '|'
            else:
                line_to_output += cell
                line_to_output += '|'
        #print(line_to_output)
        print("%d%s" % (line_no, ' '.join(line_to_output)))
        line_no += 1
    print(horizontal_line)
    print('\n')

# returns the coordinates of a player's chosen move
def get_move():
    x = None
    y = None
    valid_coords = [0, 1, 2]

    while x not in valid_coords:
        x = int(input("Enter your move's X co-ordinate(0, 1, or 2): "))
    while y not in valid_coords:
        y = int(input("Enter your move's Y co-ordinate(0, 1, or 2): "))
    
    return (x, y)

#TODO is a move valid on a given board? coordinates will be valid(between
#  0 and 2) but will the cell be empty? Can't place 'O' over 'X'
def is_move_valid(board, coordinates):

# make a single move, and return the updated board state
# assume coords are correct, validation done elsewhere
def make_move(board, coord, player):
    new_board_state = new_board()
    for i in range(BOARD_HEIGHT):
        for j in range(BOARD_WIDTH):
            new_board_state[i][j] = board[i][j]

    x = coord[0]
    y = coord[1]
    # TODO if is_move_valid()
    if new_board_state[x][y] is None:
        new_board_state[x][y] = player
    else:
        raise Exception("Co-ordinated already used")

    return new_board_state

b1 = new_board()

move_coord = (2, 0)
b1 = make_move(b1, move_coord, "X")
render(b1)

move_coord_2 = (1, 1)
b1 = make_move(b1, move_coord_2, "O")
render(b1)

b1 =  make_move(b1, move_coord_2, 'O')
render(b1)

"""
move_coords = None
while True:
    move_coords = get_move()
    if is_valid_move(board, move_coords):
        break
    else:
        print "Invalid move, try again"

board = make_move(board, move_coords, player)
"""