class Rectangle:
    def __init__(self,lenght,breadth):
        self.lenght=lenght
        self.breadth=breadth
    def area(self):
        area=self.lenght*self.breadth
        return area
r1=Rectangle(10,5)
print("The area is ",r1.area())
