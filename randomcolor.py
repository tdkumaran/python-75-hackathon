import random
n=int(input("Enter the number of color to be in"))
for x in range(n):
    list=[]
    str=input("Color:\r")
    list.append(str)
print("The random color picked is",random.choice(list))
#choosing a random color
