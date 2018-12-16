#global use
def f():
    global x
    y=x
    print("The value of y",y)
    x=10
x=7
f()
print("The value of x",x)
