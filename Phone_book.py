calllog={}

def exit():
    print("Thanks for using our service!")

def view(calllog):
    count=0
    for x,y in calllog.items():
        count +=1
        print(f"{count}.Name : {x}  Number : {y}\n".rstrip())

def add(calllog):
    add=input("Enter name : ")
    con=input("Enter number : ")
    if add not in calllog:
        if con not in calllog:
            calllog[add]=con
            print(f"Conatct {add} has been added")
    else:
        print("Sorry contact alredy exists.")

def search(calllog):
    search=input("Enter contact name : ")
    if search in calllog:
        print(f"Name : {search}\nNumber : {calllog[search]}")
    else:
        print("Sorry!No contacts found.")

def delete(calllog):
    delete=input("Enter name to delete : ")
    if delete in calllog:
        calllog.pop(delete)
        print(f"Contact {delete} has been deleted.")
    else:
        print("Sorry!No contacts found.")

def update(calllog):
    update=input("Enter name to Update Contact : ")
    if update in calllog:
        updatecon=input("Enter new contact number : ")
        calllog.update({update : updatecon})
        print("Contact number has been Updated")
        print(f"Name : {update}\nNumber : {updatecon}")
    else:
        print("Sorry!No contacts found.")

def main(calllog):
    while True:
        print("Please select the service you need")
        print("1.Add Contact\n2.Search Contact\n3.Update Contact\n4.Delete Contact\n5.View Contact\n6.Exit")
        service=input("Please Enter the service number provided : ")
        if not service.isdigit():
            print("Enter a valid service number")
            continue
        service=int(service)
        if service==1:
            add(calllog)
            continue
        elif service==2:
            search(calllog)
            continue
        elif service==3:
            update(calllog)
            continue
        elif service==4:
            delete(calllog)
            continue
        elif service==5:
            view(calllog)
            continue
        elif service==6:
            exit()
            break
        else:
            print("Please Enter a valid service provided")

main(calllog)
    
