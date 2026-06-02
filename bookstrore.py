contacts={}
def add_contact():
    name=input("Enter name: ")
    phone=input("Enter phone number: ")
    contacts[name]=phone
    print("Contact added successfully!\n")
def search_contact():
    name=input("enter name to search: ")
    if name in contacts:
        print("Name:",name)
        print("Phone:", contacts[name], "\n")
    else:
        print("Contact not found\n")
def delete_contact():
    name=input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted sucesfully!\n")
    else:
        print("Contact not found!\n")
        
while True:
    print("1.  Add Contact")
    print("2. search Contact")
    print("3. delete Contact")
    print("4. Exit")
    
    choice=int(input("Enter your choice: "))
    
    if choice == 1:
        add_contact()
    elif choice == 2:
        search_contact()
    elif choice == 3:
        delete_contact()
    elif choice == 4:
        print("Existing program.............")
        break
    else:
        print("Invalid choice!\n")