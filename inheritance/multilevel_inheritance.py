class employee:
    company="ICEC"
    name=input("Enter your name:")
    def __init__(self):
        print(f"Your name is {self.name} and company is {self.company}")

class role(employee):
    job="Junior Technician"
    def fun(self,salary):
        print(f"Your job is {self.job} and salary is {salary}")

class getinfo(role):
    age="18"

    
b=role()        #yo create huda init function khojxa since child node hunale yo employee class ma init pauxa ani tye lekhxa
b.fun("20000")
print(b.company,b.job)
a=getinfo()        #yo create huda init function khojxa since child node hunale yo employee class ma init pauxa ani tye lekhxa
print(a.age,a.company,a.job)
