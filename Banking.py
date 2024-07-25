def balance(bal):
    print(f"Your current balance is : {bal:.2f}")

def deposit():
        req=float(input("Enter amount to deposit : "))
        if req<0:
            print("Enter a valid amount")
            return 0
        return req

def withdraw(bal):
        req=float(input("Enter amount to deposit : "))
        if req<0:
            print("Enter a valid amount")
            return 0
        if req>bal:
             print("Insufficent balance")
             return 0
        return req

def main():
    bal=0
    bank=True
    while bank:
        print("Welcome to your bank account")
        print("1.Deposit cash\n2.Withdraw cash\n3.View Balance\n4.Exit")
        choice=input("Enter service number (1-4) : ")
        if not choice.isdigit():
            print("Please enter valid service number")
            continue
        choice=int(choice)
        if choice==1:
            bal+=deposit()
        elif choice==2:
            bal-=withdraw(bal)
        elif choice==3:
            balance(bal)
        elif choice==4:
            bank=False
        else:
            print("Please enter valid service number")
            continue

main()