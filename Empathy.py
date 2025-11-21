feeling = input("Do you feel happy today? (yes/no):").strip().lower()


if feeling == "yes":
    print("Then go bother someone else")
elif feeling == "no":
    help = input("Do you need any help?")
    if help == "yes":
        print("I am sorry to hear that. Please call 123")
    elif help == "no":
        print("Then go bother someone else")
    else: 
        print("Invalid input. Please answer with 'yes' or 'no'.")
else:
    print("Invalid input. Please answer with 'yes' or 'no'.")