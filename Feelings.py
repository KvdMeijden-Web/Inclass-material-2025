feeling = input("Are you feeling happy today: (Yes/No)").lower().strip()

if feeling == "yes":
    print("Then go bother someone else")
elif feeling == "no":
    help = input("Do you need help?: (yes / no)").lower().strip()
    if help == "yes":
        print("I am sorry to hear that. Please call 123")
    elif help == "no":
        print("try to think happy toughts")
    else:
        print("you wrote the wrong input")
else:
    print("you wrote the wrong input")


    

