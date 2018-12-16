#to create empty set as
num=set()
#empty set is created
num.add(1)
num.add(2)
num.add(3)
print(num)
num1=set([3,4,5])
print(num1)
print(num|num1)
#Union operation
print(num&num1)
#intersection
print(num-num1)
#set difference
print(num^num1)
#exclusive or