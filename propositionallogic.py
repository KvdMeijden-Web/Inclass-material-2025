# #proposition
R = False
S = True

# #logic
T = (R and S) or (not R and not S)

print(T)

if T == True:
    print("Robot goes outside")
else:
    print("Robot stays inside")