with open("1.txt") as f:
    content=f.read()
with open("2.txt","w") as f:
    f.write(content)