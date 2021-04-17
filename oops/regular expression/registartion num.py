import re
# list=[]
# f=open("registration num","r")
# for line in f:
#     n=line.rstrip("\n")
#     x='[kK][lL]\d{2}[a-zA-Z]{2}\d{4}$'
#     match=re.fullmatch(x,n)
#     if match!=None:
#        list.append(n)
# print(list)


n=input("enter the mail to validate")
x='^[a-z0-9_.+-]+@[a-zA-Z0-9]+\.[a-zA-z0-9]+$'
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")
