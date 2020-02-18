# Write a program that calculates and prints the value according to the given 
# formula:
# 
# Q = Square root of [(2 * C * D)/H]
# 
# Following are the fixed values of C and H:
# 
# C is 50. H is 30.
#
# D is the variable whose values should be input to your program in a 
# comma-separated sequence.For example Let us assume the following comma 
# separated input sequence is given to the program:
#
# 100,150,180
# The output of the program should be:
# 18,22,24

# Hints:
# If the output received is in decimal form, it should be rounded off to its 
# nearest value (for example, if the output received is 26.0, it should be 
# printed as 26).In case of input data being supplied to the question, it 
# should be assumed to be a console input.

from math import sqrt

C = 50
H = 30

d_ints = [int(i) for i in 
    input("Enter a comma separated list of integers: ").split(',')]

q_list = list()

for i in range(len(d_ints)):
    q = sqrt((2 * C * float(d_ints[i])) / H)
    q_list.append(int(q))

q_list_str = [str(i) for i in q_list]
print(','.join(q_list_str))

# Given solution:
"""
from math import * # importing all math functions

C,H = 50,30

def calc(D):
    return sqrt((2*C*D)/H)

D = input().split(',')    # splits in comma position and set up in list
D = [int(i) for i in D]   # converts string to integer
D = [calc(i) for i in D]  # returns floating value by calc method for every item in D
D = [round(i) for i in D] # All the floating values are rounded
D = [str(i) for i in D]   # All the integers are converted to string to be able to apply join operation

print(",".join(D))
"""