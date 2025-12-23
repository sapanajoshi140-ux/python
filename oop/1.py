class student:
    name="sapana"
    age=16
    course="python"
    def getInfo(self):
        print(f"the name is {self.name}")
    @staticmethod
    def greet():
        print("hello")
sapana=student()
sapana.name="bipana"                 #object attribute gets more preference than the class attribute
sapana.getInfo()       #yo ani student.getInfo(sapana) same ho so tya self dinxau feri ek ek parameter vo match hahaha
sapana.greet()