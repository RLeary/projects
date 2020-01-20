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
    # store board as a list of strings, print out each string
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



b1 = new_board()
b1[0][2] = 'X'
b1[1][1] = 'O'
render(b1)