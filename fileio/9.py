with open("1.txt") as f:
    content1=f.read()
with open("2.txt") as f:
    content2=f.read()
if(content1==content2):
    print("the content is same")
else:
    print("not same")
