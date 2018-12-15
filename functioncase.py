#check the number of upper and lower case
def givenstring(s):
    d={"Uppercase":0,"Lowercase":0}
    for x in s:
        if x.isupper():
	#check uppercase
            d["Uppercase"]+=1
        if x.islower():
	#check lowercase
            d["Lowercase"]+=1
    print("Original String",s)
    print("No of uppercase",d["Uppercase"])
    print("No of lowercase",d["Lowercase"])

givenstring("This is PythonHackathon Challenge")
