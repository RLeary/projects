# Write a program which can map() and filter() to make a list whose elements
# are square of even number in [1,2,3,4,5,6,7,8,9,10].
#

# Hints:
# Use map() to generate a list.Use filter() to filter elements of a list.Use
# lambda to define anonymous functions.

numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers_map = map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers_list))
print(list(even_numbers_map))

# Given solutions
"""
li = [1,2,3,4,5,6,7,8,9,10]
evenNumbers = map(lambda x: x**2, filter(lambda x: x%2==0, li))
print(evenNumbers)

# OR

def even(x):
    return x%2==0

def squer(x):
    return x*x

li = [1,2,3,4,5,6,7,8,9,10]
li = map(squer,filter(even,li))   # first filters number by even number and the apply map() on the resultant elements
print(list(li))

"""
