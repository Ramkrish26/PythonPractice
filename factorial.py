# To find a factorialof a number

num  = input("Enter the number: ")
fact=1

for i in range(int(num)-1,0,-1):
    num = int(num)*i

print (num)