# Find whether the number is divisible by both 5 and 11

num = input("Enter the number: ")

if(int(num)%5==0 and int(num)%11==0):
    print ("Number is divisible by both 5 and 11")
elif (int(num)%5==0 and int(num)%11!=0):
    print ("Numeber is divisible by 5 only")
elif (int(num)%5!=0 and int(num)%11==0):
    print ("Numeber is divisible by 11 only")
elif (int(num)%5!=0 and int(num)%11!=0):
    print ("Numeber is not divisible by both")