num1=int(input('enter number 1'))
num2=int(input('enter number 2'))
num3=int(input('enter number 3'))
if(num1>num2)&(num1>num3):
    if(num2>num3):
        print('number 2 is second largest')
    else:
        print('number 3 is second largest')
if(num2>num1)&(num2>num3):
    if(num1>num3):
        print('number 1 is second largest')
    else:
        print('number 3 is second largest')
if(num3>num1)&(num3>num2):
    if(num1>num2):
        print('number 1 is second largest')
    else:
        print('number 2 is second largest')
