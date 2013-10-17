"""
A simple and naive paydown calculator I bashed out to get a sense of
which balances I should pay down first.
"""


def print_paydown(balance, apr, monthly_payment):
    monthly_rate = apr / 12.0
    month_counter = 0
    interest_total = 0.0
    monthly_statement = ("Month: %d, "
                         "Interest this month: %.2f, "
                         "Starting balance: %.2f, "
                         "Ending balance: %.2f")
    while balance > monthly_payment:
        this_month_interest = balance * monthly_rate
        interest_total += this_month_interest
        starting_balance = balance
        ending_balance = balance + this_month_interest - monthly_payment
        print monthly_statement % (month_counter,
                                   this_month_interest,
                                   starting_balance,
                                   ending_balance)
        balance = ending_balance
        month_counter += 1
    print ("Final month paying: %d, "
           "final_payment: %.2f, "
           "total interest paid: %.2f" % (month_counter,
                                          balance * (1 + monthly_rate),
                                          interest_total))
