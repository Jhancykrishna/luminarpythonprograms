import re

# n="helloo"
# x='\w{6}'
# m="he&&**"
# match=re.fullmatch(x,n)
# if match is not None:
#     print("valid")
# else:
#     print("invalid")
# match=re.fullmatch(x,m)
# if match is not None:
#     print("valid")
# else:
#     print("invalid")


import re

n="56kg"
x='\d{2}[a-z]{2}'
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")
