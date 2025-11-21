#create a password manager.
# The password manager should be able to:
# 1. Store passwords in a dictionary.
# 2. store the dictionary in a file.
# 3. Retrieve passwords from the file.
print("Welcome to the Password Manager!\n")
choice = input("enter '1' to store a password, '2' to retrieve a password:\n ")

if choice == '1':
    service = input("Service name: ")
    password = input("Password: ")


    with open("passwords.txt", "w") as file:
        file.write(f"{service}:{password}")

    print("Password saved!")


    with open("passwords.txt", "r") as f:
        data = f.read()

    print("File content:", data)

else:
    service = input("Enter the service name to retrieve the password: ")

    with open("passwords.txt", "r") as file:
        data = file.read()
        

        if service == stored_service:
            print(f"The password for {service} is: {stored_password}")
        else:
            print(f"No password found for {service}.")