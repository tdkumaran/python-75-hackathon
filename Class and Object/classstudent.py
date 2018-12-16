class Student:
    def __init__(self, name, rollnumber):
        self.name=name
        self.rollnumber=rollnumber
    def setage(self,age):
        self.age=age
    def setmark(self, mark):
        self.mark=mark
    def display(self):
        print("Name of student:",self.name)
        print("Roll number of student",self.rollnumber)
        print("Age of student",self.age)
        print("Mark of student",self.mark)
s1=Student('Ram',16)
s1.setage(17)
s1.setmark(100)
s1.display()
s2=Student('Vikash',10)
s2.setage(10)
s2.setmark(90)
s2.display()
