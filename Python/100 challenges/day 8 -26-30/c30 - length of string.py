# Define a function that can accept two strings as input and print the string
# with maximum length in console. If two strings have the same length, then the
# function should print all strings line by line.
#
# Hints:
# Use len() function to get the length of a string.


def print_longest_string(string_one, string_two):
    if len(string_one) > len(string_two):
        print(string_one)
    elif len(string_two) > len(string_one):
        print(string_two)
    else:
        print(string_one)
        print(string_two)


print(print_longest_string("bleep", "boop"))
print(print_longest_string("boop", "bloop"))
print(print_longest_string("foo", "bar"))


# given solutions
"""
def printVal(s1,s2):
    len1 = len(s1)
    len2 = len(s2)
    if len1 > len2:
        print(s1)
    elif len1 < len2:
        print(s2)
    else:
        print(s1)
        print(s2)

s1,s2=input().split()
printVal(s1,s2)
'''Solution by: yuan1z'''
func = lambda a,b: print(max((a,b),key=len)) if len(a)!=len(b) else print(a+'\n'+b)
"""
