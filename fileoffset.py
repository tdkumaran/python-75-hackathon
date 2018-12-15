with open('new1.txt','w')as fh:
    fh.write("New line\n")
    fh.write("Another line\n")
    fh.write("adkfasfskfjakfhkasjfkdjkajfalk\n")
fh=open('new1.txt','r+')
content=fh.read(10)
print("Read string:",content)
position=fh.tell()
print("Current position:",position)
new=fh.seek(0,0)
content=fh.read(10)
print("Again read string is:",content)
fh.close()
    
