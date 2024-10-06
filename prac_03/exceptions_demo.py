"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur? non-integers, i.e. anything that is not a whole number
2. When will a ZeroDivisionError occur? when the denominator equals 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator, must not equal zero: "))
    while denominator == 0:  # when input equals 0, query user to use a different input until != 0
        denominator = int(input("The denominator must not equal zero, try again: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
