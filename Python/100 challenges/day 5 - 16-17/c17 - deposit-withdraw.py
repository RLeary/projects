# Write a program that computes the net amount of a bank account based a
# transaction log from console input. The transaction log format is shown as
# following:
#
# D 100
# W 200
# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:
#
# D 300
# D 300
# W 200
# D 100
# Then, the output should be:
#
# 500
balance = 0

while True:
    input_command = input("Enter D or W followed by space, then the value: ").split(" ")
    if len(input_command) > 2:
        print("Invalid command, exiting")
        break
    if input_command[0] == "D" or "d":
        balance += int(input_command[1])
    elif input_command[0] == "W" or "w":
        balance -= int(input_command[1])
    else:
        print("invalid input, exiting")
        break
print(balance)

# given solutions
"""
total = 0
while True:
    s = input().split()
    if not s:            # break if the string is empty
        break
    cm,num = map(str,s)    # two inputs are distributed in cm and num in string data type

    if cm=='D':
        total+=int(num)
    if cm=='W':
        total-=int(num)

print(total)

'''Solution by: leonedott'''

lst = []
while True:
  x = input()
  if len(x)==0:
    break
  lst.append(x)

balance = 0
for item in lst:
  if 'D' in item:
    balance += int(item.strip('D '))
  if 'W' in item:
    balance -= int(item.strip('W '))
print(balance)

'''Solution by: AlexanderSro'''

account = 0
while True:
    action = input("Deposit/Whitdrow/Balance/Quit? D/W/B/Q: ").lower()
    if action == "d":
        deposit = input("How much would you like to deposit? ")
        account = account + int(deposit)
    elif action == "w":
        withdrow = input("How much would you like to withdrow? ")
        account = account - int(withdrow)
    elif action == "b":
        print(account)
    else:
        quit()
"""
