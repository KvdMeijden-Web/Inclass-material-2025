# number = 1

# for number in range(1,1000000):
#     print (number)
# print("Finished")

# input_word = input("Enter a word: ")
# reversed_word = ""

# for i in input_word:
#     reversed_word = i + reversed_word
#     print(reversed_word)

ingredient = ["fries","mayonaise", "ketchup", "burger"]
short = []
long = []
for i in ingredient:
        lenght_word = len(i)
        if lenght_word <= 5:
            short.append(i)
        else:
            long.append(i)
print(short)
print(long)