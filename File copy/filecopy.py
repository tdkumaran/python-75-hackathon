fh=open("new.txt",'r')
#opening reading file
f=open("new7.txt",'r+')
#opening writing file
content=fh.readlines()
#copy everyline in new.txt to content
f.writelines(content)
#write the content in the new7.txt
fh.close()
f.close()
#both are closed

