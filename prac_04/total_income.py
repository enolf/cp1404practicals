"""
CP1404/CP5632 - Practical - Florian N Eisen
A program to calculate the cumulative income of the user
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    count_of_months = int(input("How many months? "))

    get_income(count_of_months, incomes)

    print_income_report(count_of_months, incomes)


def get_income(count_of_months, incomes):
    for month in range(1, count_of_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)


def print_income_report(count_of_months, incomes):
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, count_of_months + 1):
        income = incomes[month - 1]
        total += income
        print(f"Month {month:2} - Income: ${income:10.2f} Total: ${total:10.2f}")


main()
