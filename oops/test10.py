import re

num=(input("enter a word"))
rule="(^a[a-zA-Z0-9\W]+[b]$)"#
matcher=re.fullmatch(rule,num)
if matcher!=None:
    print("vaild")
else:
    print("invaild")