n=int(input("Enter a number:"))
i=2
while i<n:
    if(n%i==0):
        i+=1
        print("It is not a prime number")
        break

else:
    print("It is prime number")
