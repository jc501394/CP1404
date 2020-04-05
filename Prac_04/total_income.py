"""
CP1404/CP5632 Practical - Suggested Solution
Cumulative total income program
"""

def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    months = int(input("How many months? "))

    for months in range(1, months + 1):
        income = float(input("Enter income for month {}: ".format(months)))
        incomes.append(income)

    print_report(incomes)

def print_report(incomes):

    print("\nIncome Report\n-------------")

    total = 0
    for month, incomes in enumerate(incomes):
        total += incomes
        print("Month {:2} - Income: ${:10.2f} \ "
              "Total: ${:10.2f}".format(month + 1, incomes, total))

    """Print report based on incomes."""
    # Note that we do not need to pass in number_of_months
    # because we know the length of the incomes list

main()