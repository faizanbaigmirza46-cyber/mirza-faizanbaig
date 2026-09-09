balance = float(input("Enter account balance: "))
amount = float(input("Enter withdrawal amount: "))

minimum_balance = 500

if amount <= 0:
    print("Invalid withdrawal amount")
elif amount > balance:
    print("Withdrawal rejected: Insufficient balance")
elif balance - amount < minimum_balance:
    print("Withdrawal rejected: Minimum balance of 500 must be maintained")
else:
    balance = balance - amount
    print("Withdrawal approved")
    print("Remaining balance =", balance)
