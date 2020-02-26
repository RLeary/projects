# Write a program that accepts a sentence and calculate the number of upper
# case letters and lower case letters.
#
# Suppose the following input is supplied to the program:
#
# Hello world!
# Then, the output should be:
#
# UPPER CASE 1
# LOWER CASE 9

upper_count = 0
lower_count = 0

input_string = input("Enter a string to count chars and digits: ")

for i in input_string:
    if i.isupper():
        upper_count += 1
    elif i.islower:
        lower_count += 1

print("Uppercase count: ", upper_count)
print("Lowercase count: ", lower_count)

# Given solutions
"""
word = input()
upper,lower = 0,0

for i in word:
    if 'a'<=i and i<='z' :
        lower+=1
    if 'A'<=i and i<='Z':
        upper+=1

print("UPPER CASE {0}\nLOWER CASE {1}".format(upper,lower))
# OR

word = input()
upper,lower = 0,0

for i in word:
        lower+=i.islower()
        upper+=i.isupper()

print("UPPER CASE {0}\nLOWER CASE {1}".format(upper,lower))
# OR

word = input()
upper = sum(1 for i in word if i.isupper())           # sum function cumulatively sum up 1's if the condition is True
lower = sum(1 for i in word if i.islower())

print("UPPER CASE {0}\nLOWER CASE {1}".format(upper,lower))
# OR

# solution by Amitewu

string = input("Enter the sentense")
upper = 0
lower = 0
for x in string:
    if x.isupper() == True:
        upper += 1
    if x.islower() == True:
        lower += 1

print("UPPER CASE: ", upper)
print("LOWER CASE: ", lower)
"""
