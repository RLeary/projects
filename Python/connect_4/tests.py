# unit testing not done properly here
# should be import unittest, each test is class testxxx(unittest.TestCase)
# each test its own funtion, eg class test_if_baord_full(unittest.TestCase):
# def test_full(self):... def test_empty(self)....
# TODO do above ^^
from c4 import new_board, check_if_board_full, check_if_column_full, get_move, make_move ,get_valid_columns, get_drop_row_index

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
        [None, None, None, None, None, 'O'],
        [None, None, None, 'O', 'O', 'O'],
        [None, 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O']
    ]

    assert check_if_board_full(empty_board_check_full) == False
    assert check_if_board_full(full_board_check_full) == True
    assert check_if_board_full(part_full_board_check_full) == False

# Test check_if_column_full()
    board_check_column_full = [
        [None, None, None, None, None, None],
        [None, None, None, None, None, None],
        [None, None, None, None, None, None],
        [None, None, None, None, None, 'O'],
        [None, None, None, 'O', 'O', 'O'],
        [None, 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O']
    ]

    assert check_if_column_full(board_check_column_full[0]) == False
    assert check_if_column_full(board_check_column_full[5]) == False
    assert check_if_column_full(board_check_column_full[6]) == True

# Test get_valid_columns()
    # TODO implement\
    board_get_valid_cols_1 = [
        [None, None, None, None, None, None],
        ['O', 'O', 'O', 'O', 'O', 'O'],
        [None, None, None, None, None, None],
        [None, None, None, None, None, 'O'],
        [None, None, None, 'O', 'O', 'O'],
        [None, 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O']
    ]
    
    board_get_valid_cols_2 = [
        ['O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O']
    ]
    
    board_get_valid_cols_3 = [
        [None, None, None, None, None, None],
        [None, None, None, None, None, None],
        [None, None, None, None, None, None],
        [None, None, None, None, None, None],
        [None, None, None, None, None, None],
        [None, None, None, None, None, None],
        [None, None, None, None, None, None],
    ]

    valid_cols_list_1 = [0, 2, 3, 4, 5]
    valid_cols_list_2 = []
    valid_cols_list_3 = [0, 1, 2, 3, 4, 5, 6]

    assert get_valid_columns(board_get_valid_cols_1) == valid_cols_list_1
    assert get_valid_columns(board_get_valid_cols_2) == valid_cols_list_2
    assert get_valid_columns(board_get_valid_cols_3) == valid_cols_list_3

# Test get_drop_row_index()
    # TODO implement
    empty_col = [None, None, None, None, None, None]
    two_in_col = [None, None, None, None, 'O', 'O']
    five_in_col = [None, 'O', 'O', 'O', 'O', 'O']

    assert get_drop_row_index(empty_col) == 5
    assert get_drop_row_index(two_in_col) == 3
    assert get_drop_row_index(five_in_col) == 0


# Test make_move()
    # TODO implement


# Test get_move()
    # TODO once unit tests are all in TestCase classes:
    # TODO mock the user input in get_move()
    board_get_move = [
        [None, None, None, None, None, None],
        [None, None, None, None, None, None],
        [None, None, None, None, None, None],
        [None, None, None, None, None, 'O'],
        [None, None, None, 'O', 'O', 'O'],
        [None, 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O']
    ]

    #move = get_move(board)
