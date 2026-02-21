class Person:
    def __init__(self,name,gpa):
        self.name=name
        self.gpa=float(gpa)
class Student(Person):
    def display(self):
        super().__init__(self.name,self.gpa)
        return f"Student: {self.name}, GPA: {self.gpa}"
name,gpa=map(str,input().split())
student=Student(name,gpa)
print(student.display())