from tic_tac_toe import get_valid_moves, new_board, get_winner

if __name__ == "__main__":
    # Test get_valid_moves() function
    # empty board, all moves valid
    empty_board = new_board()

    full_board = [["X", "X", "O"], ["O", "O", "X"], ["X", "O", "X"]]

    test_board = [["X", None, None], ["O", "X", None], [None, None, "O"]]

    test_board_moves = [(0, 1), (0, 2), (1, 2), (2, 0), (2, 1)]

    all_moves = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

    no_moves = list()

    assert get_valid_moves(empty_board) == all_moves
    assert get_valid_moves(full_board) == no_moves
    assert get_valid_moves(test_board) == test_board_moves

    # Test get_winner() function
    # diagonal win
    board_1 = [["X", "X", None], ["O", "X", "O"], ["O", "O", "X"]]

    assert get_winner(board_1) == "X"

    # horizontal win
    board_2 = [["X", "X", "X"], ["O", "X", "O"], ["O", "O", None]]

    assert get_winner(board_2) == "X"

    # vertical win
    board_3 = [["O", "X", "X"], ["O", "X", "O"], ["O", "O", "X"]]

    assert get_winner(board_3) == "O"

    # game in progress, no winner
    board_4 = [["X", "X", None], ["O", "X", "O"], ["O", "O", None]]

    assert get_winner(board_4) == None

    # board empty
    board_5 = [[None, None, None], [None, None, None], [None, None, None]]

    assert get_winner(board_5) == None

    # board full, draw
    board_1 = [["X", "X", "O"], ["O", "O", "X"], ["X", "O", "X"]]

    assert get_winner(board_1) == None
