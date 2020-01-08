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

width = 5
height = 5

# returns a board of width x height, all dead cells
def dead_state(width, height):
    board = list()
    for i in range(height):
        row = list()
        for j in range(width):
            row.append(DEAD)
        board.append(row)
         
    return board
    
    # list comprehension - better way
    #return [[DEAD for x in range(height)] for x in range(width)]

# returns a board of width x height, random cell state
# build board using dead_state(), then randomly assign cell states
def random_state(width, height):
    board = dead_state(width, height)

    # randomise each state
    for i in range(height):
        for j in range(width):
            state = random.randint(0, 1)
            board[i][j] = state

    return board

#print(dead_state(width, height))
#print(random_state(width, height))

# render the gol board as a 2d grid, rather than printing 
# [[0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1... # etc
def render(board):
    pass

random_board = random_state(width, height)
render(random_board)