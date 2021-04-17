import re

f2=open("validphone","w")
x='[+][9][1]\d{10}$'
f=open("phone","r")
for num in f:
    number=num.rstrip('\n')
    match = re.fullmatch(x,number)
    if match!=None:
       f2.write(number)
       f2.write('\n')