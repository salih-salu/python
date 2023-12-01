class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
        
    def area(self):
    	   return self.length * self.breadth
    def per(self):
    	   return 2*(self.length + self.breadth)
    
a=int(input("Enter the lenght: "))
b=int(input("Enter the breadth: "))
rect=Rectangle(a,b)
print("Area of the rectangle is: ",rect.area())
print("perimeter of the rectangle is: ",rect.per())

