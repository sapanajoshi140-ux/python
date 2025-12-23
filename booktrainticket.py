import random
class train:
    
    def __init__(self,trainNo):
        self.trainNo=trainNo
    
    def getStatus(self):
        randomno=random.randint(1,10)
        print(f"The no of seats avaliable are {randomno}")
        seat=[]
        for i in range(randomno):
          seats=random.choice(["A","B","C"])+str(random.randint(1,randomno))
          seat.append(seats)
          print(f"The number of seats are {seats}")

        seatno=input("Enter the seat number you want to book:")
        if seatno in seat:
              print("Your ticket is confirmed")
        else:
              print("This ticket invalid try again")



    def bookTicket(self,fro,to):
        print(f"Your train of trainNo:{self.trainNo} is booked from {fro} to {to}")

    def getFare(self,fro,to):
        print(f"Your fare for the trainNo:{self.trainNo} from {fro} to {to} is {random.randint(500,1500)}")

t=train(1233)
t.getStatus()
t.bookTicket("Mahendrangar","Kathmandu")
t.getFare("Mahendranagar","Kathmandu")