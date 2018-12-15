#maximum of three numbers
def max(x,y,z):
    if x>y and x>z:
        print("The biggest number is",x)
    elif y>z:
        print("The biggest number is",y)
    else:
        print("The biggest number is",z)
x=int(input("Enter first number"))
y=int(input("Enter second number"))
z=int(input("Enter third number"))

max(x,y,z)
