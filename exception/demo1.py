# num1=int(input("enter first number"))
# num2=int(input("enter second number"))
#
# try:
#     c=num1/num2
#     print("res",c)
# except:
#     print("exception occured")

# lst=[1,2,3]
# try:
#     print(a[7])
# except Exception as e:
#     print("exception ocurred")


try:
    num1 = int(input("enter"))
    print("entered number is",num1)
except:
    print("please enter a integer value")
finally:
    print("inside finally")