#open the file in read mode
fh=open("new10.txt",'r')
#split in space marked as word
counter=fh.read().split()
#counter stores the list
print(len(counter))
#length of list gives the number of words
