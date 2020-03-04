# Write a program to generate and print another tuple whose values are even
# numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).
#
# Hints:
# Use "for" to iterate the tuple. Use tuple() to generate a tuple from a list.


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


given_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
even_list = list()

for number in given_tuple:
    if is_even(number):
        even_list.append(number)

print(tuple(even_list))

# given solutions
"""
tpl = (1,2,3,4,5,6,7,8,9,10)
tpl1 = tuple(i for i in tpl if i%2 == 0)
print(tpl1)

# OR

tpl = (1,2,3,4,5,6,7,8,9,10)
tpl1 = tuple(filter(lambda x : x%2==0,tpl))  # Lambda function returns True if found even element.
                                             # Filter removes data for which function returns False
print(tpl1)
"""
