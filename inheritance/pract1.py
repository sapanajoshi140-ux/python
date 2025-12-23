class TwoD:
    def __init__(self,i,j):
        self.i=i
        self.j=j
    def show(self):
        print(f"The 2D vector is {self.i}i + {self.j}j")

class ThreeD(TwoD):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k=k
    def show(self):
        print(f"The 3D vector is {self.i}i + {self.j}j +{self.k}k")
a=TwoD(1,3)
a.show()
b=ThreeD(2,3,4)
b.show()
       

