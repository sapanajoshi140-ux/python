with open("donkey.txt","r") as f:
    a=f.read()
    b=a.replace("donkey","####")
with open("donkey.txt","w+") as f:
    f.write(b)
    
    