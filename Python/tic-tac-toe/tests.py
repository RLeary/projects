from tic_tac_toe import get_winner

# Test get_winner function
if __name__ == "__main__":
    #diagonal win
    board_1 = [
        ['X', 'X', None],
        ['O', 'X', 'O'],
        ['O', 'O', 'X']
    ]

    assert get_winner(board_1) == 'X'

    # horizontal win
    board_2 = [
        ['X', 'X', 'X'],
        ['O', 'X', 'O'],
        ['O', 'O', None]
    ]

    assert get_winner(board_2) == 'X'

    # vertical win
    board_3 = [
        ['O', 'X', 'X'],
        ['O', 'X', 'O'],
        ['O', 'O', 'X']
    ]

    assert get_winner(board_3) == 'O'

    # game in progress, no winner
    board_4 = [
        ['X', 'X', None],
        ['O', 'X', 'O'],
        ['O', 'O', None]
    ]

    assert get_winner(board_4) == None

    # board empty
    board_5 = [
        [None, None, None],
        [None, None, None],
        [None, None, None]
    ]

    assert get_winner(board_5) == 'None'

    # board full, draw
    board_1 = [
        ['X', 'X', 'O'],
        ['O', 'X', 'O'],
        ['O', 'O', 'X']
    ]

    assert get_winner(board_1) == 'O'
