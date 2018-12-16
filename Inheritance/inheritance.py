class Student:
    #parent class(base class)
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def Name(self):
        return self.fname+self.lname
class Staff(Student):
    #child class(derived class)
    def __init__(self,fname,lname,staffnum):
        Student.__init__(self,fname,lname)
        self.staffnum=staffnum
    def Nameofstaff(self):
        return self.Name() + "," + self.staffnum
s=Student("kumaran","td")
s1=Staff("ragul","srk","10")
print(s.Name())
print(s1.Nameofstaff())
