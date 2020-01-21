BOARD_HEIGHT = 3
BOARD_WIDTH = 3
PRINTED_GRID_WIDTH = 14

# Creates a board data structure for the game
# [][], all None
def new_board():
    return [[None for x in range(BOARD_HEIGHT)] for x in range(BOARD_WIDTH)]

#print(new_board())

# render the board as a 2d grid, rather than printing 
# [[X, X, None], [O, None, None], O, None, None]] eg
def render(board):
    lines = list()
    for i in range(BOARD_HEIGHT):
        # need line as list - str cant contain None
        line = list()
        for j in range(BOARD_WIDTH):
            line.append(board[j][i])
        lines.append(line)

    #print("\n".join(lines)) cant use join() for lists, need to use for loops
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

#b1 = new_board()
#b1[0][2] = 'X'
#b1[1][1] = 'O'
#b1[2][1] = 'O'
#render(b1)

# returns the coordinates of a player's chosen move
def get_move():
    x = int(input("Enter your move's X co-ordinate: "))
    y = int(input("Enter your move's Y co-ordinate: "))
    # TODO validation
    return (x, y)

#print(get_move())

# make a single move, and return the updated board state
# assume coords are correct, validation done elsewhere
def make_move(board, coord, player):
    new_board_state = new_board()
    for i in range(BOARD_HEIGHT):
        for j in range(BOARD_WIDTH):
            new_board_state[i][j] = board[i][j]

    # TODO player - 'X' or 'O' - currently passing in 'X' or 'O'
    # maybe better way or just call as if player1:make_move(board, (x, y), 'X')
    # else#player 2: make_move(board, (x, y), 'O')
    x = coord[0]
    y = coord[1]
    new_board_state[x][y] = player

    return new_board_state

b1 = new_board()

move_coord = (2, 0)
b1 = make_move(b1, move_coord, "X")
render(b1)

move_coord_2 = (1, 1)
b1 = make_move(b1, move_coord_2, "O")
render(b1)