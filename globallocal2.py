#use of global variable
globalvar="global"
#a global variable defined
def fun():
    global globalvar
    #if this global is not defined raise an error
    localvar="local"
    globalvar=globalvar*3
    print(globalvar)
    print(localvar)

fun()
