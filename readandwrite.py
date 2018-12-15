#open or create the file in write mode
fh=open("C:/Users/KUMARAN/Desktop/python-75-hackathon/new.txt",'w')
#write one line bye line
fh.write("This is the first line\n")
fh.write("This is the second line\n")
fh.write("This is final line\n")
#close the file
fh.close()
#now open the file in read mode
fh=open("C:/Users/KUMARAN/Desktop/python-75-hackathon/new.txt",'r')
#read everything in the file and store in the list
contents=fh.readlines()
#print the list
print(contents)
