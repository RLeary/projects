# Define a function which can generate and print a tuple where the value are
# square of numbers between 1 and 20 (both included).
#
# Hints:
# Use ** operator to get power of a number.Use range() for loops.Use
# list.append() to add values into a list.Use tuple() to get a tuple

LOWER_LIMIT = 1
UPPER_LIMIT = 21


def print_square_tuple():
    sqaure_tuple = tuple([i ** 2 for i in range(LOWER_LIMIT, UPPER_LIMIT)])
    print(sqaure_tuple)


print_square_tuple()

# Given solutions
"""
def printTupple():
    lst = [i ** 2 for i in range(1, 21)]
    print(tuple(lst))

printTupple()
'''
Solution by: Seawolf159
'''
def square_of_numbers():
    return tuple(i ** 2 for i in range(1, 21))

print(square_of_numbers()) 
"""
