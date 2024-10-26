"""
CP1404/CP5632 - Practical - Florian N Eisen
Program to demonstrate a menu using python loops
"""

name = input("What is your name? ")

menu = """(H)ello
(G)oodbye
(Q)uit"""
print(menu)
action = input(">>>").upper()

while action != 'Q':
    if action == 'H':
        print(f"\nHello {name}\n")

    elif action == 'G':
        print(f"\nGoodbye, {name}\n")
    else:
        print(f"\nSorry {name} that input is invalid, try again\n")
    print(menu)
    action = input(">>>").upper()

print("Thanks for using this program")
