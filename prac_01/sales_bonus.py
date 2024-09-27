"""
CP1404/CP5632 - Practical - Florian N Eisen
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

sales = float(input("Enter Sales: $"))
bonus = 0

while sales >= 0:
    if sales < 1000:
        bonus = sales*0.1
    else:
        bonus = sales*0.15

    print(f"Bonus to the sale of ${sales} is ${bonus}\n")
    sales = float(input("Enter Sales price or input a negative to exit program: $"))
