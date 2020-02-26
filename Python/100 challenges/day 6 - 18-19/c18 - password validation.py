# A website requires the users to input username and password to register.
# Write a program to check the validity of password input by users.
#
# Following are the criteria for checking the password:
#
# At least 1 letter between [a-z]
# At least 1 number between [0-9]
# At least 1 letter between [A-Z]
# At least 1 character from [$#@]
# Minimum length of transaction password: 6
# Maximum length of transaction password: 12
# Your program should accept a sequence of comma separated passwords and will
# check them according to the above criteria. Passwords that match the criteria
# are to be printed, each separated by a comma.
#
# Example
#
# If the following passwords are given as input to the program:
#
# ABd1234@1,a F1#,2w3E*,2We3345
# Then, the output of the program should be:

# ABd1234@1

import re

MIN_LENGTH = 6
MAX_LENGTH = 12

passwords_input = input("Enter a list of comma separated passwords: ").split(",")
valid_passwords = list()

# TODO for each password in list, validate
for password in passwords_input:
    if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        continue
    else:
        pass
    # this is matching '2We3345', not excluding by @#$
    # this is passing anything in valid length with aiether a lowercase, an
    # uppercase, a number, or a $,#,@
    # if re.search(r'[A-Za-z0-9$#@]', password):
    #    valid_passwords.append(password)
    # else:
    #    pass
    if not re.search(r"[A-Z]", password):
        continue
    elif not re.search(r"[a-z]", password):
        continue
    elif not re.search(r"[0-9]", password):
        continue
    elif not re.search(r"[$#@]", password):
        continue
    else:
        pass

    valid_passwords.append(password)

print(valid_passwords)


# Given soltions
"""
def is_low(x):                  # Returns True  if the string has a lowercase
    for i in x:
        if 'a'<=i and i<='z':
            return True
    return  False

def is_up(x):                   # Returns True  if the string has a uppercase
    for i in x:
        if 'A'<= i and i<='Z':
            return True
    return  False

def is_num(x):                  # Returns True  if the string has a numeric digit
    for i in x:
        if '0'<=i and i<='9':
            return True
    return  False

def is_other(x):                # Returns True if the string has any "$#@"
    for i in x:
        if i=='$' or i=='#' or i=='@':
            return True
    return False

s = input().split(',')            
lst = []

for i in s:
    length = len(i)
    if 6 <= length and length <= 12 and is_low(i) and is_up(i) and is_num(i) and is_other(i):   #Checks if all the requirments are fulfilled
        lst.append(i)

print(",".join(lst))

# OR

def check(x):
    cnt = (6<=len(x) and len(x)<=12)
    for i in x:
        if i.isupper():
            cnt+=1
            break
    for i in x:
        if i.islower():
            cnt+=1
            break
    for i in x:
        if i.isnumeric():
            cnt+=1
            break
    for i in x:
        if i=='@' or i=='#'or i=='$':
            cnt+=1
            break
    return cnt == 5               # counting if total 5 all conditions are fulfilled then returns True

s = input().split(',')
lst = filter(check,s)             # Filter function pick the words from s, those returns True by check() function
print(",".join(lst))

# OR

import  re

s = input().split(',')
lst = []

for i in s:
    cnt = 0
    cnt+=(6<=len(i) and len(i)<=12)
    cnt+=bool(re.search("[a-z]",i))      # here re module includes a function re.search() which returns the object information
    cnt+=bool(re.search("[A-Z]",i))      # of where the pattern string i is matched with any of the [a-z]/[A-z]/[0=9]/[@#$] characters
    cnt+=bool(re.search("[0-9]",i))      # if not a single match found then returns NONE which converts to False in boolean
    cnt+=bool(re.search("[@#$]",i))      # expression otherwise True if found any.
    if cnt == 5:
        lst.append(i)

print(",".join(lst))
"""
