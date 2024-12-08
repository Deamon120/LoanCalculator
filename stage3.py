import argparse
import math

def annuity_payment(principal, interest, payment):
    i = interest / (12 * 100)
    n = math.ceil(math.log((payment / (payment - i * principal)), 1 + i))
    years = n // 12
    months = n % 12
    if years > 0 and months > 0:
        print(f"It will take {years} years and {months} months to repay this loan!")
    elif years < 1 and n > 0:
        print(f"It will take {n} months to repay this loan!")
    elif years > 0 and months < 1:
        print(f"It will take {years} years to repay this loan!")
def number_of_payment(principal, periods, interest):
    i = interest / (12 * 100)
    a = principal * ((i * ((i+1) ** periods)) / (((i+1) ** periods) - 1))
    print(f"your monthly payment = {math.ceil(a)}!")

def loan_principal(payment, periods, interest):
    i = interest / (12 * 100)
    p = payment / ((i * ((i+1) ** periods)) / (((i+1) ** periods) - 1))
    print(f"Your loan principal = {p}!")

parser = argparse.ArgumentParser()
parser.add_argument("--payment", type=float)
parser.add_argument("--principal", type=int)
parser.add_argument("--periods", type=int)
parser.add_argument("--interest", type=float)

args = parser.parse_args()
if args.principal and args.interest and args.payment:
    annuity_payment(args.principal, args.interest, args.payment)
elif args.principal and args.periods and args.interest:
    number_of_payment(args.principal, args.periods, args.interest)
elif args.periods and args.payment and args.interest:
    loan_principal(args.payment, args.periods, args.interest)