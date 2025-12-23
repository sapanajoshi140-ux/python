class number:
    a=4
    @classmethod
    def fun(self):
        print(self.a)
    
    @property
    def name(self):
        return (f"{self.fname}{self.lname}")
    @name.setter
    def name(self,value):
        self.fname=value.split(" ")[0]
        self.lname=value.split(" ")[1]

b=number()
b.a=32
b.name="Sapana Joshi"
print(b.name)
b.fun()