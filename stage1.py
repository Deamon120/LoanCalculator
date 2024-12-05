loan = int(input("Enter the loan principal:\n"))
monthly_payment = int(input("Enter the monthly payment:\n"))

result = loan // monthly_payment
print(f"\nIt will take {result} months to repay the loan")