# Write a program which accepts a string as input to print "Yes" if the string
# is "yes" or "YES" or "Yes", otherwise print "No".

input_string = input("Enter a string: ")

if input_string == "yes" or input_string == "YES":
    print("Yes")
else:
    print("No")

# given solutions
"""
'''
Solution by: Seawolf159
'''
text = input("Please type something. --> ")
if text == "yes" or text == "YES" or text == "Yes": 
    print("Yes")
else: 
    print("No")
'''
Solution by: AasaiAlangaram
'''
input = input('Enter string:')
output = ''.join(['Yes' if input == 'yes' or input =='YES' or input =='Yes' else 'No' ])
print(str(output))
"""
