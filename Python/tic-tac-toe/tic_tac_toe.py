import random

BOARD_HEIGHT = 3
BOARD_WIDTH = 3
PRINTED_GRID_WIDTH = 7

CELL_DISPLAY = {
    (0, 0): '1',
    (0, 1): '2',
    (0, 2): '3',
    (1, 0): '4',
    (1, 1): '5',
    (1, 2): '6',
    (2, 0): '7',
    (2, 1): '8',
    (2, 2): '9',
}

# Creates a board data structure for the game
# [][], all None
def new_board():
    return [[None for x in range(BOARD_HEIGHT)] for x in range(BOARD_WIDTH)]

# render the board as a 2d grid, rather than printing 
# [[X, X, None], [O, None, None], O, None, None]] eg
def render(board):
    horizontal_line = str()
    for i in range(PRINTED_GRID_WIDTH):
        horizontal_line += '-'

    lines = list()
    for x in range(BOARD_WIDTH):
        line = str()
        line_to_output = '|'
        print(horizontal_line)
        for y in range(BOARD_HEIGHT):
            if board[x][y] is None:
                line_to_output += CELL_DISPLAY[(x, y)]
                line_to_output += '|'
            else:
                line_to_output += board[x][y]
                line_to_output += '|'
        #print(line_to_output)
        print(line_to_output)
    print(horizontal_line)

# returns the coordinates of a player's chosen move
def get_move(board):
    move_int = 0
    valid_moves = get_valid_moves(board)
    valid_moves_ints = list()

    for i in range(len(valid_moves)):
        valid_moves_ints.append(CELL_DISPLAY[valid_moves[i]])

    print("Available moves: ",', '.join(str(x) for x in valid_moves_ints))

    while move_int not in valid_moves_ints:
        move_int = input("Enter your selection: ")

    # reverse CELL_DISPLAY dict to get the key from the value - this works
    #  as all kv pairs are unique
    # could probaly just get relevant CELL_DISPLAY.keys()
    coords = dict(zip(CELL_DISPLAY.values(), CELL_DISPLAY.keys()))

    return coords[move_int]

def get_valid_moves(board):
    valid_moves = list()
    for x in range(BOARD_WIDTH):
        for y in range(BOARD_HEIGHT):
            if board[x][y] is None:
                valid_moves.append((x, y))

    return valid_moves

# make a single move, and return the updated board state
# assume coords are correct, validation done elsewhere
def make_move(board, coord, player):
    new_board_state = new_board()
    for i in range(BOARD_HEIGHT):
        for j in range(BOARD_WIDTH):
            new_board_state[i][j] = board[i][j]
    
    x = coord[0]
    y = coord[1]
    if new_board_state[x][y] is None:
        new_board_state[x][y] = player
    else:
        raise Exception("Co-ordinated already used")

    return new_board_state

# very basic ai player that only makes random moves
def make_move_rand_ai(board, player):
    new_board_state = new_board()
    for i in range(BOARD_HEIGHT):
        for j in range(BOARD_WIDTH):
            new_board_state[i][j] = board[i][j]

    # TODO implement get random valid coordinates
    valid_moves = get_valid_moves(board)
    move_coord = random.choice(valid_moves)
    x = move_coord[0]
    y = move_coord[1] 

    if new_board_state[x][y] is None:
        new_board_state[x][y] = player
    else:
        raise Exception("Co-ordinate already used")

    return new_board_state

def check_if_board_full(board):
    for x in range(BOARD_HEIGHT):
        for y in range(BOARD_WIDTH):
            if board[x][y] is None:
                return False
    return True

# play game, alternating between player1 and player2
def play_game(player1, player2):
    # TODO implement
    players = [
        ('X', player1),
        ('O', player2),
    ]

    board = new_board()
    turn_number = 0
    while not check_if_board_full(board):
        current_player_symbol, current_player = players[turn_number % 2]
        print("Current player: ", current_player)
        render(board)

        if current_player == 'Human':
            move = get_move(board)
            board = make_move(board, move, current_player_symbol)
        else:
            board = make_move_rand_ai(board, current_player_symbol)
        render(board)

        if get_winner(board):
            return current_player

        turn_number += 1

    return 'Draw'

# returns the winning player
# if no winner return None
def get_winner(board):
    # TODO implement properly, cheated
    # list of all lines, if a line has 3 of same type, return player
    all_line_coords = get_all_coords()

    for line in all_line_coords:
        line_values = [board[x][y] for (x, y) in line]
        if len(set(line_values)) == 1 and line_values[0] is not None:
            return line_values[0]

    return None
    
def get_all_coords():
    all_line_coords = list()

    for x in range(BOARD_WIDTH):
        column = list()
        for y in range(BOARD_HEIGHT):
            column.append((x, y))
        all_line_coords.append(column)

    for y in range(BOARD_HEIGHT):
        row = list()
        for x in range(BOARD_WIDTH):
            row.append((x, y))
        all_line_coords.append(row)

    # diagonal
    all_line_coords.append([(0, 0), (1, 1), (2, 2)])
    all_line_coords.append([(0, 2), (1, 1), (2, 0)])
    
    return all_line_coords

if __name__ == "__main__":
    player1 = 'Human'
    player2 = 'AI'

    winner = play_game(player1, player2)
    print(winner)