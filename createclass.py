#class is like a blueprint for the object
class Person:
    #class created with the name person
    def __init__(self,name,age):
        #__inti__ function is automatically called every time when the class is used to create new object
        #like constructor
        self.name=name
        self.age=age
        #self paramater is ref to class instance itself, to access variables that belong to the class
    def description(self):
        print("He is averaging studying good boy")
p1=Person('Kumaran',19)
#creating object p1
p2=Person('Ragul',19)
#object p2
print(p1.name)
print(p1.age)
p1.description()
print(p2.name,p2.age)
p2.description()
    
