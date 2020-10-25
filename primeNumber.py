# To check whether a number is prime or not

num = input("Enter the number: ")
flag=0

if(int(num)==1):
    print("It is neither neother Prime nor Composite number")

for i in range (2,int(num)):
    if(int(num)%i==0):
        flag=1

if(flag==0):
    print("It is a prime number")
else:
    print("It is not a prime number")
