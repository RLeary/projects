# With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first
# half values in one line and the last half values in one line.

given_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
mid_point = int(len(given_tuple) / 2)
print(given_tuple[:mid_point])
print(given_tuple[mid_point:])

# Given solutions
"""
tpl = (1,2,3,4,5,6,7,8,9,10)

for i in range(0,5):
    print(tpl[i],end = ' ')
print()
for i in range(5,10):
    print(tpl[i],end = ' ')

# OR

tpl = (1,2,3,4,5,6,7,8,9,10)
lst1,lst2 = [],[]

for i in range(0,5):
    lst1.append(tpl[i])

for i in range(5,10):
    lst2.append(tpl[i])

print(lst1)
print(lst2)

# OR

'''
Solution by: CoffeeBrakeInc
'''

tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
lt = int(len(tup)/2)
print(tup[:lt], tup[lt:])

# OR

'''
Solution by: AasaiAlangaram
'''

tp = (1,2,3,4,5,6,7,8,9,10)

print('The Original Tuple:',tp)

[print('Splitted List :{List}'.format(List = tp[x:x+5])) for x in range(0,len(tp),5)]
"""
