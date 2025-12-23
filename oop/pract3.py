class calculator:
    @staticmethod
    def fun():
        print("Good day")
    num=int(input("Enter a number"))
square=calculator()
print(f"The square of {square.num} is",square.num**2)
cube=calculator()
print(f"The cube of {cube.num} is",cube.num**3)
squareroot=calculator()
print(f"The square root of {squareroot.num} is",squareroot.num**0.5)
square.fun()