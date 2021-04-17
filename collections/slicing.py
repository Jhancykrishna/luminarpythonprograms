# lst=[4,2,6,5,10]
# print(lst[2])
# print(lst[1:4])
# print(lst[1:])
# print(lst[:4])
# print(lst[-3:])
# print(lst[:-2])

lst=[3,4,8]
sum=0
for i in lst:
    sum=sum+i
lst1=[]
for i in lst:
   res=sum-i
   lst1.append(res)
print(lst1)