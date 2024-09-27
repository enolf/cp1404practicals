"""
CP1404 Sandbox | password_stars.py | Florian N Eisen
program to detect password
"""

password = str(input("Enter your minimum 4 character long password: \n"))

while password:
    if len(password) >= 4:
        print("Password secured as: ", '*'*len(password))
        break
    else:
        print("\nInvalid Password, must be 4 character long. Try again: ")
    password = str(input("\nEnter your minimum 4 character long password: \n"))
