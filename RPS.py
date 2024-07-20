import random

play=input("Enter start (or) q to Quit : ").lower()

if play!= "start":
    quit()
else:
    while True:
        user=input("Enter any one (rock / paper / scissors) : ").lower()
        comp=random.choice(["rock","paper","scissors"])
        print(f"You choose {user} and computer choose {comp}")
        if user==comp:
            print("It's a tie! Great minds thinks alike!")
            break
        elif user=="rock":
            if comp=="paper":
                print("You loose! Paper smothers Rock!")
                break
            else:
                print("You win! Rock crushes Scissors!")
                break
        elif user=="paper":
            if comp == "rock":
                print("You win! Paper smothers Rock!")
                break
            else:
                print("You loose! Scissors slice through Paper!")
                break
        elif user=="scissors":
            if comp == "rock":
                print("You loose! Rock crushes scissors!")
                break
            else:
                print("You win! Scissors slice through Paper!")
                break
    
        
