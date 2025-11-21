

def sum():
    sum = 2 + 2
    print(sum)


def sum(name):
    sum = 2+2
    return sum

def main():
    name = input("Enter your name: ")
    result = sum(name)
    print(result)

def clear_calculator():
    number_1 = float(input("Enter a number: "))
    choice = input("+, -, *:")
    number_2 = float(input("Enter another number: "))
    if choice == "+":
        result = add(number_1, number_2)
    elif choice == "-":
        result = subtract(number_1, number_2)
    elif choice == "*":
        result = multiply(number_1, number_2)
    return result

main()
sum()
clear_calculator()





# #show functions


# #build in functions
# #brackets as input.
# #different functions have different inputs.
# #Hover over function to see what input it needs.
# #random funtion example:

# #Making our own procedures:

#Calling functions is activate the function.

def add(a,b):
    total = a + b
    return total
def substract(a,b):

    total = a + b
    return total
def multiply(a,b):

    total = a + b
    return total
def main():
    number1 = int(input("Enter a number: "))
    number2 = int(input("Enter another number: "))
    result = add(number1,number2)
    print(result)

main()

# def add(num1, num2):
#     total = num1 + num2
#     return total

# def subtract(num1, num2):
#     total = num1- num2
#     return total

# def multiply(num1, num2):
#     total = num1 * num2
#     return total

# def clear_calculator():
#     number_1 = float(input("Enter a number: "))
#     choice = input("+, -, *:")
#     number_2 = float(input("Enter another number: "))
#     if choice == "+":
#         result = add(number_1, number_2)
#     elif choice == "-":
#         result = subtract(number_1, number_2)
#     elif choice == "*":
#         result = multiply(number_1, number_2)
#     return result

# def contuinue_calculator(number_1):
    
#         choice = input("+, -, *:")
#         number_2 = float(input("Enter a number: "))
#         if choice == "+":
#             result = add(number_1, number_2)
#         elif choice == "-":
#             result = subtract(number_1, number_2)
#         elif choice == "*":
#             result = multiply(number_1, number_2)

#         return result

# def main():
#     clear = True
#     while True:
#         if clear == True:
#             answer = clear_calculator()
#         else:
#             answer = float(contuinue_calculator(answer))
#         print(answer)
#         reset = input ("clear? (y/n): ")
#         if reset == "y":
#             clear = True
#         else:
#             clear = False
    
        
        

# main()

#using functions make it possible to use the results.


# def add_two(num1, num2):
#     total = num1 + num2
#     return total

# def subtract_two(num1, num2):
#     total = num1 - num2
#     return total

# def main():
    
    

#     clear = input ("clear? (y/n): ")
#     if clear == "y":
#         clear_calculator()
#     if clear == "n":
#         contuinue_calculator()
        