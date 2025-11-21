length_user = int(input("Enter the length"))
weight_user = int(input("Enter the weight"))

if length_user > 150 and weight_user <= 95:
    print("You can enter the ride")
elif length_user > 150 and not weight_user <= 95:
    print("You can enter the ride but you have to sit in the front")
else:
    print("You cannot enter the ride, you are too short")