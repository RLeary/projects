# Define a function which can print a dictionary where the keys are numbers
# between 1 and 20 (both included) and the values are square of keys.
#
# Hints:
# Use dict[key]=value pattern to put entry into a dictionary.Use ** operator to
# get power of a number.Use range() for loops

LOWER_LIMIT = 1
UPPER_LIMIT = 21


def print_square_dict():
    sqaure_dict = {i: i ** 2 for i in range(LOWER_LIMIT, UPPER_LIMIT)}
    print(sqaure_dict)


print_square_dict()

# given solutions
"""
def printDict():
	d=dict()
	for i in range(1,21):
		d[i]=i**2
	print(d)
		
printDict()

# OR

def printDict():
    dict={i:i**2 for i in range(1,21)}   # Using comprehension method and
    print(dict)

printDict()
"""
