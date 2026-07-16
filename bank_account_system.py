Account_holder_name = input("enter the account holder name : ")
Initial_bank_balance = int(input("enter the initial bank balance :"))
while True:
    print("\n________BANK MENU______")
    print("1. check the bank balance")
    print("2. deposite money ")
    print("3. withdrow money")
    print("4. exit")
    choice = input("enter your choice :")
    if choice == "1" :
        print("current balance =",  Initial_bank_balance)
    elif choice == "2":
        amount = int(input("enter the deposite amount : "))
        Initial_bank_balance = Initial_bank_balance+amount
        print(" deposite the money successfully")
        print("current balance=",Initial_bank_balance)
    elif choice == "3":
        amount = int(input("enter the withdraw money : "))
        if amount<=Initial_bank_balance:
            print("withdraw money successfully")
            Initial_bank_balance = Initial_bank_balance - amount
            print("current balance=", Initial_bank_balance)
        else:
            print("Insufficient Balance")
    elif choice == "4" :
            print("Thnak You =", Account_holder_name  )
            print("current balance=", Initial_bank_balance)
            break
else:
    print("invalid choice")
    