#defining function for add the values in the list
def sum(l):
    op=0
    for x in l:
        op=op+x
    return op
#return addition of values in the list

n=int(input("Enter the length of list"))
#input length of list
list=[]
for i in range(n):
    list.append(i)
print(list)
print(sum(list))
#sum values is printed
