"""
Name: Oliver Aschenbrenner
interest.py

Problem: Calculate and output the monthly interest charge

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def main():
    # input annual interest rate
    annual_interest_rate = eval(input("Enter the annual interest rate in percent form: "))
    # input the number of days in the billing cycle
    billing_cycle = eval(input("Enter the number of days in the billing cycle: "))
    # input the previous net balance
    previous_balance = eval(input("Enter the previous net balance: "))
    # input the payment
    payment = eval(input("Enter the payment amount: "))
    # input the day of payment
    day_of_payment = eval(input("Enter the day the payment was made: "))
    # multiply previous balance by the days in the billing cycle
    step_one = previous_balance * billing_cycle
    # multiply the payment by the (number of days in the billing cycle - the day of the payment)
    step_two = payment * (billing_cycle - day_of_payment)
    # subtract the product of step two from step one
    step_three = step_one - step_two
    # divide step three by the number of days in the billing cycle
    step_four = step_three / billing_cycle
    # find the monthly interest rate by dividing by 12
    monthly_interest_rate = (annual_interest_rate / 100) / 12
    # multiply the monthly interest rate by step four
    monthly_interest_charge = round(step_four * monthly_interest_rate, 2)
    print(monthly_interest_charge)


if __name__ == "__main__":
    main()
