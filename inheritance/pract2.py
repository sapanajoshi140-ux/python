class Animals:
   
    pass
class pets(Animals):
   pass
class dogs(pets):
   @staticmethod
   def bark():
      print("bow bow!")
a=dogs()
a.bark()
