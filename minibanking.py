account={}
while True:
    print("\n1. Create Account")
    print("2. Deposite")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Exit")
    
    choice=input("Enter Choice...")
    
    if choice =="1":
        name=input("Enter name")
        balance=int(input("Enter balance"))
        account[name]=balance
        print("Account Created!")
        
    elif choice=="2":
        name=input("Enter name")
        account=int(input("Enter account"))
        if name in account:
            account[name]+=amount
            print("Deposited!")
        else:
            print("Account not find")
    elif choice=="3":
        name=input("Enter name")
        account=int(input("Enter account"))
        if name in account:
            if accounts[name]>=amount:
                account[name]-=amount
                print("withdraw successfull")
            else:
                print("Not enough balance")
        else:
            print("Acccount not found")
    elif choice=="4":
        name=input("Enter name")
        if name in account:
            print("Balance:",account[name])
        else:
            print("Account not found")
    elif choice=="5":
        break
    else:
        print("Invalid choice")