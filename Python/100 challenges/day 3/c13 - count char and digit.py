# Write a program that accepts a sentence and calculate the number of letters
# and digits.
# 
# Suppose the following input is supplied to the program:
# 
# hello world! 123
# Then, the output should be:
# 
# LETTERS 10
# DIGITS 3

letter_count = 0
digit_count = 0

input_string = input("Enter a string to count chars and digits: ")

#for i in range(len(input_string)):
#    if input_string[i].isnumeric():
#        digit_count += 1
#    elif input_string[i].isalpha():
#        letter_count += 1
for i in input_string:
    if i.isnumeric():
        digit_count += 1
    elif i.isalpha():
        letter_count += 1

print("Letter count: ", letter_count)
print("Digit count: ", digit_count)

# Given solutions
"""
word = input()
letter,digit = 0,0

for i in word:
    if ('a'<=i and i<='z') or ('A'<=i and i<='Z'):
        letter+=1
    if '0'<=i and i<='9':
        digit+=1

print("LETTERS {0}\nDIGITS {1}".format(letter,digit))
# OR

word = input()
letter,digit = 0,0

for i in word:
    letter+=i.isalpha()         # returns True if alphabet
    digit+=i.isnumeric()        # returns True if numeric

print("LETTERS %d\nDIGITS %d"%(letter,digit))       # two different types of formating method is shown in both solution
"""