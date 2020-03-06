# Write a program which can map() to make a list whose elements are square of
# elements in [1,2,3,4,5,6,7,8,9,10].
# Use map() to generate a list.Use lambda to define anonymous functions.

numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squared_numbers_list = map(lambda x: x ** 2, numbers_list)
print(list(squared_numbers_list))

# Given solution
"""
li = [1,2,3,4,5,6,7,8,9,10]
squaredNumbers = map(lambda x: x**2, li)  # returns map type object data
print(list(squaredNumbers))               # converting the object into list
"""
