"""
CP1404/CP5632 - Practical - Florian N Eisen
Warming up to lists in python
"""

numbers = [3, 1, 4, 1, 5, 9, 2]

"""
numbers[0]?: 3
numbers[-1]?: 2
numbers[3]?: 1
numbers[:-1]?: 2, 9, 5, 1, 4, 1, 3 (3, 1, 4, 1, 5, 9)
numbers[3:4]?: 1, 5 (1)
5 in numbers?: 9 (True)
7 in numbers?: 'does not exist' (False)
"3" in numbers?: valueError (False)
numbers + [6, 5, 3]?: 9, 6, 7, 1, 5, 9, 2 ([3, 1, 4, 1, 5, 9, 2, 6, 5, 3])
"""

numbers[0] = "ten"
numbers[-1] = 1
print(numbers[2:])
print(9 in numbers)
