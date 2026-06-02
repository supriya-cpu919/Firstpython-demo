history=[]
while True:
    print("\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Show History\n6. Exit")
    choice=int(input("Enter choice: "))
    
    if choice==6:
        break
    if choice==5:
        print("History:", history)
        continue
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    
    if choice==1:
        result=a+b
        operation = f"{a} + {b} = {result}"
    elif choice==2:
        result=a-b
        operation = f"{a} - {b} = {result}"
    elif choice==3:
        result=a*b
        operation = f"{a} * {b} = {result}"
    elif choice==4:
        if b != 0:
            result=a / b
            operation = f"{a} / {b} = {result}"
        else:
            operation="Division by zero not allowed"
    else:
        print("Invalid choice")
        continue
print("Result:" , operation)
history.append(operation)
    