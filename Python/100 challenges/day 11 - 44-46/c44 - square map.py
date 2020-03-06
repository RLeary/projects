# Write a program which can map() to make a list whose elements are square of
# numbers between 1 and 20 (both included).

LOWER_LIMIT = 1
UPPER_LIMIT = 21

square_numbers = map(lambda x: x ** 2, range(1, 21))
print(list(square_numbers))

# Given solution
"""
def sqr(x):
    return x*x

squaredNumbers = list(map(sqr, range(1,21)))
print (squaredNumbers)
"""
