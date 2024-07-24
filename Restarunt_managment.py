print("Welcome to our restarunt. Here's the menu :")
menu={
    "pizza" : 40,
    "cofee" : 20,
    "burger": 50,
    "juice" : 40,
}

for i,j in menu.items():
    print(f"{i} = ${j}")
ord=0
def choice1(menu,ord):
    while True:
        choice1=input("Enter the food to order : ").lower()
        if choice1 in menu:
            ord += menu[choice1]
        else:
            print("Please enter a valid item")
            continue
        print("It would take hardly 5 min to process your order")
        choice_req=input("Order anyother please (Y/N): ").lower()
        if choice_req=="y":
            choice2=input("Enter the item name please : ").lower()
            if choice2 in menu:
                ord += menu[choice2]
                print("Thanks for your order! Have a nice day :)")
                break
            else:
                print("Please enter a valid input.")
                continue
        else:
             break
    return ord

res=choice1(menu,ord)
print(f"Total bill : ${res}")