def celcius_to_fahrenheit(celcius):
    return (celcius*9/5)+32

def celcius_to_kelvin(celcius):
    return celcius +273.15

def fahrenheit_to_celcius(fahrenheit):
    return(fahrenheit-32)*9/5

def fahrenheit_to_kelvin(fahrenheit):
    celcius=fahrenheit_to_celcius(fahrenheit)
    return celcius_to_kelvin(celcius)

def kelvin_to_celcius(kelvin):
    return kelvin-273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin-273.15)*9/5+32

def menu():
    print("----Temperature converter menu---")
    print(" 1. Celcius to fahrenheit & kelvin")
    print(" 2. Fahreheit to celcius and kelvin")
    print(" 3. Kelvin to celcius and fahrenheit")
    print(" 4. Exit")

while True:
    menu()
    choice =input("Enter the choice between 1 to 4:")

    if choice=="1":
        celcius=float(input("Enter the celcius:"))
        print(f"fahrenheit :{celcius_to_fahrenheit(celcius):.2f}")
        print(f"kelvin:{celcius_to_kelvin(celcius):.2f}")

    elif choice=="2":
        fahrenheit=float(input("enter the fahrenheit:"))
        print(f"celcius:{fahrenheit_to_celcius(fahrenheit):.2f}")
        print(f"kelvin:{fahrenheit_to_kelvin(fahrenheit):.2f}")

    elif choice=="3":
        kelvin=float(input("enter the kelvin:"))
        print(f"celcius:{kelvin_to_celcius(kelvin):.2f}")
        print(f"fahrenheit:{kelvin_to_fahrenheit(kelvin):.2f}")

    else:
        print("sucessfully exiting...")
        break


    
