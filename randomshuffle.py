import random
li=[1,2,3,4,5]
print("The list before shuffling")
for i in range(0,len(li)):
    print(li[i],end=' ')
random.shuffle(li)
print("\n")

print("The list after shuffling")
for i in range(0, len(li)):
    print(li[i],end=' ')
    
    
