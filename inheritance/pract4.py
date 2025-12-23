class complex:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __add__(self,num):
        return (f"{self.a+num.a}+ {self.b+num.b}j")
    def __mul__(self,multi):
        return (f"{self.a*multi.a}+ {self.b*multi.b}j")
    def __str__(self):
        return (f"{self.a}i + {self.b}j")

        
d=complex(3,4)
e=complex(4,5)
print("The addition is",d+e)
print("The multiplication is",d*e)
        