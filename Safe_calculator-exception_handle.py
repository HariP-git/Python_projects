def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    if y==0:
        raise ZeroDivisionError("Cannot divide by zero")
    return x/y

def menu():
    print("Safe calculator")
    print("1.Add")
    print("2.subract")
    print("3.Multiply")
    print("4.divide")
    print("5.Exit")

while True:
    menu()
    choice=input("Enter the value between 1 to 5:")

    try:
        num1=int(input("enter the number:"))
        num2=int(input("enter the number:"))
        if choice=="1":
            print("result",add(num1,num2))
        elif choice=="2":
            print("result",sub(num1,num2))
        elif choice=="3":
            print("result",mul(num1,num2))
        elif choice=="4":
            print("result",div(num1,num2))
        else:
            print("Exiting sucessfully...")
    except ValueError:
        print("Invalid input")
    except ZeroDivisionError as e:
        print(e)
    except Exception as e:
        print(e)
    finally:
        print("The program ended sucessfully...")


