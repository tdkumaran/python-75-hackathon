#create a list
lis=[1,2,3,4]
#a list is created
flist=list(filter(lambda x: (x%2 != 0) , lis))
#filter lambda used to get odd numbers
print(flist)