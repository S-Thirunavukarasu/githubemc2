#🍒 🍋 🍇 🍊 🍓 🍉 ⭐ 💎 🔔
import random
symblos=["🍒", "🍋" ,"🍇", "🍊"," 🍓", "🍉", "⭐", "💎", "🔔"]
def spin():
    return random.choices(symblos,k=3)
def result(s_sym):
    print(" | ".join(s_sym))
def win(s_sym,balance):
    if s_sym[0]==s_sym[1]==s_sym[2]:
        balance+=balance
    balance-=balance
    return balance
def main():
    print("Welcome to Slot Machine!!")
    balance=50
    while balance>0:
        print(f"Current balance : ${balance}")
        bet=input("Enter bet amount : $")
        if not bet.isdigit() :
            print("Please enter a valid amount")
            continue
        bet=int(bet)
        if bet>balance:
            print("Insufficent balance")
            continue
        elif bet<=0:
            print("Place a bet grater than 0")
            continue
        balance-=bet
        print("Spinning...........\n")
        s_sym=spin()
        result(s_sym)
        total=win(s_sym,balance)
        if total>0:
            print(f"You won!! Current balance is ${balance}")
        else:
            print("Sorry You lost.")
            print(f"Current balance is ${balance}")
        play=input("Spin again (Y/N) : ").lower()
        if play!="y":
            print(f"Thanks!Your withdrawal cash is ${balance}")
            break
        
main()
