#dictionary
dict={"myname":"abc","num":12,"age":18}
#to add country in that dictionary
dict["country"]="india"
print(dict["country"],dict["myname"])
del dict["country"]
print(dict["country"])
#gives an error because country key is deleted
print(dict["num"])
#it gives values because country key only delted
