#copy list
list1=[1,2,"raj",3,"raji"]
list2=list1
print(list2)
#both list2 and list1 point same list changes in list2 also affect list1
list2[2]=4
print(list1)
#to avoid create a separte list by slicing
list2=list1[:]
list2[4]=5
print(list1)
print(list2)

