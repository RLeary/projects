# Write a program which can compute the factorial of a given numbers.The
# results should be printed in a comma-separated sequence on a single line
# .Suppose the following input is supplied to the program: 8 Then, the output
#  should be:40320

import time

input_number = int(input("Enter an integer: "))

# recursive
def factorial_recursive(number):
    if number == 1:
        return 1
    else:
        return number * factorial_recursive(number - 1)


# iterative
def factorial_iterative(number):
    result = 1
    for i in range(1, number + 1):
        result = result * i
    return result


recursive_start = time.time()
print(factorial_recursive(input_number))
recursive_end = time.time()
print("Time for recurisve implementation: ", recursive_end - recursive_start)

iterative_start = time.time()
print(factorial_iterative(input_number))
iterative_end = time.time()
print("Time for iterative implementation: ", iterative_end - iterative_start)
