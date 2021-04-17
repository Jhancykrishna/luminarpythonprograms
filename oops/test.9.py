import re
num=input(("enter sequence"))
rule="(^[A-Z]{1}[a-z]+$)"
match = re.fullmatch(rule,num)
if match!=None:
    print("valid")
else:
    print("invalid")

