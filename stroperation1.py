#slicing
t="python"
s="challenge"
#[:] this segment of slice print entire thing
print(t[0:2]+s[:])
#strings are immutable t[1]='a' gives error
word='kumaran'
#start from beginning position
print(word[:3])
#start from 4th position
print(word[4:]+" was")
#to get the length of string use len function
print(len(t))
print(len(word))
