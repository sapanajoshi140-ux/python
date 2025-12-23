class number:
    def __init__(self,n):           
        self.n=n              # yo vaneko a.n=3 ani b.n=4 ho
    def __add__(self,num):     # yo a_add_b ho and left side means a=self vo and right side ko b=num ma gayo
        return self.n + num.n      #so yo vannale a.n+b.n vayo
a=number(3)
b=number(4)
print(a+b)