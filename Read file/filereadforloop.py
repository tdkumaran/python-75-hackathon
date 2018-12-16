n=int(input("Enter the number of lines to be printed:"))
f=open("C:/Users/KUMARAN/Desktop/python-75-hackathon/variable.py",'r')
print(f.tell())
for i in range(n):
        print(f.readline(),end=' ')
print(f.tell())
print(f.seek(50))
print(f.tell())
print(f.read(50))
