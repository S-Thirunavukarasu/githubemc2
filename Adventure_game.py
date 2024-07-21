print("Welcome to the world of mystert and adventure!!")
play=input("Embark your journy like no other. Enter 's' to start : ").lower()
if play != "s":
    quit()
else:
    while True:
        print("Your adventure begins now!!")
        adv1=input("You entered into a forest.Move left or right? :").lower()
        if adv1=="left":
            print("You discovered a hidden chest! What could be inside?")
            adv1=input("Press 'o' to open (or) 'c' to close : ").lower()
            if adv1 == "o":
                print("A riddle blocks your path.Solve it to proceesd.")
                adv1=input("Press 's' to solve (or) 'm' to move on : ").lower()
                if adv1 == "s":
                    print("Victory! You've defeated the enemy")
                    break
                else:
                    print("Defeat ! Regroup and try again.")
                    break
            else:
                print("Try to explore things out !")
                break
        elif adv1=="right":
            print("An ancient relic lies before you. Its power is immense.")
            adv1=input("Press 'o' to open (or) 'c' to close : ").lower()
            if adv1 == "o":
                print("The ancient mechanish is intricate.Can you unlock its secrets?")
                adv1=input("Press 'u' to unlock (or) 'm' to move on : ").lower()
                if adv1 == "u":
                    print("Triumph is yours! The battle is won!")
                    break
                else:
                    print("You have been bested, but don't loose hope")
                    break
            else:
                print("Unlock powers to be immense!")
                break
        else:
            print("Please enter a valid one.")
            continue
