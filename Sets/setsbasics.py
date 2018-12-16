#creating set
set1={"orange","pink","yellow","green"}
#print the element in the set1
print(set1)
#to check some element in available in the set as
print("pink" in set1)
#return boolean value
#to add some new element in the existing set as
set1.add("pink")
#only unique element in the set is printed
print(set1)
#to update a list of elements
set1.update(["green","blue"])
print(set1)
set1.remove("green")
print(set1)