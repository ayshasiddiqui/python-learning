account_holder_name = input("Enter the Account Holder Name : ")
current_balance = int(input(" Enter the Current Balance : "))
withdrawal_amount = int(input("Enter the Withdrawal Amount : "))
if withdrawal_amount <= current_balance:
    print("Withdrawal Successful")
    remaining_balance = current_balance - withdrawal_amount
    print("Remaining Balance=",remaining_balance )
else:
    print("Insufficient Balance")