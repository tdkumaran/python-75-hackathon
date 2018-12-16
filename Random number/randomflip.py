#flip coin
import random
h,t=0,0
n=int(input("Enter the number of times the flip occurs"))
for x in range(n):
    r=random.randint(0,1)
    if r==0:
        h=h+1
    else:
        t=t+1
print("No. of times head occurs: ",h)
print("No. of times tails occurs: ",t)
    
