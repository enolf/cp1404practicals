"""
CP1404 Sandbox | password_stars.py | Florian N Eisen
program to detect password
"""


def main():
    password = get_password()

    while len(password) < 4:
        password = input("\nTry again, must be 4 characters: \n")
    print_asterisks(password)


def print_asterisks(password):
    print("Password secured as: ", '*' * len(password))


def get_password():
    password = input("Enter your minimum 4 character long password: \n")
    return password


main()
