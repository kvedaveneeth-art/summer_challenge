amount = float(input("Amount:"))

if amount > 5000:
    discount = amount * 20 / 100
    final_amount = amount - discount

else:
    final_amount = amount

print("Final amount payable =",final_amount)