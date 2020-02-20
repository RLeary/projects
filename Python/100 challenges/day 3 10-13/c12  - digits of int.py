# Write a program, which will find all such numbers between 1000 and 3000
# (both included) such that each digit of the number is an even number.The 
# numbers obtained should be printed in a comma-separated sequence on a single line.

LOWER_LIMIT = 1000
UPPER_LIMIT = 3001

even_digits_list = list()

for i in range(LOWER_LIMIT, UPPER_LIMIT):
    int_as_string = str(i)
    odd_flag = False
    for j in range(len(int_as_string)):
        if int(int_as_string[j]) % 2 != 0:
            odd_flag = True
    if not odd_flag:
        even_digits_list.append(i)

even_digits_list = [str(i) for i in even_digits_list]
print(','.join(even_digits_list))

# Given solutions
"""
lst = []

for i in range(1000,3001):
    flag = 1
    for j in str(i):          # every integer number i is converted into string
        if ord(j)%2 != 0:     # ord returns ASCII value and j is every digit of i
            flag = 0          # flag becomes zero if any odd digit found
    if flag == 1:
        lst.append(str(i))    # i is stored in list as string

print(",".join(lst))        

# OR

def check(element):
    return all(ord(i)%2 == 0 for i in element)  # all returns True if all digits i is even in element

lst = [str(i) for i in range(1000,3001)]        # creates list of all given numbers with string data type
lst = list(filter(check,lst))                   # filter removes element from list if check condition fails
print(",".join(lst))

# OR

lst = [str(i) for i in range(1000,3001)]
lst = list(filter(lambda i:all(ord(j)%2 == 0 for j in i),lst ))   # using lambda to define function inside filter function
print(",".join(lst))
"""