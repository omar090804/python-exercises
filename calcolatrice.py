numero1=int(input("enter your first number "))
numero2=int(input("enter your second number "))
operation=input('enter the operation sign (+,-,*,/) ')
if operation=='+' :
    print(numero1+numero2)
elif operation=='-':
    print(numero1-numero2)
elif operation=='*':
    print(numero1*numero2)
elif operation=='/':
    if numero2 == 0:
        print("Cannot divide by zero")
        else:
        print(numero1 / numero2)
else:
    print("operation not correct ")
