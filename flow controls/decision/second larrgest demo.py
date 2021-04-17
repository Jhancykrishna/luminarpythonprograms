num1=int(input('enter number 1'))
num2=int(input('enter number 2'))
num3=int(input('enter number 3'))
if(num1<num2)&(num2<num3):
    print('number 2 is second largest')
elif(num3<num2)&(num2<num1):
    print('number 2 is second largest')
if(num2<num1)&(num1<num3):
    print('number 1 is second largest')
elif(num3<num1)&(num1<num2):
    print('number 1 is second largest')
if(num1<num3)&(num3<num2):
    print('number 3 is second largest')
elif(num2<num3)&(num3<num1):
    print('number 3 is second largest')