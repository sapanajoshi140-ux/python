class Programmer:
    depart="python"
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address
employee1=Programmer("sapana",18,"nepal")
print(employee1.name,employee1.age,employee1.address)
employee2=Programmer("bipana",30,"canada")
print(employee2.name,employee2.age,employee2.address)
employee3=Programmer("apsara",400,"heaven")
print(employee3.name,employee3.age,employee3.address)