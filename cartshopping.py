cart=[]

while True:
    print("\n1. Add 2.View 3.Total 4.Exit")
    ch=input("Choose:")
    
    if ch=='1':
        item=input("Enter item: ")
        price=int(input("Enter price:"))
        cart.append(price)
    elif ch=='2':
        print("Cart:",cart)
    elif ch=='3':
        print("Total:",sum(cart))
    elif ch=='4':
        break