#string processing (strip whitespace)
t="This is python75 hackathon challenge               "
s="         Makes a good chance to regain all python knowledge"
u="        Now both left and right side strip           "
#printing the same string
print(t)
print(s)
print(u)
#to remove trailing whitespace 
print(t.rstrip())
#to remove leading whitespace
print(s.lstrip())
#to remove both trailing and leading whitespace
print(u.strip())

