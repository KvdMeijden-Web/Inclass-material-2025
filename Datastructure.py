# # #string and stringhandling

Hello ="hello my name is Koen"
# # print(Hello)
# # print(len(Hello))
# # print(Hello[0:5])

# # # concatenation: for adding strings together (only strings)
# # name =  "12"  
# # print( "Hello "+name )
# #f-stings
# # name = "Koen"
# # age = 15
# # print(f"Hello my name is {name} and I am {age} years old")

# # #string loop
# for character in Hello:
#     print(character)
    

# print (len(name))

#selecting parts of a string (slice)
# print(Hello[0:7])
# print(Hello[:5])
#.strip(),,.lower(), .upper(), .replace(), .find()
# print(Hello.replace("Koen", "Pete"))


#cheering programme:
# name = input("what is your name?: ")
# for i in name:
#     print (i)

#split and join
# print(Hello.split(" "))
# print("_".join(Hello))

# #----Arrays and Lists----
# #List = a collection which is ordered and changeable. Allows duplicate members
# list = ["apple", "banana", "cherry"]
# print(list)


#numpy arrays are used for scientific calculations and data analysis, because they are more efficient than lists.
# import numpy
# numbers  = numpy.array([1,2,3])
# print (numbers)


# #----Stack----
# Stack = []
# Stack.append("apple")
# Stack.append("banana")
# Stack.append("cherry")
# print(Stack)

# Stack.pop(0)
# print(Stack)

# #----2D Arrays---- (embedded arrays / lists)
list_2d = [["apple", "banana", "cherry"],["orange", "kiwi", "melon"]]


# make it readable
list_2d = [
    ["apple", "banana", "cherry"],
    ["orange", "kiwi", "melon"]
    ]


list_2d[1].append("watermelon")
print(list_2d)



# import numpy
# numbers  = numpy.array([[1,2,3],[4,5,6]])
# print (numbers)

