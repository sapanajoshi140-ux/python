f=open("file3.txt")
data=f.readlines()
print(data)
f1=open("file3.txt")
line=f1.readline()
while line!="":
    print(line)
    line=f1.readline()
f.close()