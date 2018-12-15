#file open with automatically flose when operation overs
with open('new.txt','w') as f:
    f.write("Again come with other words using with\n")
    f.write("Only 2 line is enought\n")
with open('new.txt','a') as f:
    f.writelines(['hello\n','this is another two line'])
        
