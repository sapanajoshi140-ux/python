str="sapana "
f=open("file.txt","a")
f.write(str)
f=open("file.txt","r+")
data=f.read()
print(data)
f.close()