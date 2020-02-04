from c4 import new_board, render, BOARD_WIDTH, BOARD_HEIGHT

b1 = new_board()
b1[3][5] = 'O'
b1[3][3] = 'O'
b1[3][0] = 'O'
b1[3][4] = 'O'
b1[1][1] = 'O'
b1[1][4] = 'O'
b1[4][3] = 'O'
b1[5][1] = 'X'
b1[0][0] = 'X'
#render(b1)

b2 = new_board()
b2[0][0] = 'X'
b2[0][1] = 'O'
b2[0][2] = 'O'
b2[0][0] = 'X'
b2[1][3] = 'O'
b2[2][3] = 'X'
b2[3][3] = 'X'
b2[4][3] = 'X'
b2[5][3] = 'X'

b3 = new_board()
b3[0][1] = 'X'
b3[1][2] = 'X'
b3[2][3] = 'X'
b3[3][r] = 'X'

def get_winner_vertical(board):
    x_values = [0, 1, 2, 3]
    for y in range(BOARD_WIDTH):
        # three possible sets for a vertical 4

        zero_start_x_list = list()
        one_start_x_list = list()
        two_start_x_list = list()

        zero_start_x_list.append(board[y][0])
        zero_start_x_list.append(board[y][1])
        zero_start_x_list.append(board[y][2])
        zero_start_x_list.append(board[y][3])
        one_start_x_list.append(board[y][1])
        one_start_x_list.append(board[y][2])
        one_start_x_list.append(board[y][3])
        one_start_x_list.append(board[y][4])
        two_start_x_list.append(board[y][2])
        two_start_x_list.append(board[y][3])
        two_start_x_list.append(board[y][4])
        two_start_x_list.append(board[y][5])

        if len(set(zero_start_x_list)) == 1 and zero_start_x_list[0] is not None:
            return True
        elif len(set(one_start_x_list)) == 1 and one_start_x_list[0] is not None:
            return True
        elif len(set(two_start_x_list)) == 1 and two_start_x_list[0] is not None:
            return True
    return False

def get_winner_horizontal(board):
    # opposite of vertical, for x in height, change y
    # four sets
    for x in range(BOARD_HEIGHT):
        zero_start_y_list = list()
        one_start_y_list = list()
        two_start_y_list = list()
        three_start_y_list = list()

        zero_start_y_list.append(board[0][x])
        zero_start_y_list.append(board[1][x])
        zero_start_y_list.append(board[2][x])
        zero_start_y_list.append(board[3][x])
        one_start_y_list.append(board[1][x])
        one_start_y_list.append(board[2][x])
        one_start_y_list.append(board[3][x])
        one_start_y_list.append(board[4][x])
        two_start_y_list.append(board[2][x])
        two_start_y_list.append(board[3][x])
        two_start_y_list.append(board[4][x])
        two_start_y_list.append(board[5][x])
        three_start_y_list.append(board[3][x])
        three_start_y_list.append(board[4][x])
        three_start_y_list.append(board[5][x])
        three_start_y_list.append(board[6][x])

        if len(set(zero_start_y_list)) == 1 and zero_start_y_list[0] is not None:
            return True
        elif len(set(one_start_y_list)) == 1 and one_start_y_list[0] is not None:
            return True
        elif len(set(two_start_y_list)) == 1 and two_start_y_list[0] is not None:
            print('two')
            return True
        elif len(set(three_start_y_list)) == 1 and three_start_y_list[0] is not None:
            return True
    return False

def get_winner_diagonal(board):
    lines = list()

    for i in no_of_dia
    line.append(board[y][x])
    ...
    ...
    lines.append(line)

    for line in lines:
        if len(set(line)) == 1 and line[0] is not None:
            return True

    return False


print(get_winner_vertical(b1))
print(get_winner_horizontal(b2))
print(get_winner_diagonal(b3))