lst=[10,20,21,22,23,24]
flag=0
num=int(input("enter element to search"))
for i in lst:
        if(i==num):
            flag=1
            break

        else:
           pass
if(flag>0):
    print("element found")
else:
    print("element not found")