import random
#imported random 
number=random.randint(1,10)
#generate one random number
attempt=0
guess=0
while guess!=number:
    guess=int(input("guess number"))
    #guess user number 
    attempt=attempt+1
    if guess==number:
        print("Correct",attempt,"attempts")
        break
    elif guess<number:
        print("Think higher")
    else:
        print("Think lower")
        
    
