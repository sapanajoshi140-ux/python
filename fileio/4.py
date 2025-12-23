list=["sapana","bitch"]
with open("4.txt","r") as f:
    a=f.read()
    b=a.replace(list,"#"*len(list))
with open("4.txt","w+") as f:
    f.write(b)
    
    