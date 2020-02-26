# Write a program that accepts a comma separated sequence of words as input
# and prints the words in a comma-separated sequence after sorting them
# alphabetically.
#
# Suppose the following input is supplied to the program:
#
# without,hello,bag,world
# Then, the output should be:
#
# bag,hello,without,world

input_words_list = input("Enter a sequence of comma separated words: ").split(",")
sorted_words_list = sorted(input_words_list)

print(",".join(sorted_words_list))

# given solution, difference between these is sort() modifies a list, sorted()
#  creates a new list
"""
lst = input().split(',')
lst.sort()
print(",".join(lst))
"""
