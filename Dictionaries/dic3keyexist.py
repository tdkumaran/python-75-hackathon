#check key exist
d={"country":'india',"district":'madurai',"pin":623}
print(d)
#check the key district in dictionary d
if "district" in d:
    print("distrcit")
#presence make a print
for x in d:
    print(d[x])
#print all the values in the dictionary
for x in d:
    print(d.keys())
#print all the keys in the dictionary
for x in d.items():
    print(x)
#items funtion used to print all the key and values in the dictionary
