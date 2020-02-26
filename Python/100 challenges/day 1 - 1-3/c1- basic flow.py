# Write a program which will find all such numbers which are divisible by 7
# but are not a multiple of 5, between 2000 and 3200 (both included).The
# numbers obtained should be printed in a comma-separated sequence on a
# single line.

LOWER_RANGE_LIMIT = 2000
UPPER_RANGE_LIMIT = 3200
numbers_list = list()

for i in range(LOWER_RANGE_LIMIT, UPPER_RANGE_LIMIT):
    if (i % 7 == 0) and not (i % 5 == 0):
        numbers_list.append(i)

print(", ".join(str(x) for x in numbers_list))

# given solution:
"""
for i in range(2000,3201):
    if i%7 == 0 and i%5!=0:
        print(i,end=',')
print("\b")
"""
