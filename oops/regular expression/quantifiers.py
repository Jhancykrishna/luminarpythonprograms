import re

#
# x='axy+' #only this  group position revealed
# r='aaa a gaaaa aarCVXYaxynnnxayt'
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start())
#     print(match.group())

# x='a*' #A'S POSITION AS GROUPS/NOT, ALL VALID AND OTHERS POSTION SEPARATELY-ie, g,r,t positon number will be shown correpondingly g,r,t will not be shown
# r='aaa a gaaaa aart'
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start())
#     print(match.group())


# x='a?' #ALL POSITION CONSIDER SEPARATELY EVEN THE SPACE
# r='aaa a gaaaa'
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start())
#     print(match.group())

# x='a{3}' #POSITIONS where a comes 3 time as a group-here  it is0,7
# r='aaa a gaaaa'
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start())
#     print(match.group())

x='a{1,3}' #positions of minimum a 1, max a is group of 3-here it is 0,4,7,10
r='aaa a gaaaa'
matcher=re.finditer(x,r)
for match in matcher:
    print(match.start())
    print(match.group())

# x='^a' #check whether the full string start with a-here yes at 0
# r='aaa a gaaaa'
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start())
#     print(match.group())


# x='a$' #check whether the full string end with a-here yes at 10,, if mot nothing prints
# r='aaa a gaaaa'
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start())
#     print(match.group())