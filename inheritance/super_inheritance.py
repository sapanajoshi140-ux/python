class employee:
    company="ICEC"
    name=input("Enter your name:")
    def __init__(self):
        print(f"Your name is {self.name} and company is {self.company}")

class role(employee):
    job="Junior Technician"
    def __init__(self):
        super().__init__()
        print(f"Your name is sapana")

class getinfo(role):
    age="18"

    
b=role()        #yo create huda init function khojxa since child node hunale yo employee class ma init pauxa ani tye lekhxa
print(b.company,b.job)
a=getinfo()        #yo create huda init function khojxa since child node hunale yo employee class ma init pauxa ani tye lekhxa
print(a.age,a.company,a.job)
