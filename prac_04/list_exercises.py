"""
CP1404/CP5632 - Practical - Florian N Eisen
Exercise on using lists in python
"""

numbers = []
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

print("Please input 5 numbers to recieve some info about them")
for i in range(1, 6):
    numbers.append(int(input(f'Enter number {i}: ')))
print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average of the numbers is {(sum(numbers))/len(numbers)}")

user_input = input("\nPlease enter your username: ")
if user_input in usernames:
    print("Access Granted")
else:
    print("Access Denied")
