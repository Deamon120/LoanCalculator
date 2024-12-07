import math
loan = int(input("Enter the loan principal:\n"))
print("What do you want to calculate?")
print('type "m" - for number of monthly payments,')
print('type "p" - for the monthly payment:')
user_input = input()
if user_input == "m":
    monthly_payment = int(input("Enter the monthly payment:\n"))
    result = math.ceil(loan / monthly_payment)
    print(f"\nIt will take {result} months to repay the loan")
if user_input == "p":
    months = int(input("Enter the number of months:\n"))
    if loan % months != 0:
        payment = math.ceil(loan / months)
        last_month = loan - ((months - 1) * payment)
        print(f"Your monthly payment = {payment} and the last payment = {last_month}.")
    else:
        payment = loan // months
        print(f"Your monthly payment = {payment}")