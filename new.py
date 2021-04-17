lst1=[10,20,30,40]
lst2=[11,20,15,30]
lst=[]
for i in lst1:
    for j in lst2:
        if(i==j):
          lst.append(i)
print(lst)
