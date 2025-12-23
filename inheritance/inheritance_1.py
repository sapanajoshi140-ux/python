class Employee():
    name="sapana"
    age=18
    def student(self):
        print(f"The name is {self.name}")
class Programmer(Employee):
    depart="engineer"
    
a=Programmer()
print(a.name,a.depart,a.age)
a.student()