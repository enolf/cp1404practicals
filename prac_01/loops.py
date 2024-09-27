"""
CP1404/CP5632 - Practical - Florian N Eisen
Program to print loops
"""
print("a.")
for i in range(0, 101, 10):
    print(i, end=' ')
print("\n")

print("b.")
for i in range(20, 0, -1):
    print(i, end=' ')
print("\n")

print("c.")
n = int(input("Enter the number of stars (*) you want printed, linearly: "))
for n in range(0, n, 1):
    print('*', end='')
print("\n")

print("d.")
n = int(input("Enter the max number of stars (*) you want sequentially printed: "))
for n in range(1, n+1, 1):
    print('*'*n, end='\n')
print("\n")
