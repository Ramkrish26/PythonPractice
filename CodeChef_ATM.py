# cook your dish here
try:
    amount = int(input())
    balance = int(input())
    if amount < balance:
        if amount % 5 != 0:
            print("THe amount entered is not a multiple of 5")
        elif amount % 5 == 0:
            a = (balance - amount) - 0.50
            print("Account balance after withdrawal is " + str(a))
    elif amount > balance:
        print("Insufficient Balance")
except EOFError as e:
    print(end="")