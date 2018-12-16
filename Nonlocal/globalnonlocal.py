#create nonlocal
def fun():
    x="local variable"
    #local variable defined
    def fun1():
        nonlocal x
        #in nested nonlocal variable defined as x, any changes affect the local
        x="nonlocal variable"
        print("Function1 inner values is",x)
    fun1()
    print("Function outside variable",x)
fun()
#both print nonlocal
