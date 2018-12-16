class Parent:
    def __init__(self,a,b,c):
        self.a=a
        self._b=b
        self.__c=c
    def val(self):
        print(self.__c)
c1=Parent(1,2,3)
print(c1.a)
print(c1._b)
print(c1.val())

