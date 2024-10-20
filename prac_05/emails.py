"""
CP1404 - prac_05 - Florian N Eisen
Program to store email input and extract user's name
Estimated: 30 mins
Actual: 46 mins
"""


def main():
    email_filing_cabinet = {}
    email = input("Email: ")
    while email != "":
        name_extracted = extract_name(email)
        print(f"Is your name: {name_extracted}? (Y/n)")
        if input().upper() not in ["Y", ""]:
            name_extracted = input("Name: ")
        email_filing_cabinet[email] = name_extracted
        email = input("Email: ")
    for key, value in email_filing_cabinet.items():
        print(f"{value} ({key})")


def extract_name(email_input):
    name_extracted = email_input.split("@")[0]
    name_extracted = name_extracted.split(".")
    name_extracted = " ".join(name_extracted).title()
    return name_extracted


main()
