# You are required to write a program to sort the (name, age, score) tuples by
# ascending order where name is string, age and score are numbers. The tuples 
# are input by console. The sort criteria is:
# 
# 1: Sort based on name
# 2: Then sort based on age
# 3: Then sort by score
# The priority is that name > age > score.
# 
# If the following tuples are given as input to the program:

# Tom,19,80
# John,20,90
# Jony,17,91
# Jony,17,93
# Json,21,85
# Then, the output of the program should be:

# [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), 
# ('Json', '21', '85'), ('Tom', '19', '80')]
# Hints:
# In case of input data being supplied to the question, it should be assumed to
# be a console input.We use itemgetter to enable multiple sort keys.


from operator import itemgetter

# not this, input isJson,21,85\nJson,21,85\nJson,21,85
#tuples_list = input("Enter tuples: ").split(',')
tuples_list = list()

while True:
    string_input = input("Enter tuple: ")
    if not string_input:
        break
    tuples_list.append(tuple(string_input.split(',')))

sorted_tuples_list = sorted(tuples_list, key=itemgetter(0,1,2))
print(sorted_tuples_list)

# given solution
"""
lst = []
while True:
    s = input().split(',')
    if not s[0]:                          # breaks for blank input
        break
    lst.append(tuple(s))

lst.sort(key= lambda x:(x[0],x[1],x[2]))  # here key is defined by lambda and the data is sorted by element priority 0>1>2 in accending order
print(lst)
"""