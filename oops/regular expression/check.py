import re
# count=0
# matcher=re.finditer('ac',"decacfacfacghach")
# for match in matcher:
#     print("match available at:",match.start())
#     print("group:", match.group())
#     count+=1
# print("count",count)

#############rules####################
# import re
# x='[abc]' #either a,b,c
# matcher=re.finditer(x,"decacfacfacghach")
# for match in matcher:
#     print(match.start())
#     print(match.group())

# import re
# x='[^abc]' #except a,b,c all others
# matcher=re.finditer(x,"decacfacfacghach")
# for match in matcher:
#     print(match.start())
#     print(match.group())

# import re
#
# x = '[a-z]'  # a-z all small letters only,no spaces,numbers,symbols
# matcher = re.finditer(x, "deca fa**&facghzch")
# for match in matcher:
#     print(match.start())
#     print(match.group())

#
# import re
#
# x = '\s'  # check space
# matcher = re.finditer(x,"deca fafacghzch")
# for match in matcher:
#     print(match.start())
#     print(match.group())
#
# import re
#
# x = '[A-Z]'  # check cap letters
# matcher = re.finditer(x, "deca fafAghDch")
# for match in matcher:
#     print(match.start())
#     print(match.group())
#
# import re
#
# x = '[a-zA-Z]'  # check all type letters
# matcher = re.finditer(x, "deca fafAghDch")
# for match in matcher:
#     print(match.start())
#     print(match.group())
#
#
#
# x = '[a-zA-Z0-9]'  # check all letters and numbers
# matcher = re.finditer(x, "deca faf1AghDc8?6h")
# for match in matcher:
#     print(match.start())
#     print(match.group())
#
# x = '[0-9]'  # check all numbers
# matcher = re.finditer(x, "deca faf1AghDc8?6h")
# for match in matcher:
#     print(match.start())
#     print(match.group())

#

# x = '[\D]'  # except digits
# matcher = re.finditer(x,"deca fafa11233cghzch")
# for match in matcher:
#     print(match.start())
#     print(match.group())
#
# x = '[\d]'  # digits
# matcher = re.finditer(x, "deca fafa11233cghzch")
# for match in matcher:
#     print(match.start())
#     print(match.group())
# #
x = '[\w]'  # ALL WORDS EXCEPT SPECIAL CHAR
matcher = re.finditer(x, "deca fafa11233cghzch")
for match in matcher:
    print(match.start())
    print(match.group())

# x = '[\W]'  # check only SPECIAL CHARACTERS
# matcher = re.finditer(x,"deca fafa *&11233cghzch")
# for match in matcher:
#     print(match.start())
#     print(match.group())
