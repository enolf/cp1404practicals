"""
CP1404 - prac_03 - Florian N Eisen
Program to handle file reading and writing
"""

# Ask for name and write into name.txt
name_file = open("name.txt", 'w')
name = input("Enter your name: ")
name_file.write(name)
name_file.close()

# Read and print contents of name.txt
name_file = open("name.txt", 'r')
print(f"Hi {name_file.read()}")
name_file.close()

# Add numbers in line 1 ad from numbers.txt
with open("numbers.txt", 'r') as number_file:
    number_1 = int(number_file.readline())
    number_2 = int(number_file.readline())
    print(number_1 + number_2)

# Summation of all lines from numbers.txt
numbers_sum = 0
with open("numbers.txt", 'r') as number_file:
    for line in number_file:
        numbers_sum += int(line)
    print(numbers_sum)
