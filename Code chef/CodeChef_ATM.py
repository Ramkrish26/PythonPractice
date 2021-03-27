# cook your dish here
a,b =[float(a) for a in input().split(" ")]
if (a%5 == 0):
    if (a+0.50)<=b:
        print('%0.2f'%(b-a-0.50))
    else:
        print('%0.2f'%b)
else:
    print('%0.2f'%b)