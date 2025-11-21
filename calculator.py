import keyboard  # install with: pip install keyboard

while True:
    num1 = float(input("Enter first number: "))
    op = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        result = num1 / num2 if num2 != 0 else "Error: Division by zero"
    else:
        print("Invalid operator.")
        continue

    print("Answer:", result)

    print("Press ESC to quit or Enter to continue...")
    if keyboard.is_pressed("esc"):
        print("Thank you for using the calculator.")
        break

    clear = input("Clear (yes/no)? ").lower()
    while clear == "no":
        op = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter another number: "))

        if op == "+":
            result += num2
        elif op == "-":
            result -= num2
        elif op == "*":
            result *= num2
        elif op == "/":
            result = result / num2 if num2 != 0 else "Error: Division by zero"
        else:
            print("Invalid operator.")
            continue

        print("Answer:", result)
        print("Press ESC to quit or Enter to continue...")
        if keyboard.is_pressed("esc"):
            print("Thank you for using the calculator.")
            exit()

        clear = input("Clear (yes/no)? ").lower()

    if clear == "yes":
        print("Calculator cleared.\n")
        continue