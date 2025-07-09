file_name="notes.txt"

def menu():
    print("\n---note taking app----")
    print("1.Add new note")
    print("2.View all note")
    print("3.Delete all note")
    print("4.Exit")

def new_note():
    note=input("enter your new note")
    with open(file_name,"a")as file:
        file.write(note)
    print("note added sucessfully")
    
def view_notes():
    try:
        with open(file_name,"r")as file:
            notes=file.read()
            if notes:
                print("---your notes---")
                print(notes)
            else:
                print("No notes found")
    except FileNotFoundError:
        print("No file found...")

def delete_notes():
    confrim=input("Are you sure you want to delete all notes ?(y/n):")
    if confrim.lower()=="y":
        with open(file_name,"w")as file:
            pass
        print("All notes are deleted")

while True:
    menu()
    choice=input("enter your choice")
    if choice=="1":
        new_note()
    elif choice=="2":
        view_notes()
    elif choice=="3":
        delete_notes()
    else:
        print("exiting sucessfully...")
        break