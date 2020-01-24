from c4 import new_board, check_if_board_full

if __name__ == "__main__":

# Test new_board()
    expected_new_board = [
        [None, None, None, None, None, None],
        [None, None, None, None, None, None],
        [None, None, None, None, None, None],
        [None, None, None, None, None, None],
        [None, None, None, None, None, None],
        [None, None, None, None, None, None],
        [None, None, None, None, None, None]
    ]
    new_board = new_board()

    assert new_board == expected_new_board

# test check_if_board_full()
    empty_board_check_full = [
        [None, None, None, None, None, None],
        [None, None, None, None, None, None],
        [None, None, None, None, None, None],
        [None, None, None, None, None, None],
        [None, None, None, None, None, None],
        [None, None, None, None, None, None],
        [None, None, None, None, None, None]
    ]
    full_board_check_full = [
        ['O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O'],
    ]
    part_full_board_check_full = [
        [None, None, None, None, None, None],
        [None, None, None, None, None, None],
        [None, None, None, None, None, None],
        [None, None, None, None, None, None],
        [None, None, None, 'O', None, None],
        [None, 'O', None, 'O', None, None],
        ['O', 'O', 'O', 'O', None, None]
    ]

    assert check_if_board_full(empty_board_check_full) == False
    assert check_if_board_full(full_board_check_full) == True
    assert check_if_board_full(part_full_board_check_full) == False