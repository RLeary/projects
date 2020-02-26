# Use a list comprehension to square each odd number in a list. The list is
# input by a sequence of comma-separated numbers. Suppose the following input
# is supplied to the program:
#
# 1,2,3,4,5,6,7,8,9
# Then, the output should be:
#
# 1,9,25,49,81

input_list = input("Enter a comma separated list of integers: ").split(",")

input_list_ints = [int(i) for i in input_list]

squared_odds = [i * i for i in input_list_ints if i % 2 == 1]

print(squared_odds)

output_list = [str(i) for i in squared_odds]
print(",".join(output_list))

# given solution
"""
lst = [str(int(i)**2) for i in input().split(',') if int(i) % 2]
print(",".join(lst))
"""
