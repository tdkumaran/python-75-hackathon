#passbyref
def passbyref(mylist):
    print(mylist)
    #without any operation
    for x in range(3):
        mylist.append(x)
    print("Inisde funciton list values",mylist)
mylist=[5,6,7]
print("Outside funtion list values",mylist)
passbyref(mylist)
