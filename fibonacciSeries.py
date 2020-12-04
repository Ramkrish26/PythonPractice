# To generate the fibinacci series

num = 5
num1 = 0
num2 = 1

for i in range(0, int(num)):
    if(i == 0):
        print(num1)
    elif(i==1):
        print(num2)
    else:
        num3 = num1 + num2
        print(str(num3))
        num1 = num2
        num2 = num3


