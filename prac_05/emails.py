"""
CP1404 - prac_05 - Florian N Eisen
Program to store email input and extract user's name
Estimated: 30 mins
Actual: 46 mins
"""


def main():
    email_filing_cabinet = {}
    email_input = input("Email: ")
    while email_input != "":
        name_extracted = extract_name(email_input)
        print(f"Is your name: {name_extracted}? (Y/n)")
        if input().upper() not in ["Y", ""]:
            name_extracted = input("Name: ")
        email_filing_cabinet[email_input] = name_extracted
        email_input = input("Email: ")
    for key, value in email_filing_cabinet.items():
        print(f"{value} ({key})")


def extract_name(email_input):
    name_extracted = email_input.split("@")[0]
    name_extracted = name_extracted.split(".")
    name_extracted = " ".join(name_extracted).title()
    return name_extracted


main()
