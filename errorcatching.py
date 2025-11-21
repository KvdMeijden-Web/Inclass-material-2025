cal = True
def divide(a, b):
    return a / b

while cal:
    try:  
        num_1 = float(input("number:"))
        num_2 = float(input("number 2:"))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        

    try:
        result = divide(num_1, num_2)
        print("Result:", result)
        cal = False
        
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        






# while True:
#     num_1 = input("number:")
#     num_2 = input("number 2:")
#     try:
#         num_1 = float(num_1)
#         num_2 = float(num_2)
#         break
#     except ValueError:
#         print("Invalid input. Please enter numeric values.")
#         continue

# def divide(a, b):
#     return a / b

# try:
#     result = divide(num_1, num_2)
#     print("Result:", result)
# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed.")
