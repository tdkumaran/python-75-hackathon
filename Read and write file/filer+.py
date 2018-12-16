with open("new7.txt","r+") as f:
    f.seek(0,0)
    f.write("This is new writing")
    #able to use both read and write operation
    print(f.read())
    #read operation is performed
