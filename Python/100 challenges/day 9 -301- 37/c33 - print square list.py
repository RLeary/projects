# Define a function which can generate and print a list where the values are
# square of numbers between 1 and 20 (both included).
#
# Hints:
# Use ** operator to get power of a number.Use range() for loops. Use
# list.append() to add values into a list.

LOWER_LIMIT = 1
UPPER_LIMIT = 21


def print_square_list():
    sqaure_list = [i ** 2 for i in range(LOWER_LIMIT, UPPER_LIMIT)]
    print(sqaure_list)


print_square_list()

# Given solutions
"""
def printList():
	li=list()
	for i in range(1,21):
		li.append(i**2)
	print(li)
		
printList()

# OR

def printList():
    lst = [i ** 2 for i in range(1, 21)]
    print(lst)

printList()
"""
