balance = float(input("Enter the available balance:"))
withdraw = float(input("Enter withdraw amount:"))

if withdraw <= balance:
    print("Withdraw Successfull")

else:
    print("Transaction declined!")