# Define a function which can generate a dictionary where the keys are numbers
# between 1 and 20 (both included) and the values are square of keys. The
# function should just print the keys only.
#
# Hints:
# Use dict[key]=value pattern to put entry into a dictionary.Use ** operator to
# get power of a number.Use range() for loops.Use keys() to iterate keys in the
# dictionary. Also we can use item() to get key/value pairs.

LOWER_LIMIT = 1
UPPER_LIMIT = 21


def print_keys_square_dict():
    sqaure_dict = {i: i ** 2 for i in range(LOWER_LIMIT, UPPER_LIMIT)}
    print(sqaure_dict.keys())


print_keys_square_dict()

# given solution
"""
def printDict():
    dict = {i: i**2 for i in range(1, 21)}
    print(dict.keys())      # print keys of a dictionary

printDict()
"""
