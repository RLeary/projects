# With a given integral number n, write a program to generate a dictionary
# that contains (i, i x i) such that is an integral number between 1 and n
# (both included). and then the program should print the dictionary.Suppose the
#  following input is supplied to the program: 8
# Then, the output should be:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

input_number = int(input("Enter an integer: "))
square_dict = dict()
for i in range(1, input_number + 1):
    square_dict[i] = i * i
print(square_dict)


# Or use dictionary comprehension
input_number_2 = int(input("Enter an integer: "))
square_dict_2 = {i: i * i for i in range(1, input_number_2 + 1)}
print(square_dict_2)
