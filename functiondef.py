def fact(n):
    if(n==1):
        print("The output is",n)
    else:
        factorial=n*fact(n-1)
        print("The output is",factorial)
fact(3)
