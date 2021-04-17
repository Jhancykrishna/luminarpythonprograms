import re
# num=str(input("enter a word"))
# rule="([a-zA-Z]+[0-9]+$)"
# matcher=re.fullmatch(rule,num)
# if matcher!=None:
#     print("vaild")
# else:
#     print("invalid")


# num=(input("enter a word"))
# rule="(^a[a-zA-Z0-9\W]+[b]$)"#
# matcher=re.fullmatch(rule,num)
# if matcher!=None:
#     print("vaild")
# else:


#     #MIN LENGTH 8 MAX 15 EXCEPT NUMBERS-STRING
#
# num=(input("enter"))
# rule="[a-zA-Z\W]*"
# matcher=re.fullmatch(rule,num)
# if (len(num)>=8 and len(num)<=15):
#     if matcher!=None:
#         print("vaild")
#     else:
#         print("invalid")
# else:
#     print("length not in limit")


num=(input("enter"))
rule="[a-zA-Z\W{8,15}]*"
matcher=re.fullmatch(rule,num)
if (len(num)>=8 and len(num)<=15):
    if matcher!=None:
        print("vaild")
    else:
        print("invalid")
else:
    print("length not in limit")
