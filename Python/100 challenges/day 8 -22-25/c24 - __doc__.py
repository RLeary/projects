# Python has many built-in functions, and if you do not know how to use it, you
# can read document online or find some books. But Python has a built-in document
# function for every built-in functions.
#
# Please write a program to print some Python built-in functions documents,
# such as abs(), int(), raw_input()
#
# And add document for your own function
#
# Hints:
# The built-in document method is __doc__


print(str.__doc__)
print(int.__doc__)
print(abs.__doc__)


def foo(bar):
    """
    Docstring for foo()
    This function does nothing
    """
    pass


print(foo.__doc__)

# given solution
"""
print(str.__doc__)
print(sorted.__doc__)

def pow(n,p):
    '''
    param n: This is any integer number
    param p: This is power over n
    return:  n to the power p = n^p
    '''

    return n**p

print(pow(3,4))
print(pow.__doc__)
"""
