'''
@author : manojbandari
# Assignment-2 - Paying Debt off in a Year

# Now write a program that calculates the minimum fixed monthly
payment needed in order pay off a credit card balance within 12 months.
# By a fixed monthly payment, we mean a single number which does not
change each month, but instead is a constant amount that will be
# paid each month.

# In this problem, we will not be dealing with a minimum monthly payment rate.

# The following variables contain values as described below:
# balance - the outstanding balance on the credit card
# annualInterestRate - annual interest rate as a decimal

# The program should print out one line: the lowest monthly
payment that will pay off all debt in under 1 year, for example:
# Lowest Payment: 180

# Assume that the interest is compounded monthly according to the balance
at the end of the month (after the payment for that month is
# made).
# The monthly payment must be a multiple of $10 and is the same for all months.
Notice that it is possible for the balance to become
# negative using this payment scheme, which is okay.
A summary of the required math is found below:
# Monthly interest rate = (Annual interest rate) / 12.0
# Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
# Updated balance each month = (Monthly unpaid balance) +
(Monthly interest rate x Monthly unpaid balance)
'''


def paying_debtoffinayear(b_balance, annual_interest_rate, set_min):
    '''
    function to pay debt off in a year
    '''
    if b_balance <= 0:
        minimum_fixed = 0
        return minimum_fixed
    minimum_fixed = 10
    month = 0
    monthly_interest = (annual_interest_rate)/12.0
    while month <= 12:
        month += 1
        monthly_unpaid = b_balance- minimum_fixed
        b_balance = monthly_unpaid + (monthly_interest * monthly_unpaid)
        if monthly_unpaid <= 0 and month == 12:
            return minimum_fixed
        if month == 12 and monthly_unpaid > 0:
            month = 0
            minimum_fixed += 10
            b_balance = set_min
    return b_balance
def main():
    '''
    main function
    '''
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    print("Lowest Payment ",(paying_debtoffinayear(data[0], data[1], data[0])))
    
if __name__ == "__main__":
    main()
