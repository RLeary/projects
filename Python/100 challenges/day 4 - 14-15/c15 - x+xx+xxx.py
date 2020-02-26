# Write a program that computes the value of a+aa+aaa+aaaa with a given digit
# as the value of a.
#
# Suppose the following input is supplied to the program:
#
# 9
# Then, the output should be:
#
# 11106

input_integer = input("Enter an integer: ")

result = (
    int(input_integer)
    + int(2 * input_integer)
    + int(3 * input_integer)
    + int(4 * input_integer)
)

print(result)

# took input as int(input()) - causing 2*input to by 18, not 99

# given solutions
"""
a = input()
total,tmp = 0,str()        # initialing an integer and empty string

for i in range(4):
    tmp+=a               # concatenating 'a' to 'tmp'
    total+=int(tmp)      # converting string type to integer type

print(total)

# OR

a = input()
total = int(a) + int(2*a) + int(3*a) + int(4*a)  # N*a=Na, for example  a="23", 2*a="2323",3*a="232323"
print(total)
"""
