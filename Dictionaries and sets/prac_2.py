s=set()
s.add(20)
s.add(20.0)
s.add('20')
print(len(s))
dict={}
i=1
while i<=4:
  d1=input("Enter your name:")
  d2=input("Enter your favourite language:")
  dict.update({d1:d2})
  i+=1
print(dict)
enter=input("Enter your name:")
print("Your language is ",dict.get(enter))