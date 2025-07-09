import time
contact_book ={}

def menu():
    print("---contact book---")
    print("1.Add contact")
    print("2.View contact")
    print("3.Search contact")
    print("4.Edit a contact")
    print("5.Delete a contact")
    print("6.Exit a contact")

def add():
    name=input("Enter the contact name")
    phone=input("Enter contact phone number")
    email=input("Enter the contact email")
    contact_book[name]={"phone":phone,"email":email}
    print("---Contact Sucessfully added---")

def view():
    if not contact_book:
        print("Contact book empty !!!")
    else:
        for key,value in contact_book.items():
            print(f"{key}:{value}")

def search():
    name=input("Enter the value to search :")
    if name in contact_book:
        print(f"The {name}is present in contact book and details is :")
        
        print(f"name:{name}")
        print(f"phone:{contact_book[name]["phone"]}")
        print(f"phone:{contact_book[name]["email"]}")

def edit():
    name=input("Enter the name to change:")
    if name in contact_book:
        contact_book[name]=name
        email=input("enter the email to change")
        phone=input("enter the phone to change")
        contact_book[name]={"phone":phone,"email":email}
        print("Changed sucessfully")

    else:
        print("The entered name is wrong..") 

def delete():
    name=input("Enter the value to delete :")
    if name in contact_book:
        print("Deleting your details..")
        time.sleep(1)
        del contact_book[name]
        print("The details has been deleted..")

def main():
   
    while True:
        menu()
        option=input("Enter the value between 1 to 5:")
        if option=="1":
            add()
        elif option == "2":
            view()
        elif option =="3":
            search()
        elif option=="4":
            edit()
        elif option=="5":
            delete()
        else:
            exit
            print("Exiting sucessfully...")
            break

main()

        


