# Finding the largest and smallest number among 3 numbers

num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
num3 = input("Enter the third number: ")

if(int(num1) > int(num2) and int(num1)>int(num3)):
    print ("Largest number is "+num1)
elif (int(num2) > int(num1) and int(num2) > int(num3)):
    print ("Largest number is "+num2)
else:
    print ("Largest Number is "+num3)

if(int(num1) < int(num2) and int(num1)<int(num3)):
    print ("Smallest number is "+num1)
elif (int(num2) < int(num1) and int(num2) < int(num3)):
    print ("Smallest number is "+num2)
else:
    print ("Smallest Number is "+num3)