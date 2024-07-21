print("Welcome to quizz game!!")
play=input("Enter start (or) press q to Quit : ").lower()
if play!="start":
    quit()
count=0
q1=input("Enter full form of CPU : ").lower()
if q1=="central processing unit":
    count+=1
    print("That's a right answer :)")
else:
    print("Sorry better luck next time :(")
q2=input("Enter full form of GPU : ").lower()
if q2=="graphics processing unit":
    count+=1
    print("That's a right answer :)")
else:
    print("Sorry better luck next time :(")
q3=input("Enter full form of RAM : ").lower()
if q3=="random access memory":
    count+=1
    print("That's a right answer :)")
else:
    print("Sorry better luck next time :(")
q4=input("Enter full form of ROM : ").lower()
if q4=="read only memory":
    count+=1
    print("That's a right answer :)")
else:
    print("Sorry better luck next time :(")
q5=input("Enter full form of LED : ").lower()
if q5=="light emitting diode":
    count+=1
    print("That's a right answer :)")
else:
    print("Sorry better luck next time :(")

print(f"Your score : {count} / 5")
