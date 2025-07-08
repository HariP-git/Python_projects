shopping_list=[]

def show_menu():
    print("---shopping list---")
    print('1.view the list details')
    print('2.add product to list')
    print('3.remove product details')
    print('4.clear list')
    print('5.exit')
    print("---------------")

while True:
    show_menu()
    choice=int(input("enter the value from 1 to 5 :"))

    if choice==1:
        if shopping_list:
            print("---------the list is----------")
            for i,item in  enumerate(shopping_list,start=1):
                print(f"{i}.{item}") 
        else:
            print("the list is empty!!!")
    elif choice ==2:
        value=input("enter the value to append:")
        shopping_list.append(value)
    elif choice==3:
        value=input("enter the value to remove:")
        shopping_list.remove(value)
    elif choice==4:
        shopping_list.clear()
    else:
        print("sucessfully exiting!!!")
        break