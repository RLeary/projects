# Define a function which can generate a list where the values are square of
# numbers between 1 and 20 (both included). Then the function needs to print
# the last 5 elements in the list.
#
# Hints:
# Use ** operator to get power of a number.Use range() for loops.Use
# list.append() to add values into a list.Use [n1:n2] to slice

LOWER_LIMIT = 1
UPPER_LIMIT = 21


def print_square_list_last_five():
    sqaure_list = [i ** 2 for i in range(LOWER_LIMIT, UPPER_LIMIT)]
    print(sqaure_list[-5:])


print_square_list_last_five()

# Given solutions
"""
def printList():
	li=list()
	for i in range(1,21):
		li.append(i**2)
	print(li[-5:])
		
printList()

# OR

def printList():
    lst = [i ** 2 for i in range(1, 21)]
    for i in range(19,14,-1):
        print(lst[i])

printList()
"""
