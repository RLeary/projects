from gol import next_board_state, dead_state

# TODO: there's a lot of repeated code here. Can
# you move some of into reusable functions to
# make it shorter and neater?

if __name__ == "__main__":
    # TEST 1 - dead cells with no live neighbours stay dead
    #state_test_1_w = 3
    #state_test_1_h = 3
    #init_state_test_1 = dead_state(state_test_1_w, state_test_1_h)
    #expected_next_state_test_1 = dead_state(state_test_1_w, state_test_1_h)

    init_state_test_1 = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]
    expected_next_state_test_1 = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]

    actual_next_state_test_1 = next_board_state(init_state_test_1)

    if expected_next_state_test_1 == actual_next_state_test_1:
        print("Passed test 1 - dead cells with no neighbours stay dead")
    else:
        print("Failed test 1 - dead cells with no neighbours stay dead")
        print("expected result: ")
        print(expected_next_state_test_1)
        print("actual results: ")
        print(actual_next_state_test_1)

    # TEST 2 - dead cells with 3 neighbours come alive
    init_state_test_2 = [
        [0, 0, 1],
        [0, 1, 1],
        [0, 0, 0]
    ]
    expected_next_state_test_2 = [
        [0, 1, 1],
        [0, 1, 1],
        [0, 0, 0]
    ]

    actual_next_state_test_2 = next_board_state(init_state_test_2)

    if expected_next_state_test_2 == actual_next_state_test_2:
        print("Passed test 2 - dead cells with 3 neighbours come alive")
    else:
        print("Failed test 2 - dead cells with 3 neighbours come alive")
        print("expected result: ")
        print(expected_next_state_test_2)
        print("actual results: ")
        print(actual_next_state_test_2)

    # TEST 3 - Any live cell with 2 or 3 live neighbors stays alive
    init_state_test_3 = [
        [0, 1, 0],
        [1, 0, 1],
        [0, 1, 0]
    ]
    expected_next_state_test_3 = [
        [0, 1, 0],
        [1, 0, 1],
        [0, 1, 0]
    ]

    actual_next_state_test_3 = next_board_state(init_state_test_3)

    if expected_next_state_test_3 == actual_next_state_test_3:
        print("Passed test 3 - live cells with 2 or 2 neighbours stay alive")
    else:
        print("Failed test 3 - live cells with 2 or 2 neighbours stay alive")
        print("expected result: ")
        print(expected_next_state_test_3)
        print("actual results: ")
        print(actual_next_state_test_3)

    # TEST 4 - Any live cell with more than 3 live neighbors dies
    init_state_test_4 = [
        [1, 1, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 1, 1],
        [0, 0, 1, 1]
    ]
    expected_next_state_test_4 = [
        [1, 1, 0, 0],
        [1, 0, 0, 0],
        [0, 0, 0, 1],
        [0, 0, 1, 1]
    ]

    actual_next_state_test_4 = next_board_state(init_state_test_4)

    if expected_next_state_test_4 == actual_next_state_test_4:
        print("Passed test 4 - live cells with >3 neighbours die")
    else:
        print("Failed test 4 - live cells with >3 neighbours die")
        print("expected result: ")
        print(expected_next_state_test_4)
        print("actual results: ")
        print(actual_next_state_test_4)

    # TEST 5 - live cells with 0 or 1 live neighbors dies
    init_state_test_5 = [
        [0, 0, 0, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0],
        [0, 1, 0, 0]
    ]
    expected_next_state_test_5 = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]

    actual_next_state_test_ = next_board_state(init_state_test_5)

    if expected_next_state_test_5 == actual_next_state_test_5:
        print("Passed test 5 - live cells with 0 or 1 neighbours die")
    else:
        print("Failed test 5 - live cells with 0 or 1 neighbours die")
        print("expected result: ")
        print(expected_next_state_test_5)
        print("actual results: ")
        print(actual_next_state_test_5)

# test for corners?, edges?