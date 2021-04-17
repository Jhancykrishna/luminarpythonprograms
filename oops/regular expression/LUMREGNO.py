import re

f2=open("validreg","a")
x='[L][U][M]\d{2}[P][Y]\d{3}$'
f=open("lumregno","r")
for num in f:
    number=num.rstrip('\n')
    match = re.fullmatch(x,number)
    if match!=None:
       f2.write(number)
       f2.write('\n')