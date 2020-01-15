# Conway's Game of Life
# 1. Any live cell with 0 or 1 live neighbors becomes dead, because of 
# underpopulation
# 2. Any live cell with 2 or 3 live neighbors stays alive, because its 
# neighborhood is just right
# 3. Any live cell with more than 3 live neighbors becomes dead, because 
# of overpopulation
# 4. Any dead cell with exactly 3 live neighbors becomes alive, by reproduction

import random

DEAD = 0
LIVE = 1

width = 10
height = 8

# returns a board of width x height, all dead cells
def dead_state(width, height):
    """
    board = list()
    for i in range(height):
        row = list()
        for j in range(width):
            row.append(DEAD)
        board.append(row)
         
    return board
    """
    # list comprehension - better way
    return [[DEAD for x in range(height)] for x in range(width)]

# returns a board of width x height, random cell state
# build board using dead_state(), then randomly assign cell states
def random_state(width, height):
    board = dead_state(width, height)

    # randomise each state
    for i in range(get_board_width(board)):
        for j in range(get_board_height(board)):
            state = random.randint(0, 1)
            board[i][j] = state

    return board

#print(dead_state(width, height))
#print(random_state(width, height))

# get board witdh and height
def get_board_width(board):
    return len(board)

def get_board_height(board):
    return len(board[0])

# render the gol board as a 2d grid, rather than printing 
# [[0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1... # etc
def render(board):
    # dict for characters to display
    cell_display = {
        DEAD: ' ',
        # unicode for a filled in square.
        LIVE: u"\u2588"
    }
    # creates lines[], the board to print
    lines = list()
    for i in range(get_board_height(board)):
        line = str()
        line += '| ' # vertical outline
        for j in range(get_board_width(board)):
            line += cell_display[board[j][i]] * 2 # without doubling cell_display it look squished
        line += ' |' # vertical outline
        lines.append(line)

    horizontal_outline = str()
    for i in range(get_board_width(board) + 2):
        horizontal_outline += '--'

    print(horizontal_outline)
    print("\n".join(lines))
    print(horizontal_outline)

#render(random_state(width, height))

# takes a given board state, then calculate and return th next state
# according to the rules of GOL:
#   a cell with:
#       0 or 1 neighbours - dies
#       2 or 3 neighbours - lives
#       >3 neighbours - dies
#       dead with 3 neighbours - born
def next_board_state(board):
    width = get_board_width(board)
    height = get_board_height(board)
    next_state = dead_state(width, height)

    for x in range(width):
        for y in range(height):
            next_state[x][y] = next_cell_value((x, y), board)

    return next_state

# get the next value of a cell. coord - (x, y) tuple for cell co-ordinates
# returns LIVE or DEAD based on surrounding cells
def next_cell_value(coord, board):
    width = get_board_width(board)
    height = get_board_height(board)
    x = coord[0]
    y = coord[1]
    live_neighbours = 0

    # iterate around cell neighbours to count live cells
    for i in range((x-1), (x+1)+1):
        if i < 0 or i >= width:
            continue # don't go off the edge

        for j in range((y-1), (y+1)+1):
            if j < 0 or j >= height:
                continue # don't go off the edge
            
            if i == x and j == y:
                continue # a cell is not it's own neighbour

            if board[i][j] == LIVE:
                live_neighbours += 1

    if board[x][y] == LIVE:
        if live_neighbours <= 1:
            return DEAD
        elif live_neighbours <= 3:
            return LIVE
        else:
             return DEAD
    else:
        if live_neighbours == 3:
            return LIVE
        else:
            return DEAD