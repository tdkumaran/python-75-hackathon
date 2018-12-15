#listing in dictionary
d={"one":1,"two":2,"three":3}
print(list(d.keys()))
#listing the keys of dictionary
print(list(d.values()))
#listing the values of dictionary
print(list(d.items()))
#listing the keys and values of the dictionary
print("one" in d)
#check existence
print(len(d))
#length of dic
d.pop("two")
#pop operation removes the values with key
print(d)
#removed two

