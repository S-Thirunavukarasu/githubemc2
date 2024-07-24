import random

play=input("Enter start (or) q to Quit : ").lower()
count=0
if play !="start":
    quit()
else:
    while True:
        userchoice=int(input("Enter a number between 1 to 10 : "))
        compchoice=random.randint(1,11)
        if userchoice==compchoice:
            print(f"That's a correct guess of {userchoice}")
            break
        else:
            count+=1
            continue
    print(f"You took {count} attempts to guess the number")
