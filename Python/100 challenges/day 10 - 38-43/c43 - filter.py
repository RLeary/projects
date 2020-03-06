# Write a program which can filter() to make a list whose elements are even
# number between 1 and 20 (both included).

LOWER_LIMIT = 1
UPPER_LIMIT = 21

even_numbers = filter(lambda x: x % 2 == 0, range(LOWER_LIMIT, UPPER_LIMIT))
print(list(even_numbers))

# Given solutions
"""
evenNumbers = filter(lambda x: x%2==0, range(1,21))
print(evenNumbers)

# OR

def even(x):
    return x%2==0

evenNumbers = filter(even, range(1,21))
print(list(evenNumbers))
"""
