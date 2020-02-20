# Write a program that accepts a sequence of whitespace separated words as 
# input and prints the words after removing all duplicate words and sorting 
# them alphanumerically.
# 
# Suppose the following input is supplied to the program:
# 
# hello world and practice makes perfect and hello world again
# Then, the output should be:
# 
# again and hello makes perfect practice world
# Hints:
# In case of input data being supplied to the question, it should be assumed to
# be a console input.We use set container to remove duplicated data 
# automatically and then use sorted() to sort the data.
"""
def remove_duplicate_words(string):
    words = string.split()
    words_list = list()
    
    for word in words:
        if word not in words_list:
            words_list.append(word)
            
    return ' '.join(str(x) for x in words_list)
"""
def remove_duplicate_words(string):
    return ' '.join(sorted(set(string.split()), key = string.index))

input_string = input("Enter a string to remove duplicates and sort: ")
print(remove_duplicate_words(input_string))

# Given solutions
"""
word = input().split()

for i in word:
    if word.count(i) > 1:    #count function returns total repeatation of an element that is send as argument
        word.remove(i)     # removes exactly one element per call

word.sort()
print(" ".join(word))

#OR

word = input().split()
[word.remove(i) for i in word if word.count(i) > 1 ]   # removal operation with comprehension method
word.sort()
print(" ".join(word))

#OR

word = sorted(list(set(input().split())))              #  input string splits -> converting into set() to store unique
                                                       #  element -> converting into list to be able to apply sort 
print(" ".join(word))
"""