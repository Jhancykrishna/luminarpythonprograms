def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def mul(num1,num2):
    return num1*num2
def div(num1,num2):
    return num1/num2

print('select operations\n'
      '1.Addition\n'
      '2.subtractiom\n'
      "3.multiplicatiom\n"
      "4.division\n")
select=int(input("select operations"))
num1=int(input("enter first number"))
num2=int(input("enter second number"))

if select==1:
    print(num1,"+",num2,"=",add(num1,num2))
elif select==2:
    print(num1,"-",num2,"=",sub(num1,num2))
elif  select==3:
    print(num1,"*",num2,"=",mul(num1,num2))
elif select==4:
    print(num1,"/",num2,"=",div(num1,num2))

