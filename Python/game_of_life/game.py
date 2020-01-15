import random
import time

DEAD = 0
LIVE = 1

width = 10
height = 8

def dead_state(width, height):
    """Constuct an empty state with all cells set to DEAD.
    Parameters
    ----------
    width: the width of the state, in cells
    height: the height of the state, in cells
    Returns
    -------
    A state of dimensions width x height, with all cells set to DEAD
    """
    return [[DEAD for _ in range(height)] for _ in range(width)]

def random_state(width, height):
    """Construct a random state with all cells randomly set.
    Parameters
    ----------
    width: the width of the state, in cells
    height: the height of the state, in cells
    Returns
    -------
    A state of dimensions width x height, with all cells randomly set to either
        DEAD or LIVE with equal probability.
    """
    state = dead_state(width, height)
    for x in range(0, state_width(state)):
        for y in range(0, state_height(state)):
            random_number = random.random()
            if random_number > 0.85:
                cell_state = LIVE
            else:
                cell_state = DEAD
            state[x][y] = cell_state

    return state

def state_width(state):
    """Get the width of a state.
    Parameters
    ----------
    state: a Game state
    Returns
    -------
    The width of the input state
    """
    return len(state)

def state_height(state):
    """Get the height of a state.
    Parameters
    ----------
    state: a Game state
    Returns
    -------
    The height of the input state
    """
    return len(state[0])

def next_cell_value(cell_coords, state):
    """Get the next value of a single cell in a state.
    Parameters
    ----------
    cell_coords: an (x, y) tuple of the co-ordinates of a cell
    state: the current state of the Game board
    Returns
    -------
    The new state of the given cell - either DEAD or LIVE.
    """
    width = state_width(state)
    height = state_height(state)
    x = cell_coords[0]
    y = cell_coords[1]
    n_live_neighbors = 0

    # Iterate around this cell's neighbors
    for x1 in range((x-1), (x+1)+1):
        # Make sure we don't go off the edge of the board
        if x1 < 0 or x1 >= width: continue

        for y1 in range((y-1), (y+1)+1):
            # Make sure we don't go off the edge of the board
            if y1 < 0 or y1 >= height: continue
            # Make sure we don't count the cell as a neighbor of itself!
            if x1 == x and y1 == y: continue

            if state[x1][y1] == LIVE:
                n_live_neighbors += 1

    if state[x][y] == LIVE:
        if n_live_neighbors <= 1:
            return DEAD
        elif n_live_neighbors <= 3:
            return LIVE
        else:
            return DEAD
    else:
        if n_live_neighbors == 3:
            return LIVE
        else:
            return DEAD

def next_board_state(init_state):
    """Take a single step in the Game of Life.
    Parameters
    ----------
    init_state: the initial state of the Game board
    Returns
    -------
    The next state of the Game board, after taking one step for every cell in
        the previous state.
    """
    width = state_width(init_state)
    height = state_height(init_state)
    next_state = dead_state(width, height)

    for x in range(0, width):
        for y in range(0, height):
            next_state[x][y] = next_cell_value((x, y), init_state)

    return next_state

def render(board):
    # dict for characters to display
    cell_display = {
        DEAD: ' ',
        # unicode for a filled in square.
        LIVE: u"\u2588"
    }
    # creates lines[], the board to print
    lines = list()
    for i in range(state_height(board)):
        line = str()
        line += '| ' # vertical outline
        for j in range(state_width(board)):
            line += cell_display[board[j][i]] * 2 # without doubling cell_display it look squished
        line += ' |' # vertical outline
        lines.append(line)

    horizontal_outline = str()
    for i in range(state_width(board) + 2):
        horizontal_outline += '--'

    print(horizontal_outline)
    print("\n".join(lines))
    print(horizontal_outline)

b1 = random_state(width, height)
render(b1)
b2 = next_board_state(b1)
b3 = next_board_state(b2)