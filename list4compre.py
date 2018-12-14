#list comprehension
list1=[1,2,3,4,5]
def iseven(x):
    return(x%2==0)
def square(x):
    return(x*x)
print(list(map(square,list1)))
#map applies some function to every element in the list
evenlist=[]
for x in list1:
    if iseven(x):
        evenlist.append(x)
print(evenlist)
#created evenlist as sublist
print([square(x) for x in list1 if iseven(x)])
#mapping first one that applies function
#generator that is range taking element
#filter filter that with some condition
