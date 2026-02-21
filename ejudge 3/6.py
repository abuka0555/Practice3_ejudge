class Shape:
   def area(self):
            return self.width*self.Length
class Rectangle(Shape):
    def __init__ (self,width,Length):
        self.width=width
        self.Length=Length
a,b=map(int,input().split())
rectangle=Rectangle(a,b)
print(rectangle.area())
