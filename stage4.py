import argparse
import math

def calculating_differentiated_payments(principal, periods, interest):
    i = interest / (12 * 100)
    sum_month = 0
    if periods > 9:
        for m in range(1,11):
            month = math.ceil(principal / periods + i * (principal - principal * (m - 1) / periods))
            sum_month += month
            print(f"Month {m}: payment is {month}")
    else:
        for m in range(1,periods + 1):
            month = math.ceil(principal / periods + i * (principal - principal * (m - 1) / periods))
            sum_month += month
            print(f"Month {m}: payment is {month}")
    print()
    print(f"Overpayment = {sum_month - principal}")

def number_of_payment(principal, periods, interest):
    i = interest / (12 * 100)
    a = principal * ((i * ((i+1) ** periods)) / (((i+1) ** periods) - 1))
    print(f"Your annuity payment = {math.ceil(a)}!")
    print(f"Overpayment = {math.ceil(a) * periods - principal}")


def loan_principal(payment, periods, interest):
    i = interest / (12 * 100)
    p = payment / ((i * ((i+1) ** periods)) / (((i+1) ** periods) - 1))
    print(f"Your loan principal = {int(p)}!")
    print(f"Overpayment = {int(payment * periods - int(p))}")


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
    print(f"Overpayment = {int(n * payment - principal)}")


parser = argparse.ArgumentParser()
parser.add_argument("--payment", type=float)
parser.add_argument("--principal", type=int)
parser.add_argument("--periods", type=int)
parser.add_argument("--interest", type=float)
parser.add_argument("--type", type=str)

args = parser.parse_args()


if (args.principal is not None and args.principal < 0) or \
       (args.payment is not None and args.payment < 0) or \
       (args.interest is not None and args.interest < 0) or \
       (args.periods is not None and args.periods < 0):
        print("Incorrect parameters.")
elif args.type == "diff" and args.principal and args.periods and args.interest:
    calculating_differentiated_payments(args.principal, args.periods, args.interest)
elif args.type == "annuity" and args.principal and args.periods and args.interest:
    number_of_payment(args.principal, args.periods, args.interest)
elif args.type == "annuity" and args.payment and args.periods and args.interest:
    loan_principal(args.payment, args.periods, args.interest)
elif args.type == "annuity" and args.principal and args.payment and args.interest:
    annuity_payment(args.principal, args.interest, args.payment)
else:
    print("Incorrect parameters.")