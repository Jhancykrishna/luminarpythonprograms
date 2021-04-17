lst=[3,4,5,8,9,10,6,2]
lst.sort()
print(lst)
low=0
upp=len(lst)-1
num=int(input("enter element to search"))
flag=0
while(low<=upp):
    mid=(low+upp)//2
    if(num>lst[mid]):
        low=mid+1
    elif(num<lst[mid]):
        upp=mid-1
    elif(num==lst[mid]):
        flag=1
        break
if (flag>0):
    print("number found")
else:
    print("number not found")